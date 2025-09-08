from math import pi

import roboticstoolbox as rtb

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
        rtb.RevoluteDH(a=0, alpha=pi / 2, d=0.2433, offset=0),
        rtb.RevoluteDH(a=0.28, alpha=pi, d=0.03, offset=0),
        rtb.RevoluteDH(a=0, alpha=pi / 2, d=0.02, offset=0),
        rtb.RevoluteDH(a=0, alpha=pi / 2, d=0.245, offset=0),
        rtb.RevoluteDH(
            a=0, alpha=pi / 2, d=0.057, offset=0
        ),  # actually joint 5 is positive
        rtb.RevoluteDH(a=0, alpha=0, d=0.235, offset=0),
    ]

    robot = rtb.SerialLink(L, name="kinova_gen3_lite")

    q0 = [0] * 6

    print(robot.fkine(q0))

    robot.teach(q0)
