#1 가상환경 구축
#2 1에서10 리스트 4가지

# num_list1 = []
# num_list2 = []
# num_list3 = []
# num_list4 = []

# for i in range(1,101):
#     if i%2 == 0 :
#         num_list1.append(i)
# print(num_list1)

# num_list2 = [i for i in range(1,101) if i%2 == 0]
# print(num_list2)

# i = 0
# while range(1, 101):
#     i += 1
#     if i == 101:
#         break
#     elif i%2 == 0 :
#         num_list3.append(i)

# print(num_list3)

num_list4 = list(filter(lambda a : a%2 == 0, range(1,101)))

print(num_list4)

#3 조 문제 3개 이상 함수(return값 & parameters)
#4 파일 다루기 

# from pathlib import Path
# import requests

# path = Path('test3.txt')

# contents_list = path.read_text()

# print(contents_list)

# contents_list = contents_list.splitlines()
# print(contents_list)



# for i,word in enumerate(contents_list):
#     contents_list[i] = word.rstrip()
#     contents_list[i] = word.lstrip()

# print(contents_list)

# contents_list = list(set(contents_list))
# print(contents_list)
# new_contents = ('\n'.join(contents_list))
# print(new_contents)

# 5
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267'
]

from pathlib import Path
import requests
import time

# start_time = time.perf_counter()

 

# ++++ 폴더 / 파일 만들기  & request 이용하여 이미지 다운로드 하기
folder = 'images4'
path = Path (folder)
img_names = [url.split('/')[-1] + '.jpg'for url in img_urls]
file_name = path/img_names[0]
with file_name.open(mode = 'w') as file:
        file.write(' ')
for url in img_urls:
    if not path.exists():
        path.mkdir(parents = True )
        img_path = path /name
        img_data = requests.get(img_urls[0]).content
        with .open(mode = 'w') as file:
        file.(' ')
  
  
# *** threading 만들기   
# thread = threading.Thread(target = img_download, args = (url,))
# thread.start()

# 11

# import numpy as np

# array = np.arange(27).reshape((3, 3, 3))




