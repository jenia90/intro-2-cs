#!/usr/bin/env python3

import math

EPSILON = 1e-5
DELTA = 1e-3
SEGMENTS = 100


def plot_func(graph, f, x0, x1, num_of_segments=SEGMENTS, c='black'):
    """
    plot f between x0 and x1 using num_of_segments straight lines.
    use the plot_line function in the graph object. 
    f will be plotted to the screen with color c.
    """
    segment = (x1 - x0) / num_of_segments
    # set the starting point
    prev_p = x0, f(x0)
    next_p = x0 + segment
    # iterate through every value in the range of the function
    while next_p <= x1:
        graph.plot_line(prev_p, (next_p, f(next_p)), c)
        prev_p = next_p, f(next_p)
        next_p += segment


def const_function(c):
    """return the mathematical function f such that f(x) = c
    >>> const_function(2)(2)
    2
    >>> const_function(4)(2)
    4
    """
    return lambda x: c


def identity():
    """return the mathematical function f such that f(x) = x
    >>>identity()(3)
    3
    """
    return lambda x: x


def sin_function():
    """return the mathematical function f such that f(x) = sin(x)
    >>> sinF()(math.pi/2)
    1.0
    """
    return lambda x: math.sin(x)


def sum_functions(g, h):
    """return f s.t. f(x) = g(x)+h(x)"""
    return lambda x: g(x) + h(x)


def sub_functions(g, h):
    """return f s.t. f(x) = g(x)-h(x)"""
    return lambda x: g(x) - h(x)


def mul_functions(g, h):
    """return f s.t. f(x) = g(x)*h(x)"""
    return lambda x: g(x) * h(x)


def div_functions(g, h):
    """return f s.t. f(x) = g(x)/h(x)"""
    return lambda x: g(x) / h(x)


    # The function solve assumes that f is continuous.
    # solve return None in case of no solution
def solve(f, x0=-10000, x1=10000, epsilon=EPSILON):
    """return the solution to f in the range between x0 and x1"""
    if f(x0) * f(x1) >= 0:
        return None

    mid = (x0 + x1) / 2.0

    while abs(x1 - x0) / 2.0 > epsilon:
        if f(mid) == 0:
            return mid
        elif f(x0) * f(mid) < 0:
            x1 = mid
        else:
            x0 = mid
        mid = (x0 + x1) / 2
    return mid


    # inverse assumes that g is continuous and monotonic. 
def inverse(g, epsilon=EPSILON):
    """return f s.t. f(g(x)) = x"""
    def f(y):
        bound = 100
        while True:
            sol = solve(lambda x: g(x) - y, -bound, bound, epsilon)
            if sol is not None:
                return sol

            bound *= 2

    return f


def compose(g, h):
    """return the f which is the compose of g and h """
    return lambda x: g(h(x))


def derivative(g, delta=DELTA):
    """return f s.t. f(x) = g'(x)"""
    return lambda x: (g(x + delta) - g(x)) / delta


def definite_integral(f, x0, x1, num_of_segments=SEGMENTS):
    """
    return a float - the definite_integral of f between x0 and x1
    >>>definite_integral(const_function(3),-2,3)
    15
    """
    if num_of_segments > 0:
        segment = (x1 - x0) / num_of_segments
        s = 0
        for i in range(1, num_of_segments+1):
            xi = segment * i + x0
            xi_prev = segment * (i-1) + x0
            s += f((xi + xi_prev) / 2)*(xi - xi_prev)
        return s


def integral_function(f, delta=0.01):
    """return F such that F'(x) = f(x)"""
    def F(x):
        num_of_segments = math.ceil(abs(x) / delta)

        if x > 0:
            return definite_integral(f, 0, x, num_of_segments)
        elif x < 0:
            return -definite_integral(f, x, 0, num_of_segments)
        else:
            return 0

    return F


def ex11_func_list():
    """return a list of functions as a solution to q.12"""
    id_pow = mul_functions(identity(), identity())
    cos = derivative(sin_function())
    func_list = []

    func_list.append(const_function(4))

    func_list.append(sum_functions(sin_function(), const_function(4)))

    func_list.append(compose(sin_function(), sum_functions(const_function(4), identity())))

    func_list.append(mul_functions(
            sin_function(), div_functions(
                    mul_functions(id_pow,const_function(2)),const_function(100))))

    func_list.append(div_functions(sin_function(),
                           sum_functions(cos, const_function(2))))

    func_list.append(integral_function(
            sub_functions(sum_functions(id_pow, identity()), const_function(3))))

    func_list.append(inverse(mul_functions(id_pow,identity())))

    return func_list

# function that genrate the figure in the ex description
def example_func(x):
    return (x/5)**3

if __name__ == "__main__":
    import tkinter as tk
    from ex11helper import Graph
    master = tk.Tk()
    graph = Graph(master, -10, -10, 10, 10)
    # un-tag the line below after implementation of plot_func
    # plot_func(graph,example_func,-10,10,SEGMENTS,'red')
    color_arr = ['black', 'blue', 'red', 'green', 'brown', 'purple',
                 'dodger blue', 'orange']
    # un-tag the lines below after implementation of ex11_func_list
    for f in ex11_func_list():
        plot_func(graph, f, -10, 10, SEGMENTS, 'red')

    master.mainloop()
