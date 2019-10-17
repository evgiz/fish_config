
# <equation f(x)>

import sys
import argparse
import numpy
import matplotlib.pyplot as plt

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("\033[93mUsage: plot <equation>")
        exit(-1)

    start = 0
    stop = 1

    if len(sys.argv) == 4:
        start = int(sys.argv[3])
        stop = int(sys.argv[4])
    elif len(sys.argv) == 3:
        point = int(sys.argv[2])
        if point < 0:
            stat = point
        else:
            stop = point
        
    equation = sys.argv[1]
    orig_equ = equation

    equation = equation.replace("log(", "numpy.log(")
    equation = equation.replace("log2(", "numpy.log2(")
    equation = equation.replace("sin(", "numpy.sin(")
    equation = equation.replace("cos(", "numpy.cos(")
    equation = equation.replace("tan(", "numpy.tan(")
    equation = equation.replace("exp(", "numpy.exp(")

    xs = numpy.linspace(start, stop, 1000)
    ys = []

    x = 0
    for _x in xs:
        x = _x
        try:
            ys.append(eval(equation))
        except (SyntaxError, AttributeError) as err:
            print("\033[93mFailed to parse ", equation)
            print("\033[91m" + str(err))
            exit(-1)

    plt.plot(xs, ys)
    plt.draw()
    plt.title(orig_equ)
    plt.pause(.01)
    input("\033[92mPress any key to finish...")
    plt.close()