import sys,threading,os,random
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"
import pygame; from numbershortener import numbershortener as ns; from decimal import Decimal as decimal
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Cookie Clicker")
big_cookie=pygame.image.load("pictures/cookie.png")
white=(255,255,255)
black=(0,0,0)
big_cookie_mask=pygame.mask.from_surface(big_cookie)
pointer_mask=pygame.mask.Mask((1,1),True)
cookies=0
cps=0
click1=pygame.mixer.Sound("sounds/click1.wav")
click2=pygame.mixer.Sound("sounds/click2.wav")
click3=pygame.mixer.Sound("sounds/click3.wav")
click4=pygame.mixer.Sound("sounds/click4.wav")
click5=pygame.mixer.Sound("sounds/click5.wav")
click6=pygame.mixer.Sound("sounds/click6.wav")
click7=pygame.mixer.Sound("sounds/click7.wav")
def load_save_data():
  global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9,bc10,bc11,bc12,bc13,bc14,bc15,bc16,bc17
  try:
    file=open("save data.txt").read().split()
  except:
    file=open("save data.txt","w")
    file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n15\n100\n1100\n12000\n130000\n1400000\n20000000\n330000000\n5100000000\n75000000000\n1000000000000\n14000000000000\n170000000000000\n2100000000000000\n26000000000000000\n310000000000000000\n71000000000000000000\n0.1\n1\n8\n47\n260\n1400\n7800\n44000\n260000\n1600000\n10000000\n65000000\n430000000\n2900000000\n21000000000\n150000000000\n1100000000000")
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
def play_random_sound():
  exec(f"click{random.randint(1,7)}.play()")
def draw_lines():
  for x in range(1,17):
    pygame.draw.rect(screen,black,pygame.Rect(500,41*x-1,200,2))
def draw_text(text,pos,side=True,size=10):
  if not side:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0]-round(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_width()/2),pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2))
  else:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0],pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2))
def add_cookies():
  global cookies,t
  cookies+=decimal(str(cps))/10
  t=threading.Timer(0.1,add_cookies)
  t.start()
add_cookies()
load_save_data()
while True:
  screen.fill(white)
  draw_text(f"{round(cookies)} cookies",(350,100),False,30)
  draw_text(f"CpS: {cps}",(350,150),False,30)
  draw_text(f"Cursor, cost {ns(bc1)}, have {ns(b1)}",(500,20))
  draw_text(f"Grandma, cost {ns(bc2)}, have {ns(b2)}",(500,61))
  draw_text(f"Farm, cost {ns(bc3)}, have {ns(b3)}",(500,102))
  draw_text(f"Mine, cost {ns(bc4)}, have {ns(b4)}",(500,143))
  draw_text(f"Factory, cost {ns(bc5)}, have {ns(b5)}",(500,184))
  draw_text(f"Bank, cost {ns(bc6)}, have {ns(b6)}",(500,225))
  draw_text(f"Temple, cost {ns(bc7)}, have {ns(b7)}",(500,266))
  draw_text(f"Wizard Tower, cost {ns(bc8)}, have {ns(b8)}",(500,307))
  draw_text(f"Shipent, cost {ns(bc9)}, have {ns(b9)}",(500,348))
  draw_text(f"Alchemy Lab, cost {ns(bc10)}, have {ns(b10)}",(500,389))
  draw_text(f"Portal, cost {ns(bc11)}, have {ns(b11)}",(500,430))
  draw_text(f"Time Machine, cost {ns(bc12)}, have {ns(b12)}",(500,471))
  draw_text(f"Antimatter Condenser, cost {ns(bc13)}, have {ns(b13)}",(500,512))
  draw_text(f"Prism, cost {ns(bc14)}, have {ns(b14)}",(500,553))
  draw_text(f"Chancemaker, cost {ns(bc15)}, have {ns(b15)}",(500,594))
  draw_text(f"Fractal Engine, cost {ns(bc16)}, have {ns(b16)}",(500,635))
  draw_text(f"Javascript Console, cost {ns(bc17)}, have {ns(b17)}",(500,676))
  screen.blit(big_cookie,(225,225))
  pygame.draw.rect(screen,black,pygame.Rect(199,0,2,700))
  pygame.draw.rect(screen,black,pygame.Rect(499,0,2,700))
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
          play_random_sound()
  pygame.display.update()
