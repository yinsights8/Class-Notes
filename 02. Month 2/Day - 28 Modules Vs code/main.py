import Calculations
import Str_Functions

num1 = 10
num2 = 20
string = "Python And Data Science"

result1 = Calculations.addition(num1, num2)
print(f"The addition of {num1} and {num2} = {result1}")

result2 = Calculations.subtract(num1,num2)
print(f"The subtraction of {num1} and {num2} = {result2}")


print("We are executing get_upper function")
result3 = Str_Functions.get_upper(string)
print(f"The result of get_upper function = {result3}")









if __name__ == "__main__":
    print("This is main file")

