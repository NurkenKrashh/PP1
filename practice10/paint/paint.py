import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint Project")

    clock = pygame.time.Clock()
    
    radius = 10
    color_mode = 'blue'
    points = []

    tool = "brush"
    drawing = False
    start_pos = (0, 0)

    colors = {
        'blue': (0,0,255),
        'red': (255,0,0),
        'green': (0,255,0),
        'black': (0,0,0),
        'white': (255,255,255)
    }

    running = True
    while running:
        
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    running = False
                if event.key == pygame.K_F4 and alt_held:
                    running = False
                if event.key == pygame.K_ESCAPE:
                    running = False

                # 🎨 color
                if event.key == pygame.K_r:
                    color_mode = 'red'
                elif event.key == pygame.K_g:
                    color_mode = 'green'
                elif event.key == pygame.K_b:
                    color_mode = 'blue'

                # 🛠 tools
                if event.key == pygame.K_1:
                    tool = "brush"
                elif event.key == pygame.K_2:
                    tool = "rect"
                elif event.key == pygame.K_3:
                    tool = "circle"
                elif event.key == pygame.K_4:
                    tool = "eraser"

            # 🖱 mouse down
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                points = []  # 🔥 жаңа stroke басталады

                if event.button == 1:
                    radius = min(50, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)

            # 🖱 mouse up
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                end_pos = event.pos

                if tool == "rect":
                    pygame.draw.rect(screen, colors[color_mode],
                                     (start_pos[0], start_pos[1],
                                      end_pos[0]-start_pos[0],
                                      end_pos[1]-start_pos[1]), 2)

                elif tool == "circle":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    r = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(screen, colors[color_mode],
                                       start_pos, r, 2)

            # 🖱 motion
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == "brush":
                        points.append(event.pos)

                    elif tool == "eraser":
                        pygame.draw.circle(screen, (0,0,0), event.pos, radius)

        
        if drawing and tool == "brush":
            for i in range(len(points) - 1):
                drawLineBetween(screen, i, points[i], points[i + 1],
                                radius, color_mode)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (0, 0, c1)
    elif color_mode == 'red':
        color = (c1, 0, 0)
    elif color_mode == 'green':
        color = (0, c1, 0)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return

    for i in range(steps):
        t = i / steps
        x = int(start[0]*(1-t) + end[0]*t)
        y = int(start[1]*(1-t) + end[1]*t)
        pygame.draw.circle(screen, color, (x, y), width)


main()