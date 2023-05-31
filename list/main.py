my_nums = [10, 50, 0, 5, 100]

other_nums = my_nums.copy()

my_nums.append(3)
other_nums.clear()

print(id(my_nums))
print(id(other_nums))

print(my_nums, other_nums)
