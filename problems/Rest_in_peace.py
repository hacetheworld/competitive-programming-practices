def Solution(num):
    if num % 21 == 0:
        return True
    while num != 0:
        if(num % 100 == 21):
            return True

        num = num//10
    return False


for t in range(int(input())):
    num = int(input())
    if Solution(num):
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")
