sayi=int(input("Bir sayı giriniz : "))
carpantoplamı=0
for i in range(1,sayi):
    if(sayi%i==0):
        carpantoplamı+=i
    if(carpantoplamı-sayi==sayi):
        print(  sayi, " sayısı mükemmel sayıdır")
        break
    else:
        print( sayi, " sayısı mükemmel sayıdır")
        break
        
 
 



sayi=int(input("Bir sayı giriniz : "))
asal=1
for bolen in range(2,sayi):
    if(sayi%bolen==0):
        print (sayi, " sayısı asal değildir")
        asal=0
        break
    if(asal==1):
        print(sayi,  "  sayısı asaldır")
        break

    
    
    
    
    
    
    
    
    
    
    
    
    
    