import pygame
import os

# Define some colors
WHITE = (255, 255, 255)

YELLOW = [
  "emoji/yellow/mid-left.png",
  "emoji/yellow/mid-right.png",
  "emoji/yellow/down.png",
  "emoji/yellow/up.png",
  "emoji/yellow/base.png",
]
GREEN = [
  "emoji/green/left.png",
  "emoji/green/right.png",
  "emoji/green/down.png",
  "emoji/green/up.png",
  "emoji/green/base.png",
]
RED = [
  "emoji/red/left.png",
  "emoji/red/right.png",
  "emoji/red/down.png",
  "emoji/red/up.png",
  "emoji/red/base.png",
]
BLUE = [
  "emoji/blue/left.png",
  "emoji/blue/right.png",
  "emoji/blue/down.png",
  "emoji/blue/up.png",
  "emoji/blue/base.png",
]


pygame.init()
# Add Game Icon and Title
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption("Ostumoji")

pygame.joystick.init()
joysticks = []

# for all the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print("Detected joystick '",joysticks[-1].get_name(),"'")

BUTTONS_GREEN = 0
BUTTONS_RED = 1
BUTTONS_BLUE = 2
BUTTONS_YELLOW = 3
JOYSTICK_POSTION = "NONE"

# Set the width and height of the screen [width, height]
screenSize = (240,155)
bigScreenSize = (240*3,155*3)


# Loop until the user clicks the close button.
isRunning = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Current Emoji
CURRENT_COLOR = YELLOW
CURRENT_EMOJI = YELLOW[0]
CURRENT_SIZE = screenSize


# -------- Main Program Loop -----------
while isRunning:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            #print("Keydown,", event.key)
            if event.key == 27:
              pygame.quit()
        elif event.type == pygame.JOYAXISMOTION:
            lr = joysticks[event.joy].get_axis(0)
            ud = joysticks[event.joy].get_axis(1)
            if round(lr) < 0: #left
              JOYSTICK_POSTION = "LEFT"
              CURRENT_EMOJI= CURRENT_COLOR[0]
            if round(lr) > 0 : #right
              JOYSTICK_POSTION = "RIGHT"
              CURRENT_EMOJI= CURRENT_COLOR[1]
            if round(ud) > 0: #down
              JOYSTICK_POSTION = "DOWN"
              CURRENT_EMOJI= CURRENT_COLOR[2]
            if round(ud) < 0: #up
              JOYSTICK_POSTION = "UP"
              CURRENT_EMOJI= CURRENT_COLOR[3]
        elif event.type == pygame.JOYBUTTONDOWN:
            #print("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down.")
            if event.button == BUTTONS_YELLOW:
              CURRENT_COLOR= YELLOW
              CURRENT_EMOJI = CURRENT_COLOR[4]
            if event.button == BUTTONS_BLUE:
              CURRENT_COLOR= BLUE
              CURRENT_EMOJI = CURRENT_COLOR[4]
            if event.button == BUTTONS_GREEN:
              CURRENT_COLOR= GREEN
              CURRENT_EMOJI = CURRENT_COLOR[4]
            if event.button == BUTTONS_RED:
              CURRENT_COLOR= RED
              CURRENT_EMOJI = CURRENT_COLOR[4]
            if event.button == 9:
              # Controller Stick Press
              CURRENT_EMOJI = CURRENT_COLOR[4]
            if event.button == 5:
               if CURRENT_SIZE == screenSize:
                    CURRENT_SIZE = bigScreenSize
               else:
                    CURRENT_SIZE = screenSize


    #Toggle Size
    screen = pygame.display.set_mode(CURRENT_SIZE)
    #Set background
    screen.fill(WHITE)
    #Set Emoji
    picture = pygame.image.load(CURRENT_EMOJI)
    scaledImage = pygame.transform.scale(picture, CURRENT_SIZE)
    #Add Image to the Screen
    screen.blit(scaledImage,(0,0))
    #Screen-refresh
    pygame.display.flip()
    clock.tick(60)
# Close the window and quit.
pygame.quit()
