MOD = 1_000_000_007

def power(base, exponent):
    result = 1
    base = base % MOD
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exponent //= 2
    return result

def prepare_factorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    return fact

def comb(n, k, fact):
    return fact[n] * pow(fact[k] * fact[n - k] % MOD, MOD - 2, MOD) % MOD


N = int(input())
D = int(input())
L = int(input())
U = int(input())
fact = prepare_factorials(N)
answer = 0
for x in range(D, N + 1):
    for y in range(L, N  - x + 1):
        z = N - x - y
        if z < U:
            continue
        ways_positions = comb(N, x, fact) * comb(N - x, y, fact) % MOD
        ways_fill = power(10, x) * power(30, y) % MOD
        answer = (answer + ways_positions * ways_fill) % MOD
print(answer)
