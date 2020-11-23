import matplotlib.pyplot as plt
import numpy as np

def make_graph(a, delta, f, X):
    func_values = [f(x) for x in X]
    plt.plot(X, func_values)
    func_domain = list(X)
    func_range = list(func_values)
    a_minus_delta = abs(a - delta)
    a_plus_delta = abs(a + delta)
    domain_min = min(func_domain)
    domain_max = max(func_domain)
    range_min = min(func_range)
    range_max = max(func_range)

    # Grid
    plt.xlim(domain_min, domain_max)
    plt.ylim(range_min, range_max)
    plt.axhline(color='black', lw=0.5)
    plt.axvline(color='black', lw=0.5)

    # Limits and ticks

    # plt.grid('None', 'both', 'x')

    # plt.xticks([x for x in range(domain_min, domain_max + 1)] + [f'{a}', f'{a_minus_delta}', f'{a_plus_delta}'], fontsize='x-small')
    # plt.yticks([range_min, range_max, f(a), f(a_minus_delta), f(a_plus_delta)], fontsize='x-small')

    # plt.xticks([0, domain_max, a, a_minus_delta, a_plus_delta])
    # plt.yticks([0, range_max, f(a), f(a_minus_delta), f(a_plus_delta)])
    # Delta lines
    color_delta = "brown"
    plt.vlines(a_minus_delta, 0, f(a_minus_delta), linestyles='dashed', colors=color_delta)
    plt.vlines(a_plus_delta, 0, f(a_plus_delta), linestyles='dashed', colors=color_delta)
    plt.hlines(f(a_minus_delta), 0, a_minus_delta, linestyles='dashed', colors=color_delta)
    plt.hlines(f(a_plus_delta), 0, a_plus_delta, linestyles='dashed', colors=color_delta)
    plt.vlines(a, 0, f(a), linestyles='dashed', colors='purple')
    plt.hlines(f(a), 0, a, linestyles='dashed', colors='purple')
    plt.show()

if __name__ == '__main__':
    f = lambda x: x**2
    make_graph(3, 0.5, f, range(10))