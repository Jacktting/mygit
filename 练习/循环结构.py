"""
用for循环实现1~100求和
"""
sum = 0
for x in range(101):
    sum += x
print(sum)

"""
用for循环实现1~100之间的偶数求和
"""
sum = 0
for x in range(2, 101, 2):
#for x in range(0,101,2):
    sum += x
print(sum)
"""
分支结构    1~100之间的偶数求和
"""
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
"""
输出乘法口诀表(九九表)
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
"""
输入一个正整数判断它是不是素数
素数指的是只能被1和自身整除的大于1的整数。
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

"""
输入两个正整数计算它们的最大公约数和最小公倍数
"""

x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较小的数开始做递减的循环
for i in range(x, 0, -1):  #x=5,y=6
    if x % i == 0 and y % i == 0:
        print('%d和%d的最大公约数是%d' % (x, y, i))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // i))
        break

"""
打印三角形图案
*
**
***
****
***** 

    *
   **
  ***
 ****
*****

    *   1
   ***  3
  ***** 5
 *******7
*********9
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()






