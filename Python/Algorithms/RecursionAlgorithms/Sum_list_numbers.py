"""

Algo. for calculating sum of list of numbers's
list elements [2,4,5,6,7]
sum should be equal to 32

"""

def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
        
print(list_sum([2, 4, 6, 8, 12]))
