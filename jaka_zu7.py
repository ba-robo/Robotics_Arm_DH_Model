from math import pi

import numpy as np
import roboticstoolbox as rtb

if __name__ == "__main__":
    L = [
        rtb.RevoluteDH(a=0, alpha=0, d=0.12015, offset=0),
        rtb.RevoluteDH(a=0, alpha=-pi / 2, d=0.0, offset=0),
        rtb.RevoluteDH(
            a=0.360, alpha=0, d=0.00151, offset=0
        ),  # actual in opposite direction
        rtb.RevoluteDH(
            a=0.3035, alpha=0, d=0, offset=0
        ),  # actual in opposite direction
        rtb.RevoluteDH(
            a=0, alpha=-pi / 2, d=0.1135, offset=0
        ),  # actual in opposite direction
        rtb.RevoluteDH(a=0, alpha=-pi / 2, d=0.1135, offset=0),
        rtb.RevoluteDH(a=0, alpha=0, d=0.107, offset=0),
    ]

    robot = rtb.SerialLink(L, name="JAKA_ZU_7")

    q = np.deg2rad([0, 9.99908, 29.4812, -10.7592, 101.206, 29.9507, 89.9513])

    q[2:5] = q[2:5] * -1

    print(q)

    q0 = [0] * 7

    print(robot.fkine(q))

    robot.teach([0] * 7)
