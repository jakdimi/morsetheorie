import matplotlib.pyplot as plt
import numpy as np

sqrt = np.sqrt
abs = np.abs

def ellipse_parameterize(a, b, c, X):
    """ 
    Parameters are from the equation ax^2 + by^2 = c, X is a list of possible x-values. 
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
        return [(Y1, X1),(Y2, X2)]
    
    return [(X1, Y1), (X2, Y2)]
    

def plot_fig1():
    X = list(np.arange(-2, 2, 0.01))
    hyperbola1 = ellipse_parameterize(-1, 1, 1, X)
    h1X1, h1Y1 = hyperbola1[0]
    h1X2, h1Y2 = hyperbola1[1]
    hyperbola2 = ellipse_parameterize(1, -1, 1, X)
    h2X1, h2Y1 = hyperbola2[0]
    h2X2, h2Y2 = hyperbola2[1]
    circle = ellipse_parameterize(1, 1, 2, X)
    cX, cY = circle[0]

    plt.figure(figsize=(7, 7))

    # M^{c + \varepsilon}
    plt.fill_between(h1X1, h1Y1, h1Y2, color="LightBlue", zorder=1)
    # f = c + \varepsilon
    plt.plot(h1X1, h1Y1, color="black", zorder=1)
    plt.plot(h1X2, h1Y2, color="black", zorder=1)
    # M^{c - \varepsilon}
    plt.fill_betweenx(h2Y1, h2X1, 2, color="LightGreen", zorder=3)
    plt.fill_betweenx(h2Y2, h2X2, -2, color="LightGreen", zorder=3)
    # f = c - \varepsilon
    plt.plot(h2X1, h2Y1, color="black", zorder=3)
    plt.plot(h2X2, h2Y2, color="black", zorder=3)
    # \eta + \xi = 2 \vaepsilon
    plt.plot(cX, cY, color="black", zorder=4)
    # p
    plt.scatter([0],[0], zorder=5)
    plt.annotate("p", (0.05, -0.05))
    plt.axis([-2, 2, -2, 2])


def plot_fig2():
    X = list(np.arange(-2, 2, 0.01))
    hyperbola3 = ellipse_parameterize(-0.3, 3, 0.05, X)
    h3X1, h3Y1 = hyperbola3[0]
    h3X2, h3Y2 = hyperbola3[1]

    plot_fig1()

    # H
    plt.fill_between(h3X1, h3Y1, h3Y2, color="LightYellow", zorder=2)
    # H outline
    plt.plot(h3X1, h3Y1, color="black", zorder=2)
    plt.plot(h3X2, h3Y2, color="black", zorder=2)
    

if __name__ == "__main__":
    plot_fig1()
    plt.show()