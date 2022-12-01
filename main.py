import pygame
from src.menu import *

def main():
    pygame.init()
    menu = Menu()
    menu.start()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()








