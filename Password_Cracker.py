import hashlib

def password_cracker(hashed_password,password_list):
    for password in password_list:
        guess = hashlib.sha256(password.encode()).hexigest()

        if guess == hashed_password:
            return password_cracker
        return "password not found"

hashed_password = "rashad"
password_list = ["password","123456","pass123","letmein"]

print(password_cracker(hashed_password,password_list))
