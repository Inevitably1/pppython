import random
print("\t数字炸弹\n")
while 1:
    min = int(input("请输入最小数："))
    max = int(input("请输入最大数："))
a = random.randint(min,max)
print(a)
round=0
while 1:
    b=int(input("输入%d到%d的数："%(min,max)))
    if b>max or b<min:
            print("输入不合法，重新输入")
    else:
        round+=1
        if b>a:
            print("大了")
            max=b-1
        if b<a:
            print("小了")
            min=b+1
        if b==a:
            print("\tBOOM!!!")
            break
print("回合数=%d"%round)
