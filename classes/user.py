from typing_extensions import Self

class User:
    def __init__(self, name, email, password, title):
        self.name = name
        self.email = email
        self.password = password
        self.title = title

def change_pass(self, new_password):
    self.password = new_password
    
def change_title(self, new_title):
    self.title = new_title

def print_user(self):
    print(f"Name: {self.name}")
    print(f"Email: {self.email}")
    print(f"Password: {self.password}")
    print(f"Title: {self.title}")
        
user1 = User("Sumit Verma", "sumit.v@live.com", "123456", "Python Developer")
print_user(user1)
change_pass(user1, "1234567")
print("\nCHANGING PASSWORD \n")
print_user(user1)
print("\nUPDATING TITLE\n")
change_title(user1, "Python SME")
print_user(user1)