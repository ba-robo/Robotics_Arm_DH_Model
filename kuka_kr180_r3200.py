import roboticstoolbox as rtb
from math import pi

if __name__ == "__main__":
    L = [
        rtb.RevoluteMDH(a=0, alpha=0, d=0.675, offset=0),

        rtb.RevoluteMDH(a=0.35, alpha=-pi / 2, d=0, offset=0),

        rtb.RevoluteMDH(a=1.35, alpha=0, d=0, offset=0),        # passive joint

        rtb.RevoluteMDH(a=0, alpha=0, d=0, offset=0),

        rtb.RevoluteMDH(a=1.22, alpha=0, d=0, offset=0),        # passive joint

        rtb.RevoluteMDH(a=0.28, alpha=-pi / 2, d=0.25, offset=-pi)
    ]

    robot = rtb.SerialLink(L, name="KUKA_KR180_R3200")

    print(robot)

    q0 = [0] * 6

    print(robot.fkine(q0))

    robot.teach(q0)
