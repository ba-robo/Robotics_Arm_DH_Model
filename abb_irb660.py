import roboticstoolbox as rtb
from math import pi

if __name__ == "__main__":
    L = [
        rtb.RevoluteMDH(a=0, alpha=0, d=0.8, offset=0),

        rtb.RevoluteMDH(a=0.3, alpha=-pi / 2, d=0, offset=-pi / 2),

        rtb.RevoluteMDH(a=1.28, alpha=0, d=0, offset=0),        # passive joint, j3 = -j2

        rtb.RevoluteMDH(a=0, alpha=0, d=0, offset=pi / 2),

        rtb.RevoluteMDH(a=1.35, alpha=0, d=0, offset=0),        # passive joint, j5 = -j4

        rtb.RevoluteMDH(a=0.26, alpha=-pi / 2, d=0.247, offset=-pi)
    ]

    robot = rtb.SerialLink(L, name="ABB_IRB660")

    print(robot)

    q0 = [0] * 6

    print(robot.fkine(q0))

    robot.teach(q0)
