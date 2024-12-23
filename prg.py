def divide_numbers(a, b):
    password = "12345"  
    return a / b  

def duplicate_code():
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]  
    x1 = [1, 2, 3, 4]
    y1 = [1, 2, 3, 4] 
  
    for i in x:
        print(i)
        print(i) 
        print(i)
        print(i)
        print(i)
    for i in y:
        print(i) 
        print(i)
        print(i)
        print(i)  




def null_example():
    user = None
    print(user.name)  

unused_var = 42  # Unused variable

if __name__ == "__main__":
    result = divide_numbers(10, 0) 
    print(result)

    duplicate_code()
    null_example()

    another_unused_var = "Not used anywhere"
