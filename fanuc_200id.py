from math import pi

import numpy as np
import roboticstoolbox as rtb

if __name__ == "__main__":
    L = [
        rtb.RevoluteDH(a=0, alpha=0, d=0.33, offset=0),
        rtb.RevoluteDH(a=0.050, alpha=-pi / 2, d=0.0, offset=0),
        rtb.RevoluteDH(a=0.440, alpha=0, d=0.00151, offset=-pi / 2),
        rtb.RevoluteDH(a=0.035, alpha=-pi / 2, d=0, offset=0),
        rtb.RevoluteDH(a=0, alpha=pi / 2, d=0.420, offset=0),
        rtb.RevoluteDH(a=0, alpha=-pi / 2, d=0.0, offset=0),
        rtb.RevoluteDH(a=0, alpha=0, d=0.080, offset=0),
    ]

    robot = rtb.SerialLink(L, name="Fanuc_LR_Mate_200iD_7L")

    q = np.deg2rad([0, 10.0206, 20.003, 30.0118, -90.0543, -29.987, -90.0976])

    q[3:] = q[3:] * -1

    print(q)

    print(robot.fkine(q))

    robot.teach(q)
