import sympy as sp

r = sp.symbols("r_1:4")
alpha = sp.symbols("alpha_1:7")
a = sp.symbols("a_1:7")
d = sp.symbols("d_1:7")
q = sp.symbols("q_1:7")

# ===== 根据你的表格，把已知值代入 =====
known = {
    a[0]: 0,
    a[1]: sp.symbols("a2"),
    a[2]: 0,
    a[3]: 0,
    a[4]: 0,
    a[5]: 0,
    d[0]: sp.symbols("b1"),
    d[1]: sp.symbols("b2"),
    d[2]: sp.symbols("b3"),
    d[3]: sp.symbols("b4"),
    d[4]: sp.symbols("b5"),
    d[5]: 0,
    alpha[0]: sp.pi / 2,
    alpha[1]: sp.pi,
    alpha[2]: sp.pi / 2,
    alpha[3]: sp.pi / 2,
    alpha[4]: sp.pi / 2,
    alpha[5]: 0,
}


def simplify(syms):
    return sp.simplify(sp.trigsimp(syms.subs(known), deep=True))
