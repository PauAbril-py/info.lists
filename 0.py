l = []
while True:
	opt=input('1)append\t2)print full list\t3)print element from list\t4)exit')
	if opt.isnumeric() == True and int(opt) in range(1,4):
		if int(opt) == 1:
			l.append(input())
		elif int(opt) == 2:
			output = ''
			for i in range(len(l)):
				output = output , l[i]
			print(output)
		elif int(opt) == 3:
			print(l[int(input('position'))-1])
		elif int(opt) == 4:
			break