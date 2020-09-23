class User:

    def __init__(self, surname, last_name, email, username, password, gender, age, address, risk_group, shop_preference, user_id):
        self.user_id = user_id
        self.sur_name = surname
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.address = address
        self.risk_group = risk_group
        self.username = username
        self.age = age
        self.password = password
        self.shop_preference = shop_preference
        self.logged_in = False
        #when logged in change the value to True

        self.user_info_dict = dict()
        self.user_info_dict["sur name"] = self.sur_name

        self.user_info_list = []
        self.user_info_list.append(self.sur_name)
        self.user_info_list.append(self.last_name)
        self.user_info_list.append(self.email)
        self.user_info_list.append(self.gender)
        self.user_info_list.append(self.address)
        self.user_info_list.append(self.risk_group)
        self.user_info_list.append(self.shop_preference)
        self.user_info_list.append(self.age)
        self.user_info_list.append(self.password)
        self.user_info_list.append(self.user_id)
        self.user_info_list.append(self.logged_in)

    def __str__(self):
        return f'{self.sur_name} {self.address}'

class User_dict:

    def __init__(self):
        self.user_dict = dict()

    def add_user(self, user):
        if user.username not in self.user_dict:
            self.user_dict[user.username] = user.user_info_list
        else:
            print("Username already taken")
            self.create_account()

    def delete_user(self, user):
        if user.username in self.user_dict:
            self.user_dict.pop(user.username)
        else:
            print("Can't delete account, account doesn't exist")

    def get_surname(self, user):
        return self.user_dict[user][0]

    def logging_in(self):
        remaining_attempts = 3
        while remaining_attempts>0:
            # ask for username input & password
            print("Username: ")
            username_input = input()
            print("Password: ")
            password_input = input()
            if username_input in self.user_dict:
                if password_input == self.user_dict[username_input][8]:
                    print("logging in")
                    self.user_dict[username_input][10] = True
                    # open grid/app
                    break
                else:
                    remaining_attempts -= 1
                    if remaining_attempts == 0:
                        print("Wrong password. Too many tries, account blocked.")
                    else:
                        print(f'Wrong password,{remaining_attempts} remaining attempts')
            else:
                print("Wrong username")

    def create_account(self):
        count =1
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
        self.add_user(new_user)



    def print_all(self):
        for pair in self.user_dict:
            print(pair)
            print(self.user_dict[pair])
