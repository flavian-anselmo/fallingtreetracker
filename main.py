def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_forever():
    if input.is_gesture(Gesture.SHAKE):
        pins.digital_write_pin(DigitalPin.P2, 1)
        radio.send_string("Falling Tree")
    else:
        pins.digital_write_pin(DigitalPin.P2, 0)
        radio.send_string("")
    #basic.pause(100)
basic.forever(on_forever)
