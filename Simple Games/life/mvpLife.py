import pygame 
from math import floor

def count_neighbors():
    for x in range(num_blocks):
        for y in range(num_blocks):
            total = 0 
            for dx in range(-1,2):
                for dy in range(-1,2):
                    try:
                        if x+dx >= 0 and y+dy >= 0:
                            if data[x+dx][y+dy]:
                                total += 1
                    except IndexError:
                        pass
            if data[x][y]:
                total -= 1

            total_list[x][y] = total
    
def calculate_vars():
    global block_size, blank_size, cell_size, cube_boys, font

    cube_boys = [[None for _ in range(num_blocks)] for _ in range(num_blocks)]

    if len(data) < num_blocks:
        for lis in data:
            lis.append(False)
        data.append([False for i in range(num_blocks)])
        
        for lis in total_list:
            lis.append(None)
        total_list.append([None for i in range(num_blocks)])

    block_size = (screen_size / num_blocks) * offset_percent
    blank_size = (screen_size - (block_size * num_blocks)) / (num_blocks + 1)
    cell_size = block_size + blank_size

    for x in range(num_blocks):
        for y in range(num_blocks):
            x_pos = x * cell_size + blank_size
            y_pos = y * cell_size + blank_size
            cube_boys[x][y] = pygame.Rect(x_pos, y_pos, block_size, block_size)
    
    font = pygame.font.Font(pygame.font.get_default_font(), int(cell_size))

    count_neighbors()

def get_mouse_pos():
    pos = pygame.mouse.get_pos()
    x, y = (floor(pos[0] / cell_size), floor(pos[1] / cell_size))
    return (x,y)


def check_inputs():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.VIDEORESIZE:
            global screen, screen_size
            screen_size = event.size[0]
            calculate_vars()
            screen = pygame.display.set_mode((screen_size,screen_size), pygame.RESIZABLE)
        
        global drag, mouse_pos_list, brush_type
        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
            x, y = get_mouse_pos()
            brush_type = not data[x][y]

        if event.type == pygame.MOUSEBUTTONUP:
            drag = False
            mouse_pos_list = []
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_s:
                global step_mode
                if step_mode:
                    apply_rules()
                step_mode = not step_mode
            if event.key == pygame.K_e:
                global edit_mode
                edit_mode = not edit_mode

            if edit_mode:
                global time_between_updates, num_blocks

                if event.key == pygame.K_UP:
                    time_between_updates -= 50
                if event.key == pygame.K_DOWN:
                    time_between_updates += 50
                if event.key == pygame.K_LEFT:  # bug: glider stopps if make map bigger
                    if num_blocks > 1:
                        num_blocks -= 1
                        calculate_vars()
                if event.key == pygame.K_RIGHT:
                    if num_blocks < grid_size_limit:
                        num_blocks += 1
                        calculate_vars()
                
        # step
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and step_mode:
                apply_rules()
    
    if drag:  
        x, y = get_mouse_pos()

        if (x,y) not in mouse_pos_list:
            data[x][y] = brush_type
            mouse_pos_list.append((x,y))
        
        count_neighbors()

def apply_rules():
    global previous_time, total_list
    count_neighbors()

    to_change = []
    for x in range(num_blocks):
        for y in range(num_blocks):            
            total = total_list[x][y]
            if data[x][y]:
                if not(total == 2 or total == 3):
                    to_change.append((x,y)) 
            if data[x][y] == False and total == 3:
                to_change.append((x,y))

    for x,y in to_change:
        data[x][y] = not data[x][y]

    previous_time = pygame.time.get_ticks()

def draw():
    screen.fill(gapColor)

    # draw rects
    for x in range(len(cube_boys)):
        for y in range(len(cube_boys)):
            if data[x][y]:
                pygame.draw.rect(screen, onColor, cube_boys[x][y])
            else:
                pygame.draw.rect(screen, offColor, cube_boys[x][y])

    # draw totals
    if draw_totals:
        count_neighbors()
        for x in range(num_blocks):
            for y in range(num_blocks):
                if total_list[x][y] != 0:
                    text_surface = font.render(str(total_list[x][y]), True, (0, 0, 0))
                    screen.blit(text_surface, dest=((x * cell_size) + cell_size/4, y * cell_size))
    
    pygame.display.flip()


# Init Vars ---------------------------------------------------------------------
block_size, blank_size, cell_size, font = None, None, None, None # init vars

previous_time = None

drag = False # these 3 are all just init vars
mouse_pos_list = []

brush_type = True
pygame.init()

# Change Vars -------------------------------------------------------------------
screen_size = 800 # we could have a non square grid
num_blocks = 20  # maybe use scrolling to change this instead of arrows
offset_percent = .95 # I need a way to do #er of px

step_mode = True
edit_mode = True
draw_totals = True

offColor = '#333333'
onColor = '#f5f5f5'
gapColor = '#9e9e9e'

time_between_updates = 151

# Dependent --------------------------------------------------------------------------
screen = pygame.display.set_mode((screen_size, screen_size), pygame.RESIZABLE)

data = [[False for _ in range(num_blocks)] for _ in range(num_blocks)] # maybe a bigger grid than what you can see and you can move and shit
total_list = [[None for _ in range(num_blocks)] for _ in range(num_blocks)]
calculate_vars()

grid_size_limit = screen_size/3 # is this a good limit for #er of blocks

draw()
while True:
    # input + do stuff
    check_inputs() 

    if step_mode == False and (pygame.time.get_ticks() - previous_time) >= time_between_updates:
        apply_rules()

    # output
    draw()
        