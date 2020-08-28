import sys,threading,os,random; os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"; import pygame
from decimal import Decimal as decimal
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
while True:
  screen.fill(white)
  draw_text(f"{round(cookies)} cookies",(350,100),False,30)
  draw_text(f"CpS: {cps}",(350,150),False,30)
  draw_text(f"Cursor, cost (), have ()",(500,20))
  draw_text(f"Grandma, cost (), have ()",(500,61))
  draw_text(f"Farm, cost (), have ()",(500,102))
  draw_text(f"Mine, cost (), have ()",(500,143))
  draw_text(f"Factory, cost (), have ()",(500,184))
  draw_text(f"Bank, cost (), have ()",(500,225))
  draw_text(f"Temple, cost (), have ()",(500,266))
  draw_text(f"Wizard Tower, cost (), have ()",(500,307))
  draw_text(f"Shipent, cost (), have ()",(500,348))
  draw_text(f"Alchemy Lab, cost (), have ()",(500,389))
  draw_text(f"Portal, cost (), have ()",(500,430))
  draw_text(f"Time Machine, cost (), have ()",(500,471))
  draw_text(f"Antimatter Condenser, cost (), have ()",(500,512))
  draw_text(f"Prism, cost (), have ()",(500,553))
  draw_text(f"Chancemaker, cost (), have ()",(500,594))
  draw_text(f"Fractal Engine, cost (), have ()",(500,635))
  draw_text(f"Javascript Console, cost (), have ()",(500,676))
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
