numbers = [23, 56, 78, 45 ,67, 93 ,34, 21, 5]

# maxi = numbers[0]
# for number in numbers:
#     if(number > maxi):
#         maxi = number

maxi = numbers[0]
for i in range(1,len(numbers)-1):
    if (numbers[i] > maxi):
        maxi = numbers[i]
        
print(maxi)

# Obtener nueva lista con solo elementos par
new_lista = [x for x in numbers if x % 2 == 0]
print(new_lista)