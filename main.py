import pygame
import os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


YELLOW = [
  "emoji/eaPlemiddle.png",
  "emoji/normal.png"
]
GREEN = [
  "emoji/gross.png",
]
RED = [
  "emoji/angry.png",
]
BLUE = [
  "emoji/sad.png",
]




pygame.init()
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption("Ostumoji")


pygame.joystick.init()
joysticks = []

# for al the connected joysticks
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
screen = pygame.display.set_mode(screenSize)


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Current Emoji
CURRENT_EMOJI = YELLOW[0]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print("Keydown,", event.key)
            if event.key == 27:
              pygame.quit()
        elif event.type == pygame.JOYAXISMOTION:
            lr = joysticks[event.joy].get_axis(0)
            ud = joysticks[event.joy].get_axis(1)
            if round(lr) < 0: #left
              JOYSTICK_POSTION = "LEFT"
              CURRENT_EMOJI= BLUE[0]
            if round(lr) > 0 : #right
              JOYSTICK_POSTION = "RIGHT"
              CURRENT_EMOJI= RED[0]
            if round(ud) > 0: #down
              JOYSTICK_POSTION = "DOWN"
              CURRENT_EMOJI= GREEN[0]
            if round(ud) < 0: #up
              JOYSTICK_POSTION = "UP"
              CURRENT_EMOJI= YELLOW[0]
            # print("Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down.")
            if event.button == BUTTONS_YELLOW:
              CURRENT_EMOJI= YELLOW[0]
            if event.button == BUTTONS_BLUE:
              CURRENT_EMOJI= BLUE[0]
            if event.button == BUTTONS_GREEN:
              CURRENT_EMOJI= GREEN[0]
            if event.button == BUTTONS_RED:
              CURRENT_EMOJI= RED[0]

    #Set background
    screen.fill(WHITE)
    #Set Emoji
    picture = pygame.image.load(CURRENT_EMOJI)
    scaledImage = pygame.transform.scale(picture, screenSize)
    screen.blit(scaledImage,(0,0))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()