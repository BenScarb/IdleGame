import pygame

HEIGHT = 512
WIDTH = 1000

TILE_WIDTH = 50
TILE_HEIGHT = 50

to_add = []
has_changed = True
blank_bg = None
the_bg = None

lastxy = (-1, -1)
items = [(0, 0), (10, 5)]


def on_mouse_move(pos, rel, buttons):
    global to_add

    if mouse.LEFT not in buttons:
        to_add = []
    New_Box(pos)
    
def New_Box(pos):
    global to_add
    global has_changed
    global lastxy
    lastxy = (int(pos[0]/TILE_WIDTH), int(pos[1]/TILE_HEIGHT))
    top_x = lastxy[0]*TILE_WIDTH
    top_y = lastxy[1]*TILE_HEIGHT
    new_rect = Rect((top_x, top_y), (TILE_WIDTH, TILE_HEIGHT))
    to_add.append(new_rect)
    has_changed = True

def on_mouse_up(pos, button):
    global to_add
    if mouse.LEFT == button:
        to_add = []
        New_Box(pos)

def gen_background():
    global blank_bg
    if blank_bg == None:
        blank_bg = screen.surface.copy()
        blank_bg.fill((255, 128, 0))
        for X in range(0, WIDTH):
            for Y in range(0, HEIGHT):
                if X%TILE_WIDTH == 0 and Y%TILE_HEIGHT == 0:
                    pygame.draw.line(blank_bg, (128, 128, 128), (X, Y), (X+5, Y))
                    pygame.draw.line(blank_bg, (128, 128, 128), (X, Y), (X, Y+5))

                    pygame.draw.line(blank_bg, (128, 128, 128), (X+(TILE_WIDTH-5), Y), (X+TILE_WIDTH, Y))
                    pygame.draw.line(blank_bg, (128, 128, 128), (X+TILE_WIDTH, Y), (X+TILE_WIDTH, Y+5))

                    pygame.draw.line(blank_bg, (128, 128, 128), (X, Y+(TILE_HEIGHT-5)), (X, Y+TILE_HEIGHT))
                    pygame.draw.line(blank_bg, (128, 128, 128), (X, Y+TILE_HEIGHT), (X+5, Y+TILE_HEIGHT))

                    pygame.draw.line(blank_bg, (128, 128, 128), (X+(TILE_WIDTH-5), Y+TILE_HEIGHT), (X+TILE_WIDTH, Y+TILE_HEIGHT))
                    pygame.draw.line(blank_bg, (128, 128, 128), (X+TILE_WIDTH, Y+(TILE_HEIGHT-5)), (X+TILE_WIDTH, Y+TILE_HEIGHT))
    
    global items
    for item in items:
        pygame.draw.rect(blank_bg, (255, 0, 0), [item[0]*TILE_WIDTH, item[1]*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT])
    
    return blank_bg

def on_key_down(key):
    global items
    if key == keys.SPACE:
        global lastxy
        if lastxy != (-1, -1) and lastxy not in items:
            items.append(lastxy)
            global the_bg
            the_bg = gen_background()
    elif key == keys.S:
        print("Showing list:")
        for item in items:
            print(item)

def draw():
    global to_add
    global the_bg
    global has_changed

    if has_changed:
        if the_bg == None:
            the_bg = gen_background()
        screen.blit(the_bg, (0,0))

        for new_rect in to_add:
            screen.draw.filled_rect(new_rect, (0, 0, 0))
        has_changed = False

def update(dt):
    pass

if __name__ == "__main__":
    import pgzrun
    pgzrun.go()
