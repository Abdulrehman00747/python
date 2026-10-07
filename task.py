
name = str(input("name: "))
print(type(name))

age = int(input("Enter age: "))
print(type(age))

height = float(input("Enter height: "))
print(type(height))

#2. Take two floats, "a = 12.5" and "b = 4.2". Print their sum, difference, product, and quotient. Use "round(result, 2)" on each result.

a = 12.5
b = 4.2
print("sum:", round(a+b, 2))
print("difference:", round(a-b, 2))
print("product:", round(a*b, 2))
print("quotient:", round(a/b, 2))

#3. Run "5 * 2.5" and check the type of the result. Write one line explaining why it is a float.
result = 5 * 2.5
print ("result:",result, "type:", type(result))


#4. Casting: Convert the string ""25"" to "int()" and "float()", then add "10" to each. Finally, print "str(99) + "%"".

number_str = "25"
number_int = int(number_str)
number_float = float(number_str)
print("int + 10:", number_int + 10)
print("float + 10:", number_float + 10)
print("str(99) + '%':", str(99) + "%")

#part 2

#5. Mini Calculator: Take two numbers from the user with "input()" (convert to float). Print their sum and product in this format:

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print("Sum:", first_number + second_number)
print("Product:", first_number * second_number)


#6. Rectangle: Take length and width (float). Print the area and perimeter using "format()" or an f-string, to 2 decimal places.
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")





#7. Shopping Bill: Take an item name, price (float), and quantity (int). Total = price × quantity.
item_name = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Total cost for {quantity} {item_name}(s): ${total:.2f}")


#part 3

#8. On "text = "  python is FUN and powerful  "", apply "strip()", "lower()", "upper()", "title()", "capitalize()", and "swapcase()". Print each result.
text = "  python is FUN and powerful  "
print("Original:", text)
print("Strip:", text.strip())
print("Lower:", text.lower())
print("Upper:", text.upper())
print("Title:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())


# question = 8
# Run:

print("hello".center(21, "*"))
print("hello".ljust(15, "-"))
print("hello".rjust(15, "-"))
print("hello".zfill(10))

#Question = 9


#Write down the difference between them.

#10. On ""banana"", find "count("a")", "find("n")", "rfind("n")", and "index("b")".

word = "banana"

#10. On ""banana"", find "count("a")", "find("n")", "rfind("n")", and "index("b")".
#Then run "find("z")" and "index("z")" and explain the difference. What error do you get?

#question = 10

print(word.count("a"))
print(word.find("n"))
print(word.rfind("n"))
print(word.index("b"))

print(word.find("z"))
print(word.index("z"))


#11. Run "isalpha()", "isdigit()", "isalnum()", "isspace()", "isupper()", and "islower()" on:

#question = 11

words = ["Python", "2026", "Py2026", "   ", "HELLO"]

for word in words:
    print(word)
    print(word.isalpha())
    print(word.isdigit())
    print(word.isalnum())
    print(word.isspace())
    print(word.isupper())
    print(word.islower())
    print()


#part 4 split and join

#question = 12

    fruits = "apple,banana,cherry,mango"

x = fruits.split(",")
print(x)

y = " | ".join(x)
print(y)

#question = 13

text = "I love Java. Java is great. Java Java!"

print(text.replace("Java", "Python"))

print(text.replace("Java", "Python", 2))

#question = 14

email = "zarq@smit.edu.pk"

print(email.partition("@"))


#5. Use "startswith()" and "endswith()" to check whether:

#question = 15

filename = "report_final.pdf"
print(filename.endswith(".pdf"))
print(filename.startswith("report_"))

# is a PDF file.


# part 5
question = 16
#Random module

import random

print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

print(random.random())

#question = 17

import random

names = ["Ali", "Sara", "Ahmed", "Zoya"]

name = random.choice(names)

print(name.upper())

#question = 18

import random

characters = "abcdefghijklmnopqrstuvwxyz0123456789"

password = ""

for i in range(8):
    password = password + random.choice(characters)

password = password[0].upper() + password[1:]

print(password)

#question = 19

import random

name = input("Enter your name: ")
print("Hello", name.title())

number = random.randint(1, 10)

guess = int(input("Guess the number: "))

if guess == number:
    print("Correct!")
else:
    print("Wrong, the number was", number)


# question = 20

name = input("Enter student name: ")

marks1 = float(input("Enter marks: "))
marks2 = float(input("Enter marks: "))
marks3 = float(input("Enter marks: "))

total = marks1 + marks2 + marks3
average = total / 3
percentage = total / 300 * 100

print("\nStudent Result".center(30))
print("Name:", name.title())
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)

# question = 21

import random

name = input("Enter your name: ")

name = name.strip().lower().replace("   ", " ").replace(" ", ".")

id = random.randint(100, 999)

print(name + "_" + str(id))