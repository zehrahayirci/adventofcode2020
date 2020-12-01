
file1 = open("data.txt", "r")
Lines = file1.readlines() 
  
count = 0
list_number = []
# Strips the newline character 
for line in Lines: 
	list_number.insert(count,int(line))
	count+=1 

list_number.sort()
print(count)

found = False
for i in range(count):
	for j in range(count):
		for k in range(count):

			if ( list_number[i] + list_number[j] + list_number[k] ) == 2020 :
				#print(list_number[i])
				#print(list_number[j])
				found = True
				print(list_number[i] * list_number[j] * list_number[k])
				break 
			if(list_number[k]) >2020:
				break
		
		if(list_number[j]) >2020:
			break

	if (found):
		break

		


