from functools import reduce

import sympy as sp
from sympy import pprint

from cuspidal_utils import simplify
from link_transform import dh_P, dh_R, dh_T

n = 6
r = sp.symbols("r_1:4")
alpha = sp.symbols("alpha_1:7")
a = sp.symbols("a_1:7")
d = sp.symbols("d_1:7")
q = sp.symbols("q_1:7")

Q = sp.Matrix(sp.symbols("Q11:20")).reshape(3, 3)

# 定义 sin, cos 的别名符号
c = [sp.symbols(f"c{i}") for i in range(1, 7)]
s = [sp.symbols(f"s{i}") for i in range(1, 7)]

# 替换规则
subs_trig = {}
for i in range(6):
    subs_trig[sp.cos(q[i])] = c[i]
    subs_trig[sp.sin(q[i])] = s[i]

R = [dh_R(alpha[i], a[i], d[i], q[i]) for i in range(n)]
P = [dh_P(alpha[i], a[i], d[i], q[i]) for i in range(n)]
T6 = dh_T(alpha[n - 1], a[n - 1], d[n - 1], q[n - 1])

print("-----T6-----")
T6_short = T6.subs(subs_trig)
pprint(T6_short)

Q_sub = [simplify(Ti) for Ti in R]

p = sp.zeros(3, 1)  # 初始为零向量

for i in range(5):
    # 累积旋转矩阵 Q0*Q1*...*Qi
    Q_prod = reduce(lambda x, y: x * y, Q_sub[: i + 1])
    p += Q_prod * P[i + 1]

p15 = Q_sub[0].transpose() * p
p15 = simplify(p15)
p15_short = p15.subs(subs_trig)
print("-----p15-----")
pprint(p15_short)

r_vec = sp.Matrix([r[0], r[1], r[2]])
r_vec = Q_sub[0].transpose() * r_vec
r_vec = simplify(r_vec)
r_vec_short = r_vec.subs(subs_trig)
print("-----r_vec-----")
pprint(r_vec_short)

Q46 = simplify(Q_sub[3] * Q_sub[4] * Q_sub[5])
Q13 = simplify(Q_sub[2].transpose() * Q_sub[1].transpose() * Q_sub[0].transpose() * Q)
print("-----Q46-----")
pprint(Q46)
print("-----Q13-----")
pprint(Q13)
