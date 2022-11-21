## 1-masala
# sm = int(input("Uzunlikni santimetrda kiriting:"))
# m = sm//100
# m = int(sm/100)
# print(f"{sm} sm teng {m} metrga")
# L = int(input("Введите расстояние в сантиметрах (L): "))
# m = int(L / 100)
# print("Количество полных метров: ", m)

## 2-masala
# kg = int(input("Og'irlikni kilogrammda kiriting:"))
# t = kg//1000
# t = int(kg/1000)
# print(f"{kg} kg {t} tonna")

## 3-masala
# b = int(input("Fayllarni baytlarda kiriting:"))
# k = b//1024
# print(f"{b} bayt {k} kilobayt")     ###   BIRINCHI YECHIM

# import random
# b = random.randrange(1,100000)
# k = b//1024                         ### IKKINCHI YECHIM
# print(f"{b} bayt teng {k} kilbaytga")
# s = random.randrange(1,1000000)
# print("Размер файла в байтах: ", s)                  ###   UCHINCHI YECHIM INTERNETNIKI
# print("Количество полных килобайтов: ", int(s / 1024))

## 4-masala
# import random
# a = random.randrange(50,100)
# b = random.randrange(1,50)
# a = random.randrange(1,100)
# b = random.randrange(1,a)
# print("a:",a)
# print("b:",b)
# x = a//b
# print(f"a kesmada b kesmani {x} marta joylash mumkin")

## 5-masala
# import random
# a = random.randrange(50,100)
# b = random.randrange(1,50)
# a = random.randrange(1,100)
# b = random.randrange(1,a)
# print("a:",a)
# print("b:",b)
# x = a//b
# x1 = a%b
# print(f"a kesmada b kesmani {x} marta joylash mumkin")
# print(f"a kesmada b kesmani joylashmagan qismi {x1}")

## 6-masala
# import random
# N = random.randrange(10,100)
# print("N = ", N)
# print("Десятки: ", int(N/10))
# print("Единицы: ", N%10)

# x = random.randrange(10,100)
# a = x//10   #   YOKI INT(X/10)
# b = x%10
# print("x:",x)
# print(f"{x} ning o'nliklar xonasida raqam {a} ta,birliklar xonasidagi esa {b}")

## 7-masala
# import random
# x  = random.randrange(10,100)
# a = x//10 # a = int(x/10)
# b = x%10
# c = a+b
# s = a*b
# print("x:",x)
# print("a:",a)
# print("b:",b)
# print(f"{x} ning o'nliklar xonasidagi raqam {a} ta,birliklar xonasidagi raqam esa {b}")
# print(f"{x} ning raqamlar yig'indisi {c},ko'paytmasi {s}")

# N = random.randrange(10,100)
# print("N = ", N)
# d1 = int(N/10)
# d0 = N%10        ###    INTERNETDAN OLINGAN
# print("Tens: ", d1)
# print("Units: ", d0)
# print("Sum: ", d1+d0)
# print("Product: ", d1*d0)

## 8-masala
# import random
# x = random.randrange(10,100)
# print("x=",x)
# a = x//10
# b = x%10
# print("a=",a)
# print("b=",b)
# newx = b*10+a
# print(newx)
# print(f"{x} ikki xonali sonni raqamlari o'rni almashishidan hosil bo'lgan son {newx}")

## import random
## N = random.randrange(10,100)
## print("Число: ", N)
## d1 = int(N/10)
## d0 = N%10
## N_new = d0*10 + d1
## print("Десятки: ", d1)
## print("Единицы: ", d0)
## print("Новое число: ", N_new)

## 9-masala
# import random
# x = random.randrange(100,1000)
# print("x=",x)
# a = x//100
# print("a=",a)
# print(f"Uch xonali son {x} ni yuzlar xonasidagi raqami {a}")

## 10-masala
# import random
# x = random.randrange(100,1000)
# a = x//100
# print("x=",x)
# print("a=",a)
# b = x-a*100
# print("b=",b)
# s = b//10
# q = b%10
# print("q=",q)
# print("s=",s)
# print(f"Uch xonalik {x} ning birliklar xonasi raqami {q},o'nliklar xonasi raqami esa {s}")

## 11-masala
# import random
# x = random.randrange(100,1000)
# print("x=",x)
# a = x//100
# print("a=",a)
# b = x-a*100
# print("b=",b)
# c = b//10
# s = b%10
# print("c=",c)
# print("s=",s)
# d = a+c+s
# print("d=",d)
# print(f"{x} uch xonali sonni raqamlar yig'indisi {d}")

## 12-masala
# x = random.randrange(100,1000)
# print("x=",x)
# a = x//100
# print("a=",a)
# b = x-a*100
# print("b=",b)
# c = b//10
# s = b%10
# print("c=",c)
# print("s=",s)
# i = s*100
# t = c*10
# print("i=",i)
# print("t=",t)
# y = i+t+a
# print("y=",y)

# # 13-masala
# import random
# x = random.randrange(100,1000)
# print(x)
# yuzlik = x//100
# onlik = (x-yuzlik*100)//10
# birlik = (x-yuzlik*100-onlik*10)
# print(yuzlik)
# print(onlik)
# print(birlik)
# y = onlik*100
# o = birlik*10
# b = yuzlik
# j = y+o+b
# print(j)

# ## 14-masala
# import random
# # x = random.randrange(100,1000)
# x = int(input("Son kiriting:"))
# print(x)
# yuzlik = x//100
# onlik = (x - yuzlik*100)//10
# birlik = (x-yuzlik*100-onlik*10)
# print("yuzlik=",yuzlik)
# print("O'nlik=",onlik)
# print("Birlik=",birlik)
# y = birlik*100
# o = yuzlik*10
# b = onlik
# son = y+o+b
# print(son)

## 15-masala
# import random
# x = random.randrange(100,1000)
# x = int(input("Son kiriting:"))
# print("x=",x)
# yuzlik = x//100
# onlik = (x-yuzlik*100)//10
# birlik = (x-yuzlik*100-onlik*10)
# print("Yuzlik=",yuzlik)
# print("O'nlik=",onlik)
# print("Birlik=",birlik)
# y = onlik*100
# o = yuzlik*10
# b = birlik
# jami = y+o+b
# print(jami)

## 16-masala
import random
# x = random.randrange(100,1000)
# print("x=",x)
# yuzlik = x//100
# onlik = (x-yuzlik*100)//10
# birlik = x-yuzlik*100-onlik*10
# print("yuzlik=",yuzlik)
# print("O'nlik=",onlik)
# print("Birlik=",birlik)
# y = yuzlik*100
# o = birlik*10
# b = onlik
# jami = y+o+b
# print(jami)

## 17-masala
# import random
# x = random.randrange(1000,1000000)
# print("x=",x)
# a = x//100
# print("a=",a)
# c = a%10
# print(f"{x} ning yuzliklar xonasidagi soni {c}")

##  18-masala
# import random
# x = random.randrange(1000,1000000)
# print("x=",x)
# a = x//1000
# print("a=",a)
# c = a%10
# print("c=",c)
# print(f"{x} sonining migliklar xonasidagi soni {c}")

## 19-masala

# import random
# N = random.randrange(1,10000)
# print(f"{N} sekund")
# m = N//60
# print(f"{m} minut")
# print(f"{N} sekund {m} minut")

## 20-masala
# import random
# N = random.randrange(3600,100000)
# print(f"{N} sekund")
# soat = N//3600                  ##       O'ZIM ISHLAGAN VARIANT
# soat = N//60//60                ##    INTERNETNI VARIANTI
# print(f"{soat} soat")
# print(f"{N} sekund {soat} soatga teng")

# ## 21-masala
# import random
# N = random.randrange(0,1000000)
# print(f"{N} sekund")
# m = N//60
# print(f"{m} minut")
# s = N-m*60
# print(f"{s} sekund")
# print(f"Kun davomida {N} sekund yani {m} minut {s} sekund o'tdi")

# ## 22-masala
# import random
# N = random.randrange(0,100000)
# print(f"{N} sekund")
# soat = N//3600
# print(f"{soat} soat")
# s = N-soat*3600
# print(f"{s} sekund")
# print(f"{N} sekund yani {soat} soat,{s} sekund o'tdi")

# ## 23-masala
# import random
# N = random.randrange(0,1000000)
# print(f"{N} sekund")
# soat = N//3600
# print(f"{soat} soat")
# m = (N-soat*3600)//60
# print(f"{m} minut")
# sek = (N-soat*3600-m*60)
# print(f"{sek} sekund")
# print(f"{N} sekund bu {soat} soat {m} minut {sek} sekundga teng")

# 24-masala
# """Agar 0-yakshanbadan boshlansa,1-yanvar dushanba bo'lsa"""
# import random
# N = random.randrange(1,365)
# print("N=",N)
# days = ['вс', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб']     ###   INTERNETDAN KO'CHIRMA
# print(days[N % 7])

# import random
# k = random.randrange(1,366)
# i = k%7
# print("k =",k)
# print("i=",i)
# haftalar = {
#     0 : 'Yakshanba',
#     1 : 'Dushanba',
#     2 : 'Seshanba',
#     3 : 'Chorshanba',
#     4 : 'Payshanba',
#     5 : 'Juma',
#     6 : 'Shanba'
# }
# print(f"1-yanvar yilning {1}-kuni")
# print("Hafta kunining raqami=",b)
# print(f"Haftaning kuni {haftalar[b]}")
# # print(haftalar)
# print("k=",k)
# print(f"{k}-kun hafta kunini {haftalar[i]} kuniga to'g'ri keladi")

# import random
# week_days = {
#     0: 'воскресенье',
#     1: 'понедельник',
#     2: 'вторник',
#     3: 'среда',
#     4: 'четверг',
#     5: 'пятница',
#     6: 'суббота'
# }
# K = random.randrange(1,366)
# # K = 31
# print("K=",K)
# i = 1%7
# print("1-е января: ", 1)
# print("Номер дня недели: ", i)
# print("День недели:",week_days[i])
# i = K%7
# print()
# print("Номер дня года: ", K)
# print("Номер дня недели: ", i)
# print("День недели:",week_days[i])

## 25-masala
"""Agar hafta kuni 0-yakshanbadan boshlansa,1-yanvar payshanba bo'lsa"""
import random
k = random.randrange(1,366)
b = 1+3%7
i = (k+3)%7
haftalar = {
    0 : 'Yakshanba',
    1 : 'Dushanba',
    2 : 'Seshanba',
    3 : 'Chorshanba',
    4 : 'Payshanba',
    5 : 'Juma',
    6 : 'SHanba'
}
#
# print("Yilning birinchi kuni:",1)
# print("Yilning birinchi kunining raqami:",b)
# print(f"Yilning birinchi kunini hafta nomi:{haftalar[b]}")
# print("b=",b)
# print("k=",k)
# print("i=",i)
# print(f"{k} kun hafta kunini {haftalar[i]} kuniga to'g'ri keladi")

# import random
# week_days = {
#     0: 'воскресенье',
#     1: 'понедельник',
#     2: 'вторник',
#     3: 'среда',
#     4: 'четверг',
#     5: 'пятница',
#     6: 'суббота'
# }
# K = random.randrange(1,366)
# K = 31
# i = (1+3)%7
# print("1-е января: ", 1)
# print("Номер дня недели: ", i)
# print("День недели:",week_days[i])     ###   INTERNETDAN OLINGAN
# i = (K+3)%7
# print()
# print("Номер дня года: ", K)
# print("Номер дня недели: ", i)
# print("День недели:",week_days[i])

# ### 26-masala
# """Agar 1-dushanbadan boshlansa,1-yanvar seshanba bo'lsa"""
# import random
# haftalar = {
#     1 : 'Dushanba',
#     2 : 'Seshanba',
#     3 : 'Chorshanba',
#     4 : 'Payshanba',
#     5 : 'Juma',
#     6 : 'Shanba',
#     7 : 'Yakshanba'
# }
# k = random.randrange(1,366)         ###   INTERNETDAN OLINIB ISHLANDI
# i = 1%7+1
# h = k%7+1
# print("Yilning birinchi kunini raqami:",1)
# print("Birinchi kun haftalar raqamida:",i)
# print(f"Hafta kuning nomi {haftalar[i]}")
# print(f"{k}-kun haftaning {haftalar[h]} kuni")


# import random
# week_days = {
#     1: 'понедельник',
#     2: 'вторник',
#     3: 'среда',                     #### INTERNETDAN OLINDI
#     4: 'четверг',
#     5: 'пятница',
#     6: 'суббота',
#     7: 'воскресенье'
# }
# K = random.randrange(1,366)
# i = 1%7 + 1
# print("1-е января: ", 1)
# print("Номер дня недели: ", i)
# print("День недели:",week_days[i])
# i = K%7 + 1
# print()
# print("Номер дня года: ", K)
# print("Номер дня недели: ", i)
# print("День недели:",week_days[i])


# ### 27-masala
# """Agar 1-dushanba bo'lsa,1-yanvar yakshanba bo'lsa"""
# import random
# k = random.randrange(1,366)
#
# haftalar = {
#     1 : 'Dushanba',
#     2 : 'Seshanba',
#     3 : 'Chorshanba',
#     4 : 'Payshanba',
#     5 : 'Juma',
#     6 : 'Shanba',
#     7 : 'Yakshanba'
# }
# i = 1%7+6
# h = k%7-1
# print("k =",k)
# print("i =",i)
# print("h =",h)
# print(f"{k} kun haftaning {haftalar[h]} kuniga to'g'ri keladi")

# ####    28-masala
# import random
# n = random.randrange(1,8)
# k = random.randrange(1,365)
# # n = 1
# # k = 8
# weeks ={
#     1 : 'Dushanba',
#     2 : 'Seshanba',
#     3 : 'Chorshanba',
#     4 : 'Payshanba',
#     5 : 'Juma',
#     6 : 'Shanba',
#     7 : 'Yakshanba'
# }
# print(f"1-yanvar {n} kun bo'lsa")
# print(f"{k} kun haftaning qaysi kuniga to'g'ri keladi")
# c = n%7
# i = ((k+n)%7-1)
# print("c =",c)
# print(f"{haftalar[i]} kun")

# ####     29-masala
# import numpy as np
# import random
# A,B = list(np.random.choice(range(1,20),2))
# C = random.randint(1,min(A,B))
# print("A =",A,"B =",B,"C =",C)
# a = (A+B)*2
# b = C*4                        #############   O'ZIM ISHLAGAN
# print("a =",a)
# print("b =",b)
# c = a//b
# d = a%b
# print(f"To'g'ri burchakka eng ko'p joylashgan kvadratlar soni {c},joylashmay qolgan qismi esa {d}")


# import numpy as np
# import random
# A,B = list(np.random.choice(range(1, 16), 2))
# C = random.randint(1,min(A,B))
# print("A = {0}, B = {1}, C = {2}".format(A,B,C))
# a = int(A/C)
# b = int(B/C)                 #############  INTERNETDAN OLINGAN
# print("a =",a)
# print("b =",b)
# print("Площадь прямоугольника:",A*B)
# print("Площадь квадрата:",C*C)
# print("Количество квадратов на прямоугольнике:",a*b)
# print("Площадь незанятой части прямоугольника:",A*B - a*b*C*C)

# ######## 30-masala
# import random
# y = random.randrange(1,3000)       #######   O'ZIM ISHLAGAN
# print("y =",y)
# x = (y//100)+1
# print(f"{y}-yil {x} asrga teng")

# print("Введите год:", end=' ')
#
# year = int(input())
#
# if (year % 100 > 0):
#
#    century = year // 100 + 1
#
# else:
#
#    century = year // 100;
#
# print("Этот год относится к", century, "-му столетию.")

# a = int(input())
# for i in range(-a, a + 1):
#     if  i < 0 and abs(i + a + 1) != a:
#         print(i + a + 1, end=' ')
#     if i > 0:
#         print(a + 1 - i, end=' ')

