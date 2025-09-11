from py_ecc.bn128 import G1, multiply, add, FQ
from py_ecc.bn128 import curve_order as p
import random

def random_field_element():
    return random.randint(0, curve_order)

# these EC points have unknown discrete logs:
G = (FQ(6286155310766333871795042970372566906087502116590250812133967451320632869759), FQ(2167390362195738854837661032213065766665495464946848931705307210578191331138))

B = (FQ(12848606535045587128788889317230751518392478691112375569775390095112330602489), FQ(18818936887558347291494629972517132071247847502517774285883500818572856935411))

# scalar multiplication example: multiply(G, 42)
# EC addition example: add(multiply(G, 42), multiply(G, 100))

# remember to do all arithmetic modulo p

def commit(f_0, f_1, f_2, gamma_0, gamma_1, gamma_2, G, B):
    # fill this in
    # return the commitments as a tuple (C0, C1, C2)
    pass

def evaluate(f_0, f_1, f_2, u):
    return (f_0 + f_1 * u + f_2 * u**2) % p

def prove(gamma_0, gamma_1, gamma_2, u):
    # fill this in
    # return pi
    pass

def verify(C0, C1, C2, G, B, f_u, pi):
    # fill this in
    # Return true or false
    pass

## step 0: Prover and verifier agree on G and B

## step 1: Prover creates the commitments
### f(x) = f_0 + f_1x + f_2x^2
f_0 = ...
f_1 = ...
f_2 = ...

### blinding terms
gamma_0 = ...
gamma_1 = ...
gamma_2 = ...
C0, C1, C2 = commit(f_0, f_1, f_2, gamma_0, gamma_1, gamma_2, G, B)

## step 2: Verifier picks u
u = ...

## step 3: Prover evaluates f(u) and pi

f_u = evaluate(f_0, f_1, f_2, u)
pi = prove(gamma_0, gamma_1, gamma_2, u)

## step 4: Verifier accepts or rejects
if verify(C0, C1, C2, G, B, f_u, pi):
    print("accept")
else:
    print("reject")
