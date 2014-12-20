'''
originally written in java, the python version is modified to begin sorting from behind
insertion sort in reverse order: start sorting by placing the largest element at the end
'''


def insert_sort(inlist):
	size = len(inlist)
	pos = len(inlist) -2  #start from the 2nd last also fine)
	while(pos>=0):
		pivt = pos		#check through each item before the current position
		while( pivt < size-1):	
			if inlist[pivt]>inlist[pivt+1]:
				maxi = inlist[pivt]
				inlist[pivt]= inlist[pivt + 1]
				inlist[pivt + 1] = maxi
			pivt += 1
		pos -= 1
	return inlist

x = [6, 2, 3, 4, 5, 1]
y = insert_sort(x)
print(y)