#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import hashlib 
class User: 
    def __init__(self, username, password): 
#Create a new user object. The password will be encrypted before storing. 
        self.username = username 
        self.password = self._encrypt_pw(password) 
        self.is_logged_in = False 
    def _encrypt_pw(self, password): 
#Encrypt the password with the username and return the sha digest. 
        hash_string = self.username + password 
        hash_string = hash_string.encode("utf8") 
        return hashlib.sha256(hash_string).hexdigest() 
    def check_password(self, password): 
#Return True if the password is valid for this user, false otherwise. 
        encrypted = self._encrypt_pw(password) 
        return encrypted == self.password 
    
class AuthException(Exception): 
    def __init__(self, message): 
        super().__init__(message) 

class UsernameAlreadyExists(AuthException): 
    def __init__(self, username, user): 
        super().__init__(username + ' already exists for ' + str(user)) 

class PasswordTooShort(AuthException): 
    def __init__(self, password): 
        super().__init__(repr(password) + ' is too short ')
#Task3
class InvalidUsername(AuthException):
    def __init__(self, username):
        super().__init__("Username '" + username + "' does not exist")


class InvalidPassword(AuthException):
    def __init__(self, username):
        super().__init__("Password is invalid for user '" + username + "'")




#Task2 
class Authenticator:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, password):
        if len(password) < 6:
            raise PasswordTooShort(password)
        
        if username in self.users:
            raise UsernameAlreadyExists(username, self.users[username])
        
        self.users[username] = User(username, password)

#Task4
    def login(self, username, password):
        
        if username not in self.users:
            raise InvalidUsername(username)
        
        
        if not self.users[username].check_password(password):
            raise InvalidPassword(username)
        
        self.users[username].is_logged_in = True
        return True
    
# Task 5
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False

# Task 6
if __name__ == "__main__":
    auth = Authenticator()

    # Test Case 1
    try:
        auth.add_user("johnny", "johnnypassword")
        print(auth.is_logged_in("johnny"))  
        auth.login("johnny", "johnnypassword")
        print(auth.is_logged_in("johnny")) 
    except AuthException as e:
        print("AuthException: " + str(e))
    
    # Test Case 2
    try:
        auth.add_user("susan", "susanpassword")
        auth.login("susan", "5U54N")  
    except AuthException as e:
        print("AuthException: " + str(e))
    
    # Test Case 3
    try:
        auth.add_user("johnny", "johnnypassword")  
        auth.login("johnny", "johnnypassword")
        print(auth.is_logged_in("johnny"))
    except UsernameAlreadyExists as e:
        print("Username already exists: " + str(e))
        auth.add_user("johnny2", "johnnypassword")
    except InvalidPassword as e:
        print("Invalid password: " + str(e))
    except AuthException as e:
        print("Other auth exception: " + str(e))
    
    # Test Case 4
    while True:
        try:
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            auth.add_user(username, password)
            print("User " + username + " added successfully!")
            break
        except AuthException as e:
            print("Error: " + str(e))
            print("Please try again.")