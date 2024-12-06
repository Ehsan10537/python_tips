import module_1

m2_var1 = 'This is the original m2_var1'  

module_1.m1_var1 = 'This is the CHANGED m1_var1'   # we try to override the m1_var1 of module_1 in module_2


def multiply(a, b):
    print(f'Multiplication of {a} and {b} : ')
    return a*b


module_1.func = multiply      # we try to override the func function of module_1 in module_2


# the point is that when we import module_1 in module_2, we are going to be able to import module_1 from module_2 in our program.
# and in that case, the variable 'm1_var1' and the function 'func' will both get changed. but the variable m1_var2 will stays the same.