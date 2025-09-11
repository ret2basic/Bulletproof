from py_ecc.bn128 import G1, multiply, add, FQ, eq
from py_ecc.bn128 import curve_order as p
import random

def random_element():
    return random.randint(0, p)

# these EC points have unknown discrete logs:
G = (FQ(6286155310766333871795042970372566906087502116590250812133967451320632869759), FQ(2167390362195738854837661032213065766665495464946848931705307210578191331138))

H = (FQ(13728162449721098615672844430261112538072166300311022796820929618959450231493), FQ(12153831869428634344429877091952509453770659237731690203490954547715195222919))

B = (FQ(12848606535045587128788889317230751518392478691112375569775390095112330602489), FQ(18818936887558347291494629972517132071247847502517774285883500818572856935411))

# utility function
def addd(A, B, C):
    return add(A, add(B, C))

# scalar multiplication example: multiply(G, 42)
# EC addition example: add(multiply(G, 42), multiply(G, 100))

# remember to do all arithmetic modulo p
def commit(a, sL, b, sR, alpha, beta, gamma, tau_1, tau_2):
    pass
    # return (A, S, V, T1, T2)


def evaluate(f_0, f_1, f_2, u):
    return (f_0 + f_1 * u + f_2 * u**2) % p

def prove(blinding_0, blinding_1, blinding_2, u):
    # fill this in
    # return pi
    pass

## step 0: Prover and verifier agree on G and B

## step 1: Prover creates the commitments
a = ...
b = ...
sL = ...
sR = ...
t1 = ...
t2 = ...

### blinding terms
alpha = ...
beta = ...
gamma = ...
tau_1 = ...
tau_2 = ...

A, S, V, T1, T2 = commit(a, sL, b, sR, alpha, beta, gamma, tau_1, tau_2)

## step 2: Verifier picks u
u = ...

## step 3: Prover evaluates l(u), r(u), t(u) and creates evaluation proofs
l_u = evaluate(a, sL, 0, u)
r_u = evaluate(b, sR, 0, u)
t_u = evaluate(a*b, t1, t2, u)

pi_lr = prove(alpha, beta, 0, u)
pi_t = prove(gamma, tau_1, tau_2, u)

## step 4: Verifier accepts or rejects
assert t_u == (l_u * r_u) % p, "tu != lu*ru"
assert eq(add(A, multiply(S, u)), addd(multiply(G, l_u), multiply(H, r_u), multiply(B, pi_lr))), "l_u or r_u not evaluated correctly"
assert eq(add(multiply(G, t_u), multiply(B, pi_t)), addd(V, multiply(T1, u), multiply(T2, u**2 % p))), "t_u not evaluated correctly"
