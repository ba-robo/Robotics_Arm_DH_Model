from math import pi

import roboticstoolbox as rtb

if __name__ == "__main__":
    # air20a
    L = [
        rtb.RevoluteMDH(a=0, alpha=0, d=0.445, offset=0),
        rtb.RevoluteMDH(a=0.217, alpha=-pi / 2, d=0, offset=-pi / 2),
        rtb.RevoluteMDH(a=0.73, alpha=0, d=0, offset=-pi / 2),
        rtb.RevoluteMDH(a=0.15, alpha=-pi / 2, d=0.74, offset=0),
        rtb.RevoluteMDH(a=0, alpha=pi / 2, d=0, offset=0),
        rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.12, offset=pi),
    ]

    # # air10a
    # L = [
    #     rtb.RevoluteMDH(a=0, alpha=0, d=0.42, offset=0),
    #
    #     rtb.RevoluteMDH(a=0.185, alpha=-pi / 2, d=0, offset=-pi / 2),
    #
    #     rtb.RevoluteMDH(a=0.6, alpha=0, d=0, offset=-pi/2),
    #
    #     rtb.RevoluteMDH(a=0.12, alpha=-pi/2, d=0.624, offset=0),
    #
    #     rtb.RevoluteMDH(a=0, alpha=pi/2, d=0, offset=0),
    #
    #     rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.116, offset=pi)
    # ]

    robot = rtb.SerialLink(L, name="AE_air20a")

    print(robot)

    q0 = [1] * 6

    print(robot.fkine(q0))

    robot.teach(q0)
