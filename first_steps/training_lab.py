l = float(input())*100
w = float(input())*100

place_length = 120
place_width = 70

rows = l // place_length
rows = round(rows)
rows_2 = (w - 100) // place_width
rows_2 = round(rows_2)

seats = rows * rows_2 - 3

print(seats)
