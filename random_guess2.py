import random as rand

def calc(u):
    if u==1:
        return "1st Shot, fine shot!"
    elif u==2:
        return "2nd Shot, You got this!"
    elif u==3:
        return "3rd Shot, Great!"
    elif u==4:
        return "4th Shot, Thats good."
    else:
        return "Finally!"



def check():
    while 1:
        try:
            b=int(input("A number between 1 to 100: "))
            if 1<=b<=100:
                return b
            else:
                print("Stick to the numerical range.(A number between 1 to 100)")
        except ValueError:
            print("be sure to enter a number between 1 to 100 \n-------------")







def guidance(z,x):
    if -5<=z-x<=5:
        return "Close"
    elif -15<=z-x<=15:
        return "just a little close"
    else:
        return "you are so far"



def guess_rand():
    a=rand.randint(1,100)
    count=0
    count_check=True

    for i in range(1,6):
        print(f"-------------\n Attempt {i} of 5")
        print("Enter your number\n-----------")
        b=check()

        if a==b:
            r=calc(i)
            count_check=False
            return f"---- Congratulations, you won !{r}"

        elif a>b :
            print(f"Enter a greater number, {guidance(a,b)}")
            count += 1
        elif a<b :
            print(f"Enter a less number, {guidance(a,b)}")
            count+=1

    return f"\nSorry, but you lose and you dont have any chances\nnumber was {a}"


print(guess_rand())

while True:
    print("\nPlay Again?(y/n)")
    answer = str(input())
    if answer == "y" or answer == "Y":
        print(guess_rand())
    elif answer=="n" or answer=="N":
        print("Goodbye!")
        break
    else:
        print("invalid input")