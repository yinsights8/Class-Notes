import str_functions
from str_functions import get_lower
from list_functions import add_ing
from Dict import dict1, dict_functions
import str_functions as sf
from calculation import factorial as fct
import calculation as cln
from calculation import addition,factorial


print("Project Module")

def welcome(name):
    print(f"Welcome {name} to the project")



res = sf.get_list(input("Enter your string by spaces :- "))
ing_list = add_ing(get_lower(res))

print(dict_functions.get_dect(ing_list))

res1 = dict1.dict2()

print(res1)

fct.exit_msg()
# cln.addition.get_addition(600,700)
if __name__ == "__main__":
    fct.fact(6)
    # names_list = str_functions.get_list(string)
    # print(names_list)
    
    