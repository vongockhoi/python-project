import pygame
pygame.init()

screen = pygame.display.set_mode((1000,1000))

GREY = (150,150,150)
WHITE = (255,255,255)

running = True
while running:
	screen.fill(GREY)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	print(mouse_x)

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
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button ==1:
				print("xxx")
	pygame.display.flip()
pygame.quit()