import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from utils import square, is_even, celsius_to_fahrenheit

num = float(input("Enter a number: "))
print(f"Square: {square(num)}")

if is_even(int(num)):
    print(f"{int(num)} is even")
else:
    print(f"{int(num)} is odd")

print(f"{num}C is {celsius_to_fahrenheit(num)}F")