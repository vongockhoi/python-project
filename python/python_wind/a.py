import pygame
import time
import math
pygame.init()

screen = pygame.display.set_mode((1000,1000))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)

running = True
r  = 196

# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}'.format((mins*60)+secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t -= 1
#     print('Goodbye!\n\n\n\n\n')
# timed = countdown(3)

# class tim_x:
# 	def __init__(selp,toa_do_x,r,ampha):
# 		selp.x=toa_do_x+(r*math.sin(ampha))
# 		print(selp.x)
# class tim_y:
# 	def __init__(selp,toa_do_y,r,ampha):
# 		selp.y=toa_do_y-(r*math.cos(ampha))
# 		print(selp.y)
# timex = 1 
# am_pha = 6*timex*(math.pi/180)
# p1 = tim_x(387,r,am_pha)
# p2 = tim_y(454,r,am_pha)

font = pygame.font.SysFont('scans',50)
text_1 = font.render('+', True, BLACK)
clock = pygame.time.Clock()
total_secs = 0
start  = False
thoigian = 0
while running:
	screen.fill(GREY)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# print(mouse_x,mouse_y)

	pygame.draw.rect(screen, WHITE, (100,50,50,50))
	pygame.draw.rect(screen, WHITE, (100,200,50,50))
	pygame.draw.rect(screen, WHITE, (200,50,50,50))
	pygame.draw.rect(screen, WHITE, (200,200,50,50))
	pygame.draw.rect(screen, WHITE, (300,50,150,50))
	pygame.draw.rect(screen, WHITE, (300,50,150,50))
	pygame.draw.rect(screen, WHITE, (300,150,150,50))

	screen.blit(text_1, (100,50))
	# screen.blit(text_3, (200,50))
	# screen.blit(text_4, (200,200))
	# screen.blit(text_5, (300,50))
	# screen.blit(text_6, (300,150))

	pygame.draw.circle(screen, WHITE, (387,454), 200, 1)
	pygame.draw.line(screen, WHITE, (387,454), (387,266),2)

	

	x_sec = 387+190* math.sin(6*thoigian*math.pi/180)
	y_sec = 454-190* math.cos(6*thoigian*math.pi/180)
	pygame.draw.line(screen, WHITE, (387, 454), (int(x_sec),int(y_sec)),2)
	thoigian +=1
	pygame.display.update()
	clock.tick(1)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	if event.button ==1:
		# 		print("xxx")
	pygame.display.flip()
pygame.quit()