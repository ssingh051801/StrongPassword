
import string
import random

if __name__== "__main__" :
    s1 =string.ascii_uppercase
  #  print(s1)
    s2 =string.ascii_lowercase
   # print(s2)
    s3 =string.digits
   # print(s3)
    s4 =string.punctuation
   # print(s4)

    plen=int(input("Length of Password =  "))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print("PASSWORD IS = ", "".join(s[0:plen]))


