# Description:
# Created by Emilia on 2025-02-27

import pygame
import sys

pygame.init()





#import tkinter as tk

#
# def option_selected(value):
#     print(f"Selected: {value}")

#
# root = tk.Tk()
# root.title("Dropdown Example")
#
# options = ["Option 1", "Option 2", "Option 3"]
# selected = tk.StringVar(value=options[0])
#
# dropdown = tk.OptionMenu(root, selected, *options, command=option_selected)
# dropdown.pack(pady=20)
#
# root.mainloop()














# Screen settings
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("kitty")

# Define colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Define button rectangles
button1 = pygame.Rect(100, 200, 150, 50)
button2 = pygame.Rect(390, 200, 150, 50)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse clicks on buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                if button1.collidepoint(event.pos):
                    print("Button 1 clicked!")
                if button2.collidepoint(event.pos):
                    print("Button 2 clicked!")

        screen.fill(WHITE)

        # Draw buttons (filled with gray)
        pygame.draw.rect(screen, GRAY, button1)
        pygame.draw.rect(screen, GRAY, button2)

        # Optional: add text labels to the buttons
        font = pygame.font.SysFont(None, 36)
        text1 = font.render("Button 1", True, BLACK)
        text2 = font.render("Button 2", True, BLACK)
        # Center the text on each button
        screen.blit(text1, (button1.x + (button1.width - text1.get_width()) // 2,
                            button1.y + (button1.height - text1.get_height()) // 2))
        screen.blit(text2, (button2.x + (button2.width - text2.get_width()) // 2,
                            button2.y + (button2.height - text2.get_height()) // 2))

        # Update the display
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()

