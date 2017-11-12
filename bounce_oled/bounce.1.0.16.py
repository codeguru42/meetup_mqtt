# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# http://www.iotecosystem.com
# Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
import utime
import bounce_config
import bounce_oled
import bounce_random

# version
bounce_title = "Bouncer V1.0.16"

# define box to operate in
shift_y = 4
min_x = round(bounce_config.oled_width/5)
max_x = (min_x*4)-1
min_y = round(bounce_config.oled_height/5) + shift_y
max_y = ((min_y-shift_y)*4)-1


# main function
def main():

    bounce_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    bounce_oled.splash_oled(bounce_title)
    bounce_oled.clear_oled()

    x = min_x + 1
    y = min_y + 1
    dx = bounce_random.max_dxdy
    dy = bounce_random.max_dxdy

    bounce_oled.drawRect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1, 1)

    while True:

        # delete old line
        bounce_oled.drawLine(x, y, x + dx, y + dy, 0)

        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen
        if x + dx <= min_x+1:
            x = min_x + 1
            dx = bounce_random.random_dxdy()
            if (x + dx >= max_x):
                dx = bounce_random.max_dxdy

        if x + dx >= max_x - 1:
            x = max_x - 1
            dx = - bounce_random.random_dxdy()
            if (x + dx <= min_x):
                dx = bounce_random.max_dxdy

        if y + dy <= min_y + 1:
            y = min_y + 1
            dy = bounce_random.random_dxdy()
            if (y + dy >= max_y):
                dy = bounce_random.max_dxdy

        if y + dy >= max_y - 1:
            y = max_y - 1
            dy = - bounce_random.random_dxdy()
            if (y + dy <= min_y):
                dy = bounce_random.max_dxdy

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the line
        bounce_oled.drawLine(x, y, x + dx, y + dy, 1)

        # show the line on the display
        bounce_oled.oled.show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()