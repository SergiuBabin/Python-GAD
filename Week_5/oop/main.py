# def my_decorator(my_function):
#     def wrapper(nr):
#         my_function_result = my_function(nr)
#         return my_function_result ** 3
#
#     return wrapper
#
# @my_decorator
# def f1(nr):
#     return nr
#
# if __name__ == '__main__':
#     # my_decorated_function = my_decorator(f1)
#     # x = my_decorated_function(10)
#
#     x = f1(10)
#     print('x', x)


class Dog:


    def __init__(self, name, breed='Maidanez'):
        print('Dog.__init__ function called')
        self._name = name
        self.breed = breed

rex = Dog('Rex')
print(type(rex))
print('Dog name is: {} - {}'.format(rex._name, rex.breed))