import roboticstoolbox as rtb
from math import pi


if __name__ == "__main__":
    L = [
        rtb.RevoluteMDH(a=0, alpha=0, d=0.75, offset=pi/2, filp=True),

        rtb.RevoluteMDH(a=0.255, alpha=-pi / 2, d=0, offset=-pi / 2),

        rtb.RevoluteMDH(a=1.2, alpha=0, d=0, offset=0),                     # passive joint, j3 = -j2

        rtb.RevoluteMDH(a=0.26, alpha=0, d=0, offset=pi / 2, filp=True),

        rtb.RevoluteMDH(a=1.55, alpha=0, d=0, offset=0, filp=True),         # passive joint, j5 = -j4

        rtb.RevoluteMDH(a=0.25, alpha=-pi / 2, d=0.24, offset=pi / 2)
    ]

    robot = rtb.SerialLink(L, name="KAWASAKI_CP130")

    print(robot)

    q0 = [0] * 6

    print(robot.fkine(q0))

    robot.teach(q0)
