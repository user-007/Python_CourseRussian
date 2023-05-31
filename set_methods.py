my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection('abcd'))
print(other_set.issubset(my_set))
print(my_set.issuperset(other_set))

