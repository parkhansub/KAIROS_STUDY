#a 와 b를 받아서 더하는 함수 만들기

# def add_num(a,b):
#     print(a+b)


# add_num(2,3)

#lanbda를 이용하여 함수 지정
# add_num = lambda a, b : a+b
# print(add_num(2,3))

# word_len = lambda w: len(w)

# print(word_len("hello world"))

# spu = lambda x : x*x
# print(spu(3))

# my_list = [x*x for x in range(4)]
# print(my_list)

# my_list_x = list(map(lambda x : x*x,my_list))
# print(my_list_

# num_list = list(map(lambda x : x+1,range(10)))
# print(num_list)

# num_list2 = list(filter(lambda x : x%2 == 0,num_list))
# print(num_list2)

# num_list3 = list(map(lambda x,y : x+y,num_list,num_list2 ))
# print(num_list3)

# max_num = lambda x, y : print(x) if x > y else print(y)
# max_num(1,3)

#연습문제 1: 리스트의 각 요소에 2를 더한 새로운 리스트 생성**
#문제: 주어진 리스트의 각 요소에 2를 더한 새로운 리스트를 생성하는 
#lambda 함수를 작성하세요.

original_list = [1, 3, 5, 7, 9]

new_list = list(map(lambda x : x+2 , original_list))
print(new_list)

# 연습문제 2: 홀수인 경우에만 제곱한 리스트 생성**
# 문제: 주어진 리스트에서 홀수인 경우에만 
# 해당 숫자를 제곱한 새로운 리스트를 생성하는 lambda 함수를 작성하세요.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_numbers = list(map(lambda x : x*x , 
list(filter(lambda x : x % 2 == 1,numbers))))
print(new_numbers)

# 연습문제 3: 문자열의 길이가 5보다 큰 경우만 필터링**
# 문제: 주어진 문자열 리스트에서 길이가 5보다 큰 문자열만 
# 필터링하는 lambda 함수를 작성하세요.

words = ["apple", "banana", "kiwi", "orange", "grape"]

cho_words = list(map(lambda x : x,
list(filter(lambda x : len(x) > 5 , words))))
print(cho_words)

# 연습문제 4: 두 리스트의 각 요소를 곱한 리스트 생성**
# 문제: 두 개의 리스트가 주어졌을 때, 각 요소를 곱한 결과로 
# 이루어진 새로운 리스트를 생성하는 lambda 함수를 작성하세요.

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

pro_list = list(map(lambda x,y : x*y,list1,list2))
print(pro_list)

# 연습문제 5: 주어진 숫자의 제곱 또는 세제곱 계산**
# 문제: 주어진 숫자가 짝수인 경우에는 제곱하고, 
# 홀수인 경우에는 세제곱한 결과를 반환하는 lambda 함수를 작성하세요.

number = 7

num = lambda x : print(x*x) if x % 2 == 0 else print(x*x*x)
num(number)

# 연습문제 6:  
# 문제: 1~10까지의 숫자 중 lamda를 이용해서 숫자를 짝수, 
# 홀수 그리고 0으로 구분하기

numbers2 = [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = list(map(lambda x : "0" if x == 0 else ("홀수" if x%2 == 1 else "짝수"), numbers2))
print(num)

#연습문제 7: 문자열 리스트의 각 문자열에 접두사 추가

string_list = ["apple", "banana", "kiwi", "orange", "grape"]
prefix = "fruit_"

awn_list = list(map(lambda x : x+prefix , string_list))
print(awn_list)



