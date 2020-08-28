import pygame,sys
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Cookie Clicker")
big_cookie=pygame.image.load("pictures/cookie.png")
white=(255,255,255)
black=(0,0,0)
big_cookie_mask=pygame.mask.from_surface(big_cookie)
pointer_mask=pygame.mask.Mask((1,1),True)
cookies=0
def drawlines():
  for x in range(1,17):
    pygame.draw.rect(screen,black,pygame.Rect(500,41*x-1,200,2))
def drawtext(text,pos,side=True,size=30):
  if not side:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0]-round(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_width()/2),pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2))
  else:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0],pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2))
while True:
  screen.fill(white)
  drawtext(f"{cookies} cookies",(350,100),False)
  drawtext(f"Cursor, cost (), have ()",(500,20),size=10)
  drawtext(f"Grandma, cost (), have ()",(500,61),size=10)
  drawtext(f"Farm, cost (), have ()",(500,102),size=10)
  drawtext(f"Mine, cost (), have ()",(500,143),size=10)
  drawtext(f"Factory, cost (), have ()",(500,184),size=10)
  drawtext(f"Bank, cost (), have ()",(500,225),size=10)
  drawtext(f"Temple, cost (), have ()",(500,266),size=10)
  drawtext(f"Wizard Tower, cost (), have ()",(500,307),size=10)
  drawtext(f"Shipent, cost (), have ()",(500,348),size=10)
  drawtext(f"Alchemy Lab, cost (), have ()",(500,389),size=10)
  drawtext(f"Portal, cost (), have ()",(500,430),size=10)
  drawtext(f"Time Machine, cost (), have ()",(500,471),size=10)
  drawtext(f"Antimatter Condenser, cost (), have ()",(500,512),size=10)
  drawtext(f"Prism, cost (), have ()",(500,553),size=10)
  drawtext(f"Chancemaker, cost (), have ()",(500,594),size=10)
  drawtext(f"Fractal Engine, cost (), have ()",(500,635),size=10)
  drawtext(f"Javascript Console, cost (), have ()",(500,676),size=10)
  
  screen.blit(big_cookie,(225,225))
  pygame.draw.rect(screen,black,pygame.Rect(199,0,2,700))
  pygame.draw.rect(screen,black,pygame.Rect(499,0,2,700))
  drawlines()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      if event.button in [1,2,3]:
        mouse_pos=pygame.mouse.get_pos()
        if big_cookie_mask.overlap_area(pointer_mask,(mouse_pos[0]-225,mouse_pos[1]-225)):
          cookies+=1
  pygame.display.update()
