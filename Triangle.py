def CollectVar():
     x = int ( input ("Enter a base length: "))
     
     if (x % 2) == 0:
          RightTri(x)
          
     else:
          IsoTri(x)
            
    
def IsoTri(x):
    y = int(((x-1) / 2))
    z = str(" ")
    star = 0
    gap = 0
    x = x
    ins = ("*" + ((z)*gap) + "*")

    print (((z)*y) + ("*") + ((z)*y))
    star +=1
    gap = 1
    while star < x:
        ins = ("*" + ((z)*gap) + "*")
        if len(ins) == x:
            print(("*")*x)
            CollectVar()
            
            
            break
        y -= 1
        print (((z)*y) + ins + ((z)*y))
        star += 1
        gap += 2
        
def RightTri(x):
     gap = 0
     layer = ("*" + ((" ")*gap) + ("*"))
     x = x
     star = 1
     print("*")

     while star < x:

          if star >= 2:
               gap += 1

         

          layer = ("*" + ((" ")*gap) + ("*"))
          
          if len(layer) == x:
               layer = (("*")*x)
               print(layer)
               CollectVar()
          else:
               print(layer)
               star += 1
               

        
               
          
          

    
    
    
CollectVar()
