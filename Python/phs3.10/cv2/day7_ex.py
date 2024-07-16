import numpy as np

# 문제 1: 딕셔너리에서 값이 특정 문자열과 일치하는 키-값 쌍 찾기 

string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}
search_value = "brown"

sech_dict = dict(filter(lambda x : x[1] == "brown" , string_dict.items()))

print(sech_dict)

# 문제 2: 딕셔너리의 값들을 모두 대문자로 변환

string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}

up_dict = dict(map(lambda x : (x[0],x[1].upper()) , string_dict.items()))

print(up_dict)

# 문제 3: 딕셔너리의  key  value를 바꾸기

string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}

ch_dict = dict(map(lambda a : (a[1],a[0]), string_dict.items()))

print(ch_dict)

# 문제 4: 문자열 리스트의 각 문자열을 역순으로 변환

string_list = ["apple", "banana", "kiwi", "orange", "grape"]

# sorted(string_list, reverse = True)

print(sorted(string_list, reverse = True))

# 문제 5 문자열 딕셔너리를 value를 중심으로 sort하기

string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}

print(dict(sorted(string_dict.items(), key= lambda item : item[1])))

