# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import component_pb2 as component__pb2


class RotateStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Rot = channel.unary_unary(
        '/Rotate/Rot',
        request_serializer=component__pb2.Data.SerializeToString,
        response_deserializer=component__pb2.Status.FromString,
        )


class RotateServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Rot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RotateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Rot': grpc.unary_unary_rpc_method_handler(
          servicer.Rot,
          request_deserializer=component__pb2.Data.FromString,
          response_serializer=component__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Rotate', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
