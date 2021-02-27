for i in sys.stdin:
	ab = i.split()
	S = float(ab[0])
	R = float(ab[1])
	V = ((R*(S+0.16))/0.067)**(1/2)
	print(int(V))
