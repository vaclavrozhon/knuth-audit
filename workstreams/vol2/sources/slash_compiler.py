"""Experimental Python compilation front-end for TAOCP 4.5.1-15.

Supported: scalar real arithmetic, integer control variables, ordinary Python
containers/functions, float literals/conversions, and selected math/NumPy
scalar functions. Imports of other packages and type introspection are rejected.
This is a local compile pipeline, not a patch to the installed interpreter.
"""
import ast
import builtins
from fractions import Fraction as F
import math
from slash_arithmetic import SlashFormat, as_pair


def sign(u):
    return (u > 0) - (u < 0)


class Slash:
    def __init__(self, runtime, pair):
        self.runtime, self.pair = runtime, pair

    def _op(self, other, op):
        y = self.runtime.make(other)
        u,a = self.pair; v,b = y.pair
        self.runtime.operations += 1
        if self.pair == (0,0) or y.pair == (0,0):
            return Slash(self.runtime,(0,0))
        if op == '-':
            v = -v
            op = '+'
        if op == '+':
            if a == 0 and b == 0:
                return Slash(self.runtime,(u,0) if u==v else (0,0))
            if a == 0:return Slash(self.runtime,(u,0))
            if b == 0:return Slash(self.runtime,(v,0))
            return self.runtime.make(F(u,a)+F(v,b))
        if op == '*':
            if a == 0 or b == 0:
                return Slash(self.runtime,(sign(u)*sign(v),0))
            return self.runtime.make(F(u,a)*F(v,b))
        if op == '/':
            if (a == b == 0) or (u == v == 0):return Slash(self.runtime,(0,0))
            if v == 0:return Slash(self.runtime,(sign(u),0))
            if a == 0:return Slash(self.runtime,(sign(u)*sign(v),0))
            if b == 0:return self.runtime.make(0)
            return self.runtime.make(F(u,a)/F(v,b))
        raise ValueError(op)

    def __add__(self,y):return self._op(y,'+')
    def __sub__(self,y):return self._op(y,'-')
    def __mul__(self,y):return self._op(y,'*')
    def __truediv__(self,y):return self._op(y,'/')
    def __radd__(self,y):return self.runtime.make(y)._op(self,'+')
    def __rsub__(self,y):return self.runtime.make(y)._op(self,'-')
    def __rmul__(self,y):return self.runtime.make(y)._op(self,'*')
    def __rtruediv__(self,y):return self.runtime.make(y)._op(self,'/')
    def __neg__(self):return Slash(self.runtime,(-self.pair[0],self.pair[1]))
    def __pos__(self):return self
    def __abs__(self):return Slash(self.runtime,(abs(self.pair[0]),self.pair[1]))
    def __bool__(self):return self.pair != (0,1)

    def __pow__(self, exponent):
        if not isinstance(exponent,int):
            raise NotImplementedError('only integral powers in this experiment')
        u,a=self.pair
        if not a:
            if not u:return Slash(self.runtime,(0,0))
            if exponent==0:return self.runtime.make(1)
            return self.runtime.make(0) if exponent<0 else Slash(self.runtime,(u**exponent,0))
        if not u and exponent<0:return Slash(self.runtime,(1,0))
        self.runtime.operations += 1
        return self.runtime.make(F(u,a)**exponent)

    def _value(self):
        u,a=self.pair
        return F(u,a) if a else math.copysign(math.inf,u) if u else math.nan

    def _compare(self,other,op):
        y=other._value() if isinstance(other,Slash) else other
        x=self._value()
        if op=='eq':return x==y
        if op=='lt':return x<y
        if op=='le':return x<=y
        if op=='gt':return x>y
        if op=='ge':return x>=y
        raise ValueError(op)

    def __eq__(self,y):return self._compare(y,'eq')
    def __ne__(self,y):return not self==y
    def __lt__(self,y):return self._compare(y,'lt')
    def __le__(self,y):return self._compare(y,'le')
    def __gt__(self,y):return self._compare(y,'gt')
    def __ge__(self,y):return self._compare(y,'ge')
    def __float__(self):return float(self._value())
    def __str__(self):return str(float(self))
    __repr__=__str__
    def __format__(self,spec):return format(float(self),spec)


class ScalarFunctions:
    def __init__(self,runtime,module):
        self.runtime,self.module=runtime,module
    def __getattr__(self,name):
        if name in ('pi','e','inf','nan'):
            return self.runtime.make(getattr(self.module,name))
        if name not in ('sqrt','log','log2','log10','exp','sin','cos','tan','atan','hypot'):
            raise NotImplementedError('unsupported scalar function '+name)
        fn=getattr(self.module,name)
        def invoke(*args):
            self.runtime.special_calls += 1
            result=fn(*[float(x) if isinstance(x,Slash) else x for x in args])
            return self.runtime.make(float(result))
        return invoke


class SlashRuntime:
    def __init__(self,q=27):
        self.format=SlashFormat(size=q)
        self.operations=self.special_calls=0

    def make(self,x=0.0):
        if isinstance(x,Slash):
            if x.runtime is self:return x
            return Slash(self,x.pair) if x.pair[1]==0 else self.make(F(*x.pair))
        if isinstance(x,str):x=float(x)
        if isinstance(x,float) and not math.isfinite(x):
            return Slash(self,(0,0) if math.isnan(x) else (sign(x),0))
        return Slash(self,self.format.round(F(x)))

    def input(self,x):
        if isinstance(x,float):return self.make(x)
        if isinstance(x,list):return [self.input(y) for y in x]
        if isinstance(x,tuple):return tuple(self.input(y) for y in x)
        if isinstance(x,dict):return {k:self.input(v) for k,v in x.items()}
        return x

    def print(self,*args,fractional=False,**kwargs):
        def render(x):
            if isinstance(x,Slash):
                if not fractional:return str(x)
                u,a=x.pair
                return f'{u}/{a}' if a else '+inf' if u>0 else '-inf' if u<0 else 'undefined'
            if isinstance(x,list):return '['+', '.join(render(y) for y in x)+']'
            if isinstance(x,tuple):return '('+', '.join(render(y) for y in x)+(',' if len(x)==1 else '')+')'
            return str(x)
        builtins.print(*[render(x) for x in args],**kwargs)

    def compile(self,source,filename='<slash>'):
        tree=SlashTransformer().visit(ast.parse(source,filename))
        ast.fix_missing_locations(tree)
        import numpy
        def power(x,y):
            if isinstance(x,int) and isinstance(y,int) and y>=0:return x**y
            return self.make(x)**y
        env={'_slash_float':self.make,'_slash_div':lambda x,y:self.make(x)/y,'_slash_pow':power,
             '_slash_print':self.print,'_slash_math':ScalarFunctions(self,math),
             '_slash_numpy':ScalarFunctions(self,numpy)}
        exec(compile(tree,filename,'exec'),env)
        return env


class SlashTransformer(ast.NodeTransformer):
    def visit_Constant(self,node):
        if isinstance(node.value,complex):
            raise NotImplementedError('complex values')
        if isinstance(node.value,float):
            # Preserve the parser's binary64 literal value, then round to slash.
            return ast.copy_location(ast.Call(ast.Name('_slash_float',ast.Load()),[node],[]),node)
        return node

    def visit_Name(self,node):
        if node.id in ('float','print'):
            if not isinstance(node.ctx,ast.Load):
                raise NotImplementedError('rebinding '+node.id)
            return ast.copy_location(ast.Name('_slash_'+node.id,ast.Load()),node)
        return node

    def visit_arg(self,node):
        if node.arg in ('float','print') or node.arg.startswith('_slash_'):
            raise NotImplementedError('reserved argument '+node.arg)
        return self.generic_visit(node)

    def visit_FunctionDef(self,node):
        if node.name in ('float','print') or node.name.startswith('_slash_'):
            raise NotImplementedError('reserved function '+node.name)
        return self.generic_visit(node)

    def visit_Call(self,node):
        if isinstance(node.func,ast.Name) and node.func.id in ('isinstance','type','complex','eval','exec','compile','__import__'):
            raise NotImplementedError('unsupported reflective call '+node.func.id)
        return self.generic_visit(node)

    def visit_BinOp(self,node):
        self.generic_visit(node)
        if isinstance(node.op,ast.Div):
            return ast.copy_location(ast.Call(ast.Name('_slash_div',ast.Load()),[node.left,node.right],[]),node)
        if isinstance(node.op,ast.Pow):
            return ast.copy_location(ast.Call(ast.Name('_slash_pow',ast.Load()),[node.left,node.right],[]),node)
        return node

    def visit_AugAssign(self,node):
        self.generic_visit(node)
        if isinstance(node.op,(ast.Div,ast.Pow)):
            if not isinstance(node.target,ast.Name):
                raise NotImplementedError('augmented division/power target must be a name')
            fn='_slash_div' if isinstance(node.op,ast.Div) else '_slash_pow'
            value=ast.Call(ast.Name(fn,ast.Load()),[ast.Name(node.target.id,ast.Load()),node.value],[])
            return ast.copy_location(ast.Assign([node.target],value),node)
        return node

    def visit_Import(self,node):
        result=[]
        for alias in node.names:
            if alias.name not in ('math','numpy'):
                raise NotImplementedError('unsupported import '+alias.name)
            result.append(ast.copy_location(ast.Assign([ast.Name(alias.asname or alias.name,ast.Store())],
                          ast.Name('_slash_'+alias.name,ast.Load())),node))
        return result

    def visit_ImportFrom(self,node):
        if node.module not in ('math','numpy') or node.level:
            raise NotImplementedError('unsupported import from '+str(node.module))
        result=[]
        for alias in node.names:
            if alias.name=='*':raise NotImplementedError('star import')
            value=ast.Attribute(ast.Name('_slash_'+node.module,ast.Load()),alias.name,ast.Load())
            result.append(ast.copy_location(ast.Assign([ast.Name(alias.asname or alias.name,ast.Store())],value),node))
        return result
