import pygame
import sys
import math

pygame.init()

# Dimensiones de la ventana y de las celdas
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 32
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Editor de Tiles")

# Función para obtener la posición de la celda bajo el mouse
def get_cell_under_mouse():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    cell_x, cell_y = math.floor(mouse_x / CELL_SIZE), math.floor(mouse_y / CELL_SIZE)
    return cell_x, cell_y

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener la celda bajo el mouse
    cell_x, cell_y = get_cell_under_mouse()


    # Dibujar la celda en la que está el mouse
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (math.floor(pygame.mouse.get_pos()[0] / 32) * 32 , 0, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

pygame.quit()
sys.exit()
