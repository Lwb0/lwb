#冒泡排序
num = [12,5,645,4,6,7,80,28,471]
#外层循环控制找多少次最大数
for i in range(len(num)):
    #内层循环控制找每一个最大数要比较的次数
    for j in range(len(num)-1-i):
        if num[j] > num[j+1]:
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp

print(num)