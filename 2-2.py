import random
n = random.randint(1,20) 
a = int(input("number:"))
counter = 0
while True:
    guess = int(input("請在1~20間猜一個數字(只能猜五次):")
    if guess>20 or guess<0:
        print("輸入錯誤，請重新輸入!!!")
        counter = counter +1
    else:
        if counter == 5:
            print("just 5 times")
            break
        elif guess > a:
            print("小一點")
            counter =counter+ 1
        elif guess < a:
            print("大一點")
            counter =counter+ 1
        else:
            print("Bingo!!!")
            counter =counter+ 1
            print("你猜了"+str(counter)+"次就答對了")
            break