"""Integer-only programs for TAOCP 1.2.8-3 and 1.2.8-38.

Usage: python3 fibonacci_tools.py sequence --through 1000
       python3 fibonacci_tools.py nim 1000 999
       python3 fibonacci_tools.py play 1000
Proofs and an independent game validator accompany this file.
"""
from argparse import ArgumentParser
from functools import cache
import json


@cache
def fib(n):
    """F_n at any integer index, by binary doubling."""
    if n < 0:
        return (-1 if n % 2 == 0 else 1) * fib(-n)
    return fib_pair(n)[0]


@cache
def fib_pair(n):
    if n == 0:
        return 0, 1
    a, b = fib_pair(n // 2)
    c, d = a * (2*b-a), a*a+b*b
    return (d, c+d) if n % 2 else (c, d)


def sequence(through):
    """Yield F_1,...,F_through using only addition."""
    if through < 0:
        raise ValueError("through must be nonnegative")
    a, b = 0, 1
    for _ in range(through):
        a, b = b, a+b
        yield a


@cache
def zeckendorf(n):
    """Descending indices, each >=2 and with gaps >=2."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    if not n:
        return ()
    k = 2
    while fib(k+1) <= n:
        k += 1
    answer = []
    while n:
        if fib(k) <= n:
            answer.append(k)
            n -= fib(k)
            k -= 2
        else:
            k -= 1
    return tuple(answer)


def nim_move(n, limit):
    """An optimal legal move, or None when there is no legal move."""
    if n < 0 or limit < 0:
        raise ValueError("pile and limit must be nonnegative")
    if not n or not limit:
        return None
    least = fib(zeckendorf(n)[-1])
    return least if least <= limit else 1


def nim_winning_moves(n, limit):
    """Every winning legal move, using the proven suffix criterion."""
    if n < 0 or limit < 0:
        raise ValueError("pile and limit must be nonnegative")
    terms = [fib(k) for k in zeckendorf(n)]
    suffix, answer = 0, []
    for j in range(len(terms)-1, -1, -1):
        suffix += terms[j]
        if suffix <= limit and (j == 0 or terms[j-1] > 2*suffix):
            answer.append(suffix)
    return answer


def play(n, human_first=False):
    if n < 1:
        raise ValueError("initial pile must be positive")
    limit, human = n-1, human_first
    while n:
        name = "You" if human else "Computer"
        if limit == 0:
            print(f"{name} lose: no legal move.")
            return
        maximum = min(n, limit)
        if human:
            while True:
                try:
                    take = int(input(f"{n} chips; take 1..{maximum}: "))
                except ValueError:
                    continue
                if 1 <= take <= maximum:
                    break
        else:
            take = nim_move(n, limit)
            print(f"Computer takes {take}; {n-take} remain.")
        n -= take
        if not n:
            print(f"{name} win.")
            return
        limit, human = 2*take, not human


def main():
    parser = ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("sequence")
    p.add_argument("--through", type=int, default=1000)
    p = sub.add_parser("nim")
    p.add_argument("pile", type=int)
    p.add_argument("limit", type=int)
    p = sub.add_parser("play")
    p.add_argument("pile", type=int)
    p.add_argument("--human-first", action="store_true")
    args = parser.parse_args()
    if args.command == "sequence":
        for value in sequence(args.through):
            print(value)
    elif args.command == "nim":
        print(json.dumps({"move": nim_move(args.pile, args.limit),
                          "winning_moves": nim_winning_moves(args.pile, args.limit)}))
    else:
        play(args.pile, args.human_first)


if __name__ == "__main__":
    main()
