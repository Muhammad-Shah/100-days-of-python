
from turtle import pos, position


row_1 = ["📜", "📜", "📜"]
row_2 = ["📜", "📜", "📜"]
row_3 = ["📜", "📜", "📜"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")
position = input("Where do you want to put trasure? ") #23 (2 number col & 3 row)

horizental = int(position[0]) # 2
vertical = int(position[1]) # 3

# ***********************************
# selected_row = map[vertical-1]
# selected_row[horizental-1] = "*"

# ***********************************
map[vertical-1][horizental-1] = "*"
# ***********************************

print(f"{row_1}\n{row_2}\n{row_3}")


