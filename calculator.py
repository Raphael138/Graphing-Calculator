import pygame
import sys
import math
import numpy as np
from calculator_parser import parser
from calculator_output import SyntaxAnalysis

# Defining constants(colors, widths, etc..)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (150, 150, 150)
dark_grey = (100, 100, 100)
light_grey = (200, 200, 200)
graph_color = (37, 150, 190)
line_width = 2
pi = math.pi
origin = (100, 250)
time_t = 0

# Initializing pygame
pygame.init()
clock = pygame.time.Clock()

# Setting up input box
input_box = pygame.Rect(350, 460, 300, 32)
outline_input_box = pygame.Rect(350, 460, 300, 32)
input_active = False
text = [' ', 'y', '=']

# Setting up input buttons
buttons_active = [False for i in range(25)]
buttons_box = [pygame.Rect(960+i*58, 10+j*78, 48, 48)
               for j in range(5) for i in range(5)]

# The function we are currently plotting
function_to_plot = ''
prev_function_to_plot = ''

# Creating the screen
max_x = 750
max_y = 180
screen_height = 500
screen_width = 1000+250
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Graphing software")

# Initializing images
pi_img = pygame.image.load("pi.png")
pi_img = pygame.transform.scale(pi_img, (22, 22))

# Initializing fonts
x_y_font = pygame.font.Font('freesansbold.ttf', 12)
input_font = pygame.font.Font(None, 27)
button_font = pygame.font.Font(None, 42)
x_text = x_y_font.render('x', True, black, white)
y_text = x_y_font.render('y', True, black, white)

# given a string, output [list of x coordinates, list of y coordinates]
def plot_input(string):
    try:
        parsed_function = parser.parse(string)
        x = np.arange(0,2*pi*3, 0.01)
        sa = SyntaxAnalysis(x, parsed_function)
        x = x * 42.5
        y = sa.output(time_t)
        return [origin[0]+int(i) for i in x], [origin[1]-int(i) for i in y]
    except Exception as err: 
        return -1

# Draws the buttons
def drawButton(screen):
    pygame.draw.rect(screen, (50, 50, 50), (950, 0, 300, 500))
    for j in range(5):
        for i in range(5):
            button_color = grey
            if buttons_active[j*5+i]:
                button_color = light_grey
            pygame.draw.rect(screen, button_color, (960+i*58, 10+j*78, 48, 48))

    # First row
    y_button = button_font.render("y", True, black)
    screen.blit(y_button, (975, 20))
    x_button = button_font.render("x", True, black)
    screen.blit(x_button, (1033, 20))
    t_button = button_font.render("t", True, black)
    screen.blit(t_button, (1095, 20))
    op_button = button_font.render("(", True, black)
    screen.blit(op_button, (1153, 20))
    cp_button = button_font.render(")", True, black)
    screen.blit(cp_button, (1211, 20))

    # Second row
    eq_button = button_font.render("=", True, black)
    screen.blit(eq_button, (975, 98))
    plus_button = button_font.render("+", True, black)
    screen.blit(plus_button, (1033, 98))
    minus_button = button_font.render("-", True, black)
    screen.blit(minus_button, (1095, 98))
    div_button = button_font.render("/", True, black)
    screen.blit(div_button, (1153, 100))
    mult_button = button_font.render("*", True, black)
    screen.blit(mult_button, (1211, 105))

    # Third row
    cos_button = button_font.render("cos", True, black)
    screen.blit(cos_button, (960, 176))
    sin_button = button_font.render("sin", True, black)
    screen.blit(sin_button, (1021, 176))
    tan_button = button_font.render("tan", True, black)
    screen.blit(tan_button, (1079, 176))
    screen.blit(pi_img, (1145, 180))
    dot_button = button_font.render(".", True, black)
    screen.blit(dot_button, (1211, 176))

    # Fourth row
    zero_button = button_font.render("0", True, black)
    screen.blit(zero_button, (975, 257))
    one_button = button_font.render("1", True, black)
    screen.blit(one_button, (1033, 257))
    two_button = button_font.render("2", True, black)
    screen.blit(two_button, (1094, 257))
    three_button = button_font.render("3", True, black)
    screen.blit(three_button, (1150, 257))
    four_button = button_font.render("4", True, black)
    screen.blit(four_button, (1210, 257))

    # Fifth row
    five_button = button_font.render("5", True, black)
    screen.blit(five_button, (975, 335))
    six_button = button_font.render("6", True, black)
    screen.blit(six_button, (1033, 335))
    seven_button = button_font.render("7", True, black)
    screen.blit(seven_button, (1094, 335))
    eight_button = button_font.render("8", True, black)
    screen.blit(eight_button, (1150, 334))
    nine_button = button_font.render("9", True, black)
    screen.blit(nine_button, (1210, 335))


# Graphing function
def graph(screen):
    # Declaring global var
    global function_to_plot, prev_function_to_plot

    # Draw buttons
    drawButton(screen)

    # X-axis
    pygame.draw.line(screen, black, (100, 250), (900, 250), width=line_width)
    pygame.draw.polygon(screen, black, ((900, 248), (900, 254), (903, 251)))
    screen.blit(x_text, (907, 257))
    for i in range(1, 7):
        pygame.draw.line(screen, black, (99+i*max_x/(2*math.pi), 246),
                         (99+i*max_x/(2*math.pi), 256), width=line_width)

    # Y-axis
    pygame.draw.line(screen, black, (100, 50), (100, 450), width=line_width)
    pygame.draw.polygon(screen, black, ((98, 50), (104, 50), (101, 47)))
    pygame.draw.polygon(screen, black, ((98, 450), (104, 450), (101, 453)))
    screen.blit(y_text, (107, 40))

    # Drawing input box and input
    box_color = light_grey if input_active else grey
    pygame.draw.rect(screen, box_color, input_box)
    pygame.draw.rect(screen, dark_grey, outline_input_box, width=line_width)
    function_text = input_font.render("".join(text), True, black)
    screen.blit(function_text, (350, 467))

    # Draw math function
    if input_active:
        function_to_plot = prev_function_to_plot
    else:
        prev_function_to_plot = function_to_plot

    input_function = plot_input("".join(function_to_plot[3:]))
    if type(input_function) == tuple:
        x, y = input_function
        for i in range(len(x)):
            pygame.draw.circle(screen, graph_color, (x[i], y[i]), 1)


# Event loop
c = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = True
            if buttons_box[0].collidepoint(event.pos):
                text.append('y')
                buttons_active[0] = True
            if buttons_box[1].collidepoint(event.pos):
                text.append('x')
                buttons_active[1] = True
            if buttons_box[2].collidepoint(event.pos):
                text.append('t')
                buttons_active[2] = True
            if buttons_box[3].collidepoint(event.pos):
                text.append('(')
                buttons_active[3] = True
            if buttons_box[4].collidepoint(event.pos):
                text.append(')')
                buttons_active[4] = True
            if buttons_box[5].collidepoint(event.pos):
                text.append('=')
                buttons_active[5] = True
            if buttons_box[6].collidepoint(event.pos):
                text.append('+')
                buttons_active[6] = True
            if buttons_box[7].collidepoint(event.pos):
                text.append('-')
                buttons_active[7] = True
            if buttons_box[8].collidepoint(event.pos):
                text.append('/')
                buttons_active[8] = True
            if buttons_box[9].collidepoint(event.pos):
                text.append('*')
                buttons_active[9] = True
            if buttons_box[10].collidepoint(event.pos):
                text.append('cos')
                buttons_active[10] = True
            if buttons_box[11].collidepoint(event.pos):
                text.append('sin')
                buttons_active[11] = True
            if buttons_box[12].collidepoint(event.pos):
                text.append('tan')
                buttons_active[12] = True
            if buttons_box[13].collidepoint(event.pos):
                text.append('(pi)')
                buttons_active[13] = True
            if buttons_box[14].collidepoint(event.pos):
                if '0' <= text[-1] and '9' >= text[-1]:
                    text[-1] += '.'
                else:
                    text.append('.')
                buttons_active[14] = True
            for i in range(15, 25):
                if buttons_box[i].collidepoint(event.pos):
                    if '0' <= text[-1] and '9' >= text[-1] or text[-1] == '.':
                        text[-1] += str(i-15)
                    else:
                        text.append(str(i-15))
                    buttons_active[i] = True
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    function_to_plot = text
                elif event.key == pygame.K_BACKSPACE:
                    if len(text) > 3:
                        text = text[:-1]
                elif event.unicode == '(':
                    text.append(event.unicode)
                    buttons_active[3] = True
                elif event.unicode == ')':
                    text.append(event.unicode)
                    buttons_active[4] = True
                elif event.unicode == '=':
                    text.append(event.unicode)
                    buttons_active[5] = True
                elif event.unicode == '+':
                    text.append(event.unicode)
                    buttons_active[6] = True
                elif event.unicode == '-':
                    text.append(event.unicode)
                    buttons_active[7] = True
                elif event.unicode == '/':
                    text.append(event.unicode)
                    buttons_active[8] = True
                elif event.unicode == '*':
                    text.append(event.unicode)
                    buttons_active[9] = True
                elif event.unicode == '.':
                    if '0' <= text[-1] and '9' >= text[-1]:
                        text[-1] += '.'
                    else:
                        text.append('.')
                    buttons_active[14] = True
                elif event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    if ('0' <= text[-1] and '9' >= text[-1]) or text[-1] == '.':
                        text[-1] += event.unicode
                    else:
                        text.append(event.unicode)
                    buttons_active[15+int(event.unicode)] = True
                elif event.key == pygame.K_y:
                    text.append(event.unicode)
                    buttons_active[0] = True
                elif event.key == pygame.K_x:
                    text.append(event.unicode)
                    buttons_active[1] = True
                elif event.key == pygame.K_t:
                    text.append(event.unicode)
                    buttons_active[2] = True

                if input_font.render("".join(text), True, black).get_width() > 300:
                    text = text[:-1]

    # Resetting old screen
    screen.fill(white)

    # Graphing
    graph(screen)

    # Resetting buttons
    if c == 3:
        c = 0
        buttons_active = [False for i in range(25)]
        time_t+=1

    # Setting time between frames
    c += 1
    clock.tick(15)

    pygame.display.update()
