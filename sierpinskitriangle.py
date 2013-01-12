import pygame


pygame.init()

black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((600,600))
screen.fill(black)



def midpoint((x0,y0),(x1,y1)):
    return(((x0+x1)/2,(y0+y1)/2))

  
a = [[(300,190), (450,450), (150,450)]]

pygame.draw.polygon(screen, white ,(a[0][0], a[0][1], a[0][2]), 1)
j = 0
i=0
length = len(a)
for i in range(729):
    a1 = a[i][0]
    a2 = a[i][1]
    a3 = a[i][2]
    md1 = midpoint(a1, a2)
    md2 = midpoint(a2, a3)
    md3 = midpoint(a3, a1)
    a.append([a1,md1,md3])
    a.append([md1,a2,md2])
    a.append([md2,a3,md3])

for element in a:
      elem = element
      pygame.draw.polygon(screen,white,(elem[0],elem[1],elem[2]),1)
      

pygame.display.update()
raw_input('Press any key to stop')


