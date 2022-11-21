# 1-masala
# a = float(input("Kvadratning tomonini kiriting"))
# p = 4*a     #  Kvadratning perimetrini aniqlash
# print(f"Kvadratning perimetri {p} ga teng")

# 2-masala
# a = int(input("Sonni kiriting:"))
# s = a*a    #   Kvadratning yuzasini aniqlash
# print(f"Kvadratning yuzasi {s} ga teng")

# 3-masala

# """To'g'ri to'rtburchakni tomonlari a va b berilgan,uning yuzasi va perimetri aniqlansin"""
# a = float(input("a tomonini kiriting:"))
# b = float(input("b tomonini kiriitng:"))
# s = a*b
# p = 2*(a+b)
# print(f"To'g'ri to'rtburchakning yuzi {s},perimetri esa {p} ga teng")

# # 4-masala
# """Aylananing diametri berilgan(d),uning uzunligi aniqlansin """
# pi = 3.14
# d = float(input("Aylananing diametrini kiriting:"))
# l = d*pi
# print(f"Aylananing uzunligi {l} ga teng")

# # 5-masala
# """Kubning yon tomoni a berilgan,uning hajmi va to'la sirti aniqlansin"""
# a = float(input("Kubning yon tomonini kiriting:"))
# v = a*a*a
# s = 6*a*a
# print(f"Kubning hajmi {v},sirti esa {s} ga teng")

# # 6-masala
# """Paralelepepidning tomonlari (a,b,c) berilgan,uning hajmi va to'la sirti aniqlansin"""
# a = float(input("Paralelepepidni birinchi tomonini kriting:"))
# b = float(input("Paralelepepidni ikkinchi tomonini kiriting:"))
# c = float(input("Paralelepepidni uchinchi tomonini kiriting:"))
# v = a*b*c
# s = 2*(a*b+b*c+a*c)
# print(f"Paralelepepidni hajmi {v},sirti esa {s} ga teng")

# # 7-masala
# """Doiraning radiusi berilgan(r),uning uzunligi(l) va yuzasi(s) aniqlansin"""
# r = float(input("Doiraning radiusi kiriting"))
# pi = 3.14
# l = 2*pi*r
# s = pi*r*r
# print(f"uzunligi:{l},yuzasi:{s}")

# # 8-masala
# """Ikkita sonning o'rta arifmetiki aniqlansin"""
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting"))
# c = (a+b)/2
# print(f"Ikki sonning o'rta arifmetiki {c}")
# print((9*9)**0.5)

# # 9-masala
# """Ikkita manfiy bo'lmagan son kiritiligan,ularning o'rta geometrigi aniqlansin"""
# a = float(input("Birinchi musbat sonni kiriting:"))
# b = float(input("Ikkinchi musbat sonni kiriiting:"))
# c = (a*b)**0.5
# print(c)

# # 10-masala
# a = float(input("Nolga teng bo'lmagan birinchi sonni kiriting:"))
# b = float(input("Nolga teng bo'lmagan ikkinchi sonni kiriting:"))
# c = a+b
# d = a*b
# a1 = a*a
# b1 = b*b
# print(f"Ikki sonni yig'indisi {c},ko'paytmasi {d},a1 sonni kvadrati {a1},b1 esa {b1}")

# # 11-masala
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# x = a+b
# x1 = a*b
# c = a if a>0 else -a
# d = b if b>0 else -b
# print(f"Sonlarning yig'indisi {x},ko'paytmasi {x1},modullari esa {c} va {d}")

# # 12-masala
# a = int(input("To'g'ri uchburchakning birinchi katetini kiriting:"))
# b = int(input("To'g'ri uchburchakning ikkinchi katetini kiriting:"))
# c = ((a*a)+(b*b))**0.5
# p = a+b+c
# print(f"To'g'ri uchburchakning gipotenuzasi {c},perimetri esa {p}")

# 13-masala
# r1 = float(input("Birinchi katta aylana radiusini kiriting:"))
# r2 = float(input("Ikkinchi kichik aylana radiusini kiriting:"))
# pi = 3.14
# s1 = pi*r1**2
# s2 = pi*r2**2
# s3 = s1-s2
# print(f"Birinchi katta aylananing yuzi {s1},ikkinchi kichkina aylananing yuzi {s2},katta aylananing yuzasi {s1},"
#       f"va kichik aylananing yuzasini {s2}  ayirmasi esa {s3}")

# # 14-masala
# l = float(input("Aylananing uzunligini kiriting:"))
# pi = 3.14
# d = l/3.14
# r=d/2
# l = 2*pi*r
# s = pi*(r**2)
# print(f"Aylananing radiusi {r},yuzasi esa {s}")
#
# # 15-masala
# s = float(input("Aylananing yuzasini kiriting:"))# S=p*r2
# pi = 3.14
# r = s/pi**0.5
# d = r*2
# print(f"Aylananing radiusi {r},diametri esa {d}")

# 16-masala
# a = int(input("Birinchi nuqtani kiriting:"))
# b = int(input("Ikkinchi nuqtani kiriting:"))
#
# c = a - b
# if c < 0:
#     c = c * (-1)
# print(c)

# # 17-masala
# print("Sonlar o'qida a,b,c nuqtalarni kiriting\n>>>")
# a = int(input("Birinchi a nuqtani kiriting:"))
# b = int(input("Ikkinchi b nuqtani kiriting:"))
# c = int(input("Uchinchi c nuqtani kiriting:"))
# ac = c-a
# bc = c-b
# abc = ac+bc
# print(f"ac kesmaning uzunligi {ac},bc ni uzunligi {bc} va ularning yig'indisi {abc}")

# 18-masala
# print("Sonlar o'qidagi a,b,c nuqtalarni kiriting,c nuqta a va b nuqtalar orasida\n>>>")
# a = int(input("a nuqtani kiriting:"))
# b = int(input("b nuqtani kiriting:"))
# c = int(input("c nuqtani kiriting,c nuqta a nuqtadan katta va b nuqtadan kichik bo'lishi kerak:"))
# ac = c-a
# bc = b-c
# abc = ac*bc
# print(f"ac kesma uzunligi {ac},bc niki {bc},ularning ko'paytmasi esa {abc}")

# 19-masala
# import random
#
# print("To'g'ri to'rtburchakning qarama qarshi uchlari koordinatalarini kiriting:")
# x = int(input("x o'qidagi birinchi koordinatani kiriting:"))
# x1 = int(input("x o'qidagi ikkinchi koordinatani kiriting:"))
# y = int(input("y o'qidagi birinchi koordinatani kiriting:"))
# y1 = int(input("y o'qidagi ikkinchi koordinatani kiriting:"))

# c1 = abs(x-x1)
# c2 = abs(y-y1)
# p = 2*(c1+c2)
# s = c1*c2
# print(f"To'g'ri to'rtburchakning tomonlari {c1} va {c2},perimetri {p},yuzasii esa {s}")
#
# x1,x2 = random.sample(range(-10, 10), 2)
# y1,y2 = random.sample(range(-10, 10), 2)

# print("(x1, y1): ({0},{1})".format(x1, y1))
# print("(x2, y2): ({0},{1})".format(x2, y2))
# side1 = abs(x1 - x2)
# side2 = abs(y1 - y2)
# P = 2 * (side1 + side2)
# S = side1 * side2
# print("Сторона 1: ", side1)
# print("Сторона 2: ", side2)
# print("Периметр: ", P)
# print("Площадь: ", S)

# 20-masala
# """Tekislikdagi  berilgan  ikki  nuqta (x1,y1) va (x2,y2) orasidagi  masofa  topilsin."""
# x1 = int(input("x1 ni nuqtasini kiriting:"))
# y1 = int(input("y1 ni nuqtasini kiriting:"))
# x2 = int(input("X2 ni nuqtasini kiriting:"))
# y2 = int(input("y2 ni nuqtasini kiriting:"))
# c1 = abs(x1-x2)
# c2 = abs(y1-y2)
# m = ((c1**2)+(c2**2))**0.5
# print(f"Masofa {m}")

# 21-masala
# """Uchburchakning uchta tomoni uchlari koordinatalari berilgan,
# ikki nuqta orasidagi masofani,uchburchakning perimetri va yuzasini toping"""
# print("x,x1,x2,y,y1,y2 koordinatalarini kiriting:")
# x = int(input("x ni kiriting:"))
# x1 = int(input("x1 ni kiriting:"))
# x2 = int(input("x2 ni kiriting:"))
# y = int(input("y ni kiriting:"))
# y1 = int(input("y1 ni kiriting:"))
# y2 = int(input("y2 ni kiriting:"))
# c = abs(x-x1)
# d = abs(y-y1)
# c1 = abs(x1-x2)
# d1 = abs(y1-y2)
# c2 = abs(x-x2)
# d2 = abs(y-y2)
# a = ((c**2)+(d**2))**0.5
# b = ((c1**2)+(d1**2))**0.5
# c = ((c2**2)+(d2**2))**0.5
# p = a+b+c
# s = (p*(p-a)*(p-b)*(p-c))**0.5
# print(f"Uchburchakning ikki nuqtalar orasidagi masofa {a},{b},{c},perimetri {p},yuzasi esa {s}")

# 22-masala
# """Kiritilgan a va b sonlarini o'rni bilan almashtirib a va b ni yangi qiymatini ekranga chiqaring"""
# a = int(input("Birinchi sonni kiriting:"))
# b = int(input("Ikkinchi sonni kiriting:"))
# c=a
# a=b      ### BIRINCHI USUL
# b=c
# a,b=b,a     ###  IKKINCHI USUL
# print(f"{a},{b}")
# a=int(input ("Введите 1е : "))
# b=int(input ("Введите 2е : "))
# c=a
# a=b
# b=c
# print(a,b)

# # 23-masala
# """Kiritilgan a,b va c sonini a ni b ga b ni c ga va c ni a ga almashtirib.a,b,c ni yangi qiymatini ekranga chiqaring"""
# a = int(input("a ni qiymatini kiriting:"))
# b = int(input("b ni qiymatini kiriting:"))
# c = int(input("c ni qiymatini kiriting:"))
# # a,b,c=c,a,b    ###  IKKINCHI YECHIM
# v = b
# b = a
# a = c
# c = v
# print(a, b, c)

# # 24-masala
# """A,B va C sonlari  berilgan.A ni qiymati C ga, C ni qiymati B ga va B ni qiymati A ga
# almashtirilsin. A, B va C ning yangi qiymatilari ekranga chiqarilsin."""
# a = int(input("a ni qiymatini kiriting:"))
# b = int(input("b ni qiymatini kiriting:"))
# c = int(input("c ni qiymatini kiriting:"))
# v=a
#
# print(a,b,c)

# 25-masala
# x = int(input("x ni qiymatini kiriting:"))
# y = 3*(x**5)-6*(x**2)-7
# print(y)
#
# 26-masala
# x = int(input("x ni qiymatini kiriting:"))
# y = 4*((x-3)**5)-7*((x-3)**3)+2
# print(y)
#
# 27-masala
# print("Sonni 2,4,8 darajalarga oshiruvchi funksiya")
# a =int(input("Biron son kiriting:"))
# a=a**2,a**4,a**8
# print(a)
#
# 28-masala
# print("Sonni 2,3,5,10,15 darajalarga oshirish")
# a = int(input("Biron son kiriting:"))
# a = a**2,a**3,a**5,a**10,a**15
# print(a)
#
# 29-masala
# import math
# x = float(input("Burchak gradiusini kiriting:"))
# radian = x*3.14/180
# print(f"{x} ning radiani {radian}")

# 30-masala
# x = float(input("Burchak radianini kiriting:"))
# gradus = x*180/3.14
# print(f"{x} radiani {gradus} gradusga teng")

# 31-masala
# tf = float(input("Farangeyt gradusini kiriting:"))
# tc = (tf*9/5)+32
# print(f"{tf} farangeyt gradusi {tc} selsiy gradusiga teng")
#
# 32-masala
# tc = float(input("Celsiy gradusini kiriting:"))
# tf = (tc-32)/1.8
# print(f"{tc} celsiy gradusi teng {tf} frangeyt gradusiga")
#
# 33-masala
# x = float(input("Nechi kilo konfet olasiz?:"))
# y = float(input("Narhi qancha bo'lsin?:"))
# narh = x*y
# if x<0 or y<0:
#     print("Musbat son kiriting")
# else:
#     print(f"{x} kilo konfet {y} so'm narhda {narh} so'm bo'ladi")
#
# 34-masala
# sh = float(input("Nechi kilo shokolat olasiz?:"))
# n = int(input("Necha so'mligidan?:"))
# k = float(input("Nechi kilo konfet olasiz?:"))
# s = int(input("Nechi so'mligidan?:"))
# shnarh = sh*n
# knarh = k*s
# c = shnarh-knarh
# if sh<0 or n<0 or k<0 or s<0:
#     print("Musbat son kiriting!")
# elif knarh>shnarh:
#     d = abs(shnarh-knarh)
#     print(f"{k} konfet {d} so'm qimmat {sh} shokolatdan")
# elif knarh==shnarh:
#     print("Narhlar teng")
# else:
#     print(f"{sh} shokolat {c} so'm qimmat {k} konfetdan")
#
# 35-masala
# q = float(input("Qayiqni jim turgan daryo suvidagi tezligini kiriting:"))
# d = float(input("Daryo oqimi tezligini kiriting:"))
# t1 = float(input("Qayiqning daryo bo'yicha harakatlanish vaqtini kiriting:"))
# t2 = float(input("Qayiqning daryo oqimiga qarshi harakatlanish vaqtini kiriting:"))
# s = q*t1+(q-d)*t2
# print(f"Qayiqni yurgan yo'li {s} km.")
#
# 36-masala
# v1 = int(input("Birinchi avto tezligini kiriting:"))
# v2 = int(input("Ikkinchi avto tezligini kiriting:"))
# s = int(input("Ular orasidagi masofani kiriting:"))
# t = int(input("Qancha soat yurishini kiriting:"))
# s1 = v1*t
# s2 = v2*t
# finalMasofa = s+s1+s2
#
# 37-masala
# b = int(input("Birinchi avto tezligini kiriting:"))
# i = int(input("Ikkinchi avto tezligini kiriting:"))
# m = int(input("Ular orasidagi masofani kiriting:"))
# t = int(input("Qancha soat yurishini kiriting:"))
# d = (b*t)+(i*t)
# if m<d:
#     c=abs(m-d)
#     print(f"Ikkala mashina {t} soatdan keyin {c} km bir biridan o'tib ketib uzoqlashadi")
# else:
#     c=m-d
#     print(f"Ikkala moshina orasi {t} soatda {c} km qoladi")
#
# 38-masala
# """Tenglamani toping a*x+b=0"""
# a = int(input("a ni koeffitsientini kiriting:"))
# b = int(input("b ni koeffitsientini kiriting:"))
# x=-b/a
# print(x)
#
# import random
#
# r = list(range(-10, 0)) + list(range(1, 11))
# A = random.choice(r)
# B = random.randrange(-20, 21)
# x = -B / A
# y = A * x + B
# print("Ax + B = 0")
# print("A = ", A)
# print("B = ", B)
# print("x = ", -B / A)
# print("({0}) * ({1}) + ({2}) = {3}".format(A, x, B, y))
#
# 39-masala
# a = int(input("a ni koeffisentini kiriting:"))
# print("DIQQAT! b ni koeffitsenti a va c koeffitsentidan ikki baravar ko'p bo'lishi shart")
# b = int(input("b ni koeffitsentini kiriting:"))
# c = int(input("c ni koeffisentini kiriting:"))
# d = b**2-4*a*c
# x1 = (-b+(d**0.5))/2*a
# x2 = (-b-(d**0.5))/2*a
# print("d=",d)
# print("x1=",x1)
# print("x2=",x2)
#
# 40-masala
# a1 = int(input("a1 ni koeffitsentini kiriting:"))
# b1 = int(input("b1 ni koeffitsentini kiriting:"))
# c1 = int(input("c1 ni koeffitsentini kiriting:"))
# a2 = int(input("a2 ni koeffitsentini kiriting:"))
# b2 = int(input("b2 ni koeffitsentini kiriting:"))
# c2 = int(input("c2 ni koeffitsentini kiriting:"))
# print("a1=",a1)
# print("b1=",b1)
# print("c1=",c1)
# print("a2=",a2)
# print("b2=",b2)
# print("c2=",c2)
# d = (a1*b2-a2*b1)
# x = (c1*b2-c2*b1)/d
# y = (a1**c2-a2*c1)/d
# print("d=",d)
# print("x=",x)
# print("y=",y)
