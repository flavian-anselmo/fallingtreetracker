radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
// basic.pause(100)
basic.forever(function () {
    if (input.isGesture(Gesture.Shake)) {
        radio.sendString("Falling Tree")
        pins.digitalWritePin(DigitalPin.P2, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P2, 0)
        radio.sendString("")
    }
})
