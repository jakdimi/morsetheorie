import matplotlib.pyplot as plt
import numpy as np


def torus(r, R, u, v):
    x = (R + r*np.cos(v))*np.cos(u)
    y = r*np.sin(v)
    z = (R + r*np.cos(v))*np.sin(u)
    return (x, y, z)


def gradf_direction(r, R, u, v):
    y_rot = rotation_matrix([0, -1, 0], u)
    z_rot = rotation_matrix([0, 0, 1], v)
    del_u = np.dot(y_rot, [0, 0, 1])
    del_v = np.dot(y_rot, np.dot(z_rot, [0, 1, 0]))
    return (R + r* np.sin(v))*np.cos(u)*del_u - r*np.sin(v)*np.sin(u)*del_v


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


def plot_fig1_torus_plane(ax):
    ax.computed_zorder=False
    x2 = np.linspace(-5, 5, 5)
    y2 = np.linspace(-5, 5, 5)
    x2, y2 = np.meshgrid(x2, y2)
    z2 = np.ones((5, 5))
    z2 = -4*z2

    ax.plot_surface(x2, y2, z2, color="LightGreen", zorder=1)

    
    N1 = 50
    N2 = 20

    u = np.linspace(0, 2 * np.pi, N1)
    v = np.linspace(0, 2 * np.pi, N2)
    u, v = np.meshgrid(u, v)

    x1, y1, z1 = torus(1, 3, u, v)

    ax.plot_surface(x1, y1, z1, color="LightBlue", zorder=2)

    ax.scatter([0, 0, 0, 0], [0, 0, 0, 0], [-4, -2, 2, 4], color="red", zorder=3)

    ax.text(0, 0, -4.5, "p", zorder=3)
    ax.text(0, 0, -1.5, "q", zorder=3)
    ax.text(0, 0, 1.5, "r", zorder=3)
    ax.text(0, 0, 4.5, "s", zorder=3)

    ax.set_aspect('equal')
    ax.axis('off')
    ax.view_init(elev=10, azim=-99, roll=0)


def plot_fig4_gradient_of_hightmapping(ax):
    ax.computed_zorder=False
    N11 = 50
    N12 = 20

    u1 = np.linspace(0, 2 * np.pi, N11)
    v1 = np.linspace(np.pi, 2 * np.pi, N12)
    u1, v1 = np.meshgrid(u1, v1)

    x1, y1, z1 = torus(1, 3, u1, v1)

    ax.plot_surface(x1, y1, z1, color="LightBlue", zorder=1)

    N21 = 20
    N22 = 5

    u2 = np.linspace(0, 2 * np.pi, N21)
    v2 = np.linspace(np.pi, 2 * np.pi, N22)
    u2, v2 = np.meshgrid(u2, v2)

    x2, y2, z2 = torus(1.01, 3, u2, v2)

    dx = np.zeros((N22, N21))
    dy = np.zeros((N22, N21))
    dz = np.zeros((N22, N21))

    for i, (u_row, v_row) in enumerate(zip(u2, v2)):
        for j, (u_entry, v_entry) in enumerate(zip(u_row, v_row)):
            dx1, dy1, dz1 = gradf_direction(1, 3, u_entry, v_entry)
            dx[i][j] = dx1
            dy[i][j] = dy1
            dz[i][j] = dz1

    # Plot the surface
    ax.quiver(x2, y2, z2, dx, dy, dz, length=0.5, normalize=True, color="red", zorder=2)

    # Set an equal aspect ratio
    ax.set_aspect('equal')
    ax.axis('off')
    ax.view_init(elev=0, azim=-90, roll=0)


if __name__ == "__main__":
    dpi=500
    show=False

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plot_fig1_torus_plane(ax)
    fig.canvas.manager.set_window_title("Me-Diagram1-torus-plane")
    plt.savefig("../results/Me-Diagram1-torus-plane.png", dpi=dpi)
    if show:
        plt.show()
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plot_fig4_gradient_of_hightmapping(ax)
    fig.canvas.manager.set_window_title("Me-Diagram4-gradient-of-hightmapping")
    plt.savefig("../results/Me-Diagram4-gradient-of-hightmapping.png", dpi=dpi)
    if show:
        plt.show()
