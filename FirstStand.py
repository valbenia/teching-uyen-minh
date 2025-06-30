# hocGioi = True
# chamChi = True
# khoe = False
# conNgoan = hocGioi and chamChi and khoe
# # print("Con ngoan" if conNgoan else "Con khong ngoan")
# a = 10
# # parent block vs child block
# def example():
#     for i in range(5):
#         if i == 6:
#             print(a)
#             b = 20
#         print(i)
#     print("End of example function")
#     print(a)

# example()

# Note: 
def is_Even(number):
    return True if number % 2 == 0 else False

def is_Even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def is_Even(number):
    return number % 2 == 0

# A B C D F
# Nhập điểm số (0-10) từ bàn phím
# In ra xếp loại tương ứng:
# - Điểm >= 8.5: Giỏi
# - Điểm >= 7.0: Khá
# - Điểm >= 5.5: Trung bình
# - Còn lại: Cần cố gắng thêm
# Code của bạn:

# score = float(input("Nhập điểm số (0-10): "))
# print("score:", score)

# def check_score(score):
#     if score > 10 or score < 0:
#         return "Điểm không hợp lệ"
    
#     if score >= 8.5:
#         return "Giỏi"
#     elif score >= 7.0:
#         return "Khá"
#     elif score >= 5.5:
#         return "Trung bình"
#     else:
#         return "Cần cố gắng thêm"

# print(check_score(score))
# range(20) => (0,19) 
# (1,20) => range(1, 21)

# Nhập một năm từ bàn phím
# Kiểm tra và in ra thông báo năm đó có phải năm nhuận hay không
# Năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100
# hoặc năm chia hết cho 400

# year = 2025

# year (chia het cho 4 va khong chia het cho 100) or (chia het cho 400)
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0:
#         if year % 100 == 0:
#             return False
#         else:
#             return True
#     else:
#         return False

# def times_table(number):
#     # for i in range(1, 11):
#     #     print(number, " * ", i, " = ", number * i)
#     temp = 1
#     while temp <= 10:
#         print(number, "*", temp, "=", number * temp)
#         temp += 1

# times_table(5)

# *      *
# **    **
# ***  ***
# ********
# sol:
# def print_star(n):
#     for i in range(1, n+1):
#         print(" " * i + "*" * (n-i) + " " * i + " " * i + "*" * (n-i) + " " * i)
# print_star(10)





# def print_star_line(index, maxLength):
#     result = ""
#     total_length = 2 * maxLength
    
#     for i in range(1, total_length + 1):
#         if i <= index or i > total_length - index:
#             result += "*"
#         else:
#             result += " "
    
#     return result

# for i in range(1, 5):
#     print(print_star_line(i, 4))

        
# def is_prime(n):
#     if n <= 3:
#         return True
    
#     for i in range(2, n+1):
#         if i == n:
#             return True
#         if n % i == 0:
#             return False
#     return True

# for i in range(2, 200):
#     if is_prime(i):
#         print(i, "is prime")
#     else:
#         print(i, "is not prime")

# students = [
#     {"name": "Nguyen Van A", "age": 10,"score": 8.5},
#     {"name": "Tran Thi B", "age": 11,"score": 7.0},
#     {"name": "Le Van C", "age": 12, "score": 5.5},
#     {"name": "Pham Thi D", "age": 9, "score": 4.0}
# ]

# avg = sum/count
# ex = mul/count

# print("Student list:")
# print("Name\t\t\tScore")
# sum = 0
# count = 0
# for student in students:
#     print( student["name"], "\t\t" ,student["score"])
#     sum = sum + student["score"]
#     count += 1 # count = count + 1
# print("Average score:", sum/count)

x = 10
y = 20
print("x = ", x, "y = ", y)

temp = x
x = y
y = temp
print("x = ", x, "y = ", y)

# sorting [1, 3, 2, 5, 4]
# [1, 2, 3, 4, 5]

type(True)