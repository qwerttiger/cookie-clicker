import sys,threading,os,random,time; os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"; import pygame; from numbershortener import numbershortener as ns; from decimal import Decimal as decimal
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Cookie Clicker")
big_cookie=pygame.image.load("pictures/cookie.png")
white=(255,255,255)
black=(0,0,0)
big_cookie_mask=pygame.mask.from_surface(big_cookie)
pointer_mask=pygame.mask.Mask((1,1),True)
click1=pygame.mixer.Sound("sounds/click1.wav")
click2=pygame.mixer.Sound("sounds/click2.wav")
click3=pygame.mixer.Sound("sounds/click3.wav")
click4=pygame.mixer.Sound("sounds/click4.wav")
click5=pygame.mixer.Sound("sounds/click5.wav")
click6=pygame.mixer.Sound("sounds/click6.wav")
click7=pygame.mixer.Sound("sounds/click7.wav")
buy1=pygame.mixer.Sound("sounds/buy1.wav")
buy2=pygame.mixer.Sound("sounds/buy2.wav")
buy3=pygame.mixer.Sound("sounds/buy3.wav")
buy4=pygame.mixer.Sound("sounds/buy4.wav")
x=None
def buy(num):
  if num*41-41<=mouse_pos[1]<num*41 and cookies>=eval(f"bc{num}"):
    exec(f"cookies-=bc{num}",globals())
    exec(f"bc{num}=round(bc{num}*1.15)",globals())
    exec(f"b{num}+=1",globals())
    exec(f"cps+=decimal(str(bp{num}))",globals())
    play_random_buy()
def clear_save():
  file=open("save data.txt","w")
  file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n15\n100\n1100\n12000\n130000\n1400000\n20000000\n330000000\n5100000000\n75000000000\n1000000000000\n14000000000000\n170000000000000\n2100000000000000\n26000000000000000\n310000000000000000\n71000000000000000000\n0.1\n1\n8\n47\n260\n1400\n7800\n44000\n260000\n1600000\n10000000\n65000000\n430000000\n2900000000\n21000000000\n150000000000\n1100000000000\n0\n0")
  file.close()
def load_save_data():
  global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9,bc10,bc11,bc12,bc13,bc14,bc15,bc16,bc17,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,bp10,bp11,bp12,bp13,bp14,bp15,bp16,bp17,cookies,cps
  try:
    file=open("save data.txt").read().split()
  except:
    file=open("save data.txt","w")
    file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n15\n100\n1100\n12000\n130000\n1400000\n20000000\n330000000\n5100000000\n75000000000\n1000000000000\n14000000000000\n170000000000000\n2100000000000000\n26000000000000000\n310000000000000000\n71000000000000000000\n0.1\n1\n8\n47\n260\n1400\n7800\n44000\n260000\n1600000\n10000000\n65000000\n430000000\n2900000000\n21000000000\n150000000000\n1100000000000\n0\n0")
    file.close()
    file=open("save data.txt").read().split()
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
  bp1=float(file[34])
  bp2=float(file[35])
  bp3=float(file[36])
  bp4=float(file[37])
  bp5=float(file[38])
  bp6=float(file[39])
  bp7=float(file[40])
  bp8=float(file[41])
  bp9=float(file[42])
  bp10=float(file[43])
  bp11=float(file[44])
  bp12=float(file[45])
  bp13=float(file[46])
  bp14=float(file[47])
  bp15=float(file[48])
  bp16=float(file[49])
  bp17=float(file[50])
  cookies=decimal(file[51])
  cps=decimal(file[52])
def play_random_click():
  a=random.randint(1,7)
  exec(f"click{a}.play()")
  a+=random.randint(1,5)
  a=a%7
  a=7 if a==0 else a
  time.sleep(0.1)
  exec(f"click{a}.play()")
def play_random_buy():
  exec(f"buy{random.randint(1,4)}.play()")
def draw_lines():
  for x in range(1,17):
    pygame.draw.rect(screen,black,pygame.Rect(500,41*x-1,200,2))
def draw_text(text,pos,size=8,side=True):
  if not side:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0]-round(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_width()/2),pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2))
  else:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0],pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2))
def add_cookies():
  global cookies,t
  cookies+=decimal(str(cps))/10
  t=threading.Timer(0.1,add_cookies)
  t.start()
def unblocker():
  while not finish:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        t.cancel()
        sys.exit()
def inputcommand():
  global x
  x=input("Command (\"quit\" to quit): ").lower()
def command():
  global loop,x,finish
  finish=False
  del x
  threading.Thread(target=inputcommand).start()
  ok=False
  while not ok:
    try:
      x
    except:
      pass
    else:
      ok=True
  if x in ["quit","exit"]:
    loop=False
  else:
    try:
      print("Output:",eval(x,globals())) if eval(x,globals())!=None else exec(x,globals())
    except:
      try:
        exec(x,globals())
      except Exception as e:
        print(f"Error: {e}")
  finish=True
load_save_data()
add_cookies()
while True:
  screen.fill(white)
  if cookies!=decimal("infinity"):
    draw_text(f"{ns(round(cookies))} cookies",(350,100),25,False)
  else:
    draw_text(f"{ns(decimal('infinity'))} cookies",(350,100),25,False)
  draw_text(f"CpS: {ns(cps)}",(350,150),18,False)
  draw_text(f"Cursor, cost {ns(bc1)}, have {b1}",(500,20))
  draw_text(f"Grandma, cost {ns(bc2)}, have {b2}",(500,61))
  draw_text(f"Farm, cost {ns(bc3)}, have {b3}",(500,102))
  draw_text(f"Mine, cost {ns(bc4)}, have {b4}",(500,143))
  draw_text(f"Factory, cost {ns(bc5)}, have {b5}",(500,184))
  draw_text(f"Bank, cost {ns(bc6)}, have {b6}",(500,225))
  draw_text(f"Temple, cost {ns(bc7)}, have {b7}",(500,266))
  draw_text(f"Wizard Tower, cost {ns(bc8)}, have {b8}",(500,307))
  draw_text(f"Shipent, cost {ns(bc9)}, have {b9}",(500,348))
  draw_text(f"Alchemy Lab, cost {ns(bc10)}, have {b10}",(500,389))
  draw_text(f"Portal, cost {ns(bc11)}, have {b11}",(500,430))
  draw_text(f"Time Machine, cost {ns(bc12)}, have {b12}",(500,471))
  draw_text(f"Antimatter Condenser, cost {ns(bc13)}, have {b13}",(500,512))
  draw_text(f"Prism, cost {ns(bc14)}, have {b14}",(500,553))
  draw_text(f"Chancemaker, cost {ns(bc15)}, have {b15}",(500,594))
  draw_text(f"Fractal Engine, cost {ns(bc16)}, have {b16}",(500,635))
  draw_text(f"Python Console, cost {ns(bc17)}, have {b17}",(500,676))
  draw_text("Console",(350,550),25,False)
  screen.blit(big_cookie,(225,225))
  pygame.draw.rect(screen,black,pygame.Rect(199,0,2,700))
  pygame.draw.rect(screen,black,pygame.Rect(499,0,2,700))
  pygame.draw.rect(screen,black,pygame.Rect(300,500,100,100),1)
  draw_lines()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      t.cancel()
      sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      if event.button in [1,2,3]:
        mouse_pos=pygame.mouse.get_pos()
        if big_cookie_mask.overlap_area(pointer_mask,(mouse_pos[0]-225,mouse_pos[1]-225)):
          cookies+=1
          threading.Thread(target=play_random_click).start()
        if mouse_pos[0]>=500:
          for _ in range(1,18):
            buy(_)
        if 300<=mouse_pos[0]<=400 and 500<=mouse_pos[1]<=600:
          loop=True
          while loop:
            finish=False
            threading.Thread(target=command).start()
            unblocker()
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_s and (event.mod & pygame.KMOD_CTRL):
        open("save data.txt","w").write(eval("chr(10).join([str(x) for x in [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9,bc10,bc11,bc12,bc13,bc14,bc15,bc16,bc17,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,bp10,bp11,bp12,bp13,bp14,bp15,bp16,bp17,cookies,cps]])"))

  pygame.display.update()
