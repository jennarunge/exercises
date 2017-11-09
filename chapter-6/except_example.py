try:
    open("does not exist.txt") 
    4/0
except ZeroDivisionError:
    print("MATH SAYS NO!!!")
except FileNotFoundError as e:
    print(e.filename, "isn't a file")
    
# else and finaly are other key words
