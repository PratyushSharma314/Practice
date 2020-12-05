if __name__ == '__main__':

    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    marks = [m[:][1] for m in records]
    marks = set(marks)
    marks = sorted(list(marks))
    #print(marks)
    second_lowest = marks[1]

    names = []
    for i in records:
        if i[1] == second_lowest:
            names.append(i[0])
        
    names = sorted(names)
    for n in names:
        print(n)

    
