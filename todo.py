l=[]
while True:
    print("--------TO DO LIST--------")
    print("1.Add tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Exit")
    print("##############################")
    choice=input("Enter your choice: ")
    if choice=="1":
        task=input("add the task : ")
        l.append(task)
        print("Task is added !!")
        print("-------------------------------")
    elif choice=="2":
        if len(l)==0:
            print("no tasks")
        else:
            for i in range(len(l)): #shows tasks with numbers
                print(i+1,l[i])
                print("------------------------------")
    elif choice=="3":
        if len(l)==0:
            print("no tasks to delete")
        else:
            tsk=int(input("enter the task to delete: "))
            if 0<tsk<=len(l):
                l.pop(tsk-1)
                print("Task deleted !!")
            else:
                print("invalid number")
    elif choice=='4':
        print("well done!!!")