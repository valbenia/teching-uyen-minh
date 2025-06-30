# a = 100

# arr = [1, 2, 3, 4, 5]
# print(arr)

def check_even_odd(numer):
    if numer % 2 == 0:
        print(numer, " is even")
    else:
        print(numer, " is odd")
    

# for item in arr:
#     print("processing item: ", item)
#     check_even_odd(item)

# print("end of for loop")


# a = 10

# while a > 0:
#     a = a - 1
#     print("processing item: ", a)
#     check_even_odd(a)



def sum_numbers(a, b):
    return a + b


# global variable and local variable
# multiple blocks of code
def example():
    a = 10
    for i in range(5):
        if i == 3:
            print(a)
        print(i)
    print("End of example function")

example()
    

x = 10
y = 11
result = sum_numbers(b=1, a=2)
print("Sum of ", x, " and ", y, " is ", result)