from math import pi

import roboticstoolbox as rtb

if __name__ == "__main__":
    L = [
        rtb.RevoluteDH(a=0, alpha=pi / 2, d=0.2433, offset=0),
        rtb.RevoluteDH(a=0.28, alpha=pi, d=0.03, offset=0),
        rtb.RevoluteDH(a=0, alpha=pi / 2, d=0.02, offset=0),
        rtb.RevoluteDH(a=0, alpha=pi / 2, d=0.245, offset=0),
        rtb.RevoluteDH(
            a=0, alpha=pi / 2, d=0.057, offset=0
        ),
        rtb.RevoluteDH(a=0, alpha=0, d=0.235, offset=0),
    ]

    robot = rtb.SerialLink(L, name="kinova_gen3_lite")

    q0 = [0] * 6

    print(robot.fkine(q0))

    robot.teach(q0)
