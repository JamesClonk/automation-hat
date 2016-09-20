import mock
import sys

rpi = mock.Mock()
rpi.GPIO = mock.Mock()
rpi.GPIO.input = mock.Mock(return_value=0)

sys.modules['RPi'] = rpi
sys.modules['RPi.GPIO'] = 0 # Fix RPi.GPIO import error insanity

sn3218 = mock.Mock()
sn3218.i2c = mock.Mock()
sn3218.i2c.read_i2c_block_data = mock.Mock(return_value=[0,0,0])

sys.modules['sn3218'] = sn3218

import automationhat
import RPi.GPIO

print("--Lights--")
assert str(automationhat.light).split(", ") == ["warn","comms","power"], "Lights missing one of [warn, comms, power]: {}".format(str(automationhat.light))
print(automationhat.light)
print("")

print("--Relays--")
assert str(automationhat.relay).split(", ") == ["three","two","one"], "Relay missing one of [one, two, three]: {}".format(str(automationhat.relay))
assert isinstance(automationhat.relay.one.light_no, automationhat.SNLight), "Relay one missing NO light"
assert isinstance(automationhat.relay.one.light_nc, automationhat.SNLight), "Relay one missing NC light"

print(automationhat.relay)
print("")

print("--Digital Outputs--")
assert str(automationhat.output).split(", ") == ["three","two","one"], "Output missing one of [one, two, three]: {}".format(str(automationhat.output))
print(automationhat.output)
print("")

print("--Digital Inputs--")
print(automationhat.input)
assert automationhat.input.one.read() == 0, "Input reading HIGH, should be LOW"
print(automationhat.input.read())
print("")

print("--Analog Inputs--")
print(automationhat.analog)

automationhat.analog.auto_light(False)
assert automationhat.analog.one._en_auto_lights == False, "Auto lights should be False/Disabled"

automationhat.analog.auto_light(True)
assert automationhat.analog.one._en_auto_lights == True, "Auto lights should be True/Enabled"

print(automationhat.analog.read())
print("")