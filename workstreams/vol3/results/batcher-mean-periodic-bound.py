"""One targeted interval enclosure for the first Fourier amplitude; no enumeration."""
import json
from mpmath import iv

iv.dps = 45
a = iv.mpf(1) / 4
t = iv.pi / iv.ln(2)
s = iv.mpc(0, 2*t)
K = 64
A = K+a
z = sum((iv.mpf(k)+a)**(-s) for k in range(K))
z += A**(1-s)/(s-1) + A**(-s)/2
z += s*A**(-s-1)/12
z -= s*(s+1)*(s+2)*A**(-s-3)/720
# Euler--Maclaurin through B4; sup |B4({x})|=1/30, Re(s)=0.
remainder = abs(s*(s+1)*(s+2)*(s+3))/(2160*A**3)
z_abs_upper = abs(z)+remainder
sinh_pi_t = (iv.exp(iv.pi*t)-iv.exp(-iv.pi*t))/2
gamma_abs = iv.sqrt(iv.pi/(t*sinh_pi_t))
amplitude_one_upper = 2*gamma_abs*z_abs_upper/(iv.ln(2)*iv.sqrt(1+4*t*t))
# Proved analytically for every k>=1: amplitude_k <4.65*sqrt(k)*10**(-3*k).
# For k>=2, sqrt(k)<=k sums to the following exact rational tail majorant.
r = iv.mpf('0.001')
tail_upper = iv.mpf('4.65')*(r/(1-r)**2-r)
total_upper = amplitude_one_upper+tail_upper
assert amplitude_one_upper.b < iv.mpf('0.0004903')
assert tail_upper.b < iv.mpf('0.0000094')
assert total_upper.b < iv.mpf('0.0005')
print(json.dumps({
    'method': '45-digit interval arithmetic;64 finite Hurwitz terms, explicit B4 integral remainder, exact Gamma modulus, analytic infinite Fourier tail',
    't': str(t), 'hurwitz_finite_real': str(z.real),
    'hurwitz_finite_imag': str(z.imag),
    'hurwitz_remainder_bound': str(remainder),
    'first_amplitude_upper_enclosure': str(amplitude_one_upper),
    'tail_upper_enclosure': str(tail_upper),
    'total_upper_enclosure': str(total_upper),
    'proved_target': 'sum of absolute Fourier amplitudes <0.0005'
}, indent=2))
