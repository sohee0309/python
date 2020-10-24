#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from multiprocessing import Pool
import time
import os

def my_func(work): # work로 0~29
    print("일(={0})에 Process ID = {1}".format(work, os.getpid()))
    time.sleep(1) # 1초
    return work

if __name__ == '__main__': # 지금 작업하는 공간의 이름이 main이라면
    p = Pool(3) # 3은 프로세스의 개수
    startTime = int(time.time())
    print(p.map(my_func, range(0, 30))) # my_func 는 작업을 할 수 있는 도구, Pool은 map이라는 함수 제공
    endTime = int(time.time())
    print("작업 시간 = 약 {0}s".format(endTime - startTime))


# In[ ]:





# In[ ]:





# In[ ]:




