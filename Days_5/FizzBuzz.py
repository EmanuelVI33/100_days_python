for number in range(1,101):
    s = ""
    if(number % 3 == 0):
        s += "Fizz"
    if(number % 5 == 0):
        s += "Buzz"
    print(s if s != "" else number)