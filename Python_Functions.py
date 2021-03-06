# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bPWWi0j41XoGXAZhkwxJIaOGf2gbcft2

Functions and Passing Multiple Arguments using list and tuple
"""

def fn(a,b):
    f = a + b
    return print(f)

if __name__ == "__main__":
    fn(2,3)

def fn(a=1,b=5):
    f = a + b
    return print(f)

if __name__ == "__main__":
    fn()

#Multiple Keyword arguments    
    
def fn(a,b):
    f = a + b
    return print(f)

if __name__ == "__main__":
    fn(a=5,b=6)

def fn(**kwargs):
  f=1
  for key, i in kwargs.items():
      print(i)

if __name__ == "__main__":
    fn(a=9,b=7,g=8)

 #multiple arguments   

def fn(*args):
  f=0
  for i in args:
    f += i
    print(f)
if __name__ == "__main__":
    fn(6,7,7,7)
    
#Passing hardcode List and add the elements     

def fn(*args):
  f=0
  for i in args:
    f += i
    print(f)
if __name__ == "__main__":
  user_list=[6,7,8]
  for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
  x= tuple(user_list)
  print(type(x))
  print(x)
  fn(*x)
    
#Passing input List and add the elements     

def fn(*args):
  f=0
  for i in args:
    f += i
  print(f)
if __name__ == "__main__":
  input_string = input('Enter elements of a list separated by space ')
  user_list = input_string.split()
  for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
  x= tuple(user_list)
  print(type(x))
  print(x)
  fn(*x)
