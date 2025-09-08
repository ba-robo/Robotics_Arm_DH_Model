from math import pi

import roboticstoolbox as rtb

if __name__ == "__main__":
    L = [
        rtb.PrismaticMDH(a=0, alpha=-pi / 2, theta=-pi / 2, qlim=[0, 2]),  # y-axis
        rtb.PrismaticMDH(a=0, alpha=-pi / 2, theta=-pi / 2, qlim=[0, 2]),  # x-axis
        rtb.PrismaticMDH(a=0, alpha=-pi / 2, theta=0, qlim=[0, 0.4]),  # z-axis
        rtb.RevoluteMDH(a=0, alpha=0, d=0.4865, offset=0),
        rtb.RevoluteMDH(a=0.15, alpha=-pi / 2, d=0, offset=-pi / 2),
        rtb.RevoluteMDH(a=0.7, alpha=0, d=0, offset=0),
        rtb.RevoluteMDH(a=0.11, alpha=-pi / 2, d=0.678, offset=0),
        rtb.RevoluteMDH(a=0, alpha=pi / 2, d=0, offset=0),
        rtb.RevoluteMDH(a=0, alpha=-pi / 2, d=0.135, offset=pi),
    ]

    robot = rtb.SerialLink(L, name="Mobile_ABB_IRB1660id")

    print(robot)

    robot.teach([0] * 9)
