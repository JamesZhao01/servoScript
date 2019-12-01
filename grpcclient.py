import component_pb2 as comp
import component_pb2_grpc as grpcs
import grpc
import time

channel = grpc.insecure_channel('localhost:50051')
stub = grpcs.RotateStub(channel)

future = stub.Rot(comp.Data(angle1=120, angle2=120))

print(future)