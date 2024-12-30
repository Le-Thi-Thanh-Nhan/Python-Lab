#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = [1,2,3,4,5,6]
print(a[-1], a[len(a)-1])
print(a[1:4])


# In[5]:


a = ['cat', 'dog', 'monkey']
for i in a:
    print(i)


# In[9]:


#nhập dãy n số thực và sắp xếp theo thứ tự tăng dần
a=[]
n = int (input("Nhập số lượng phần tử: "))
for i in range(n):
    tg = input(f"A[{i}] = ")
    tg = float(tg)
    a.append(tg)

# sắp xếp
for i in range(n-1):
    for j in range(i+1, n):
        if (a[j]<a[i]):
            tg = a[i]
            a[i]= a[j]
            a[j]= tg
# in dãy đã sắp xếp
print(a)

#for i in range(n):
    #print(f"{a[i]} ")
b = enumerate(a)
for i, v in b:
    print(f"{i}  {v} ")        
    


# In[12]:


# nhập vào từ bàn phìm 1 xâu ký tự, hãy đếm số từ của xâu và 
# số lần xuất hiện của từng từ trong xuất hiện trong xâu đó
s= "nhập vào từ bàn phìm 1 xâu ký tự, hãy đếm số từ của xâu và số lần xuất hiện của từng từ trong xuất hiện trong xâu đó"
dic = dict({})
ws = s.split()
for w in ws:
    if w in dic:
        dic[w]= dic[w]+1
    else:
        dic.update({w:1})
#in kết quả
for w in dic.keys():
    print(f" Từ [{w}] xuất hiện {dic[w]} lần")


# In[24]:


# nhập vào từ bàn phìm 1 xâu ký tự, hãy đếm số từ của xâu và 
# số lần xuất hiện của từng từ trong xuất hiện trong xâu đó
from pyvi import ViTokenizer, ViPosTagger
 
#s= u"nhập vào từ bàn phím 1 xâu ký tự, hãy đếm số từ của xâu và số lần xuất hiện của từng từ trong xâu ký tự đó"
s= "Trường Đại học Kinh tế - Kỹ thuật Công nghiệp"
dic = dict({})
#ws = s.split()
ws= ViTokenizer.tokenize(s)
print(ws)
ws = ws.split()
for w in ws:
    if w in dic:
        dic[w]= dic[w]+1
    else:
        dic.update({w:1})
#in kết quả
for w in dic.keys():
    print(f" Từ [{w}] xuất hiện {dic[w]} lần")


# In[30]:


from pyvi import ViTokenizer, ViPosTagger


#s1 = "Truyện Kiều đã viết bởi Nguyễn Du, Truyện Kiều là một tác phẩm lớn"
#s2 = "Nguyễn Du đã sáng tác Truyện Kiều, Nguyễn Du là một nhà thơ lớn"
s1 = "Truyện Kiều đã viết bởi Nguyễn Du"
s2 = "Nguyễn Du đã viết Truyện Kiều"
s1= ViTokenizer.tokenize(s1)
s2= ViTokenizer.tokenize(s2)


s1 = set(s1.split())
s2= set(s2.split())
print(s1)
print(s2)

overlap =  s1.intersection(s2)
union = s1.union(s2)

similarity = len(overlap)/len(union)
print(similarity)


# In[32]:


d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"

for key in d.keys():
    print(f"{key} - {d[key]}")


# In[33]:


import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"


# In[34]:


import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"


# In[ ]:


#Cho ma trận số thực n hàng m cột, 
# a. hãy tìm phần từ lớn nhất, nhỏ nhất của ma trân.
# b. Hãy tìm điểm yên ngựa Tức là là phần tử lớn nhất trong cột 
#và nhỏ nhất trong hàng chứa nó hoặc
#là phần tử nhỏ nhất trong cột và lớn nhất trong hàng chứa nó

