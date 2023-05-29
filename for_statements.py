# while문의 기본 구조
# while 조건식: #조건식이 참인 경우 반복 => 무한반복이 기본전제
#      ~ 실행문
# a = 10
# while a>5:
#     print("참입니다.")

# 조건을 체크 후 True이면 실행문을 1회 실행시키고, 다시 조건을 체크하러 돌아온다. 그리고 True이면 또 다시 실행
# 그러다, 조건이 False가 되면 while문 종료.
a = 0
while a<5:
    print(str(a)+'번 반복')
    a+=1

# 1~1000까지만 프린트 되도록 출력
a = 1
while a <1001:
    print(str(a) + '번 반복')
    a+=1

a = 0
while a <1000:
    a+=1
    print(str(a) + '번 반복')
    
# 1~1000까지 모두 더한 값(b), 평균값 출력
a=1
b=0
while a <1001:
    b+=a
    a+=1
print(b)
print(b/1000)

# while문에서 반복을 진행하다가 break를 만나면, 반복문 종료.
# 1) if문을 써서 XXX한 조건에 break
a=1
b=0
while True:
    b+=a
    if a == 1000:
        break
    a+=1
print(b)
print(b/1000)

# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동.
# 하단에 불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 해준다. 
# 아래와 같이 코딩하면 hello가 무한 출력
# a = 0
# while a<1000:
#     print("hello")
#     continue
#     a+=1
# 문제
a=0
b=0
while a<1000:
    a+=1
    if a % 2 == 0:
        #continue문을 활용해서 coding
        continue   
    b+=a       
print(b)

# 2) 1~1000중에 홀수만 더해서 출력 #251001
a=0
b=0
while a<1001:
    a+=1
    if a % 2!=0:
        b+=a
print(b)
#문제 : 나만의 리스트 만들기
# 리스트의 크기를 키보드로 입력받아 그 크기만큼 임의 숫자를 리스트에 추가하고, 리스트의 크기와 값 전체를 출력하라.
# while True:
#     num = int(input("리스트의 크기를 입력하세요: "))
#     if num > 10:
#         print("다시 입력해주세요: ")
#         continue
#     lista=[]
#     a=0
#     while a < num:
#         listvalue = input("리스트의 값을 입력해주세요: ")
#         lista.append(listvalue)
#         a+=1
#     print(lista)

# # 내가 푼 것
# listsize = int(input("리스트의 크기를 입력하세요: "))
# a=0
# lista=[]
# while a<listsize:
#     listavalue=input("리스트의 값을 입력하세요: ")
#     lista.append(listavalue)
#     a+=1
# print(lista)

# 문제 : 로또 번호 생성기
# 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자. 
# 랜덤의 값을 추출하는 파이썬 라이브러리 -> random 

import random
print(random.randint(1,45))
lista=[]
listasize=1
while listasize < 7:
    randNum = random.randint(1,45)
    lista.append(randNum)
    listasize+=1
print(lista)

# for 문의 기본 구조
# for 변수 in 반복가능한 자료형 (iterable)
#     실행문
list = [1,2,3,4,5,6,7,8,9,10] # list는 대괄호써야함 / multiple 한 자료형
for a in list : 
    print('원소 : ' , a)

# range문법 : range(x,y) x이상y미만
for a in range(1,101):

# range의 의미: iterable 객체
# a = list(range(1,10))
# print(v1)

# range(x,y) : x이상 y미만의 숫자를 담은 객체
# range(y) : 0이상 y미만의 숫자를 담은 객체
    v1 = list(range(10,20))
# for a in 리스트를 써서 v1의 값을 모두 출력
for a in v1:
    print(a)
# for a in range를 써서 v1[index]의 형태로 v1의 값을 모두 출력
for a in range(0,10):
    print(v1[a])

# for a in 리스트 구문으로는 원본리스트 데이터를 변경할 수 없다. ->  인덱스로 !
lista = [10,20,30,40,50,60,70,80,90,100]
lista[5] = 100
# for a in lista:
#     a = 100 #이런 방식으로는 원본의 lista의 값을 변경할 수 없다.

# 직접 리스트의 index로 접근해야지 원본을 바꿀 수 있다. 
for a in range(len(lista)):
    lista[a] = 100

print(lista)

# 리스트를 만드는 방법 중에 리스트 컴프리헨션이라는 방법이 있다. 
# 리스트에 0~9까지를 담는 방법
#방법1
lista = [0,1,2,3,4,5,6,7,8,9]
#방법2
lista = list(range(10))
#방법3
lista =[]
for a in range(10):
    lista.append(a)
    
#방법4 : 리스트컴프리헨션
# 장점: 간결하다.
lista=[a*2 for a in range(10)]
print(lista)

# 홀수인 값에 2를 곱한 값만을 list로 만들어라.
lista =[]
for a in range(10):
    if a % 2!=0:
        lista.append(a*2)

lista=[a*2 for a in range(10) if a%2 !=0]
print(lista)