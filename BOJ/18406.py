n = input()
length = len(n)
if length % 2 == 1:
    print("READY")
elif sum(int(i) for i in n[:length//2]) == sum(int(j) for j in n[length//2:]):
    print("LUCKY")
else:
    print("READY")