import sys #import sys to exit
import threading #import threading for timers and threads
import random #import random for random numbers
import time #import time to sleep
import os #import os to hide support prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide" #hide support prompt
import pygame #import pygame
from decimal import Decimal as decimal #import decimal numbers with infinite precision
################################################################################
white=(255,255,255) #set white colour
black=(0,0,0) #set black colour

pygame.init() #initiate pygame
screen=pygame.display.set_mode([700,700]) #make screen
surface=pygame.Surface([700,700]) #make surface
surface2=pygame.Surface([700,700]) #make surface2
pygame.display.set_caption("Cookie Clicker") #set caption
surface.set_colorkey(white) #set white colourkey
surface2.set_colorkey(white) #set white colourkey

fps_track=False #set fps track to false

pointer_mask=pygame.mask.Mask((1,1),True) #pointer mask
big_cookie=pygame.image.load("pictures/cookie.png") #big cookie picture
big_cookie_mask=pygame.mask.from_surface(big_cookie) #big cookie mask
gold_cookie=pygame.image.load("pictures/golden.png") #golden cookie picture
gold_cookie_mask=pygame.mask.from_surface(gold_cookie) #golden cookie mask

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
gold_sound=pygame.mixer.Sound("sounds/golden.wav")

x=None #set x to be nothing

rightpanel="b"

mute=False #set mute to false

question=pygame.image.load("pictures/question.png")
achievements=[[a,b,pygame.image.load("pictures/"+c+".png"),d,e] for a,b,c,d,e in eval("["+open("achievements.txt").read().replace("]","],")+"]")]
achievements_to_unlock=achievements[:]

goldens=[]

upgrades=[[a,b,c,pygame.image.load("pictures/"+d+".png"),e,f] for a,b,c,d,e,f in eval("["+open("upgrades.txt").read().replace("]","],")+"]")]
upgrades_to_unlock=upgrades[:]
upgrades_buyable=[]
################################################################################
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
  if num*43-43<=mouse_pos[1]<num*43 and cookies>=eval(f"bc{num}"): #if you click on it and you can buy it
    exec(f"cookies-=bc{num}",globals()) #decrease your cookies
    exec(f"bc{num}=round(bc{num}*1.15)",globals()) #increase the price
    exec(f"b{num}+=1",globals()) #add 1 to bought
    exec(f"cps+=bp{num}",globals()) #add the cps to your cps
    
    if not mute: #if unmuted
      play_random_buy() #play the buy sound

def clear_cookies(): #clear cookies
  global achievements_to_unlock
  file=open("save data.txt","w") #open the file
  file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n15\n100\n1100\n12000\n130000\n1400000\n20000000\n330000000\n5100000000\n75000000000\n1000000000000\n14000000000000\n170000000000000\n2100000000000000\n26000000000000000\n310000000000000000\n0.1\n1\n8\n47\n260\n1400\n7800\n44000\n260000\n1600000\n10000000\n65000000\n430000000\n2900000000\n21000000000\n150000000000\n0\n1\n0\n100\n0\n0\n0\n0") #write to file
  file.close() #close file
  achievements_to_unlock=achievements[:]
  load_save_data() #load save data

def load_save_data(): #load save data
  global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9,bc10,bc11,bc12,bc13,bc14,bc15,bc16,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,bp10,bp11,bp12,bp13,bp14,bp15,bp16,cookies,cps,cpc,total_cookies,multiplier,unlock_achievements,achievements_to_unlock,ft,unlocked_upgrades,bought_upgrades #global variables
  try: #try to
    file=open("save data.txt").read().split() #open file for reading
  except: #if the file does not exist
    file=open("save data.txt","w") #open file for writing
    file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n15\n100\n1100\n12000\n130000\n1400000\n20000000\n330000000\n5100000000\n75000000000\n1000000000000\n14000000000000\n170000000000000\n2100000000000000\n26000000000000000\n310000000000000000\n0.1\n1\n8\n47\n260\n1400\n7800\n44000\n260000\n1600000\n10000000\n65000000\n430000000\n2900000000\n21000000000\n150000000000\n0\n1\n0\n100\n0\n0\n0\n0") #write this
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
  bc1=int(file[16])
  bc2=int(file[17])
  bc3=int(file[18])
  bc4=int(file[19])
  bc5=int(file[20])
  bc6=int(file[21])
  bc7=int(file[22])
  bc8=int(file[23])
  bc9=int(file[24])
  bc10=int(file[25])
  bc11=int(file[26])
  bc12=int(file[27])
  bc13=int(file[28])
  bc14=int(file[29])
  bc15=int(file[30])
  bc16=int(file[31])
  bp1=decimal(file[32])
  bp2=decimal(file[33])
  bp3=decimal(file[34])
  bp4=decimal(file[35])
  bp5=decimal(file[36])
  bp6=decimal(file[37])
  bp7=decimal(file[38])
  bp8=decimal(file[39])
  bp9=decimal(file[40])
  bp10=decimal(file[41])
  bp11=decimal(file[42])
  bp12=decimal(file[43])
  bp13=decimal(file[44])
  bp14=decimal(file[45])
  bp15=decimal(file[46])
  bp16=decimal(file[47])
  cookies=decimal(file[48])
  cpc=int(file[49])
  total_cookies=decimal(file[50])
  multiplier=int(file[51])
  unlock_achievements=bin(int(file[52]))[:-2:-1]
  ft=timer(int(file[53]),finishfrenzy) if file[53]!="0" else timer(0,lambda:None)
  unlocked_upgrades=bin(int(file[54]))[:-2:-1]
  bought_upgrades=bin(int(file[55]))[:-2:-1]
  cps=sum([eval(f"b{bnum}*bp{bnum}") for bnum in range(1,17)])*multiplier/100
  
  
  while len(unlock_achievements)<len(achievements):
    unlock_achievements="0"+unlock_achievements

  achievement_id=1
  for achievement_unlocked in unlock_achievements:
    if int(achievement_unlocked):
      achievements_to_unlock[achievement_id-1]=[]

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
  for x in range(1,16): #for every number in here
    pygame.draw.rect(surface,black,pygame.Rect(500,round(700/16*x-1),200,2)) #draw a line corresponding to the number

def draw_text(text,pos,size=8,side=True,surface=screen): #draw text
  if not side: #if not side
    surface.blit(pygame.font.SysFont("arial",size).render(text,True,black),(pos[0]-round(pygame.font.SysFont("arial",size).render(text,True,black).get_width()/2),pos[1]-pygame.font.SysFont("arial",size).render(text,True,black).get_height()/2)) #draw it
  else: #if side
    surface.blit(pygame.font.SysFont("arial",size).render(text,True,black),(pos[0],pos[1]-pygame.font.SysFont("arial",size).render(text,True,black).get_height()/2)) #draw it

def draw_text2(text,pos,size=(180,25)):
  x=pygame.font.SysFont("arial",22).render(text,True,black)
  if x.get_width()<=size[0]:
    draw_text(text,(pos[0],pos[1]+size[1]//2),22)
  else:
    screen.blit(pygame.transform.smoothscale(pygame.font.SysFont("arial",1000).render(text,True,black),size),pos)

def add_cookies(): #add cookies
  global cookies,total_cookies,t #global variables
  
  cookies+=cps*multiplier/decimal(1000) #add cookies
  total_cookies+=cps*multiplier/decimal(1000) #add total cookies
  
  t=timer(0.1,add_cookies) #t is a timer
  t.start() #start timer

def unblocker(): #unblocker
  while not finish: #while not finish
    for event in pygame.event.get(): #for every event
      if event.type==pygame.QUIT: #if quit pygame
        pygame.quit() #pygame quit
        t.cancel() #cancel timer
        th.cancel() #cancel timer
        if fps_track: #if tracking fps
          tm.cancel() #cancel timer
        sys.exit() #exit

def inputcommand(): #input
  global x #global x
  x=input("Command (\"quit\" to quit): ") #input

def save(autosave=False):
  ft.cancel()
  open("save data.txt","w").write(eval("chr(10).join([str(x) for x in [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9,bc10,bc11,bc12,bc13,bc14,bc15,bc16,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,bp10,bp11,bp12,bp13,bp14,bp15,bp16,cookies,cpc,total_cookies,multiplier,int(unlock_achievements[::-1],2),0 if round(ft.timeleft)<=0 else round(ft.timeleft),int(unlocked_upgrades[::-1],2),int(bought_upgrades[::-1],2)]])")) #save
  if not autosave:
    print("saved!") #print saved
  else:
    print("autosaved") #print autosaved
  ft.start()

def autosave():
  global th #global th
  
  save(True) #save

  th=timer(60,autosave) #th is a timer
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
  
  if x.lower() in ["quit","exit"]: #if x is exit or quit
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

def changesurface():
  #these are all text that either never changes of changes when a building is bought
  surface.fill(white)

  if rightpanel=="b":
    draw_text(f"Cursor, cost {numbershortener(bc1)}, have {b1}",(500,22),surface=surface)
    draw_text(f"Grandma, cost {numbershortener(bc2)}, have {b2}",(500,66),surface=surface)
    draw_text(f"Farm, cost {numbershortener(bc3)}, have {b3}",(500,109),surface=surface)
    draw_text(f"Mine, cost {numbershortener(bc4)}, have {b4}",(500,153),surface=surface)
    draw_text(f"Factory, cost {numbershortener(bc5)}, have {b5}",(500,197),surface=surface)
    draw_text(f"Bank, cost {numbershortener(bc6)}, have {b6}",(500,241),surface=surface)
    draw_text(f"Temple, cost {numbershortener(bc7)}, have {b7}",(500,284),surface=surface)
    draw_text(f"Wizard Tower, cost {numbershortener(bc8)}, have {b8}",(500,328),surface=surface)
    draw_text(f"Shipent, cost {numbershortener(bc9)}, have {b9}",(500,372),surface=surface)
    draw_text(f"Alchemy Lab, cost {numbershortener(bc10)}, have {b10}",(500,416),surface=surface)
    draw_text(f"Portal, cost {numbershortener(bc11)}, have {b11}",(500,459),surface=surface)
    draw_text(f"Time Machine, cost {numbershortener(bc12)}, have {b12}",(500,503),surface=surface)
    draw_text(f"Antimatter Condenser, cost {numbershortener(bc13)}, have {b13}",(500,547),surface=surface)
    draw_text(f"Prism, cost {numbershortener(bc14)}, have {b14}",(500,591),surface=surface)
    draw_text(f"Chancemaker, cost {numbershortener(bc15)}, have {b15}",(500,634),surface=surface)
    draw_text(f"Fractal Engine, cost {numbershortener(bc16)}, have {b16}",(500,678),surface=surface)
    draw_lines()

def draw():
  surface2.fill(white)

  pygame.draw.rect(surface2,black,pygame.Rect(199,0,2,700)) #draw filler 1
  pygame.draw.rect(surface2,black,pygame.Rect(499,0,2,700)) #draw filler 2
  pygame.draw.rect(surface2,black,pygame.Rect(300,500,100,100),1) #draw mute/unmute box

  draw_text("Achivevements",(100,50),15,False,surface2)
  pygame.draw.rect(surface2,black,pygame.Rect(0,99,200,2))

  draw_text("Upgrades",(100,150),15,False,surface2)
  pygame.draw.rect(surface2,black,pygame.Rect(0,199,200,2))

def track_fps(): #track fps
  global tm #global timer
  
  print(round(1/(t1-t2),1)) #print fps
  
  tm=timer(1,track_fps) #tm is a timer
  tm.start() #start timer

class timer: #class timer
  def __init__(self,interval,func): #def __init__
    self.interval=interval #interval
    self.timeleft=interval
    self.func=func #and function to call
    self.starttime=time.time()
    self.settimer()
  
  def settimer(self): #set the timer
    self.timer=threading.Timer(self.timeleft,self.func) #set the timer
  
  def start(self): #def start
    self.settimer()
    self.timer.start() #and start
    self.starttime=time.time()
  
  def cancel(self): #def cancel timer
    self.timer.cancel() #cancel
    self.timeleft=self.interval-time.time()+self.starttime

  def howlongleft(self):
    return self.interval-time.time()+self.starttime

def unlock_achievement(achievement_id,will_print=True):
  global unlock_achievements,achievements_to_unlock
  if will_print:
    print(f"Achievement: {achievements[[a for _,_,_,a,_ in achievements].index(achievement_id)][1]}")
  list_unlock_achievements=list(unlock_achievements)
  list_unlock_achievements[achievement_id-1]="1"
  unlock_achievements="".join(list_unlock_achievements)
  achievements_to_unlock[[a for _,_,_,a,_ in achievements_to_unlock].index(achievement_id):[a for _,_,_,a,_ in achievements_to_unlock].index(achievement_id)+1]=[]

def debug_game():
  try:
    for achievement_id in range(1,len(achievements)+1):
      unlock_achievement(achievement_id,False)
  except:
    pass

class golden:
  def __init__(self):
    self.pos=[random.randint(0,608),random.randint(0,608)]
    self.randout=random.choice(["Lucky","Frenzy"])
    self.timestart=time.time()
  
  def check(self):
    if gold_cookie_mask.overlap_area(pointer_mask,(pygame.mouse.get_pos()[0]-self.pos[0],pygame.mouse.get_pos()[1]-self.pos[1])):
      return True      
  
  def effect(self):
    if self.randout=="Lucky":
      global cookies,total_cookies
      cookies+=15+min(round(decimal(0.15)*cookies),900*cps)
      total_cookies+=15+min(round(decimal(0.15)*cookies),900*cps)
    if self.randout=="Frenzy":
      frenzy()
  
  def draw(self):
    screen.blit(gold_cookie,self.pos)
    if time.time()>=self.timestart+15:
      goldens.remove(self)

def frenzy():
  global multiplier,ft
  if ft.howlongleft()<=0:
    multiplier*=7
  else:
    del ft
  ft=timer(77,finishfrenzy)

def finishfrenzy():
  global multiplier
  multiplier=round(multiplier/7)

def spawn_golden():
  global goldens
  x=golden()
  goldens+=[x]
  gold_sound.play()

def golden_timer():
  spawn_golden()
  gt=timer(60,golden_timer)
  gt.start()

################################################################################
load_save_data() #load save data
add_cookies() #add cookies
th=timer(60,autosave) #the autosaving timer
th.start() #start timer
changesurface() #change the surface (actually make the surface)
draw()
t1=time.time() #t1 is the time
tm=timer(1,track_fps) #fps timer but don't start it
gt=timer(60,golden_timer)
gt.start()
while True: #game loop
  try:
    x=0
    for unlock_cond,name,_,achievement_id,_ in achievements_to_unlock:
      if eval(unlock_cond):
        print(f"Achivement: {name}")
        list_unlock_achievements=list(unlock_achievements)
        list_unlock_achievements[achievement_id-1]="1"
        unlock_achievements="".join(list_unlock_achievements)
        achievements_to_unlock[x:x+1]=[]
      x+=1
  except:
    pass

  try:
    x=0
    for _,unlock_cond,name,_,upgrade_id,_ in upgrades_to_unlock:
      if eval(unlock_cond):
        list_unlocked_upgrades=list(unlocked_upgrades)
        list_unlocked_upgrades[upgrade_id-1]="1"
        unlocked_upgrades="".join(list_unlocked_upgrades)
        upgrades_to_unlock[x:x+1]=[]
      x+=1
  except:
    pass
      
  screen.fill(white) #fill screen with white
  
  if cookies!=decimal("infinity"): #if not infinity cookies
    draw_text(f"{numbershortener(round(cookies))} cookies",(350,100),25,False) #draw text
  else: #if infinity cookies
    draw_text(f"{numbershortener(decimal('infinity'))} cookies",(350,100),25,False) #draw text
  
  draw_text(f"CpS: {numbershortener(cps)}",(350,150),18,False) #draw cps
  screen.blit(big_cookie,(225,225)) #draw big cookie
  screen.blit(surface,(0,0))
  screen.blit(surface2,(0,0))

  cps=sum([eval(f"b{bnum}*bp{bnum}") for bnum in range(1,17)])*multiplier/100
  
  if rightpanel=="a":
    for _,name,icon,achievement_id,desc in achievements:
      if unlock_achievements[achievement_id-1]=="1":
        screen.blit(icon,(500+25*((achievement_id-1)%8),25*((achievement_id-1)//8)))
        if 500+25*((achievement_id-1)%8)<=pygame.mouse.get_pos()[0]<=525+25*((achievement_id-1)%8) and 25*((achievement_id-1)//8)<=pygame.mouse.get_pos()[1]<=25+25*((achievement_id-1)//8):
          pygame.draw.rect(screen,(0,0,0),pygame.Rect(320,25*((achievement_id-1)//8),180,50),1)
          pygame.draw.rect(screen,(128,128,128),pygame.Rect(321,25*((achievement_id-1)//8)+1,178,48))
          draw_text2(f"{name}:",(320,25*((achievement_id-1)//8)))
          draw_text2(f"{desc}",(320,25*((achievement_id-1)//8+1)))
      else:
        screen.blit(question,(500+25*((achievement_id-1)%8),25*((achievement_id-1)//8)))
        if 500+25*((achievement_id-1)%8)<=pygame.mouse.get_pos()[0]<=525+25*((achievement_id-1)%8) and 25*((achievement_id-1)//8)<=pygame.mouse.get_pos()[1]<=25+25*((achievement_id-1)//8):
          pygame.draw.rect(screen,(0,0,0),pygame.Rect(320,25*((achievement_id-1)//8),180,50),1)
          pygame.draw.rect(screen,(128,128,128),pygame.Rect(321,25*((achievement_id-1)//8)+1,178,48))
          draw_text2("???:",(320,25*((achievement_id-1)//8)))
          draw_text2("???",(320,25*((achievement_id-1)//8+1)))

  if rightpanel=="u":
    for effect,name,icon,upgrade_id,desc in [(a,b,c,d,e) for a,_,b,c,d,e in upgrades if unlocked_upgrades[d-1]=="1"]:
      screen.blit(icon,(500+25*((upgrade_id-1)%8),25*((upgrade_id-1)//8)))
      if 500+25*((upgrade_id-1)%8)<=pygame.mouse.get_pos()[0]<=525+25*((upgrade_id-1)%8) and 25*((upgrade_id-1)//8)<=pygame.mouse.get_pos()[1]<=25+25*((upgrade_id-1)//8):
        if pygame.mouse.get_pressed()!=(0,0,0): #if you click
          exec(effect)
          upgrades[[d for _,_,_,_,d,_ in upgrades].index(upgrade_id):[d for _,_,_,_,d,_ in upgrades].index(upgrade_id)+1]=[]
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(320,25*((upgrade_id-1)//8),180,50),1)
        pygame.draw.rect(screen,(128,128,128),pygame.Rect(321,25*((upgrade_id-1)//8)+1,178,48))
        draw_text2(f"{name}:",(320,25*((upgrade_id-1)//8)))
        draw_text2(f"{desc}",(320,25*((upgrade_id-1)//8+1)))
        
  
  draw_text("Unmute" if mute else "Mute",(350,550),15,False) #draw mute/unmute text

  [gc.draw() for gc in goldens]
  
  for event in pygame.event.get(): #for every event
    if event.type==pygame.QUIT: #if quit pygame
      pygame.quit() #pygame quit
      t.cancel() #cancel timer
      th.cancel() #cancel timer
      if fps_track: #if track fps
        tm.cancel() #cancel timer
      sys.exit() #exit
    if event.type==pygame.MOUSEBUTTONDOWN: #if you click
      if event.button in [1,2,3]: #if you click and not scroll
        mouse_pos=pygame.mouse.get_pos() #set mouse_pos to mouse position
        if not sum([int(bool(gc.check())) for gc in goldens]):
          if big_cookie_mask.overlap_area(pointer_mask,(mouse_pos[0]-225,mouse_pos[1]-225)): #if you click the big cookie
            cookies+=cpc #add cpc to cookies
            total_cookies+=cpc #add cpc to total cookies
            
            if not mute: #if not muted
              threading.Thread(target=play_random_click).start() #play random click sound
          
          if mouse_pos[0]>=500 and rightpanel=="b": #if you buy
            for _ in range(1,17): #for everything in the range
              buy(_) #see if you bought it
            changesurface()

          if mouse_pos[0]<=200 and mouse_pos[1]<=100:
            if rightpanel!="a":
              rightpanel="a"
            else:
              rightpanel="b"
            changesurface()

          if mouse_pos[0]<=200 and 100<=mouse_pos[1]<=200:
            if rightpanel!="u":
              rightpanel="u"
            else:
              rightpanel="b"
            changesurface()
          
          if 300<=mouse_pos[0]<=400 and 500<=mouse_pos[1]<=600: #if mute/unmute
            mute=not mute #mute/unmute

        for gc in goldens[::-1]:
          if gc.check():
            gc.effect()
            goldens.remove(gc)
            break
    
    if event.type==pygame.KEYDOWN: #if key down
      if event.key==pygame.K_s and (event.mod & pygame.KMOD_CTRL): #if you press ctrl-s
        save() #save
      if event.key==pygame.K_j and (event.mod & pygame.KMOD_CTRL) and (event.mod & pygame.KMOD_SHIFT):
        loop=True #loop is true
        t.cancel() #cancel timer
        th.cancel() #cancel timer
        if fps_track: #if tracking fps
          tm.cancel() #cancel timer
        ft.cancel()
        while loop: #while loop
          finish=False #finish is false
          threading.Thread(target=command).start() #start command line
          unblocker() #unblock
        t.start() #restart timer
        th.start() #restart timer
        if fps_track: #if tracking fps
          tm.start() #restart timer
        ft.start()
  
  t1,t2=time.time(),t1 #change t1 and t2
  
  pygame.display.update() #update pygame
