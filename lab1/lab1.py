
# ====================================1========================
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = last_name + " " + first_name
print(full_name[::-1])

# ====================================2========================
n = int(input("Enter an integer: "))

nn = n * 10 + n
nnn = n * 100 + nn
result = n + nn + nnn
print(result)


# ====================================3=========================
radius = 6
volume = (4/3) * math.pi * radius ** 3

print("The volume of the sphere is:", volume)

# =====================================4=========================
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

# =====================================5=========================
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height
print("The area of the triangle is:", area)

# ================================6==================================
n = 5

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n-1):
    for j in range(n-i-1):
        print("*", end=" ")
    print()

# ======================7==============================================
word = input("Enter a word: ")
print("The reversed word is:", word[::-1])


# ==============================8=====================================
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)
# ====================================9========================

a, b = 0, 1

while a < 50:
    print(a, end=' ')
    a, b = b, a + b

print()
# ====================================10========================
string = input("Enter a string: ")

num_digits = 0
num_letters = 0

for char in string:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1

print("Number of digits:", num_digits)
print("Number of letters:", num_letters)
