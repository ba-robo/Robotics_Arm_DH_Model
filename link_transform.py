import sympy as sp


def dh_T(al, a_val, d_val, th):
    ct, st = sp.cos(th), sp.sin(th)
    ca, sa = sp.cos(al), sp.sin(al)
    return sp.Matrix(
        [
            [ct, -st * ca, st * sa, a_val * ct],
            [st, ct * ca, -ct * sa, a_val * st],
            [0, sa, ca, d_val],
            [0, 0, 0, 1],
        ]
    )


def dh_R(al, a_val, d_val, th):
    ct, st = sp.cos(th), sp.sin(th)
    ca, sa = sp.cos(al), sp.sin(al)
    return sp.Matrix(
        [
            [ct, -st * ca, st * sa],
            [st, ct * ca, -ct * sa],
            [0, sa, ca],
        ]
    )


def dh_P(al, a_val, d_val, th):
    ct, st = sp.cos(th), sp.sin(th)
    return sp.Matrix([a_val * ct, a_val * st, d_val])
