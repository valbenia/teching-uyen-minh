a = 1
b = 2
c = a + b / 0
# try:
#     # This will raise a ZeroDivisionError
#     c = a + b / 0
# except Exception as e:
#     print(f"An error occurred when calculating c: {e}")
#     c = 0
d = a + b + c
print(d)