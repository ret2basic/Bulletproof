from py_ecc.bn128 import is_on_curve, FQ, G1
from py_ecc.fields import field_properties
field_mod = field_properties["bn128"]["field_modulus"]
from hashlib import sha256
from libnum import has_sqrtmod_prime_power, sqrtmod_prime_power

b = 3 # for bn128, y^2 = x^3 + 3
public_random = "RareSkills"  # publicly agreed random string / number

# initial x: hash(generator_x || generator_y || public_random) per algorithm description
g_x = G1[0].n  # underlying int inside FQ
g_y = G1[1].n
x = int(sha256(f"{g_x}{g_y}{public_random}".encode('ascii')).hexdigest(), 16) % field_mod

vector_basis = []

# number of points desired
n = 4

for _ in range(n):
    entropy = 0
    # find an x that is on the curve (so that x^3 + b is a quadratic residue)
    while not has_sqrtmod_prime_power((x**3 + b) % field_mod, field_mod, 1):
        x = (x + 1) % field_mod
        entropy += 1

    # pick the upper or lower y based on parity of entropy (deterministic choice)
    y = list(sqrtmod_prime_power((x**3 + b) % field_mod, field_mod, 1))[entropy & 1 == 0]
    point = (FQ(x), FQ(y))
    assert is_on_curve(point, b), "sanity check"
    vector_basis.append(point)

    # derive next starting x: hash(x || y || public_random)
    x = int(sha256(f"{point[0].n}{point[1].n}{public_random}".encode('ascii')).hexdigest(), 16) % field_mod 

print(vector_basis)
