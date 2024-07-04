'''
Game Graphics
'''
import pygame
import settings
def display_score(score):
    '''
    Display the player's score on the screen
    '''
    value = settings.score_font.render("Score: " + str(score), True, settings.white)
    settings.window.blit(value, [10, 10])
def draw_snake(snake_size, snake_list):
    '''
    Draw the snake on the game window
    '''
    for x in snake_list:
        pygame.draw.rect(settings.window, settings.green, [x[0], x[1], snake_size, snake_size])