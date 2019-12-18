#!/usr/bin/python

L1 = {'1' : ['A' , 'B' , 'C', 'D'], '2' : ['B', 'A', 'C', 'D'], '3' : ['B', 'C', 'A', 'D'], '4' : ['B', 'A', 'D', 'C']}
L2 = {'A' : ['4', '2', '3', '1'] , 'B' : ['2', '1', '3', '4'] , 'C' : ['1', '2', '3', '4'] , 'D' : ['4', '1', '2', '3']}

new = []
array = []
z = 0
k = 1
while (k <= len(L1)):
	empty = []
	k = str(k)
	for i in L1[k]:
		if (i not in new):
			if (k not in new):
				var = L1[k].index(i)
				i = str(i)
				var2 = L2[i].index(k)
				tot = var + var2
				empty.append(tot)
				if (tot == min(empty)):
					temp = []
					new.append(i)
					temp.append(i)
					temp.append(k)
					new.append(k)
					array.append(temp)
	k = int(k)
	k += 1

print array
