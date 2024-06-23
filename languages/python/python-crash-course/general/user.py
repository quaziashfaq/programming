#!/usr/bin/env python3

class User:
    '''A general user (in server) class'''
    def __init__(self, first_name, last_name, login_id):
        self.first_name = first_name
        self.last_name = last_name
        self.login_id = login_id
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.login_id}'s full name is {self.first_name.title()} {self.last_name.title()}. Logins attempted: {self.login_attempts}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = [
                'can add post',
                'can delete post',
                'can ban user',
                ]

    def show_privileges(self):
        print(f'The admin has the below privileges:')
        for priv in self.privileges:
            print(priv)


class Admin(User):
    def __init__(self):
        super().__init__("", "", 'admin')
        self.privileges = Privileges()
    
if __name__ == '__main__':
    admin = Admin()
    admin.describe_user()
    admin.privileges.show_privileges()
