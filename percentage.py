if __name__ == '__main__':
    
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    avg_marks = (sum(marks))/3
    avg_marks = "{:.2f}".format(avg_marks)
    print(avg_marks)


