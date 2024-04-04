import random

n=int(input("Siyahida nece element olacaginin sayini daxil edin: "))
result=1
ran_list=random.sample(range(4,48),n)
print(ran_list)
for x in ran_list:
    if (x%3)==1:
        print(x)
        result*=x
print(result)