from socket import *
import json
import RPi.GPIO as GPIO
import time


def server_program():
    servoPIN = 18
    servoPIN2 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN2, GPIO.OUT)
    GPIO.setup(servoPIN, GPIO.OUT)
    p=GPIO.PWM(servoPIN, 50)
    p2 = GPIO.PWM(servoPIN2, 50)
    p.start(6)
    p2.start(6)
    time.sleep(1.5)
    host = '192.168.137.198'
    port= 5015

    server_socket = socket(AF_INET, SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(2)


    while True:
        print("awaiting_conn")
        conn, address = server_socket.accept()

        print("conn from " + str(address))

        while True:
            data = conn.recv(1024).decode()

            if not data:
                print("break")
                break
            jsondata = json.loads(data)
            print(str(jsondata['angle1']))
            print(str(jsondata['angle2']))
            p.ChangeDutyCycle(int(jsondata['angle1']))
            p2.ChangeDutyCycle(int(jsondata['angle2']))
            time.sleep(1.5)
            conn.send("lmao".encode())
        print("end")
        conn.close()


server_program();
