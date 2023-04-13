year = int(input("Which year do you want to check? "))

def isLeapYear(year: int):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


# if(year % 4 == 0):
#     if (year % 100 == 0):
#         if (year % 400 == 0):
#             print("Loop Year")
#         else:
#             print("No Loop Year")
#     else:
#         print("Loop Year")
# else:
#     print("No Loop Year")
    
print("Loop Year" if isLeapYear(year) else "No Loop Year")