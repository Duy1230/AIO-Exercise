############### Cau 5###############
def check_the_number(n):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        # Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)
    if n in list_of_numbers:
        results = "True"
    if n not in list_of_numbers:
        results = "False"
    return results


N = 7
assert check_the_number(N) == "False"

N = 2
result = check_the_number(N)
print(f"Exercise 5: {result}")

############### Cau 6###############


def my_function(data, max, min):
    result = []
    for i in data:
        # Neu i < min thi them min vao result
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
maximum = 1
minimum = 0
assert my_function(max=maximum, min=minimum, data=my_list) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
maximum = 2
minimun = 1
print(f"Exercise 6: {my_function(max=maximum, min=minimum, data=my_list)}")


############### Cau 7###############
def my_function(x, y):
    # Your code here
    # Su dung extend de noi y vao x
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function(list_num1, my_function(list_num2, list_num3)) == ['a', 2, 5, 1, 1,
                                                                     0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(f"Exercise 7: {my_function(
    list_num1, my_function(list_num2, list_num3))}")


############### Cau 8###############
def my_function(list):
    # Your code here
    return min(list)


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(f"Exercise 8: {my_function(my_list)}")

############### Cau 9###############


def my_function(list):
    # Your code here
    return max(list)


my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(f"Exercise 9: {my_function(my_list)}")

############### Cau 10###############


def my_function(intergers, number=1):
    return number in intergers


my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(f"Exercise 10:{my_function(my_list, 2)} ")

############### Cau 11###############


def my_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    # Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho so luong phan tu trong list_mums
    return var/len(list_nums)


assert my_function([4, 6, 8]) == 6
print(f"Exercise 11: {my_function()}")


############### Cau 12###############
def my_function(data):
    var = []
    for i in data:
        # Your code here
        # Neu i chia het cho 3 thi them i vao list var
        if i % 3 == 0:
            var.append(i)
    return var


assert my_function([3, 9, 4, 5]) == [3, 9]
print(f"Exercise 12: {my_function([1, 2, 3, 5, 6])}")


############### Cau 13###############
def my_function(y):
    var = 1
    while (y > 1):
        var *= y
        y -= 1
    return var


assert my_function(8) == 40320
print(f"Exercise 13: {my_function(4)}")


############### Cau 14###############
def my_function(x):
    return ''.join(reversed(x))


x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(f"Exercise 14:{my_function(x)}")


############### Cau 15###############
def function_helper(x):
    if x > 0:
        return 'T'
    else:
        return 'N'


def my_function(data):
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(f"Exercise 15: {my_function(data)}")


############### Cau 16###############

def function_helper(x, data):
    for i in data:
        # Your code here
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)

    return res


lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(f"Exercise 16: {my_function(lst)}")
