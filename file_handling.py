from tqdm import tqdm


def read(file_name):
    with open('input/'+file_name, 'r') as f:
        capacity, types_count = [int(x) for x in f.readline().split()]
        pizzas = [int(slices) for slices in tqdm(f.readline().split(), 'reading')]
    return capacity, pizzas


def write(file_name, types_count, selected_pizzas):
    with open('output/'+file_name.replace('in', 'out'), 'w') as f:
        f.write(str(types_count) + '\n')
        for pizza in selected_pizzas:
            f.write(str(pizza) + ' ')


if __name__ == '__main__':
    capacity, pizzas = read('a_example.in')