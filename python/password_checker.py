# password strength checker
import re 

# condition to be checked
# min 8 char, digit, uppercase, lowercase, special char

def check_password_strength(password):
    if len(password) < 8:
        return "Weak! password must be at least 8 chars "
    
    if not any(char.isdigit() for char in password):
        return "weak! password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "weak! password must contain an upper letter"
    
    if not any(char.islower() for char in password):
        return "weak! password must contain a lower chars"
    
    if not re.search(r'[!@#$%^&*(){}".<>?]', password):
        return "Medium! password must contain a special chars"
    
    return "Strong! Your password is secured!"

def password_checker():
    print("Welcome!")
    
    while True:
        password = input("Enter your password or type 'quit to exit:")
        
        if password.lower() == 'exit' :
            print("Thank you for using this tool")
            break
        
        result = check_password_strength(password)
        print(result)
        
# Run the password checker tool
if __name__=="__main__":
    password_checker()
    
        
    