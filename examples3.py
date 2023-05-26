# arr = ["a","b","c"]
# result = "".join(arr)
# print(result)


# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(sum(numbers)/len(numbers))

# participant = ['leo','kiki','eden']
# completion = ['eden','kiki']

# participant.count = completion.count + 1


# participant = ["mislav","stanko","mislav","ana"]
# completion = ["stanko","ana","mislav"]
# dict1 = {}

# num_list = [12,4,15,46,38,-2,15]
# for num in num_list:
#     if num < 0 :
#         print(num_list.index(num))
#         break 
# for num in num_list:
#     if 

# order = [29423]
# for a in str(order) :
#     if int(a) % 3 == 0:
#         print(order.count(a))

#369게임 (다시 풀어보기)
def solution(order):
    answer = 0
    for a in ['3','6','9']:
        answer += str(order).count(a)
    return answer

def solution(order):
    answer = 0
    for a in list(str(order)):
        if a in ['3','6','9'] :
            answer += 1
    return answer