a = int(input())
if a < 0 and >= 100000:
    print("INVALID")
if a % 4 == 0 and a % 4 != 0 or a % 400 == 0:
	print("YES")
else:
	print("NO")