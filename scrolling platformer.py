import pygame,random
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Scrolling platformer")
level=1
player=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/player.png")
levelpic=None
groundmask=None
lavamask=None
jumpymask=None
fastleftmask=None
fastrightmask=None
watermask=None
shrinkmask=None
normalmask=None
winmask=None
areamask=None
screenposx=0
screenposy=2800
screen.fill((255,255,255))
def loadlevel():
  global levelpic,groundmask,lavamask,jumpymask,fastleftmask,fastrightmask,watermask,shrinkmask,normalmask,winmask,areamask
  levelpic=pygame.image.load(f"C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/levels/{level}.png")
  groundmask=pygame.mask.from_threshold(levelpic,(0,0,0))
  lavamask=pygame.mask.from_threshold(levelpic,(255,0,0))
  jumpymask=pygame.mask.from_threshold(levelpic,(255,255,100))
  fastleftmask=pygame.mask.from_threshold(levelpic,(0,255,0))
  fastrightmask=pygame.mask.from_threshold(levelpic,(255,0,255))
  watermask=pygame.mask.from_threshold(levelpic,(0,255,255))
  shrinkmask=pygame.mask.from_threshold(levelpic,(0,100,0))
  normalmask=pygame.mask.from_threshold(levelpic,(0,0,100))
  winmask=pygame.mask.from_threshold(levelpic,(255,255,0))
  areamask=pygame.mask.from_threshold(levelpic,(255,100,255))
while True:
  loadlevel()
  while True:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.exit()
    screen.blit(levelpic,(-screenposx,-screenposy))
    pygame.display.flip()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      screenposy-=10
    if keys[pygame.K_LEFT]:
      screenposx-=10
    if keys[pygame.K_RIGHT]:
      screenposx+=10
