import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
import numpy as np

sqrt = np.sqrt
abs = np.abs

def ellipse_parameterize(a, b, c, X):
    """ 
    Parameters are from the equation plt^2 + by^2 = c, X is a list of possible x-values. 
    Returns a list of pairs of x- and y-values
    """
    if c < 0:
        a = -a
        b = -b 
        c = -c

    if (a < 0 and b <= 0) or (a == 0 and b == 0):
        return [[],[],[]]
    
    switched = False
    if b <= 0:
        switched = True
        a, b = b, a

    X1, X2, Y1, Y2 = [], [], [], []
    for x in X:
        y_sq = (c - a*x*x)/b
        if y_sq >= 0:
            X1.append(x)
            X2.append(x)
            Y1.append(sqrt(y_sq))
            Y2.append(-sqrt(y_sq))
    
    if a > 0 and b > 0:
        # plot a real ellipse 
        X2.reverse()
        Y2.reverse()
        X2.append(X1[0])
        Y2.append(Y1[0])
        return [(X1 + X2, Y1 + Y2)]
    
    if switched:
        return [(Y1, X1), (Y2, X2)]
    
    return [(X1, Y1), (X2, Y2)]


def format_axes(ax, epsilon=1):
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])

    ax.set_xlabel(r"$(u_1, ..., u_k)$")
    ax.set_ylabel(r"$(u_{k + 1}, ..., u_n)$")

    formatter = FixedFormatter([r"$-\varepsilon$", r"$0$", r"$\varepsilon$"])
    locator = FixedLocator([-epsilon, 0, epsilon])
    ax.xaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_locator(locator)
    ax.yaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_locator(locator)


def plot_fig1(ax, annotate=True, draw_lines=True, draw_circle=True, del_x=0.01):
    X = list(np.arange(-2, 2, del_x))
    hyperbola1 = ellipse_parameterize(-1, 1, 1, X)
    h1X1, h1Y1 = hyperbola1[0]
    h1X2, h1Y2 = hyperbola1[1]
    hyperbola2 = ellipse_parameterize(1, -1, 1, X)
    h2X1, h2Y1 = hyperbola2[0]
    h2X2, h2Y2 = hyperbola2[1]
    circle = ellipse_parameterize(1, 1, 2, X)
    cX, cY = circle[0]

    # M^{c + \varepsilon}
    ax.fill_between(h1X1, h1Y1, h1Y2, color="LightBlue", zorder=1)
    # f = c + \varepsilon
    ax.plot(h1X1, h1Y1, color="black", zorder=1)
    ax.plot(h1X2, h1Y2, color="black", zorder=1)
    # M^{c - \varepsilon}
    ax.fill_betweenx(h2Y1, h2X1, 2, color="LightGreen", zorder=3)
    plt.fill_betweenx(h2Y2, h2X2, -2, color="LightGreen", zorder=3)
    # f = c - \varepsilon
    ax.plot(h2X1, h2Y1, color="black", zorder=3)
    ax.plot(h2X2, h2Y2, color="black", zorder=3)
    
    if draw_lines:
        # f = c
        ax.plot([-2, 2], [-2, 2], "--",  color="blue", zorder= 1)
        ax.plot([-2, 2], [2, -2], "--", color="blue", zorder= 1)

    if draw_circle:
        # \eta + \xi = 2 \vaepsilon
        plt.plot(cX, cY, color="black", zorder=4)
    # p
    ax.scatter([0],[0], zorder=5)
    ax.annotate(r"$p$", (0.05, -0.05))

    if annotate:
        ax.annotate(r"$M^{c - \varepsilon}$", (-1.9, 0))
        ax.annotate(r"$M^{c + \varepsilon}$", (-0.4, 0.8))
        ax.annotate(r"$\xi + \eta = \varepsilon$", (0.4, -1.45))
        ax.annotate(r"$f = c + \varepsilon$", (-1.45, -1.9))
        ax.annotate(r"$f = c - \varepsilon$", (1.55, -1.1))
        ax.annotate(r"$f = c$", (1.9, -1.85), color="blue")
    
    format_axes(ax)


def plot_fig2(ax, del_x=0.01):
    X = list(np.arange(-2, 2, del_x))
    hyperbola3 = ellipse_parameterize(-0.3, 3, 0.05, X)
    h3X1, h3Y1 = hyperbola3[0]
    h3X2, h3Y2 = hyperbola3[1]

    plot_fig1(ax, annotate=False, draw_lines=False, draw_circle=False, del_x=del_x)

    # H
    plt.fill_between(h3X1, h3Y1, h3Y2, color="LightYellow", zorder=2)
    # H outline
    plt.plot(h3X1, h3Y1, color="black", zorder=2)
    plt.plot(h3X2, h3Y2, color="black", zorder=2)


def plot_fig3(ax, del_x=0.01):
    X = list(np.arange(-2, 2, del_x))

    plot_fig2(ax, del_x=del_x)

    ellipse1 = ellipse_parameterize(1, 2, 2, X)
    eX, eY = ellipse1[0]

    plt.plot(eX, eY, color="black", zorder=10)



def plot_fig4(ax, del_x=0.01):
    X = list(np.arange(-2, 2, del_x))

    ax.tick_params(
        which='both',
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False)
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_xlabel(r"$(u_1, ..., u_k)$")
    ax.set_ylabel(r"$(u_{k + 1}, ..., u_n)$")

    hyperbola1 = ellipse_parameterize(1, -1, 1, X)
    h1X1, h1Y1 = hyperbola1[0]
    h1X2, h1Y2 = hyperbola1[1]
    hyperbola2 = ellipse_parameterize(-1, 3, 1, X)
    h2X1, h2Y1 = hyperbola2[0]
    h2X2, h2Y2 = hyperbola2[1]

    case1 = [ x >= -1 and x <= 1 for x in h2X1 ]

    # Handle
    ax.fill_between(h2X1, h2Y1, h2Y2, color="LightYellow", zorder=1)
    ax.fill_between(h2X1, h2Y1, h2Y2, color="orange", where=case1, zorder=2)
    ax.plot(h2X1, h2Y1, color="black", zorder=2)
    ax.plot(h2X2, h2Y2, color="black", zorder=2)

    # M^{c - \varepsilon}
    ax.fill_betweenx(h1Y1, h1X1, 2,color="LightGreen", zorder=2)
    ax.fill_betweenx(h1Y2, h1X2, -2, color="LightGreen", zorder=2)
    ax.plot(h1X1, h1Y1, color="black", zorder=3)
    ax.plot(h1X2, h1Y2, color="black", zorder=3)
    

if __name__ == "__main__":
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig1(ax1, del_x=0.001)
    plt.show()
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig2(ax1, del_x=0.001)
    plt.show()
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig3(ax1, del_x=0.001)
    plt.show()
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig4(ax1, del_x=0.001)
    plt.show()