nlist = input().split("\n")
for i in nlist: 
	x = i.split()
	R = float(x[0])
	S = float(x[1])
	V = ((R*(S+0.16))/0.067)**(1/2)
	print(int(V))
