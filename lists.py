if __name__ == '__main__':
    N = int(input())
    
    task_list = []
    value_list = []
    for _ in range(N):
        task, *value = input().split()
        value = list(map(int, value))
        task_list.append(task)
        value_list.append(value)
    
    #print(task_list)
    #print(value_list)

    operate_list = []

    for i in range(N):

        if task_list[i] == 'append':
            operate_list.append(value_list[i][0])
        
        elif task_list[i] == 'sort':
            operate_list.sort()
        
        elif task_list[i] == 'print':
            print(operate_list)
        
        elif task_list[i] == 'pop':
            operate_list.pop()

        elif task_list[i] == 'insert':
            operate_list.insert(value_list[i][0], value_list[i][1])

        elif task_list[i] == 'remove':
            operate_list.remove(value_list[i][0])
        
        elif task_list[i] == 'reverse':
            operate_list.reverse()

        else:
            print("incorrect task found")


        

