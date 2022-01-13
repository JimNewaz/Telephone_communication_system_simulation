from random import seed
from random import randint
from random import choice
import time

print("☎ ☎ ☎ Telephone Communication System ☎ ☎ ☎")

print()

# seed random number generator
seed(1)
def Empty(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1


tel=[1,2,3,4,5,6,7,8]   # No of Telephones
free=[1,2,3,4,5,6,7,8]  # Initially all are free
busylist=[]
freeline=[1,2,3]   
processed=0
completed=0
busy=0
blocked=0
sim_time=0
call_length=0
sender=0
receiver=0
line_no=0
departure=[]    #four value-> call_end_time, from,to,line no

while(sim_time<120):           #Until 120
  sim_time= sim_time+1

  while(Empty(departure) and (sim_time==departure[0][0])):
    print(f"call between {departure[0][1]} and {departure[0][2]} finished at {departure[0][0]}")
    completed=completed+1
    print(f"Total completed call= {completed}\n")
    free.append(departure[0][1])
    free.append(departure[0][2])
    freeline.append(departure[0][3])
    busylist.remove(departure[0][1])
    busylist.remove(departure[0][2])
    del departure[0]


  is_call_arrive=randint(0,5)  #random no between 0-5

  if(is_call_arrive==1):      #call arrive in every 5 min
    processed=processed+1
    sender=choice(free)
    free.remove(sender)       #remove from free
    busylist.append(sender)   #mark as busy
    tmp=tel
      #  print(sender)
      #  print(tel)
      #  print(tmp)
    tel.remove(sender)        #sender can not call himself
    receiver=choice(tel)      #select a receiver
    tel.append(sender)        

    if(Empty(freeline)):
       if receiver in busylist:
         print(f"{sender} is trying to call {receiver} but line is Busy.")
         busy=busy+1
         print(f"Busy line is {busylist}")
         print(f"Busy= {busy}\n")
         free.append(sender)
         busylist.remove(sender) 

       else:
         free.remove(receiver)      #As the receiver is not in the busylist, add the receiver to the busy list and remove from free list
         busylist.append(receiver)
         line_no=choice(freeline)   #Choose a line no and remove it from freeline
         freeline.remove(line_no)
         call_length=randint(20,50)
         dept_time=sim_time+call_length
         #value = end_time, from, to, line
         val=(dept_time,sender,receiver,line_no)
         print(f"{sender} calls {receiver} at {sim_time} by line no {line_no} with aprox call lenth {call_length}\n")
         departure.append(val)
         departure.sort()
    else:
      print(f"{sender} is trying to call {receiver} but no free Line.")
      print(f"departure list {departure}") 
      blocked=blocked+1             #if no line free,then call will be blocked
      print(f"no of blocked call= {blocked}\n")
      free.append(sender)
      busylist.remove(sender) 

print(f"total no of call processed= {processed} ")
print(f"total number of call completed= {completed}")
print(f"total number of call blocked= {blocked}")
print(f"total number of call found busy= {busy}")
