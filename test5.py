# 1 Listin bütün elementləri cəmini(hasilini) hesablayın

# ededler=[2,8,6,1,3,4]
# 1 ededlerin cemi
# zero=0
# for x in ededler:
#     zero+=x
#     print(zero)
# 2 ededlerin hasili
# zero=1
# for x in ededler:
#     zero*=x    
#     print(zero)


# 2.Verilən list elementlərini sağdan sola çap edin


# meyveler=['heyva','nar','qarpiz','alma','gilas','banan']
# meyveler.reverse()
# print(meyveler)


# 3 İki fərqli list yaradın və listləri merge edin(zip metodu)
# list1=[]
# a =['qar','ciy','arm']
# b =['piz','elek','ud']      
# c=zip(a,b)


# for (x,y) in c:
#     d=x+y
#     list1.append(d)
# print(list1)



# 4 Listin içində bir neçə list olsun, 3ci elementinin 2ci indeksinə dəyər əlavə edin
# list1=['Php','Javascript',['react','vue','nodeJs'],'C#',]
# list1[2].insert(2,'angular')
# print(list1)


# 5 List yaradın , listin hər hansı dəyərinin indeksini tapın və həmin indeksə başqa dəyər əlavə edin

# meyveler=['heyva','nar','qarpiz','alma','gilas','banan']
# print(meyveler.index('alma'))
# meyveler[3]='armud'
# print(meyveler)


# 6 Verilmiş listin ədədi ortasını tapın

# ededler=[2,15,6,1,30,0]
# zero=0
# a=len(ededler)


# for x in ededler:
#     zero+=x
# y=zero/a
# print((y))


# 7 İnputdan gələn iki rəqəm aralığında yerləşən rəqəmlərin cüt və ya tək olduğunu(əlavə olaraq cüt rəqəmlərin sayını hesablayın) tapıın

# a=int(input("Eded daxil edin :"))
# b=int(input("Ikinci ededi daxil edin :"))
# cut_eded=0

# for x in range(a,b+1):
#     if x % 2 ==0 :
#         cut_eded +=1
# print(cut_eded)


# 8 Təkrar elemetlərdən ibarət list yaradın, sonra bu listdən təkrarlanmayan list yaradın

# a=['alma','armud','alma','qarpiz','heyva','qarpiz']
# print(set(a))




# 9. 3 rəqəmdən  ibarət list yaradın və bu listin rəqəmlərindən yarana biləcək kombinasiyaları çap edin

# a=[10,24,9]
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)



# 10 1.a = {'ad':['Fuad','Rovsen','Orxan']}

# Proqram Sorushur :
# 	Secim Edin : (1) Elave et (2) Sil 
	
# 	Error Mesajlari :
# 		Ad daxil etmediniz
# 		Bu ad bazada yoxdur


# a = {'ad':['Fuad','Rovsen','Orxan']}

# query=int(input("Secim Edin : (1) Elave et (2) Sil : "))

# if query==1:
#     add=input("Elave etmek isdediyiniz adi daxil edin : ")
#     if add=="":
#       print("Ad daxil etmediniz")  
#     elif add in a["ad"]:
#         print("Bu ad bazada var")
#     else:
#         a['ad'].append(add)
#         print(a)
# if query==2:
#     remove=input("Silmek isdediyiniz adi daxil edin : ")
#     if remove=='':
#         print("Ad daxil etmediniz") 
#     elif remove not in a['ad']:
#         print("Bu ad bazada yoxdur")
#     else:
#         a["ad"].remove(remove)
#         print(a)
    

# 11
# Virtual Printer:

# Daxil Edin : Java
# Say: 6

# a=input("Cap etmek isdeyinizi metni daxil edin :")
# b=int(input("Sayini daxil edin :"))

# i=0
# while i<=b:
#     print(i,a)
#     i+=1
    


 
