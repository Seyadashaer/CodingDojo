# 1. Countdown
def count_down(x):
    result = []
    for i in range(x,-1,-1):
        result.append(i)
    return result
print(count_down(7))
print(count_down(10))
print("---------------------------------------")

# 2. Print and Return
def print_and_return(my_list):
    print(my_list[0])
    return my_list[1]
print(print_and_return([5,7]))
print("---------------------------------------")

# 3. First Plus Length 
def first_and_length(my_list):
    return my_list[0] + len(my_list)
print(first_and_length([2,7,4,5,6,8]))
print("---------------------------------------")

# 4. Values Greater than Second
def values_greater_than_second(my_list):
    if len(my_list) < 2:
        return False
    new_list = []
    count = 0
    for i in range(0, len(my_list)):
        if my_list[i]>my_list[1]:
            new_list.append(my_list[i])
            count += 1 
    print(count)
    return(new_list)
x= [10,1,2,5,6,7,8,1,20]
print(values_greater_than_second(x))
print("---------------------------------------")


# 5. This Length, That Value 
def length_and_value(size,value):
    new_list = []
    for i in range(0,size):
        new_list.append(value)
    return new_list
print(length_and_value(5,9))
print(length_and_value(11,10))
print("---------------------------------------")




    