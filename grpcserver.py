import component_pb2_grpc as grpcs
import component_pb2 as comp
import grpc
import RPi.GPIO as GPIO
import time

from concurrent import futures

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p=GPIO.PWM(servoPIN, 50)
p.start(2.5)

class Servicer(grpcs.RotateServicer):
    def Rot(self, request, context):
        print(request.angle1)
        print(request.angle2)
        return comp.Status(message = "ok")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpcs.add_RotateServicer_to_server(Servicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

serve()