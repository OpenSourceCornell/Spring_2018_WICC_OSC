#return the combination of the two lists such that their elements alternate
#unless one list runs out of elements
#ex: ['a','b','c','d'], ['1','2']
#return: ['a','1','b','2','c','d']
def alternating_lists(list1, list2):
	Alt_list=[]
	if len(list1)>len(list2):
		for i in range(len(list1)):
			if i<len(list2): Alt_list.extend([list1[i],list2[i]])
			else: Alt_list.append(list1[i])
	else:
		for i in range(len(list2)):
			if i<len(list1): Alt_list.extend([list1[i],list2[i]])
			else: Alt_list.append(list2[i])
	return Alt_list
    
