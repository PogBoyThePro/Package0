command = '_'
import os
clear = lambda: os.system('cls')
clear()
Cops_And_Robbers=0
import random, time, pyttsx3
import os




 
from time import sleep

#
fuel=1.5
#
print ('write "help"+Enter Key for commands')
import time 
started=False
stopped=True
def is_equals(var1, var2, t="str"):
    if t== "str":
        var1 = str(var1)
        var2 = str(var2)
    elif t == "int":
        var1 = int(var1)
        var2 = int(var2)
#
    if var1 == var2:
        return True
    return False
while True:
    command = input(':').lower()
    if is_equals(command,"start",t="str"):
 #           
        if started==False:
            sleep(1)
            Cops_And_Robbers+=1
            started=True
            print ("started....vroom vroom")           
            while Cops_And_Robbers==3:
                fuel=fuel-0.5
                sleep(2)
                print(fuel)
            stopped=Falsegbg
            
#
        
        
            if fuel<=0:
                print("Not Enough fuel to run")
                break
 #   
        
  #           
        elif started==True:
            print('baka it has already started!!!!')
#
    elif command==('stop'):
        if stopped ==True:
            print('car has been already stoped!')
   #         
        elif stopped==False:
         print('ok the car is being stoped!!')
         started=False
         stopped=True
         print(f'Fuel left = {fuel}litres')
#     
    elif command=='speed up':
        if started==True:
            print ("You crashed into a tree and died re-run the code again go to play more in other words 'Game-over'!")
            break
        elif started==False:
            print("The car did not even start baka")

#
    elif command=='quit':
        time.sleep(0.5)
        print ("closing files ...")
        time.sleep(0.5)
        clear()
        print ("shutting down")
        clear()
        print("process complete")
        break
#
    elif command=='re fuel':
         print ("you re-fueled your car PoGZ")
         fuel=9.4
#
    elif command=='check fuel':
        print (f'fuel is {fuel}litres :)')
 #       
    elif command == 'help':
        print('start - to start')
        print ("stop to stop")
        print('speed up to speed up')
        print("check fuel")
        print("re fuel")
        print ("quit")
    
#
    elif fuel==0:
        print("the car is out of fuel!")

#
    else :
        print('what are you talking about?!')
   
