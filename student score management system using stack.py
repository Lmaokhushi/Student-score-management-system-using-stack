student = []
def push_fxn():
    input_tp=input("enter (student_name, student_marks):")
    student.append(input_tp)
def pop_fxn():
    print("popped item:", student.pop())
def traversal():
    print(student)
menu_dict={'1':push_fxn,'2':pop_fxn,'3':traversal}
while True:
    opt=input('\nEnter 1 to add data, 2 to delete data, 3 to traverse and print the data, 0 to quit:\n')
    if opt=='0':
        break
    menu_dict[opt]()

