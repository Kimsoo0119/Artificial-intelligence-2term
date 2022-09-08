
a = 123
print(a)
print(123.456, "Hellow world!")

a = 3
b = 4
c = a + b
print("덧셈:", c)
d = a - b
print("뺄셈:", d)
e = a * b
print("곱셈", e)
print("거듭제곱", a ** 3)

g = a / b
print(g)
h = a // b
print(h)

print(7//3)
print(7/3)
i = a % b
print(i)
print(7 % 3)
j = 5
j += 3
print(j)
k = 5
k -= 2
print(k)
l = 2.367e5
print(l)
m = 2.3e-5
print(2.3e-5)


#list
aa = [1,2,3,4,5]
print(a[2])
bb = [4, 5, 6, 7,] 
print(b[3])

#object oriented(객체 지향)
cc = [1, 2, 3, 4]
print(cc)
cc.append(6)
print(cc)
cc.append(9)
print(cc)

dd = [[1,2,3], [4,5,6]]
print(d) 
ee = [1, 2]
print(ee * 3)

#tuple
aaa = (1, 2, 3, 4, 5)
bbb = aaa[2]
print(bbb)

ccc = (3, )
print(ccc)

ddd=[1, 2, 3]
ddd_1,ddd_2,ddd_3 = ddd
print(ddd_1,ddd_2,ddd_3)

eee = (4, 5, 6)
eee_1,eee_2,eee_3 = eee

print(eee_1,eee_2,eee_3)

#if 조건문
a = 2
if a > 3:
    print(a + 2)
else:
    print(a - 2)

b = 8
if b == 7:
    print(b + 2)
else:
    print(b - 2)

#for 반복문
for a in [4, 7, 10]:
    print(a + 1)
for b in range (10, 20): # 시험 대상 ㅎㅎㅎ
    print(b)

#function 함수
def my_func(x):  # function정의는 def로 함
    y = 2 * x +3
    print(y)
    
my_func(3)

def my_func_2(a, b):
    print(a + b)
    
my_func_2(5, 6)

def my_func_3_1(a, b):
    c = a + b
    return c
d = my_func_3_1(5, 6)
print(d)

def my_func_3_2(a, b):
    c = a + b
    d = a - b
    return (c, d) #반환을 튜플로 할 수 있음

e, f = my_func_3_2(5, 6) #튜플의 요소를 각각 저장
print(e,f)

# scope global(전역)로 설정되어 있는 변수의 값을 local(지역)에서 
# 변경 하면 전역으로 설정한 값이 변경된다.

w = 123 #Global

def show_number():
    global w 
    w = 200
    z = 456 #Local
    print(w, z)
print(w)
show_number()
print(w)
