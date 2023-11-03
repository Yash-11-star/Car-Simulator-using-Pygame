import pygame
import time

pygame.init()

win = pygame.display.set_mode((850, 600))
pygame.display.set_caption("Car Dashboard")

bg = pygame.image.load('frame.png')
bar = pygame.image.load('speed_bar.png')
bat = pygame.image.load('battery.png')
ce = pygame.image.load('check_engine.png')
ct = pygame.image.load('coolant_temp.png')
seatbelt_open = pygame.image.load('seatbelt_open.png')
seatbelt_closed = pygame.image.load('seatbelt_closed.png')
fuel = pygame.image.load('fuel.png')
fuel_meter = pygame.image.load('fuel_meter.png')
oil = pygame.image.load('oil.png')
left_sig = pygame.image.load('turn_signal_left.png')
right_sig = pygame.image.load('turn_signal_right.png')
camera_frame = pygame.image.load('camera_frame.jpg')
camera_view = pygame.image.load('camera_view.jpg')
radio = pygame.image.load('radio.png')
blink = pygame.image.load('blink.png')
clock = pygame.time.Clock()

width = 88
height = 19

velocity = 0
rpm = 0
distance = 0
dist_change = 0
dist = 0
pointer_pos = [(145, 465), (145, 440), (145, 420), (142, 400), (145, 380), (145, 360), (150, 350), (170, 340), (190, 340), (207, 340), (222, 336), (250, 336), (268, 345)]
seatbelt = False
gear = 'N'


global Isrightvisable
Isrightvisable = True
Isrightpressed = False
Isleftpressed = False
global Isleftvisable
Isleftvisable = True
global Timesincelastblink
Timesincelastblink = time.time()
global Timesincelastblink2
Timesincelastblink2 = time.time()


def redrawGameWindow():
    global Isrightvisable
    global Isleftvisable
    global Isleftpressed
    global Isrightpressed
    global Timesincelastblink
    global Timesincelastblink2
    distance_KM = font.render("{:.2f}".format(float(dist)) + 'km', 1, (255, 255, 255))
    text_g = font.render('Gear ' + str(gear), 1, (255, 255, 255))
    text_rpm = font.render("RPM", True, (255, 255, 255))
    text = font.render(str(int(velocity)) + ' km/h ', 1, (255, 255, 255))
    win.blit(bg, (0, 0))
    # win.blit(fuel_meter, (60, 350))
    win.blit(camera_frame, (370, 250))
    win.blit(camera_view, (375, 255))
    win.blit(radio, (500, 50))
    win.blit(bat, (50, 50))
    win.blit(ce, (120, 50))
    win.blit(ct, (190, 50))
    win.blit(fuel, (260, 50))
    win.blit(oil, (330, 50))
    if seatbelt:
        win.blit(seatbelt_closed, (400, 30))
    else:
        win.blit(seatbelt_open, (400, 30))

    pygame.draw.circle(win, (255, 0, 255), (212, 400), 100, width=2)
    pygame.draw.circle(win, (255, 0, 255), (212, 400), 10, width=2)

    pygame.draw.polygon(win, (255, 0, 255), ((212, 400), pointer_pos[int(velocity//10)], (210, 395)))

    speed_font = pygame.font.SysFont("comicsans", 15)
    win.blit(speed_font.render("120", True, (255, 255, 255)), (265, 337))
    win.blit(speed_font.render("110", True, (255, 255, 255)), (250, 318))
    win.blit(speed_font.render("100", True, (255, 255, 255)), (220, 308))
    win.blit(speed_font.render("90", True, (255, 255, 255)), (198, 305))
    win.blit(speed_font.render("80", True, (255, 255, 255)), (177, 308))
    win.blit(speed_font.render("70", True, (255, 255, 255)), (155, 318))
    win.blit(speed_font.render("60", True, (255, 255, 255)), (135, 330))
    win.blit(speed_font.render("50", True, (255, 255, 255)), (123, 350))
    win.blit(speed_font.render("40", True, (255, 255, 255)), (120, 370))
    win.blit(speed_font.render("30", True, (255, 255, 255)), (117, 390))
    win.blit(speed_font.render("20", True, (255, 255, 255)), (122, 410))
    win.blit(speed_font.render("10", True, (255, 255, 255)), (127, 430))
    win.blit(speed_font.render("0", True, (255, 255, 255)), (139, 450))
    win.blit(text, (175, 460))
    win.blit(text_g, (90, 220))
    win.blit(bar, (712, 374))
    win.blit(text_rpm, (742, 510))
    win.blit(distance_KM, (200, 160))

    rpm_font = pygame.font.SysFont('freesansbold.tf', 15, False)
    rpm_range_vals = [(698, 480), (698, 459), (698, 438), (698, 417), (698, 396), (698, 376)]
    for i in range(1, 7):
        rpm_range = rpm_font.render(str(i*1000), True, (255, 255, 255))
        win.blit(rpm_range, rpm_range_vals[i-1])

    if rpm > 20:
        pygame.draw.rect(win, (0, 255, 0), (724, 480, width, height))
    if rpm > 40:
        pygame.draw.rect(win, (0, 255, 0), (724, 459, width, height))
    if rpm > 60:
        pygame.draw.rect(win, (0, 255, 0), (724, 438, width, height))
    if rpm > 80:
        pygame.draw.rect(win, (255, 255, 0), (724, 417, width, height))
    if rpm > 100:
        pygame.draw.rect(win, (255, 255, 0), (724, 396, width, height))
    if rpm >= 119:
        pygame.draw.rect(win, (255, 255, 0), (724, 375, width, height))
   


    if Isleftvisable:
        win.blit(left_sig, (120, 150))
    else:
        win.blit(blink, (120, 150))
    if Isrightvisable:
        win.blit(right_sig, (330, 150))
    else:
        win.blit(blink, (330, 150))

    if Isleftpressed:
        Isrightvisable = True
        Isrightpressed = False
        currenttime = time.time()
        if currenttime - Timesincelastblink > 0.5:
            if Isleftvisable:
                Isleftvisable = False
            else:
                Isleftvisable = True
            Timesincelastblink = time.time()

    if Isrightpressed:
        Isleftvisable = True
        Isleftpressed = False
        currenttime2 = time.time()
        if currenttime2 - Timesincelastblink2 > 0.5:
            if Isrightvisable:
                Isrightvisable = False
            else:
                Isrightvisable = True
            Timesincelastblink2 = time.time()

    pygame.display.update()


# mainloop
font = pygame.font.SysFont('freesansbold.tf', 30, False)
run = True
while run:
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if velocity > 119:
        velocity = 119
    elif velocity <= 0:
        velocity = 0

    if rpm > 119:
        rpm = 119
    elif rpm <= 0:
        rpm = 0
    
    
    if keys[pygame.K_d]:
        gear_d = 'D'
        gear = 'D'

    if gear != 'N' and keys[pygame.K_SPACE] == True:
            velocity += 1
            rpm += 2
            if velocity > 10:
                gear = 1
            if velocity > 30:
                gear = 2
            if velocity > 40:
                gear = 3
            if velocity > 60:
                gear = 4
            if velocity > 80:
                gear = 5
            if velocity > 100:
                gear = 6
            # calculating distance of the car
            dist += velocity / 3600

    if keys[pygame.K_SPACE] == False and velocity > 0:
            if keys[pygame.K_b]:
                velocity -= 1
                rpm -= 2
                if velocity > 10:
                    gear = 1
                if velocity > 30:
                    gear = 2
                if velocity > 40:
                    gear = 3
                if velocity > 60:
                    gear = 4
                if velocity > 80:
                    gear = 5
                if velocity > 100:
                    gear = 6
                # calculating distance of the car
                dist += velocity / 4000
            else:
                velocity -= 0.3
                rpm -= 1
                if velocity > 10:
                    gear = 1
                if velocity > 30:
                    gear = 2
                if velocity > 40:
                    gear = 3
                if velocity > 60:
                    gear = 4
                if velocity > 80:
                    gear = 5
                if velocity > 100:
                    gear = 6
                # calculating distance of the car
                dist += velocity / 5000
                    
    if velocity <= 0 and keys[pygame.K_n]:
        gear = 'N'
        gear_d = 'N'

    if keys[pygame.K_SPACE] and gear != "N":
        velocity += 1

    if keys[pygame.K_s]:
        seatbelt = True

    if keys[pygame.K_o]:
        seatbelt = False

    if (keys[pygame.K_SPACE] == False and velocity > 0):
        if keys[pygame.K_b]:
            velocity -= 1
            rpm -= 2
            if(dist_change>0):
                dist_change = 0.0006 * velocity
                if dist_change <= 0:
                    dist_change *= -1
            else:
                dist_change = 0

        else:
            velocity -= 0.3
            rpm -= 1
            dist_change = 0.003 *  velocity
            if dist_change <= 0:
                dist_change *= -1

    if(not keys[pygame.K_SPACE] and not keys[pygame.K_b]):
        dist_change = 0

    distance += dist_change
    if dist_change <= 0:
        dist_change *= -1

    if keys[pygame.K_LEFT]:
        Isrightpressed = False
        if Isleftpressed:
            Isleftpressed = False
            pygame.time.wait(250)
            if not Isrightvisable:
                Isrightvisable = 1

        else:
            Isleftpressed = True
            pygame.time.wait(250)
        
    if keys[pygame.K_RIGHT]:
        Isleftpressed = False
        if Isrightpressed:
            Isrightpressed = False
            pygame.time.wait(250)
            if not Isleftvisable:
                Isleftvisable = 1
        else:
            Isrightpressed = True
            pygame.time.wait(250)
        
    if not Isleftpressed:
        Isleftvisable = True
    if not Isrightpressed:
        Isrightvisable = True

    redrawGameWindow()
pygame.quit()

