#for i, value in enumerate(["milk" , "bread", "cheese"]):
from User import User
from User import User_dict
i = 1
value = "milk"
exec("var%s=value" % i)
print(var1)
count = 1
print("Creating an account...")
print("What is your surname: ")
surname_input = input()
print("what is your last name: ")
last_name_input = input()
print("what is your email: ")
email_input = input()
print("what is your username: ")
username_input = input()
print("what is your password: ")
password_input = input()
print("what is your gender: ")
gender_input = input()
print("what is your age: ")
age_input = input()
print("what is your address: ")
address_input = input()
print("what is your risk_group: ")
risk_group_input = input()
print("what is your shop_preference: ")
shop_preference_input = input()
user_id = 50
new_user = User(surname_input, last_name_input, email_input, username_input, password_input, gender_input, age_input, address_input, risk_group_input, shop_preference_input, user_id)
#new_user = "yooww"
exec("user%s=new_user" % count)
print(user1)