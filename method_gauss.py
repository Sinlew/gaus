
import os



def prnA(a,dere,be):
    for i in range(dere):
        for j in range(be+1):
            if j==be:
                print("|",'%9.2f'%a[i][j],end='')
            else: print('%9.2f'%a[i][j],end='')
        print(end='\n')
    print(end='\n')

os.system('mode con: cols=100 lines=40')


raz = int(input("Введите размерность основной матрицы: "))
a = list()
for i in range(raz):
    spisok = input(f"Введите {raz+1} чисел через пробел, где последнее число значение расширенной матрицы {i+1} строки \n").split()
    a.append(list(map(int, spisok)))


#a=[[0,2,0,4,5],   [0,2,0,4,5],   [0,5,0,8,5],   [1,2,8,1,1]]

der,b = len(a),len(a[0])-1

print("Данная матрица \n")
prnA(a,der,b)

fl = 0
print("Избавление от нулей на главной диагонали \n")
for i in range(der):
    for k in range(der):
        if a[i][i]==0:
            fl =1
            a[i],a[k]=a[k],a[i]
            prnA(a,der,b)
if fl == 0:
    print("----- \n")

for i in range(der):
    if a[i][i]==0:
        print("Одна или несколько переменных не могут иметь не нулевой коэффициент на главной диагонали")
        en = input()
        exit()           


print('Прямой ход \n')
#Прямой ход
for i in range(der-1):
    if sum(a[i][:-1])==0:
        print("система либо несовмествна, либо имеет бесконечное число корней")
        en = input()
        exit()
    for k in range(i+1,der):
        d=-a[k][i]/a[i][i]
        for j in range(der+1):
            a[k][j]+=a[i][j]*d
    prnA(a,der,b)

print('Обратный ход \n')

#Обратный ход
for i in range(der-1,-1,-1):
    for k in range(i-1,-1,-1):
        
        d=-a[k][i]/a[i][i]
        for j in range(der,0,-1):
            a[k][j]+=a[i][j]*d
    prnA(a,der,b)

#Нахождение корней 
print("Корни уравнения \n")
for i in range(der):
    print(f"X{i+1}={'%9.2f'%(a[i][-1]/a[i][i])}")

en = input()
