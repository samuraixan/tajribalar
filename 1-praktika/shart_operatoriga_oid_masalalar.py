# # 1-masala
# x = float(input("Butun son kiriting:"))
# if 0>x:
#     print(x)
# else:
#     print(x+1)

# # 2-masala
# x = float(input("Butun son kiriting:"))
# if 0>x:
#     x = x-2
# else:
#     x = x+1
# print(x)

# # 3-masala
# x = float(input("Sonni kiriting:"))
# if 0<x:
#     x = x+1
# elif x==0:
#     x = 10
# else:
#     x = x-2
# print(x)

# 4-5-masalalar
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c = int(input("Uchinchi sonni kiriting:"))
# sana = 0
# mana = 0
# if a>0:
#     sana = sana + 1
# else: mana = mana+1
# if b>0:
#     sana = sana + 1
# else:mana = mana +1
# if c>0:
#     sana = sana + 1
# else:
#     mana = mana + 1
# print(f"Musbat sonlar {sana} ta,manfiy sonlar {mana} ta")

# 6-masala
# a= int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# if a>b:
#     print(f"Sonlarni kattasi {a}")
# else:
#     print(f"Sonlarni kettasi {b}")

# 7-masala
# a, b = map(int, input().split())
# print(1 if a < b else 2)
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# if a<b:
#     print(f"Kichik {a} sonni tartib raqami 1")
# else:
#     print(f"Kichik raqam {b} sonni tartib raqami 1")

# 8-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# if a>=b:
#     print(f"{a},{b}")
# else:
#     print(f"{b},{a}")

# 9-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# if a>b:
#     a=a-b
#     print(a,b)
# else:
#     print(a,b)

# 10-masala
# import random
# A = random.randrange(-3,3)
# B = random.randrange(-3,3)
# print("Число A:", A)
# print("Число B:", B)
# if A != B:
#     A = B = A+B
# else:
#     A = B = 0
# print("Число A:", A)
# print("Число B:", B)

# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# if a!=b:
#     a=a+b
#     b=a
#     print(a,b)
# else:
#     a=0
#     b=a
#     print(a,b)

# 11-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# if a!=b and a>b:
#     b=a
#     print(a,b)
# elif b>a:
#     a=b
#     print(a,b)
# elif a==b:
#     a=0
#     b=a
#     print(a,b)

# 12-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c = int(input("Uchinchi sonni kiriting:"))     ###     UCHINCHI YECHIM
# if a<b and b<c:
#     print(f"Eng kichiki {a}")
# elif a>b<c:
#     print(f"eng kichiki {b}")
# else:
#     print(f"eng kichiki {c}")
# print("Число a:", a)
# print("Число b:", b)
# print("Число c:", c)
# if a < b:
#     mn = a                   ###   BIRINCHI YECHIM
# else:
#     mn = b
# if mn > c:
#     mn = c
# print()
# print("Минимум:", mn)
# print(min(a,b,c))       ##    IKKINCHI YECHIM

# 13-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c = int(input("Uchinchi sonni kiriting:"))
# if a<=b<=c or c<=b<=a:
#     print(f"O'rta son {b}")
# elif b<=a<=c or c<=a<=b:
#     print(f"O'rta son {a}")
# elif a<=c<=b or b<=c<=a:
#     print(f"O'rta son {c}")

# 14-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c = int(input("Uchinchi sonni kiriting:"))
# if a<=b<=c:
#     print(a,b,c)
# elif b<=a<=c:
#     print(b,a,c)
# elif c<=a<=b:
#     print(c,a,b)
# elif a<=c<=b:
#     print(a,c,b)
# elif c<=b<=a:
#     print(c,b,a)
# else:
#     print(b,c,a)

# 15-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c = int(input("Uchinchi sonni kiriting:"))
# import random as r
# a = r.randrange(1,20)
# b = r.randrange(1,20)
# c = r.randrange(1,20)
# print(a)
# print(b)
# print(c)
#
# if a<=b<=c or a<=c<=b:
#     y = b+c
#     print(f"Sonlarning ikkita kattasini yig'indisi {y}")
# elif b<=a<=c or b<=c<=a:
#     y = a+c
#     print(f"Sonlarning ikkita kattasini yig'indisi {y}")
# elif c<=b<=a or c<=a<=b:
#     y = b+a
#     print(f"Sonlarning ikkita kattasini yig'indisi {y}")
# elif a<=c<=b:
#     y = c+b
#     print(f"Sonlarning ikkita kattasini yig'indisi {y}")
# elif c<=a<=b:
#     y = a+b
#     print(f"Sonlarning ikkita kattasini yig'indisi {y}")
# elif b<=c<=a:
#     y = c+a
#     print(f"Sonlarning ikkita kattasini yig'indisi {y}")
# import random
# A = random.randrange(-30,30)
# B = random.randrange(-30,30)
# C = random.randrange(-30,30)
# print("Число A:", A)
# print("Число B:", B)
# print("Число C:", C)
# if (C <= A and A <= B) or (C <= B and B <= A):
#     m = A + B
# elif (B <= A and A <= C) or (B <= C and C <= A):
#     m = A + C
# elif (A <= C and C <= B) or (A <= B and B <= C):
#     m = B + C
# print()
# print("Сумма:", m)

# 16-masala
# import random as r
# a = r.randrange(-10,10)
# b = r.randrange(-10,10)
# c = r.randrange(-10,10)

# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c = int(input("Uchinchi sonni kiriting:"))
# if a<b<c:
#     print(a)
#     print(b)
#     print(c)
#     a=a*2
#     b=b*2
#     c=c*2
#     print(a,b,c)
# else:
#     print(a)
#     print(b)
#     print(c)
#     a=-a
#     b=-b
#     c=-c
#     print(a,b,c)

# 17-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c  = int(input("Uchinchi sonni kiriting:"))
# if a<b<c or c<b<a:
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
#     a=a*2
#     b=b*2
#     c=c*2
#     print(a,b,c)
# else:
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
#     a=-a
#     b=-b
#     c=-c
#     print(a,b,c)

# 18-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c = int(input("Uchinchi sonni kiriting:"))
# if a==b or b==a:
#     print("c")
# elif b==c or c==b:
#     print("a")
# elif a==c or c==a:
#     print("b")
# else:
#     print("Ikkita bir xil(teng) son kiriting!")

import random


# def RandNum():
#     l = []
#     x1, x2 = random.sample(range(-10, 10), 2)
#     N = random.randrange(1, 4)
#     if N == 1:
#         l.append(x1)
#         l.append(x1)
#         l.append(x2)
#     elif N == 2:
#         l.append(x1)
#         l.append(x2)
#         l.append(x2)
#     else:
#         l.append(x2)
#         l.append(x1)
#         l.append(x2)
#     return l
#
#
# A, B, C = RandNum()
# print("Число A:", A)
# print("Число B:", B)
# print("Число C:", C)
# if A == B:
#     print("C")
# elif A == C:
#     print("B")
# else:
#     print("A")

# 19-masala
# import random
#
#
# def RandNum():
#     l = []
#     x1, x2 = random.sample(range(-10, 10), 2)
#     N = random.randrange(1, 5)
#     if N == 1:
#         l.append(x1)
#         l.append(x1)
#         l.append(x2)
#         l.append(x1)
#     elif N == 2:
#         l.append(x1)
#         l.append(x1)
#         l.append(x2)
#         l.append(x1)
#     elif N == 3:
#         l.append(x1)
#         l.append(x1)
#         l.append(x2)
#         l.append(x1)
#     else:
#         l.append(x1)
#         l.append(x1)
#         l.append(x2)
#         l.append(x1)
#     return l
#
#
# A, B, C, D = RandNum()
# print("Число A:", A)
# print("Число B:", B)
# print("Число C:", C)
# print("Число D:", D)
# if A == B:
#     if A == D:
#         print("C")
#     else:
#         print("D")
# else:
#     if A == C:
#         print("B")
#     else:
#         print("A")

# 20-masala
# import random
# a,b,c = random.sample(range(-10,10), 3)
# print("a=",a)
# print("b=",b)
# print("c=",c)
# ab = abs(a-b)
# ac = abs(a-c)
# print(f"ab orasidagi masofa {ab},ac niki esa {ac}")
# if ab>ac:
#     print(f"a ga yaqini c")
# elif ab<ac:
#     print(f"a ga yaqini b")
# else:
#     print("a ham b ham teng uzoqlikda a dan")

# 21-masala
