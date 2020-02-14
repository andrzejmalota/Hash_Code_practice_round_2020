from tqdm import tqdm
import numpy as np


def solve_dynamic(capacity, pizzas):
    values = pizzas
    weights = pizzas

    items_ids = [[[] for c in range(capacity + 1)] for r in range(len(values) + 1)]
    profits = [[0 for c in range(capacity + 1)] for r in range(len(values) + 1)]

    for r in tqdm(range(1, len(values) + 1), 'solving'):
        for c in range(1, capacity + 1):
            if weights[r - 1] <= c:
                remaining_capacity = c - weights[r - 1]
                if profits[r - 1][remaining_capacity] + values[r - 1] > profits[r - 1][c]:
                    if sum([weights[x] for x in items_ids[r - 1][remaining_capacity]]) + weights[r - 1] <= c:
                        profits[r][c] = profits[r - 1][remaining_capacity] + values[r - 1]
                        items_ids[r][c] += items_ids[r - 1][remaining_capacity]
                        items_ids[r][c].append(r - 1)
                else:
                    if values[r - 1] > profits[r - 1][c]:
                        profits[r][c] = values[r - 1]
                        items_ids[r][c].append(r - 1)
                    else:
                        profits[r][c] = profits[r - 1][c]
                        items_ids[r][c] += items_ids[r - 1][c]
            else:
                profits[r][c] = profits[r - 1][c]
                items_ids[r][c] += items_ids[r - 1][c]

    return len(items_ids[-1][-1]), items_ids[-1][-1]


def solve_greedy(capacity, pizzas):
    remaining_capacity = capacity
    selected_pizzas = []

    for i in range(len(pizzas)-1, 0, -1):
        if remaining_capacity - pizzas[i] >= 0:
            selected_pizzas.append(i)
            remaining_capacity -= pizzas[i]

    return len(selected_pizzas), selected_pizzas


def solve_greedy_with_replacement(capacity, pizzas):
    remaining_capacity = capacity
    selected_pizzas = []

    for i in range(len(pizzas)):
        if remaining_capacity - pizzas[i] >= 0:
            selected_pizzas.append(i)
            remaining_capacity -= pizzas[i]
        else:
            remaining_capacity -= (pizzas[i] - selected_pizzas[-1])
            selected_pizzas[-1] = i

    return len(selected_pizzas), selected_pizzas
