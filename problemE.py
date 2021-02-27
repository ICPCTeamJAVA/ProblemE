import sys
res = ""
for i in sys.stdin:
	ab = i.split()
	R = int(ab[0])
	S = float(ab[1])
	V = int((((R*(S+0.16))/0.067))**(1/2))
	print(V)
