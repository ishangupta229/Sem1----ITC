print("PROGRAM TO CHECK PALINDROME")

y = input("Enter a word, phrase, sequence or number : \n")
def is_palindrome(string): 
  
    string = string.lower() 
  
    reverse_string = string[::-1] 
  
    if string == reverse_string: 
        return True
    return False


print(is_palindrome(y))