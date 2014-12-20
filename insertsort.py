'''
originally written in java, the python version is modified to begin sorting from behind
insertion sort in reverse order: start sorting by placing the largest element at the end
'''


def insert_sort(inlist):
	pos = len(inlist) -1  #start from the last item ( or the 2nd last also fine)
	while(pos>=0):
		pivt = pos -1		#check through each item before the current position
		while(pivt >= 0):	
			if inlist[pivt]>inlist[pos]:
				temp = inlist[pos]
				inlist[pos] = inlist[pivt]
				inlist[pivt]= temp
			pivt -= 1
		pos -= 1
	return inlist

x = [6, 2, 3, 4, 5, 1]
y = insert_sort(x)
print(y)