# 1-mavzuga doir misollsr
#print('Assalom alaykum')
#print(Hayrli tong!)
#print(2+4*2)
#print(19/5)
#print(2**4)

#print('''"Nexia", "Tiko", 'Damas' ko'rganlar qilar havas''')
##5 ning 4-darajasini toping
#print(5**4)
##22 ni 4 ga bo'lganda qancha qoliq qoladi?
#print(22%4)
##Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
#print("Tomonlari 125 ga teng kvadratning yuzi S=",125**2, "\nTomonlari 125 ga teng kvadratning perimetri P=",125*4  )
##Diametri 12 ga teng bo'lgan doiraning yuzini toping (p=3.14)
#diametr=12
#p=3.14
#radius=diametr/2
#print(radius**2*p)

#katet_a=6
#katet_b=7
#gipotenuza=(katet_a**2+katet_b**2)**(1/2)
#print(gipotenuza)


#4-DARS

#salom="Hello world"
#print(salom)
#xabar="Olam aro atagan tanho"
#print(xabar)
#xabar="Bir yoki ikki"
#print(xabar)
#radius=5
#pi=3.14159
#aylana_yuzi=pi*radius**2
#print("Rdiusi", radius, "ga teng aylananing yuzi=", aylana_yuzi)

#5-DARS

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#print(kocha, "ko'chasi", mahalla, "mahallasi", tuman, "tumani", viloyat, "viloyati")
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " +
#tuman + " tumani, " + viloyat + " viloyati")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
#kocha=input("Qaysi ko'chada tursiz?>>>\n")
#mahalla=input("Mahallangiz?>>>\n")
#tuman=input("Qaysi tumandansiz?>>>\n")
#viloyat=input("Viloyatingizni kiriting?>>>\n")
##print("Sizning manzilingiz", kocha, "ko'chasi", mahalla, "mahallasi", tuman, "tumani", viloyat, "viloyati")
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      #tuman + " tumani, " + viloyat + " viloyati")
#print("Sizning manzilingiz:\n",kocha, "ko'chasi\n",mahalla, "mahallasi\n",tuman, "tumani\n",viloyat, "viloyati")
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
#print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      #tuman + " tumani,\n" + viloyat + " viloyati")

#manzil=f"Sizning manzilingiz \n{kocha.title()} ko'chasi, \n{mahalla.title()} mahallasi, \n{tuman.title()} tumani, \n{viloyat.title()} viloyati."
#print(manzil)


#6-DARS

#son=float(input("Istalgan sonni kiriting:>>>\n"))
#kvadrat=son**2
#kub=son**3
#print(f"{son} ning kvadrati={kvadrat}, {son} ning kubi={kub}")

#yosh=int(input("Yoshingiz nechchida?>>>"))
#print("Sizning tug'ilgan yilingiz", 2022-yosh)
#print("Istalgan ikki sonni kiriting:")
#a=float(input("Birinchi sonni kiriting:>>>"))
#b=float(input("Ikkinchi sonni kiriting:>>>"))
#print(f"{a}+{b}={a+b}\n{a}-{b}={a-b}\n{a}*{b}={a*b}\n{a}/{b}={a/b}")

#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#x = int(input("Istalgan son kiriting:\n>>>"))
#print(x, " ning kvadrati ", x**2, " ga teng")
#print(x, " ning kubi ", x**3, " ga teng")

# Foydalanuvchining yoshini so'rang, 
# va uning tug'ilgan yilini hisoblab, konsolga chiqaring.
#yosh = int(input("Yoshingiz nechida? \n>>>"))
#t_yil = 2020-yosh
#print("Siz ", t_yil, " da tug'ilgansiz")
## Foydalanuvchidan ikki son kiritshni so'rab, 
## kiritilgan sonlarning yig'indisi, ayirmasi,ko'paytmasi va bo'linmasini chiqaruvchi dastur
#a = float(input("Birinchi sonni kiriting: "))
#b = float(input("Ikkinchi sonni kiriting: "))
#print(f"{a}+{b}=", a+b)
#print(f"{a}-{b}=", a-b)
#print(f"{a}x{b}=", a*b)
#print(f"{a}/{b}=", a/b)

#7-DARS

#ismlar=["Umid","Murod","Oqil"]
#for ism in ismlar:
    #print(f"Salom {ism} ishlar yahshimi?")

#ismlar=["Umid","Murod","Oqil"]
#print("Salom", ismlar[0].title())
#print(ismlar[1].upper(), "do'stim qachon qaytasiz?")
#print(ismlar[2].lower(), "qayda ishlayapsan?")

#sonlar=[10, 11, 11.5, -25, 20.25]
#print(sonlar[0]+sonlar[1])
#print(sonlar[2]/sonlar[3]+sonlar[4])
#sonlar[0]=20
#sonlar[4]=sonlar[4]+0.75
#sonlar[1]=sonlar[2]
#print(sonlar)

#t_shahslar=["Navoiy","Yassaviy","Temur","Bobur","Buhoriy"]
#z_shahslar=["Ahmedov","Qosimov","Hoshimov","T.Malik","Eshoqulov"]
#t=t_shahslar.pop(4)
#z=z_shahslar.pop(4)
#print(f"Men tarihiy shahslardan {t_shahslar[4]} bilan, zamonaviy shahslardan esa {z_shahslar[4]} \
#bilan suhbatlashishni hohlardim.")
#print(f"Men tarihiy shahslardan {t_shahslar.pop(4)} bilan, zamonaviy shahslardan esa {z_shahslar.pop(4)} \
#bilan suhbatlashishni hohlardim.")
#print(f"Men tarihir shahslardan {t} bilan zamonamiz odamlaridan {z} bilan suhbatlashmoqchiman")


#
#friends=[]
#friends.append("Umid")
#friends.append("Murod")
#friends.append("Oqil")
#friends.append("Golib")
#friends.append("Gayrat")
#friends.append("Hurshid")
#print(friends)
#friends.remove("Golib")
#friends.remove("Gayrat")
#friends.remove("Hurshid")
#print(friends)
#friends.insert(0,"Yorqin")
#friends.insert(1,"Shuhrat")
#friends.insert(-1,"Azizi")
#print(friends)
#mehmonlar=[]
##a=friends.pop(2)
##b=friends.pop(2)
##c=friends.pop(3)
##mehmonlar.append(a)
##mehmonlar.append(b)
##mehmonlar.append(c)
#mehmonlar.append(friends.pop(2))
#mehmonlar.append(friends.pop(2))
#mehmonlar.append(friends.pop(3))
#print(mehmonlar)

#davlatlar=["Gana","Togo","Peru","Chili","Misr","Qatar","Yaman","Xitoy"]
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar, reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)
#
#juft_sonlar=list(range(120,1200,2))
#print(juft_sonlar)
#jami=sum(juft_sonlar)
#print(jami)
#eng_katta=max(juft_sonlar)
#eng_kichik=min(juft_sonlar)
#print(eng_katta-eng_kichik)
#print(len(juft_sonlar))
#boshi=juft_sonlar[:20]
#urtasi=juft_sonlar[270:291]
#ohiri=juft_sonlar[520:]
#print(f"1- 20 ta sonlar {boshi}, o'rtasidagi 20 ta sonlar {urtasi}, oxiridagi 20 ta sonlar {ohiri}")


#taomlar=["quymoq","norin","palov","mastava","hunon"]
#nonushta=taomlar[:]
#nonushta.remove("palov")
#nonushta.remove("hunon")
#nonushta.remove("norin")
#nonushta.append("atala")
#nonushta.append("qaymoq")
#print(taomlar)
#print(nonushta)
#nonushta=tuple(nonushta)
##nonushta[0]="qaymoq va non"
#print(type(nonushta))
#nonushta=list(nonushta)
#nonushta[0]="non"
#print(nonushta)

#9-DARS

#ismlar=["Oqil","Murod","Umid","Golib","Hurshid"]
#for ism in ismlar:
      #print(f"Do'stim {ism} qachon choyhona?")
#n=len(ismlar)
#print(f"Kod {n} marta takrorlandi")
#
#toq_sonlar=list(range(11,100,2))
##print(toq_sonlar)
#for kub in toq_sonlar:
      #print(f"{kub}ning kubi {kub**3} ga teng.")

#kinolar=[]
#print("Beshta eng sevimli kinoingizni kiriting:")
#for k in range(5):
      #kinolar.append(input(f"{k+1}-sevimli kinoingiz:\n"))
#print(kinolar)

#odamlar=[]
#odam=input("Bugun nechta odam bilan suhbatlashdingiz?\n")
#for i in range(odam):
 #     odamlar.append(input(f"{i+1}- ko'rishgan odamingiz kim?\n"))
#print(odamlar)

#10-DARS
#cars=["toyota","mazda","hyundai","gm","kia"]
#for car in cars:
      #if car=="gm":
            #print(car.upper())
      #else:
            #print(car.title())

#cars=["toyota","mazda","hyundai","gm","kia"]
#for car in cars:
      #if car!="gm":
            #print(car.title())
      #else:
            #print(car.upper())

#login=input("Ismingiz nima?>>>\n")
#if login.lower()=="admin":
      #print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yhatini ko'rasizmi?")
#else:
      #print(f"Xush kelbsiz, {login.title()}")

#print("Ikkita son kiriting:")
#a=float(input("Birinchi sonni kiriting>>>\n"))
#b=float(input("Ikkinchi sonni kiriting>>>\n"))
#if a==b:
      #print("Sonlar teng ekan!!!")

#a=float(input("Istalgan sonni kiriting:>>>\n"))
#if a>=0:
      #print(f"{a} soni musbat son.")
#else:
      #print(f"{a} soni manfiy son.")
#a=float(input("Istalgan sonni kiriting:>>>\n"))
#if a>=0:
      #print(f"{a} sonining ildizi {a**(1/2)} ga teng")
#else:
      #print("Musbat son kiriting!!")

#11-DARS

#son=int(input("Juft son kiriting:\n"))
#if son%2==0:
      #print("Rahmat")
#else:
      #print("Bu juft son emas!!")

#yosh=int(input("Yoshingiz nechchida?\n"))
#if yosh<=4 or yosh>=60:
      #print("Sizga kirish bepul!!!")
#elif yosh <=18:
      #print("Sizga kirish 10000 so'm.")
#else:
      #print("Sizga kirish 20000 so'm")

#print("Ikkita sonni kiriting:")
#a=float(input("Birinchi son:>>>"))
#b=float(input("Ikkinchi son:>>>"))
#if a==b:
      #print("a=b")
#elif a>b:
      #print("a>b")
#else:
      #print("a<b")


#mahsulotlar=["karam","olma","pepsi","cola","pista","tuz","go'sht","uzum","tuhum","kofe"]
#savat=[]
#print("Kerakli mahsulotlarni kiriting:")
#savat.append(input("Birinchi mahsulotni kiriting:>>>"))
#savat.append(input("Ikkinchi mahsulotni kiriting:>>>"))
#savat.append(input("Uchinchi mahsulotni kiriting:>>>"))
#savat.append(input("To'rtinchi mahsulotni kiriting:>>>"))
#savat.append(input("Beshinchi mahsulotni kiriting:>>>"))
#for n in savat:
      #if n in mahsulotlar:
            #print("Mahsulot do'konimizda bor.")
      #else:
            #print("Mahsulot do'konimizda yo'q")

#mahsulotlar=["karam","olma","pepsi","cola","pista","tuz","go'sht","uzum","tuhum","kofe"]
#print("Beshta mahsulot kiriting:")
#savat=[]
#bor_mahsulotlar=[]
#mavjud_emas=[]
#for n in range(5):
      ##savat.append(input(f"{n+1}-mahsulotni kiriting:>>>").lower())
      #savat.append(input(f"{n+1}-mahsulotni kiriting:>>>"))
#for mahsulot in savat:
      #if mahsulot in mahsulotlar:
            #bor_mahsulotlar.append(mahsulot)
      #else:
            #mavjud_emas.append(mahsulot)
#if mavjud_emas:
      ##print(f"Quyidagi mahsulotlar do'konimizda yoq:{mavjud_emas}")
      #print(f"Quyidagi mahsulotlar do'konimizda yoq: ")
      #for mahsulot in mavjud_emas:
            #print(mahsulot)
#else:
      #print("Siz so'ragan barcha mahsulotlar do'konimizda bor!")

#users=["anvar","olim","murod","umid","oqil"]
#login=input("Yangi login kiriting:>>>").lower()
#if login in users:
      #print("Login band, yangi login tanlang!")
#else:
      #print("Hush kelibsiz", login)

#son=int(input("Butun son kiriting:>>>"))
#print(f"{son} 2 dan 10 gacha bo'lgan sonlardan:")
#for n in range(2,10):
      #if not (son%n):
            #print(f"{n} ga qoldiqsiz bo'linadi.")

#12-DARS HATOLAR BILAN ISHLASH

#son=float(input("Juft son kiriting: "))
#if son%2==0:
      #print("Bu son juft emas")
#else:
      #print("Rahmat")

# BU yerda mantiqiy hato

##yosh=(input("Yoshingiz nechchida?")) TypeError: '<=' not supported between instances of 'str' and 'int
#yosh=int(input("Yoshingiz nechchida?"))
#if yosh<=4 or yosh>=60:
      #narh=0
##elif yosh<18 SyntaxError: expected ':'
#elif yosh<18:
      #narh=10000
#else:
      #narh=20000
      ##print(f"CHipta {narh} so'm") MANTIQIY HATO
#print(f"CHipta {narh} so'm")

#x=float(input("Birinchi son:>>>"))
#y=float(input("Ikkinchi son:>>>"))
#if x==y:
      #print(f"{x}={y}")
#elif x<y:
      ##print(f'{x}<{y}")
      #print(f"{x}<{y}")      
#else:
      #print(f"{x}>{y}")

#mahsulotlar=["un","yog","sovun","tuhum","piyoz",
            #"kartoshka","olma","banan","uzum","qovun"]
#savat=[]            
#for n in range(5):
      ##savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ")) NameError: name 'savat' is not defined
     #savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#if savat:
      ##for mahsulot in savat   SyntaxError: expected ':'
      #for mahsulot in savat:
            #if mahsulot in mahsulotlar:
                  #print(f"Do'konimizda {mahsulot} bor")
            #else:
                  #print(f"Do'konimizda {mahsulot} yo'q")
#else:
      #print("Savatingiz bo'sh")                        

#mahsulotlar=["un","yog","sovun","tuhum","piyoz",
            #"kartoshka","olma","banan","uzum","qovun"]
#savat=[]            
#for n in range(5):
     #savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#bor_mahsulotlar=[]
#mavjud_emas=[]
#for mahsulot in savat:
      #if mahsulot in mahsulotlar:
            ##bor_mahsulotlar.append(mahslot) NameError: name 'mahslot' is not defined. Did you mean: 'mahsulot'?
            #bor_mahsulotlar.append(mahsulot)
      #else:
            #mavjud_emas.append(mahsulot)
#if mavjud_emas:
      #print("Do'konimizda quyidagi mahsulotlar yo'q:")
      #for mahsulot in mavjud_emas:
            #print(mahsulot)
#else:
      #print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
                       