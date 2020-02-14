from file_handling import read, write
from solvers import solve_dynamic, solve_greedy, solve_greedy_with_replacement


def main():
    input_files = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']

    # Dynamic programming
    for input_file in input_files[:3]:
        capacity, pizzas = read(input_file)
        types_count, selected_pizzas = solve_dynamic(capacity, pizzas)
        write(input_file, types_count, selected_pizzas)

    # Greedy algorithm
    for input_file in input_files[3:]:
        capacity, pizzas = read(input_file)
        types_count, selected_pizzas = solve_greedy_with_replacement(capacity, pizzas)
        write(input_file, types_count, selected_pizzas)


if __name__ == '__main__':
    main()