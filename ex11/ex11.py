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
    pass


def const_function(c):
    """return the mathematical function f such that f(x) = c
    >>> const_function(2)(2)
    2
    >>> const_function(4)(2)
    4
    """
    pass


def identity():
    """return the mathematical function f such that f(x) = x
    >>>identity()(3)
    3
    """
    pass


def sin_function():
    """return the mathematical function f such that f(x) = sin(x)
    >>> sinF()(math.pi/2)
    1.0
    """
    pass


def sum_functions(g, h):
    """return f s.t. f(x) = g(x)+h(x)"""
    pass


def sub_functions(g, h):
    """return f s.t. f(x) = g(x)-h(x)"""
    pass


def mul_functions(g, h):
    """return f s.t. f(x) = g(x)*h(x)"""
    pass

def div_functions(g, h):
    """return f s.t. f(x) = g(x)/h(x)"""
    pass

    # The function solve assumes that f is continuous.
    # solve return None in case of no solution
def solve(f, x0=-10000, x1=10000, epsilon=EPSILON):
    """return the solution to f in the range between x0 and x1"""
    pass

    # inverse assumes that g is continuous and monotonic. 
def inverse(g, epsilon=EPSILON):
    """return f s.t. f(g(x)) = x"""
    pass


def compose(g, h):
    """return the f which is the compose of g and h """
    pass


def derivative(g, delta=DELTA):
    """return f s.t. f(x) = g'(x)"""
    pass


def definite_integral(f, x0, x1, num_of_segments=SEGMENTS):
    """
    return a float - the definite_integral of f between x0 and x1
    >>>definite_integral(const_function(3),-2,3)
    15
    """
    pass


def integral_function(f, delta=0.01):
    """return F such that F'(x) = f(x)"""
    pass


def ex11_func_list():
    """return a list of functions as a solution to q.12"""
    pass


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
    # for f in ex11_func_list():
    #     plot_func(graph, f, -10, 10, SEGMENTS, 'red')

    master.mainloop()
