import pygame,sys
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Cookie Clicker")
big_cookie=pygame.image.load("pictures/cookie.png")
white=(255,255,255)
big_cookie_mask=pygame.mask.from_surface(big_cookie)
pointer_mask=pygame.mask.Mask((1,1),True)
screen.fill(white)
screen.blit(big_cookie,(75,225))
cookies=0
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      mouse_pos=pygame.mouse.get_pos()
      if big_cookie_mask.overlap_area(pointer_mask,(mouse_pos[0]-75,mouse_pos[1]-225)):
        cookies+=1
        print(cookies)
  pygame.display.update()
