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
font=pygame.font.SysFont("arial",30)
def drawlines():
  for x in range(1,17):
    pygame.draw.rect(screen,black,pygame.Rect(500,41*x-1,200,2))
while True:
  screen.fill(white)
  cookies_text=font.render(f"{cookies} cookies",True,black)
  screen.blit(cookies_text,(350-cookies_text.get_width()/2,100-cookies_text.get_height()/2))
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
