a = 100
# 특정한 input값이 있을 때, 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자. 
# 그런데 해당 연산은 매우 빈번하게 사용이 된다고 가정하자.
result = (((a+10)*20)/10)**2
print(result)

b = 200
result2 = (((b+10)*20)/10)**2
print(result2)
# 복잡 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자. 
# input값이 있어도 되고, 없어도 된다. 
# return값이 있어도 되고, 없어도 된다. 

def myFunc(myInput):
    calc = (((myInput+10)*20)/10)**2
    return calc
# 정의된 함수를 호출할 때는 함수명(input)의 형태로 호출하게 된다. 
result2 = myFunc(200) #200을 함수식에 input해서 return값이 도출된다. 


# myInput = int(input("숫자를 입력하세요: "))
# def myFunc(myInput):
#     calc = (((myInput+10)*20)/10)**2
#     return calc
# result = myFunc(myInput)
# print(result)

# 함수 직접 구현해보기
# 함수명은 myPlustFunc
# 함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 함수
# 예를 들면 100을 입력하면 1+2+3+4....+100
myInput = int(input("숫자를 입력하세요: "))
def myPlusFunc(myInput):
    for a in range(1,myInput+1):
        tot +=a 
    return tot
# 출력해보기
result = myPlusFunc(10)
print(result)

# 함수 직접 구현해보기
# input값을 2개를 받아 2값을 더한 뒤, *2만큼 하여 return하는 함수를 만들어보자.
# 그리고, 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자.
def myPlusFunc(myInput1,myInput2):
    calc = (myInput1+myInput2)*2
    return calc
# 출력해보기
result = myPlusFunc(10,20)
print(result)

# 문제)
# 리스트의 index함수를 쓰지 않고, for문 또는 while문을 통해 숫자 9가 몇 번째 인덱스에 있는 값인지 
# print해보자.  
# index함수
lista = [1,4,6,9,9]
print(lista.index(9)) 
# for문/while문
lista = [1,4,6,9,9]
for a in range(len(lista)):
    if lista[a] == 9:
        print(a)
        break
# 함수로 구현
# 위의 for문을 활용하여 myIndex라는 이름의 함수를 만들고자 한다.
# input값이 2개 (list, 찾고자하는 값)
# print는 함수내에서 하지 않고, return에 값을 담는다. 
def myIndex(n1,n2):
    result = 0
    for n2 in range(len(n1)):
        if lista[a] == n2:
            result = a
            return n2
            break
    return result
    
# 출력해보기
lista = [1,4,6,9,9]
result = myIndex(lista,9)
print(result)

def myIndex(n1,n2):
    for n2 in range(len(n1)):
        if lista[a] == n2:
            print(n2)
            break
        
lista = [1,4,6,9,9]
def myIndex(i1,i2):
    result = -1
    for a in range(len(i1)):
        if lista[a] == i2:
            result = a
            break
    return result

def myIndex(i1,i2):
    for a in range(len(i1)):
        if lista[a] == i2:
            print(a)
            break

lista = [1,4,6,9,9]
r1 = myIndex(lista, 9)
print(r1)