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
        return (X1 + X2, Y1 + Y2)
    
    if switched:
        return ((Y1, X1), (Y2, X2))
    
    return ((X1, Y1), (X2, Y2))


def format_axes(ax, labelx=True, labely=True, epsilon=1):
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])

    ax.set_xlabel(r"$(u_1, ..., u_k)$")
    ax.set_ylabel(r"$(u_{k + 1}, ..., u_n)$")

    formatter = FixedFormatter([r"$-\sqrt{\varepsilon}$", r"$0$", r"$\sqrt{\varepsilon}$"])
    locator = FixedLocator([-epsilon, 0, epsilon])
    empty_formatter = FixedFormatter([])
    empty_locator = FixedLocator([])
    if labelx:
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
    else:
        ax.xaxis.set_major_locator(empty_locator)
        ax.xaxis.set_major_formatter(empty_formatter)
    if labely:
        ax.yaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(formatter)
    else:
        ax.yaxis.set_major_locator(empty_locator)
        ax.yaxis.set_major_formatter(empty_formatter)


def plot_fig1_U_parameterized(ax, del_x=0.01):
    X = list(np.arange(-3, 3, del_x))
    ((h1X1, h1Y1), (h1X2, h1Y2)) = ellipse_parameterize(-1, 1, 1, X)
    ((h2X1, h2Y1), (h2X2, h2Y2)) = ellipse_parameterize(1, -1, 1, X)
    (cX, cY) = ellipse_parameterize(1, 1, 2, X)

    # M^{c + \varepsilon}
    ax.fill_between(h1X1, h1Y1, h1Y2, color="LightBlue", zorder=1)
    # f = c + \varepsilon
    ax.plot(h1X1, h1Y1, color="black", zorder=1)
    ax.plot(h1X2, h1Y2, color="black", zorder=1)
    # e^k
    ax.plot([-2, 2], [0, 0], color="red", zorder=2.5)
    # M^{c - \varepsilon}
    ax.fill_betweenx(h2Y1, h2X1, 2, color="LightGreen", zorder=3)
    plt.fill_betweenx(h2Y2, h2X2, -2, color="LightGreen", zorder=3)
    # f = c - \varepsilon
    ax.plot(h2X1, h2Y1, color="black", zorder=3)
    ax.plot(h2X2, h2Y2, color="black", zorder=3)
    
    # f = c
    ax.plot([-2, 2], [-2, 2], "--",  color="blue", zorder= 1)
    ax.plot([-2, 2], [2, -2], "--", color="blue", zorder= 1)

    # \eta + \xi = 2 \vaepsilon
    plt.plot(cX, cY, color="black", zorder=4)

    # p
    ax.scatter([0],[0], color="blue", zorder=5)

    # boundary of e^k
    ax.scatter([-1, 1],[0, 0], color="red", zorder=5)

    # annotate
    ax.annotate(r"$p$", (0.05, -0.05))
    ax.annotate(r"$M^{c - \varepsilon}$", (-1.9, 0))
    ax.annotate(r"$M^{c + \varepsilon}$", (-0.4, 0.8))
    ax.annotate(r"$\xi + \eta = \varepsilon$", (0.4, -1.45))
    ax.annotate(r"$f = c + \varepsilon$", (-1.45, -1.9))
    ax.annotate(r"$f = c - \varepsilon$", (1.55, -1.1))
    ax.annotate(r"$f = c$", (1.9, -1.85), color="blue")
    ax.annotate(r"$e^k$", (0.8, -0.13), color="red")
    
    format_axes(ax)


def plot_fig2_handle(ax, del_x=0.01):
    X = list(np.arange(-3, 3, del_x))
    ((h1X1, h1Y1), (h1X2, h1Y2)) = ellipse_parameterize(-1, 1, 1, X)
    ((h2X1, h2Y1), (h2X2, h2Y2)) = ellipse_parameterize(1, -1, 1, X)
    ((h3X1, h3Y1), (h3X2, h3Y2)) = ellipse_parameterize(-0.3, 3, 0.05, X)

    # Fill M^{c + \varepslon}
    ax.fill_between(h1X1, h1Y1, h1Y2, color="LightBlue", zorder=1)
    # Outline M^{c + \varepsilon}
    ax.plot(h1X1, h1Y1, color="black", zorder=1)
    ax.plot(h1X2, h1Y2, color="black", zorder=1)
    # Fill Handle
    ax.fill_between(h3X1, h3Y1, h3Y2, color="LightYellow", zorder=2)
    # Outline Handle
    ax.plot(h3X1, h3Y1, color="black", zorder=2)
    ax.plot(h3X2, h3Y2, color="black", zorder=2)
    # Fill M^{c - \varepsilon}
    ax.fill_betweenx(h2Y1, h2X1, 2, color="LightGreen", zorder=3)
    ax.fill_betweenx(h2Y2, h2X2, -2, color="LightGreen", zorder=3)
    # Outline M^{c - \varepsilon}
    ax.plot(h2X1, h2Y1, color="black", zorder=3)
    ax.plot(h2X2, h2Y2, color="black", zorder=3)
    # p
    ax.scatter([0],[0], color="blue", zorder=4)
    ax.annotate(r"$p$", (0.05, -0.05))
    # Format axes
    format_axes(ax)


def plot_fig3_handle_ellipse(ax, del_x=0.01):
    X = list(np.arange(-3, 3, del_x))

    plot_fig2_handle(ax, del_x=del_x)

    (eX, eY) = ellipse_parameterize(1, 2, 2, X)

    # Plot Ellipse
    plt.plot(eX, eY, color="black", zorder=10)



def plot_fig4_handle_cases(ax, del_x=0.01):
    X = list(np.arange(-3, 3, del_x))

    ((h1X1, h1Y1), (h1X2, h1Y2)) = ellipse_parameterize(1, -1, 1, X)
    ((h2X1, h2Y1), (h2X2, h2Y2)) = ellipse_parameterize(-1, 3, 1, X)
    ((lX1, lY1), (lX2, lY2)) = ellipse_parameterize(1, 0, 1, X)

    case1 = [ x >= -1 and x <= 1 for x in h2X1 ]

    # Fill Handle
    ax.fill_between(h2X1, h2Y1, h2Y2, color="LightYellow", zorder=1)
    ax.fill_between(h2X1, h2Y1, h2Y2, color="orange", where=case1, zorder=1)

    # Border Case 1 and 2
    ax.plot(lX1, lY1, color="black", zorder=2)
    ax.plot(lX2, lY2, color="black", zorder=2)

    # Fill white
    ax.fill_between(h2X1, h2Y1, 2, color="white", zorder=3)
    ax.fill_between(h2X2, h2Y2, -2, color="white", zorder=3)
    ax.plot(h2X1, h2Y1, color="black", zorder=3)
    ax.plot(h2X2, h2Y2, color="black", zorder=3)

    # Fill M^{c - \varepsilon}
    ax.fill_betweenx(h1Y1, h1X1, 2,color="LightGreen", zorder=4)
    ax.fill_betweenx(h1Y2, h1X2, -2, color="LightGreen", zorder=4)
    
    # Outlines M^{c - \varepsilon}
    ax.plot(h1X1, h1Y1, color="black", zorder=5)
    ax.plot(h1X2, h1Y2, color="black", zorder=5)

    format_axes(ax, labely=False)
    

if __name__ == "__main__":
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig1_U_parameterized(ax1, del_x=0.001)
    fig.canvas.manager.set_window_title("Me-Diagram6-U-parameterized")
    plt.show()
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig2_handle(ax1, del_x=0.001)
    fig.canvas.manager.set_window_title("Me-Diagram7-handle")
    plt.show()
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig3_handle_ellipse(ax1, del_x=0.001)
    fig.canvas.manager.set_window_title("Me-Diagram8-handle-ellipse")
    plt.show()
    fig, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    plot_fig4_handle_cases(ax1, del_x=0.001)
    fig.canvas.manager.set_window_title("Me-Diagram9-handle-cases")
    plt.show()