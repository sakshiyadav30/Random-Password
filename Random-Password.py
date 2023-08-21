import random                      
   
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"  
  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
    selected_char = random.sample(list_of_chars, len)  
  
    # converting the list into the string  
    pass_str = "".join(selected_char)  
      
    # returning the generated password string  
    return pass_str  
  
# main function  
if __name__ == "__main__":  

    len = int(input("Enter the length of the Password: "))  
  
    # calling the generate_password() function and storing the returned value in a variable  
    pass_str = generate_password(len)  
  
    # printing the final result for the users  
    print("A randomly generated Password is:", pass_str)  