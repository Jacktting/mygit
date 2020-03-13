"""
找出所有水仙花数
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：1^3 + 5^3+ 3^3=153。
"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

"""
正整数的反转
"""
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

"""
《百钱百鸡》问题
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，
用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

"""
生成斐波那契数列的前20个数。
数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
"""
x=1
y=1
for i in range(10):
    print(x)
    print(y)
    x=x+y
    y=x+y

"""
找出10000以内的完美数
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
"""
import math

for num in range(1,1000):
    result = 0
    for i in range(1,int(math.sqrt(num))+1):
        if(num%i==0):
            result += i
            if num // i != i and i>1:
                result += num // i
    if result == num:
        print(num)
"""
输出100以内所有的素数
只能被1和自身整除的正整数（不包括1)
"""
for num in range(2,100):
    flag = True
    for i in range(2,int(math.sqrt(num))+1):
        while(num % i == 0):
            flag = False
            break
    if flag:
        print("num:",num)



