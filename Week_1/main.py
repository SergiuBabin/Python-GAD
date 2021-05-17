# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

#
# my_int = 7
# print('my_int', my_int, type(my_int))
# my_float_from_int = float(my_int)
# print('my_float_from_int', my_float_from_int, type(my_float_from_int))
#
#
# my_complex = 3+5j
# print('my_complex', my_complex, type(my_complex))
#
# my_div = 1 // 2
# print('my_div', my_div)
#
# print(1 in [1,2,3])
# print('p' in 'python')

# price = 20.00
# name = 'Burger'
# msg = 'Top Product: {a} cost only ${b:.2f}.'.format(a=name, b=price)
# print('msg', msg)

# price = 20.00
# name = 'Burger'
# msg = f'Top Product: {name} cost only ${price:.2f}.'
# print('msg', msg)

# price = 20.00
# name = 'Burger'
# msg = 'Top Product: %s cost only $%.2f.' % (name, price)
# print('msg', msg)

# my_list = [8, 2, -3, "a", True]
# print(my_list, type(my_list))
# print(False in my_list)

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(len(my_list))

# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])

# new_list = my_list[0:2:2]
# print("new_list", new_list)

# my_list[2] = ['a', [1, 2], 4, 5, 6, 7]
# print(my_list)
# print(my_list[2])
# print(my_list[2][1])
# print(my_list[2][1][0])

# new_list = my_list[::-1]
# print(my_list)
# print(new_list)


# Tupluri
#
# print(my_list, type(my_list), id(my_list))
# my_tuplu = tuple(my_list)
# print(my_tuplu, type(my_tuplu), id(my_tuplu))
#
#
# my_lis = list(my_tuplu)
# print(my_lis, type(my_lis), id(my_lis))

# my_dict = {'a': 12, 'b': 'abc', 3: 22}
# print(my_dict['b'])
# print(my_dict.get('a', 'my default value'))
#
# print('a' in my_dict)

'''
homework
'''

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print(sorted(my_list))
print(sorted(my_list, reverse=True))

print(my_list[1:4:2] + my_list[6:8:1] + my_list[9:10:1])
print(my_list[0:5:2] + my_list[5:9:3])

print(my_list[2:5:2] + my_list[9:10])

print(my_list)


# Tik-Tak-Toe
def print_format_game(vals):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(vals[0], vals[1], vals[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(vals[3], vals[4], vals[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(vals[6], vals[7], vals[8]))
    print("\t     |     |")
    print("\n")


print_format_game([1, 2, 3, 4, 5, 6, 7, 8, 9])

