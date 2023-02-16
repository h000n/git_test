# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np


# number = 0
# lists = [0]*101
# for z in range(1000):
#     success = 0
#     prisoners = list(range(100))
#     boxes = dict()
#     np.random.shuffle(prisoners)
#     for i,n in enumerate(prisoners):
#         boxes[i] = n
#     # print(prisoners,boxes)
#     for prisoner in prisoners:
#         box_num = prisoner
#         for _ in range(50):
#             box_result = boxes[box_num]
#             if box_result == prisoner:
#                 success +=1
#                 break
#             else:
#                 box_num = box_result
#     if success == 100:
#         number += 1

#     lists[success] += 1

# plt.figure(figsize=(16,9))
# sns.barplot(x=list(range(101)),y=lists)
# plt.show()

from secrets import choice
from tqdm import tqdm
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

number = 0
lists = [0]*101
for sim in tqdm(range(10000)):
    success = 0
    prisoners = list(range(100))
    boxes = dict()
    np.random.shuffle(prisoners)
    for i,n in enumerate(prisoners):
        boxes[i] = n
    # print(prisoners,boxes)
    for prisoner in prisoners:
        # for _ in range(50):
        #     box_num = random.randint(0,99)
        #     box_result = boxes[box_num]
        #     if box_result == prisoner:
        #         success +=1
        #         break
        choices  = np.random.choice(range(100),size=50,replace=False)
        for choic in choices:
            if boxes[choic] == prisoner:
                success += 1
    # if success == 100:
    #     number += 1
    lists[success] += 1

plt.figure(figsize=(56,10))
sns.barplot(x=list(range(101)),y=lists)
plt.show()