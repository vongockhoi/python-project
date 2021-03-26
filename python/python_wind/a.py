import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000,1000))

GREY = (150,150,150)
WHITE = (255,255,255)

running = True
r  = 196

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}'.format((mins*60)+secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')
countdown(120)
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

	# screen.blit(text_1, (100,50))
	# screen.blit(text_2, (100,200))
	# screen.blit(text_3, (200,50))
	# screen.blit(text_4, (200,200))
	# screen.blit(text_5, (300,50))
	# screen.blit(text_6, (300,150))

	pygame.draw.circle(screen, WHITE, (387, 454), 200, 1)
	pygame.draw.circle(screen, WHITE, (387, 454),0)
	pygame.draw.line(screen, WHITE, (387, 258), (387, 454),2)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button ==1:
				print("xxx")
	pygame.display.flip()
pygame.quit()