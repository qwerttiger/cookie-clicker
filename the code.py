import sys #import sys to exit
import threading #import threading for timers and threads
import random #import random for random numbers
import time #import time to sleep
import os #import os to hide support prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide" #hide support prompt
import pygame #import pygame
from decimal import Decimal as decimal #import decimal numbers with infinite precision

pygame.init() #initiate pygame
screen=pygame.display.set_mode([700,700]) #make screen
pygame.display.set_caption("Cookie Clicker") #set caption

white=(255,255,255) #set white colour
black=(0,0,0) #set black colour

pointer_mask=pygame.mask.Mask((1,1),True) #pointer mask
big_cookie=pygame.image.load("pictures/cookie.png") #big cookie picture
big_cookie_mask=pygame.mask.from_surface(big_cookie) #big cookie mask

click1=pygame.mixer.Sound("sounds/click1.wav") #click sound 1
click2=pygame.mixer.Sound("sounds/click2.wav") #click sound 2
click3=pygame.mixer.Sound("sounds/click3.wav") #click sound 3
click4=pygame.mixer.Sound("sounds/click4.wav") #click sound 4
click5=pygame.mixer.Sound("sounds/click5.wav") #click sound 5
click6=pygame.mixer.Sound("sounds/click6.wav") #click sound 6
click7=pygame.mixer.Sound("sounds/click7.wav") #click sound 7
buy1=pygame.mixer.Sound("sounds/buy1.wav") #buy sound 1
buy2=pygame.mixer.Sound("sounds/buy2.wav") #buy sound 2
buy3=pygame.mixer.Sound("sounds/buy3.wav") #buy sound 3
buy4=pygame.mixer.Sound("sounds/buy4.wav") #buy sound 4

x=None #set x to be nothing

mute=False #set mute to false

def numbershortener(num): #numbershortener
  if num<1000000:
    return str(num)
  elif num<1000000000:
    return str(round(num/1000000,3))+" million"
  elif num<1000000000000:
    return str(round(num/1000000000,3))+" billion"
  elif num<1000000000000000:
    return str(round(num/1000000000000,3))+" trillion"
  elif num<1000000000000000000:
    return str(round(num/1000000000000000,3))+" quadrillion"
  elif num<1000000000000000000000:
    return str(round(num/1000000000000000000,3))+" quintillion"
  elif num<1000000000000000000000000:
    return str(round(num/1000000000000000000000,3))+" sextillion"
  elif num<1000000000000000000000000000:
    return str(round(num/1000000000000000000000000,3))+" septillion"
  elif num<1000000000000000000000000000000:
    return str(round(num/1000000000000000000000000000,3))+" octillion"
  elif num<1000000000000000000000000000000000:
    return str(round(num/1000000000000000000000000000000,3))+" nonillion"
  elif num<1000000000000000000000000000000000000:
    return str(round(num/1000000000000000000000000000000000,3))+" decillion"
  else:
    return "Infinity"

def buy(num): #buy building number num
  if num*41-41<=mouse_pos[1]<num*41 and cookies>=eval(f"bc{num}"): #if you click on it and you can buy it
    exec(f"cookies-=bc{num}",globals()) #decrease your cookies
    exec(f"bc{num}=round(bc{num}*1.15)",globals()) #increase the price
    exec(f"b{num}+=1",globals()) #add 1 to bought
    exec(f"cps+=decimal(str(bp{num}))",globals()) #add the cps to your cps
    
    if not mute: #if unmuted
      play_random_buy() #play the buy sound

def clear_cookies(): #clear cookies
  file=open("save data.txt","w") #open the file
  file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n15\n100\n1100\n12000\n130000\n1400000\n20000000\n330000000\n5100000000\n75000000000\n1000000000000\n14000000000000\n170000000000000\n2100000000000000\n26000000000000000\n310000000000000000\n71000000000000000000\n0.1\n1\n8\n47\n260\n1400\n7800\n44000\n260000\n1600000\n10000000\n65000000\n430000000\n2900000000\n21000000000\n150000000000\n1100000000000\n0\n0\n1\n0\n100") #write to file
  file.close() #close file
  
  load_save_data() #load save data

def load_save_data(): #load save data
  global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9,bc10,bc11,bc12,bc13,bc14,bc15,bc16,bc17,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,bp10,bp11,bp12,bp13,bp14,bp15,bp16,bp17,cookies,cps,cpc,total_cookies,multiplier #global variables
  try: #try to
    file=open("save data.txt").read().split() #open file for reading
  except: #if the file does not exist
    file=open("save data.txt","w") #open file for writing
    file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n15\n100\n1100\n12000\n130000\n1400000\n20000000\n330000000\n5100000000\n75000000000\n1000000000000\n14000000000000\n170000000000000\n2100000000000000\n26000000000000000\n310000000000000000\n71000000000000000000\n0.1\n1\n8\n47\n260\n1400\n7800\n44000\n260000\n1600000\n10000000\n65000000\n430000000\n2900000000\n21000000000\n150000000000\n1100000000000\n0\n0\n1\n0\n100") #write this
    file.close() #close file
    file=open("save data.txt").read().split() #read file

  #set the variables
  b1=int(file[0])
  b2=int(file[1])
  b3=int(file[2])
  b4=int(file[3])
  b5=int(file[4])
  b6=int(file[5])
  b7=int(file[6])
  b8=int(file[7])
  b9=int(file[8])
  b10=int(file[9])
  b11=int(file[10])
  b12=int(file[11])
  b13=int(file[12])
  b14=int(file[13])
  b15=int(file[14])
  b16=int(file[15])
  b17=int(file[16])
  bc1=int(file[17])
  bc2=int(file[18])
  bc3=int(file[19])
  bc4=int(file[20])
  bc5=int(file[21])
  bc6=int(file[22])
  bc7=int(file[23])
  bc8=int(file[24])
  bc9=int(file[25])
  bc10=int(file[26])
  bc11=int(file[27])
  bc12=int(file[28])
  bc13=int(file[29])
  bc14=int(file[30])
  bc15=int(file[31])
  bc16=int(file[32])
  bc17=int(file[33])
  bp1=decimal(str(file[34]))
  bp2=decimal(str(file[35]))
  bp3=decimal(str(file[36]))
  bp4=decimal(str(file[37]))
  bp5=decimal(str(file[38]))
  bp6=decimal(str(file[39]))
  bp7=decimal(str(file[40]))
  bp8=decimal(str(file[41]))
  bp9=decimal(str(file[42]))
  bp10=decimal(str(file[43]))
  bp11=decimal(str(file[44]))
  bp12=decimal(str(file[45]))
  bp13=decimal(str(file[46]))
  bp14=decimal(str(file[47]))
  bp15=decimal(str(file[48]))
  bp16=decimal(str(file[49]))
  bp17=decimal(str(file[50]))
  cookies=decimal(str(file[51]))
  cps=decimal(str(file[52]))
  cpc=int(file[53])
  total_cookies=decimal(str(file[54]))
  multiplier=int(file[55])

def play_random_click(): #play random click sound
  a=random.randint(1,7) #set a to a random number
  exec(f"click{a}.play()") #play sound
  a+=random.randint(1,5) #add
  a=7 if a==7 else a%7 #adjust to a number that make sense
  time.sleep(0.1) #wait a little bit
  exec(f"click{a}.play()") #play sound

def play_random_buy(): #play random buy sound
  exec(f"buy{random.randint(1,4)}.play()") #play sound

def draw_lines(): #draw these lines
  for x in range(1,17): #for every number in here
    pygame.draw.rect(screen,black,pygame.Rect(500,41*x-1,200,2)) #draw a line corresponding to the number

def draw_text(text,pos,size=8,side=True): #draw text
  if not side: #if not side
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0]-round(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_width()/2),pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2)) #draw it
  else: #if side
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0],pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2)) #draw it

def add_cookies(): #add cookies
  global cookies,total_cookies,t #global variables
  
  cookies+=decimal(str(cps))*multiplier/1000 #add cookies
  total_cookies+=decimal(str(cps))*multiplier/1000 #add total cookies
  
  t=threading.Timer(0.1,add_cookies) #t is a timer
  t.start() #start timer

def unblocker(): #unblocker
  while not finish: #while not finish
    for event in pygame.event.get(): #for every event
      if event.type==pygame.QUIT: #if quit pygame
        pygame.quit() #pygame quit
        t.cancel() #cancel timer
        th.cancel() #cancel timer
        sys.exit() #exit

def inputcommand(): #input
  global x #global x
  x=input("Command (\"quit\" to quit): ").lower() #input

def save(autosave=False):
  open("save data.txt","w").write(eval("chr(10).join([str(x) for x in [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9,bc10,bc11,bc12,bc13,bc14,bc15,bc16,bc17,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,bp10,bp11,bp12,bp13,bp14,bp15,bp16,bp17,cookies,cps,cpc,total_cookies,multiplier]])")) #save
  if not autosave:
    print("saved!") #print saved
  else:
    print("autosaved") #print autosaved

def autosave():
  global th #global th
  
  save(True) #save

  th=threading.Timer(60,autosave) #th is a timer
  th.start() #start timer

def command(): #command
  global loop,x,finish #global variables
  
  finish=False #set finish to false
  
  del x #delete x
  threading.Thread(target=inputcommand).start() #find x
  
  ok=False #set ok to be false
  while not ok: #while you don't know x
    try: #try to
      x #find x
    except: #if x is not defined
      pass #pass
    else: #then,
      ok=True #ok is true
  
  if x in ["quit","exit"]: #if x is exit or quit
    loop=False #break out of loop
  else: #else
    try: #try to
      print("Output:",eval(x,globals())) if eval(x,globals())!=None else exec(x,globals()) #output
    except: #if that didn't work
      try: #then
        exec(x,globals()) #do this
      except Exception as e: #if THAT didn't work
        print(f"Error: {e}") #then print error message
  
  finish=True #finish

#real game starts here
load_save_data() #load save data
add_cookies() #add cookies
th=threading.Timer(60,autosave)

while True: #game loop
  screen.fill(white) #fill screen with white
  
  if cookies!=decimal("infinity"): #if not infinity cookies
    draw_text(f"{numbershortener(round(cookies))} cookies",(350,100),25,False) #draw text
  else: #if infinity cookies
    draw_text(f"{numbershortener(decimal('infinity'))} cookies",(350,100),25,False) #draw text
  
  draw_text(f"CpS: {numbershortener(cps)}",(350,150),18,False) #draw cps
  
  #these are all building text
  draw_text(f"Cursor, cost {numbershortener(bc1)}, have {b1}",(500,20))
  draw_text(f"Grandma, cost {numbershortener(bc2)}, have {b2}",(500,61))
  draw_text(f"Farm, cost {numbershortener(bc3)}, have {b3}",(500,102))
  draw_text(f"Mine, cost {numbershortener(bc4)}, have {b4}",(500,143))
  draw_text(f"Factory, cost {numbershortener(bc5)}, have {b5}",(500,184))
  draw_text(f"Bank, cost {numbershortener(bc6)}, have {b6}",(500,225))
  draw_text(f"Temple, cost {numbershortener(bc7)}, have {b7}",(500,266))
  draw_text(f"Wizard Tower, cost {numbershortener(bc8)}, have {b8}",(500,307))
  draw_text(f"Shipent, cost {numbershortener(bc9)}, have {b9}",(500,348))
  draw_text(f"Alchemy Lab, cost {numbershortener(bc10)}, have {b10}",(500,389))
  draw_text(f"Portal, cost {numbershortener(bc11)}, have {b11}",(500,430))
  draw_text(f"Time Machine, cost {numbershortener(bc12)}, have {b12}",(500,471))
  draw_text(f"Antimatter Condenser, cost {numbershortener(bc13)}, have {b13}",(500,512))
  draw_text(f"Prism, cost {numbershortener(bc14)}, have {b14}",(500,553))
  draw_text(f"Chancemaker, cost {numbershortener(bc15)}, have {b15}",(500,594))
  draw_text(f"Fractal Engine, cost {numbershortener(bc16)}, have {b16}",(500,635))
  draw_text(f"Python Console, cost {numbershortener(bc17)}, have {b17}",(500,676))
  
  draw_text("Command Line",(350,550),15,False) #command line text
  
  if cookies!=decimal("infinity"): #if not infinity cookies
    draw_text(f"Total cookies: {numbershortener(round(total_cookies))}",(0,20),15) #total cookies text
  else: #if infinity cookies
    draw_text(f"Total cookies: {numbershortener(decimal('infinity'))} cookies",(0,20),15) #total cookies text
  screen.blit(big_cookie,(225,225)) #draw big cookie
  
  pygame.draw.rect(screen,black,pygame.Rect(199,0,2,700)) #draw filler 1
  pygame.draw.rect(screen,black,pygame.Rect(499,0,2,700)) #draw filler 2
  
  pygame.draw.rect(screen,black,pygame.Rect(300,500,100,100),1) #draw command line box

  pygame.draw.rect(screen,black,pygame.Rect(300,650,100,50),1) #draw mute/unmute box
  draw_text("Unmute" if mute else "Mute",(350,675),15,False) #draw mute/unmute text
  
  draw_lines() #draw lines
  
  for event in pygame.event.get(): #for every event
    if event.type==pygame.QUIT: #if quit pygame
      pygame.quit() #pygame quit
      t.cancel() #cancel timer
      th.cancel() #cancel timer
      sys.exit() #exit
    if event.type==pygame.MOUSEBUTTONDOWN: #if you click
      if event.button in [1,2,3]: #if you click and not scroll
        mouse_pos=pygame.mouse.get_pos() #set mouse_pos to mouse position
        
        if big_cookie_mask.overlap_area(pointer_mask,(mouse_pos[0]-225,mouse_pos[1]-225)): #if you click the big cookie
          cookies+=cpc #add cpc to cookies
          total_cookies+=cpc #add cpc to total cookies
          
          if not mute: #if not muted
            threading.Thread(target=play_random_click).start() #play random click sound
        
        if mouse_pos[0]>=500: #if you buy
          for _ in range(1,18): #for everything in the range
            buy(_) #see if you bought it
        
        if 300<=mouse_pos[0]<=400 and 500<=mouse_pos[1]<=600: #if click console
          loop=True #loop is true
          
          while loop: #while loop
            finish=False #finish is false
            threading.Thread(target=command).start() #start command line
            unblocker() #unblock

        if 300<=mouse_pos[0]<=400 and 650<=mouse_pos[1]<=700:
          mute=not mute
    
    if event.type==pygame.KEYDOWN: #if click down
      if event.key==pygame.K_s and (event.mod & pygame.KMOD_CTRL): #if you press ctrl-s
        save() #save
  
  pygame.display.update() #update pygame
