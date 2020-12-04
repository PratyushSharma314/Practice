
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
c_list = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]

result_list = []

for s in c_list:
    if sum(s) != n:
        result_list.append(s)

print(result_list)




