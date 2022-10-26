"""Practice different math expressions and calculations."""
import math
# Declare num_a and num_b
num_a = 5
num_b = 2


#1. Sum and difference

sum = num_a + num_b
print(f"{num_a} + {num_b} = {sum}")

difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")

#2. Float division

division = num_a / num_b
print(f"{num_a} / {num_b} = {division}")

#3. Integer division
division = num_a // num_b
print(f"{num_a} // {num_b} = {division}")

#4. Powerful operations
multiply_numbers = num_a * num_b
print(f"{num_a} * {num_b} = {multiply_numbers}")

#5. Find average
average = (num_a + num_b) / 2
print(f"{num_a + num_b} / 2 = {average}")

#6. Area of a circle
radius = 2
circle_area = math.pi * radius ** 2
print(f"{math.pi} * {radius} ** 2 equal {circle_area}")

#7 Area of an equilateral triangle
side_length = 3
height= 4.4
triangle_area = side_length * round(4.4)
print(triangle_area)

#8 Calculate discriminate
Discriminate = 6 ** 2 - 4 * 1 * 5
a = 1
b = 6
c = 5
print(f"{b} ** 2 - 4 * {a} * {c} = {Discriminate}")

#9 Calculate hypotenuse length
c = a + b
a = 3
b = 4
area = a ** 2 * b ** 2 / math.sqrt(144)
print(area)

#10 Calculate cathetus

a = 2
c = 8
b = math.sqrt((c**2 - a**2))
print(b)

#11 Time converter
seconds = 149032
minutes = seconds // 60
hours = minutes // 60
minutes = minutes % 60
seconds = seconds % 60
print(hours, minutes, seconds)

#12 Student helper
angle = 67
sine = math.sin(math.pi / 2)
cosine = math.cos(math.pi * 5)
print(math.cos(math.pi * 5))

#13 Greetins
for lots_of_heys in range(5):
    print("Hey")

#14 Adding numbers
num_a = 4
num_b = 6
string_numbers = str(num_a) + str(num_b)
print(string_numbers)