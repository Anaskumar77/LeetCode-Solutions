target = 10
position = [6,8]
speed = [3,2]

# v1 = 0
# num = 0 
# l = len(position)
# List = []
# for i in range(l):
#     List.append([position[i],speed[i]])

# List.sort(key = lambda x : x[0])

# print(List)
# for i in range(l-1,-1,-1):
#     v2 = (target - List[i][0]) / List[i][1]
#     if v1  < v2:
#         num += 1
#         v1 = v2

# print(num)        

def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    v1 = 0
    num = 0 
    l = len(position)
    List = []
    for i in range(l):
        List.append([position[i],speed[i]])

    List.sort(key = lambda x : x[0])

    for i in range(l-1,-1,-1):
        v2 = (target - List[i][0]) / List[i][1]
        if v1  < v2:
            num += 1
            v1 = v2
    return num

print(carFleet(target,position,speed))



        

