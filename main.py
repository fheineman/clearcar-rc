def flashGrn():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
    basic.pause(150)
def clrColors():
    global green, yellow, red, blue, white
    green = 0
    yellow = 0
    red = 0
    blue = 0
    white = 0
def flashYel():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.YELLOW)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(200)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.YELLOW)
    basic.pause(200)
def flashBlue():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.BLUE)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.BLUE)
    basic.pause(150)
def flashRed3():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.RED)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.RED)
    basic.pause(150)
motorLspeed = 0
motorRspeed = 0
white = 0
blue = 0
red = 0
yellow = 0
green = 0
angle = 90
joyH = 512
joyV = 512
DFRobotMaqueenPlus.servo_run(Servos.S1, angle)
DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.WHITH)
music.play_tone(262, music.beat(BeatFraction.WHOLE))

def on_forever():
    global motorRspeed, motorLspeed
    if joyH < 450 and joyV > 550:
        motorRspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorLspeed = Math.map(joyV, 550, 1023, 10, 255) / Math.map(joyH, 0, 450, 12, 4)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, motorRspeed)
    elif joyH > 550 and joyV > 550:
        motorLspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorRspeed = Math.map(joyV, 550, 1023, 10, 255) / Math.map(joyH, 550, 1023, 4, 12)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, motorRspeed)
    elif joyH < 450 and joyV < 450:
        motorRspeed = Math.map(joyV, 0, 450, 255, 10)
        motorLspeed = Math.map(joyV, 0, 450, 255, 10) / Math.map(joyH, 0, 450, 12, 4)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, motorRspeed)
    elif joyH > 550 and joyV < 450:
        motorLspeed = Math.map(joyV, 0, 450, 255, 10)
        motorRspeed = Math.map(joyV, 0, 450, 255, 10) / Math.map(joyH, 550, 1023, 4, 12)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, motorRspeed)
    elif joyV > 550:
        motorLspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorRspeed = motorLspeed
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, motorRspeed)
    elif joyV < 450:
        motorLspeed = Math.map(joyV, 10, 450, 255, 0)
        motorRspeed = motorLspeed
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, motorRspeed)
    elif joyH < 450:
        motorLspeed = Math.map(joyH, 0, 450, 127, 10)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, motorLspeed)
    elif joyH > 550:
        motorLspeed = Math.map(joyH, 550, 1023, 10, 127)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, motorLspeed)
    else:
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 0)
basic.forever(on_forever)

def on_forever2():
    if green == 1:
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.WHITH)
    elif yellow == 1:
        flashYel()
    elif red == 1:
        flashRed3()
    elif blue == 1:
        flashBlue()
    elif white == 1:
        flashGrn()
    else:
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.WHITH)
basic.forever(on_forever2)

def on_forever3():
    if blue == 1:
        music.play_melody("C5 G C5 G C5 G C5 G ", 240)
basic.forever(on_forever3)

def on_forever4():
    global joyH, joyV
    if pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) < 3000 and pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) > 750:
        joyH = Math.map(pins.pulse_in(DigitalPin.P1, PulseValue.HIGH),
            1000,
            2000,
            1023,
            0)
    if pins.pulse_in(DigitalPin.P2, PulseValue.HIGH) < 3000 and pins.pulse_in(DigitalPin.P2, PulseValue.HIGH) > 750:
        joyV = Math.map(pins.pulse_in(DigitalPin.P2, PulseValue.HIGH),
            1000,
            2000,
            0,
            1023)
basic.forever(on_forever4)
