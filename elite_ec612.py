import roboticstoolbox as rtb
from math import pi

if __name__ == "__main__":
    # L = [
    #     rtb.RevoluteMDH(a=0, alpha=0, d=0.185, offset=0),
    #
    #     rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.174, offset=0),
    #
    #     rtb.RevoluteMDH(a=0.615, alpha=0, d=0, offset=0),
    #
    #     rtb.RevoluteMDH(a=0.5725, alpha=0, d=0, offset=0),
    #
    #     rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.1165, offset=0),
    #
    #     rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.1038, offset=0)
    # ]

    L = [
        rtb.RevoluteMDH(a=0, alpha=0, d=0.185, offset=0),

        rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.174, offset=0),

        rtb.RevoluteMDH(a=0.615, alpha=0, d=0, offset=0),

        rtb.RevoluteMDH(a=0.5725, alpha=0, d=0, offset=0),

        rtb.RevoluteMDH(a=0, alpha=pi / 2, d=-0.1165, offset=pi, flip=True),       # actually joint 5 is positive

        rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.1038, offset=pi)
    ]

    robot = rtb.SerialLink(L, name="Elite_ec612")

    q0 = [0] * 6

    print(robot.fkine(q0))

    robot.teach(q0)
