import board
import pwmio
import time

buzzer = pwmio.PWMOut(board.A2, variable_frequency=True)
buzzer.frequency = 440
OFF = 0
ON = 2**15

while True:
    buzzer.duty_cycle = ON
    time.sleep(0.5)
    buzzer.duty_cycle = OFF
    time.sleep(0.5)