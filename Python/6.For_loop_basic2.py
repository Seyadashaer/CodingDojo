# 1. Biggie Size
def biggie_size(my_list):
    for i in range(0,len(my_list)):
        if my_list[i] > 0: 
            my_list[i] = "big"
    return my_list

print(biggie_size([-8,7,8,-1,-3,0]))
print("---------------------------------------")

# 2. Count Positives
def count_positives(my_list): 
    count = 0
    for i in my_list:
        if i>0:
            count += 1 
    my_list[-1] = count
    return my_list

print(count_positives([1,-1,-1,7,9,9]))
print("---------------------------------------")

# 3. Sum Total
def sum_total(my_list):
    sum = 0
    for i in my_list:
        sum += i 
    return sum 

print(sum_total([2,6,1,3]))
print("---------------------------------------")

# 4. Average
def return_average(my_list):
    sum = 0
    for i in my_list:
        sum += i 
        average = sum/len(my_list)
    return average

print(return_average([2,5,4,3]))
print("---------------------------------------")

# 5. Length
def return_length(my_list):
    return len(my_list)

print(return_length([]))
print(return_length([3,7,8,4]))
print("---------------------------------------")

# 6. Minimum 
def return_minimum(my_list):
    if len(my_list) == 0 :
        return False
    min_value = my_list[0]
    for i in my_list:
        if i<min_value:
            min_value = i
    return min_value

print(return_minimum([]))
print(return_minimum([3,4,5,6,1,-2]))
print("---------------------------------------")

# 7. Maximum
def return_maximum(my_list):
    if len(my_list) == 0 :
        return False
    max_value = my_list[0]
    for i in my_list:
        if i>max_value:
            max_value = i
    return max_value

print(return_maximum([]))
print(return_maximum([3,4,5,6,1,-2]))
print("---------------------------------------")

# 8. Ultimate Analysis
def ultimate_analysis(my_list): 
    new_dict = {'sumTotal': sum_total(my_list), 'average': return_average(my_list), 'minimum': return_minimum(my_list), 'maximum': return_maximum(my_list), 'length': return_length(my_list) }
    return new_dict

print(ultimate_analysis([3,4,5,6,1,-2]))
print("---------------------------------------")

# 9. Reverse List
def reverse_list(my_list): 
    left_index = 0
    right_index = len(my_list) -1
    while left_index < right_index : 
        temp_value = my_list[left_index]
        my_list[left_index] = my_list[right_index]
        my_list[right_index] = temp_value
        left_index += 1
        right_index -= 1
    return my_list

print(reverse_list([3,4,5,6,1,-2]))
print("---------------------------------------")



