import roboticstoolbox as rtb
from math import pi

if __name__ == "__main__":
    L = [
        rtb.PrismaticDH(a=0, alpha=pi / 2, theta=pi, qlim=[0, 2]),  # y-axis
        rtb.PrismaticDH(a=0, alpha=pi / 2, theta=0, qlim=[0, 2]),  # x-axis
        rtb.PrismaticDH(a=0, alpha=-pi / 2, theta=-pi / 2, qlim=[0, 0.5]),    # z-axis
        rtb.PrismaticDH(a=0, alpha=0, theta=0, qlim=[-0.4, 0.2]),    # z-axis
    ]

    robot = rtb.SerialLink(L, name="Gantry")

    print(robot)

    robot.teach([0.1] * 4)
