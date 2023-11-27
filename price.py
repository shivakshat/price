print(
                '''menu
      s.no. item        price
      1.    pizza       100/-
      2.    tikki       70/-
      3.    panipuri    50/-
      4.    rasgulla    14/-(1 piece)
      5.    gulab jamun 14/-(1 piece)
      6.    ckn. tikka  180/-
      7.    mtn. chaap  250/-
      8.    burger      50/-
      9.    lassi       40/-
      10.   kulfi faluda70/-'''
      )
price_of_pizza=100
price_of_tikki=70
price_of_panipuri=50
price_of_rasgulla=14
price_of_gulabjamun=14
price_of_ckntikka=180
price_of_mtnchaap=250
price_of_burger=50
price_of_lassi=40
price_of_kulfifaluda=70
c='more'
bill1=0
bill2=0
bill3=0
bill4=0
bill5=0
bill6=0
bill7=0
bill8=0
bill9=0
bill10=0
while c=='more':
    ch=int(input("enter your choice 1-10"))
    if ch==1:
        kitne_pizza=int(input("no.of pizza"))
        bill1=bill1+price_of_pizza*kitne_pizza
    elif ch==2:
        kitne_tikki=int(input("no.of tikki"))
        bill2=bill2+price_of_tikki*kitne_tikki
    elif ch==3:
        kitne_panipuri=int(input("no.of panipuri"))
        bill3=bill3+price_of_panipuri*kitne_panipuri
    elif c==4:
        kitne_rasgulla=int(input("no.of rasgulla"))
        bill4=bill4+price_of_rasgulla*kitne_rasgulla
    elif ch==5:
        kitne_gulabjamun=int(input("no.of gulabjamun"))
        bill5=bill5+price_of_gulabjamun*kitne_gulabjamun
    elif ch==6:
        kitne_ckntikka=int(input("no.of ckntikka"))
        bill6=bill6+price_of_ckntikka*kitne_ckntikka
    elif ch==7:
        kitne_mtnchaap=int(input("no.of mtnchaap"))
        bill7=bill7+price_of_mtnchaap*kitne_mtnchaap
    elif ch==8:
        kitne_burger=int(input("no.of burger"))
        bill8=bill8+price_of_burger*kitne_burger
    elif ch==9:
        kitne_lassi=int(input("no.of lassi"))
        bill9=bill9+price_of_lassi*kitne_lassi
    elif ch==10:
        kitne_kulfifaluda=int(input("no.of kulfifaluda"))
        bill10=bill10+price_of_kulfifaluda*kitne_kulfifaluda
    
    c=input('more or not')
total_bill=bill1+bill2+bill3+bill4+bill5+bill6+bill7+bill8+bill9+bill10
print(total_bill)