values = [4, 2, 7]

try:
    print(values[3])
except IndexError as err:
    print(f'Something went wrong: {err}')