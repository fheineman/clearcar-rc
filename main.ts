function rightForward () {
    pins.digitalWritePin(DigitalPin.P15, 0)
    pins.digitalWritePin(DigitalPin.P16, 1)
    pins.analogWritePin(AnalogPin.P2, motorRspeed)
}
function leftForward () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P13, 1)
    pins.analogWritePin(AnalogPin.P1, motorLspeed)
}
function leftReverse () {
    pins.digitalWritePin(DigitalPin.P12, 1)
    pins.digitalWritePin(DigitalPin.P13, 0)
    pins.analogWritePin(AnalogPin.P1, motorLspeed)
}
function stopAll () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P13, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)
    pins.digitalWritePin(DigitalPin.P16, 0)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
}
function rightReverse () {
    pins.digitalWritePin(DigitalPin.P15, 1)
    pins.digitalWritePin(DigitalPin.P16, 0)
    pins.analogWritePin(AnalogPin.P2, motorRspeed)
}
let motorLspeed = 0
let motorRspeed = 0
led.enable(false)
let joyH = 512
let joyV = 512
music.playTone(262, music.beat(BeatFraction.Whole))
basic.forever(function () {
    if (pins.pulseIn(DigitalPin.P3, PulseValue.High) < 3000 && pins.pulseIn(DigitalPin.P3, PulseValue.High) > 750) {
        joyH = Math.map(pins.pulseIn(DigitalPin.P3, PulseValue.High), 1000, 2000, 1023, 0)
    }
    if (pins.pulseIn(DigitalPin.P4, PulseValue.High) < 3000 && pins.pulseIn(DigitalPin.P4, PulseValue.High) > 750) {
        joyV = Math.map(pins.pulseIn(DigitalPin.P4, PulseValue.High), 1000, 2000, 0, 1023)
    }
})
basic.forever(function () {
    if (joyH < 450 && joyV > 550) {
        motorRspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorLspeed = motorRspeed / Math.map(joyH, 0, 450, 12, 4)
        leftForward()
        rightForward()
    } else if (joyH > 550 && joyV > 550) {
        motorLspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorRspeed = motorLspeed / Math.map(joyH, 550, 1023, 4, 12)
        leftForward()
        rightForward()
    } else if (joyH < 450 && joyV < 450) {
        motorRspeed = Math.map(joyV, 0, 450, 255, 10)
        motorLspeed = motorRspeed / Math.map(joyH, 0, 450, 12, 4)
        leftReverse()
        rightReverse()
    } else if (joyH > 550 && joyV < 450) {
        motorLspeed = Math.map(joyV, 0, 450, 255, 10)
        motorRspeed = motorLspeed / Math.map(joyH, 550, 1023, 4, 12)
        leftReverse()
        rightReverse()
    } else if (joyV > 550) {
        motorLspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorRspeed = motorLspeed
        leftForward()
        rightForward()
    } else if (joyV < 450) {
        motorLspeed = Math.map(joyV, 10, 450, 255, 0)
        motorRspeed = motorLspeed
        leftReverse()
        rightReverse()
    } else if (joyH < 450) {
        motorLspeed = Math.map(joyH, 0, 450, 127, 10)
        leftReverse()
        rightForward()
    } else if (joyH > 550) {
        motorLspeed = Math.map(joyH, 550, 1023, 10, 127)
        leftForward()
        rightReverse()
    } else {
        stopAll()
    }
})
