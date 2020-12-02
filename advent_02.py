

def passwordcount_1(Lines):
	validcount=0
	for line in Lines: 
		values =line.split()[0]
		min_val = int(values.split('-')[0])
		max_val = int(values.split('-')[1])
		constraint = (line.split()[1])[0]
		password=line.split()[2]
		count = 0 
		for c in password:
			if(c == constraint):
				count+=1
		if (count <= max_val) and (count >= min_val):
			validcount+=1
	print(validcount)

def passwordcount_2(Lines):
	validcount=0
	for line in Lines: 
		values =line.split()[0]
		min_val = int(values.split('-')[0])
		max_val = int(values.split('-')[1])
		constraint = (line.split()[1])[0]
		password=line.split()[2]
		flag = 0 
		if password[max_val-1] == constraint :
			flag +=1
		if password[min_val-1] == constraint :
			flag +=1
		if flag == 1:
			validcount+=1
	print(validcount)

if __name__ == '__main__':
	file1 = open("data_02.txt", "r")
	Lines = file1.readlines() 
	passwordcount_2(Lines)





