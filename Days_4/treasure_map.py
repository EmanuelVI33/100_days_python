row1 = ["👨","👨","👨"]
row2 = ["👨","👨","👨"]
row3 = ["👨","👨","👨"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put treasure? ")
col = int(position) // 10
fil = int(position) % 10
map[fil-1][col-1] = "X"

print(f"{row1}\n{row2}\n{row3}")