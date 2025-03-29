def move_zero(list,n):
    dummy = []
    count_zeros = 0
    for num in list :
        if num != 0 :
            dummy.append(num)
        else:
            count_zeros+=1
    dummy.extend([0]*count_zeros)
    return dummy



list = []
n = int(input("Enter size "))
for _ in range(n):
    a = int(input())
    list.append(a)
store = move_zero(list,n)
print(store)