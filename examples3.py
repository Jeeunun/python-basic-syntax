# # arr = ["a","b","c"]
# # result = "".join(arr)
# # print(result)


# # numbers = [1,2,3,4,5,6,7,8,9,10]
# # print(sum(numbers)/len(numbers))

# # participant = ['leo','kiki','eden']
# # completion = ['eden','kiki']

# # participant.count = completion.count + 1


# # participant = ["mislav","stanko","mislav","ana"]
# # completion = ["stanko","ana","mislav"]
# # dict1 = {}

# # num_list = [12,4,15,46,38,-2,15]
# # for num in num_list:
# #     if num < 0 :
# #         print(num_list.index(num))
# # #         break 
# # # for num in num_list:
# # #     if 

# # # order = [29423]
# # # for a in str(order) :
# # #     if int(a) % 3 == 0:
# # #         print(order.count(a))

# # #369게임 (다시 풀어보기)
# # def solution(order):
# #     answer = 0
# #     for a in ['3','6','9']:
# #         answer += str(order).count(a)
# #     return answer

# # def solution(order):
# #     answer = 0
# #     for a in list(str(order)):
# #         if a in ['3','6','9'] :
# #             answer += 1
# #     return answer
# # lista = [90,25,67,45,80]
# # for score in lista:
# #     if score >= 60:
# #         print(lista.index(score)+1,"번 학생은 합격입니다.")
# #     else :
# #         print(lista.index(score)+1,"번 학생은 불합격입니다.")

# # lista = [90,25,67,45,80]
# # num = 1
# # for score in lista:
# #     if score >= 60:
# #         print("%d 번 학생은 합격입니다."%num)
# #     else :
# #          print("%d 번 학생은 불합격입니다."%num)
# #     num+=1

# # lista = [90,25,67,45,80]
# # for a in range((len(lista))):
# #     if lista[a]>= 60:
# #         print("%d 번 학생은 합격입니다." %(a+1))
# #     else :
# #          print("%d 번 학생은 불합격입니다." %(a+1))

# lista = ['b','b','ab','a','b','a']
# num = 1
# for a in lista:
#     if a == 'a':
#         print("%d 번째 고객이 이벤트에 당첨되었습니다." %num)
#         num+=1
#         break
# lista = ['b','b','ab','a','b','a']
# for a in range(len(lista)):
#     if list[a] == 'a':
#         print("%d 번째 고객이 이벤트에 당첨되었습니다." % (a+1))
#         break

# answer = 0
# for a in range(len(lista)):
#     if lista[a] == 'a':
#         answer = a + 1
#         # break를 넣고 안넣고 결과값 차이 확인
#         break
# print(str(answer),"번째 고객이 당첨되었습니다.")

# numinput = int(input("구구단 몇단을 계산해드릴까요?: "))
# for a in range(1,11):
#     print(f'{numinput} * {a} = {numinput * a}')

# numinput = int(input("구구단 몇단을 계산해드릴까요?: "))
# for a in range(1,11):
#     print(f"{numinput} X {a} = {numinput * a}")          

# for a in range(1,11):
#     for b in range(1,11):
#         print(f"{a} X {b} = {a*b}")

# for a in range(5,10):
#     for b in range(1,11):
#         print(f"{a} X {b} = {a * b}")

# num = 5        
# while num < 10:
#     for a in range(1,11):
#         print(f"{num} X {a} = {num * a}") 
#     num +=1  
# lista = [10,20,30,40]
# temp = lista[0]
# lista[0] = lista[1]
# lista[1] = temp
# print(lista)

# lista = [93,45,21,30,20,94,66,71,45]
# # 위 리스트를 어떻게 오름차순 정렬 할 것인가?
# lista.sort()
# print(lista)

# lista = [93,45,21,30,20,94,66,71,45]

# for a in range(len(lista)):
#     k = len(lista) - 1
#     for b in range(1,k):
#         if lista[b-1] >= lista[b]:
#             temp = lista[b-1]
#             lista[b-1] = lista[b]
#             lista[b] = temp
# print(lista)

# for a in range(len(lista)):
#     for b in range(a+1,len(lista)):
#         if lista[a] >= lista[b]:
#             temp = lista[a]
#             lista[a] = lista[b]
#             lista[b] = temp
# print(lista)

# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
# answer = []
# # answer = [[arr1[0][0]+arr2[0][0], arr1[0][1]+arr2[0][1]], [arr1[1][0]+arr2[1][0], arr1[1][1]+arr2[1][1]]]
# for a in range(len(arr1)):
#     temp = []
#     for b in range(len(arr1[a])):
#         temp.append(arr1[a][b]+arr2[a][b])
#     answer.append(temp)
# print(answer)

# 버블정렬 : 큰 수를 마지막으로 밀어내는 것. 
# lista = [93,45,21,30,20,94,66,71,45]
# # 내가 푼 것.
# for a in range(len(lista)): #a=0~8
#     for b in range(a+1,len(lista)): #b=1~8
#         if lista[a] > lista[b]:
#             temp = lista[b]
#             lista[b] = lista[a]     
#             lista[a] = temp #변화된 값
# print(lista)

# # 옆에 있는 값과 비교
# arr = [93,45,21,30,20,94,66,71,45]
# for i in range(len(arr) - 1, 0, -1): #range(8,0,-1) => 8번째부터 0까지 간격0 => i =8~0
#     for j in range(i):              #j = 7~0
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # arr[8] < arr[7] => arr[8] = arr[7]
# # 결과 93,45,21,30,20,94,66,45,71
# # arr[8] = 45 => 비교해야할 대상
# # arr[8] < arr[6] => arr[8] = arr[6]
# # arr = [93,45,21,30,20,94,66,71,45]
# for i in range(len(arr) - 1, 0, -1): #range(8,0,-1) => 8번째부터 0까지 간격0 => i =8~0
#     for j in range(i):              #j = 7~0
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# myInput = int(input("숫자를 입력하세요: "))
# def myFunc(myInput):
#     calc = (((myInput+10)*20)/10)**2
#     return calc
# calc = myFunc(myInput)

# def myPlusFunc(myInput1,myInput2):
#     calc = (myInput1+myInput2)*2
#     return calc

# result = myPlusFunc(10,20)
# print(result)

# lista = [1,4,6,9]
# for a in range(len(lista)):
#     if lista[a] == 9:
#         print(a)

# def myIndex(i1,i2):
#     for a in range(len(i1)):
#         if lista[a] == i2:
#             print(a)
#             break

# lista = [1,4,6,9,9]
# r1 = myIndex(lista, 9)
# print(r1)

# lista = ['b','b','ab','a','b','a']
# # 출력 결과 : n번째 고객이 이벤트에 당첨되었습니다.
# for a in range(len(lista)):
#     if lista[a] == 'a':
#         print(a+1,"번째 고객이 이벤트에 당첨되었습니다.")
#         break

# def myIndex(l, num):
#     for a in range(len(l)):
#         if l[a] == num:
#             return a

# result = myIndex([1,2,3,4,5,6,7,8,9],5)
# print(result)

lista = [93,45,21,30,20,94,66,71,45]
# [1] 93과 45 비교 
# temp = lista[0]
# lista[0] = lista[1]
# lista[1] = temp
# [2] 93과 21 비교
# temp = lista[1]
# lista[1] = lista[2]
# lista[2] = temp
# [3] 93과 30 비교
# [4] 93과 20 비교
# [5] 93과 94 비교
# [6] 94와 66 비교
# [7] 94와 71 비교
# [8] 94와 45 비교 
# [45,21,30,20,93,66,71,45,94]
# ---------------------
# [1] 45와 21비교
# [2] 45와 30비교
# [3] 45와 20비교
# [4] 45와 93비교
# [5] 93과 66비교
# [6] 93과 71비교
# [7] 93과 45비교 
# [21,30,20,45,66,71,45,93,94] => 여기서 아까 확인한 값도 제외해야함. 
for a in range(len(lista)-1):#마지막수는 굳이 확인안해도 큰 수이기 때문에
    for b in range(len(lista)-a-1) #정리된 데이터는 반복할 필요가 없어서 a회 제외