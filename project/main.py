import machine
import socket
import time

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266</title> </head>
    <body>
		<h1>Hi, i'm ESP8266</h1>
    </body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(5)

led = machine.Pin(2, machine.Pin.OUT)

print('Server listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)

    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break

    print(line)

    response = html

    cl.send(response)
    cl.close()

    
    led.low()
    time.sleep(1)
    led.high()
