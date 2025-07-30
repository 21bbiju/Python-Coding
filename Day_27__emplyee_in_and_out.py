class Employee:
    
    def __init__(self):
        print('Emplyee created')

    def __del__(self):
        print("Destrutor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function and..')
    return obj

print('Calling Create_obj() (function...')
obj = Create_obj()
print('Program End...')          