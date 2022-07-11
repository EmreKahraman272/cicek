import turtle as t
from time import sleep
def cicek_cizme(y,re,b,l,v):
    for i in range(y):
        t.up()
        t.goto(0, 0)
        t.down()
        t.fillcolor(renkler[re])
        t.begin_fill()
        t.circle(boyutlar[b], v)
        t.left(l)
        t.circle(boyutlar[b], v)
        t.end_fill()
    sleep(3)

renkler = {"Mavi":"Blue",
           "Sarı":"Yellow",
           "Kırmızı":"Red",
           "Beyaz":"White"}
boyutlar = {"Büyük": 300,
            "Orta": 150,
            "Küçük": 100}


print("""////Çicek çizime hoşgeldiniz !//// """)
print("Renklerimiz: ",*renkler)
print("Boyutlarımız.",*boyutlar)

y = int(input("Kaç yapraklı olsun? \t\t-> "))
re = str(input("Çiceğin rengi ne olsun? \t-> "))
b = str(input("Boyutu ne olsun? \t\t\t-> "))
l = (360 / y)
v = (180 - l)
cicek_cizme(y,re,b,l,v)

