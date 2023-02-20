# 选择法排序
num = [4, 45, 12, 456, 1, 53, 21]
for i in range(len(num)-1):
    for j in range(len(num)-1-i):
        if num[i] > num[j+i+1]:
            temp = num[i]
            num[i] = num[j+i+1]
            num[j+1+i] = temp

print(num)