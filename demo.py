#冒泡排序
a = [12,45,7,453,64,213,56]
 #外层循环控制找多少次最大数
 for i in range(len(a)):
     #内层循环控制找每一个最大数要比较的次数
     for j in range(len(a)-1-i):
         if a[j] > a[j+1]:
             temp = a[j]
             a[j] = a[j+1]
            a[j+1] = temp

print(a)