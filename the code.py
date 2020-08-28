import sys,threading,os; os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"; import pygame
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
def drawlines():
  for x in range(1,17):
    pygame.draw.rect(screen,black,pygame.Rect(500,41*x-1,200,2))
def drawtext(text,pos,side=True,size=10):
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
  drawtext(f"{round(cookies)} cookies",(350,100),False,30)
  drawtext(f"CpS: {cps}",(350,150),False,30)
  drawtext(f"Cursor, cost (), have ()",(500,20))
  drawtext(f"Grandma, cost (), have ()",(500,61))
  drawtext(f"Farm, cost (), have ()",(500,102))
  drawtext(f"Mine, cost (), have ()",(500,143))
  drawtext(f"Factory, cost (), have ()",(500,184))
  drawtext(f"Bank, cost (), have ()",(500,225))
  drawtext(f"Temple, cost (), have ()",(500,266))
  drawtext(f"Wizard Tower, cost (), have ()",(500,307))
  drawtext(f"Shipent, cost (), have ()",(500,348))
  drawtext(f"Alchemy Lab, cost (), have ()",(500,389))
  drawtext(f"Portal, cost (), have ()",(500,430))
  drawtext(f"Time Machine, cost (), have ()",(500,471))
  drawtext(f"Antimatter Condenser, cost (), have ()",(500,512))
  drawtext(f"Prism, cost (), have ()",(500,553))
  drawtext(f"Chancemaker, cost (), have ()",(500,594))
  drawtext(f"Fractal Engine, cost (), have ()",(500,635))
  drawtext(f"Javascript Console, cost (), have ()",(500,676))
  screen.blit(big_cookie,(225,225))
  pygame.draw.rect(screen,black,pygame.Rect(199,0,2,700))
  pygame.draw.rect(screen,black,pygame.Rect(499,0,2,700))
  drawlines()
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
  pygame.display.update()
