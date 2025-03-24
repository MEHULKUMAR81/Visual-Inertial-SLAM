import numpy as np

def se3_hat(xi):
    """Convert 6D twist vector to se(3) matrix."""
    v, w = xi[:3], xi[3:]
    w_hat = np.array([
        [0, -w[2], w[1]],
        [w[2], 0, -w[0]],
        [-w[1], w[0], 0]
    ])
    se3 = np.zeros((4, 4))
    se3[:3, :3] = w_hat
    se3[:3, 3] = v
    return se3
