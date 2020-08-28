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
def drawtext(text,pos,centre_or_topleft=True,size=30):
  if not centre_or_topleft:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0]-round(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_width()/2),pos[1]-pygame.font.SysFont("arial",size).render(text,True,(0,0,0)).get_height()/2))
  else:
    screen.blit(pygame.font.SysFont("arial",size).render(text,True,(0,0,0)),(pos[0],pos[1]))
while True:
  screen.fill(white)
  drawtext(f"{cookies} cookies",(350,100),False)
  drawtext("Cursor",(500,41))
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
