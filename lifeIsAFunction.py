import math

print("Life is a function, so lets use some to perform efficient calculations...\n")

#Criteria 1: Area of a Circle
print("Our first function will be the function of a circle:\n")

#Function to calculate area of circle... A = pi * r**2
def area_of_circle(radius):
    circle_area = math.pi * float(radius)**2
    return circle_area
#Assigning radius input values to test
radius1 = input("Enter the radius of circle1: \n")
radius2 = input("Enter the radius of circle2: \n")
radius3 = input("Enter the radius of circle3: \n")
radius4 = input("Enter the radius of circle4: \n")
radius5 = input("Enter the radius of circle5: \n")

#Running function with given radii
area1 = area_of_circle(radius1)
area2 = area_of_circle(radius2)
area3 = area_of_circle(radius3)
area4 = area_of_circle(radius4)
area5 = area_of_circle(radius5)

#Printing areas calculated by function
print("The area of circle 1 is:", area1)
print("The area of circle 2 is:", area2)
print("The area of circle 3 is:", area3)
print("The area of circle 4 is:", area4)
print("The area of circle 5 is:", area5)
print()

#Criteria 2: Taxes

print("Our second function will calculate tax and add it to our subtotal to provide a complete total...")

#Calculating total after taxes by adding the product of our money and tax rate to the original money value
def tax_total(money, tax_rate):
    complete_total = float(money) + (float(money) * (float(tax_rate) / 100))
    return complete_total

#Assigning values for our first parameter: money and second parameter: tax_rate
money1 = input("Enter the amount of money from subtotal1: \n")
tax_rate1 = input("Enter the tax rate from subtotal1: \n")
money2 = input("Enter the amount of money from subtotal2: \n")
tax_rate2 = input("Enter the tax rate from subtotal2: \n")
money3 = input("Enter the amount of money from subtotal3: \n")
tax_rate3 = input("Enter the tax rate from subtotal3: \n")

#Running function and assigning return values to total variables
total1 = tax_total(money1, tax_rate1)
total2 = tax_total(money2, tax_rate2)
total3 = tax_total(money3, tax_rate3)

#Printing our calculated totals
print("Our first total is:", total1)
print("Our second total is:", total2)
print("Our third total is:", total3)
print()

#Criteria 3: Temperature

print("Our last function will convert temperature from Fahrenheit to Celsius...")

#Function that calculates temperature from fahrenheit to celsius
def f_to_c(temp_f):
    temp_c = (float(temp_f) - 32) * (5 / 9)
    return temp_c

#Assigning Fahrenheit temperatures to variables

tempF1 = input("Enter your first temperature in degress Fahrenheit: \n")
tempF2 = input("Enter your second temperature in degress Fahrenheit: \n")
tempF3 = input("Enter your third temperature in degress Fahrenheit: \n")
tempF4 = input("Enter your fourth temperature in degress Fahrenheit: \n")

#Assigning function return values to variable for printing

tempC1 = f_to_c(tempF1)
tempC2 = f_to_c(tempF2)
tempC3 = f_to_c(tempF3)
tempC4 = f_to_c(tempF4)

print("Our first temperature is:", str(tempC1), "degrees C")
print("Our second temperature is:", str(tempC2), "degrees C")
print("Our third temperature is:", str(tempC3), "degrees C")
print("Our fourth temperature is:", str(tempC4), "degrees C")
print("\nThis was definitely more efficient than using individual lines of code for our calculations!")