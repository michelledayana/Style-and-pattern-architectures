import grpc
from concurrent import futures
import time

import hello_pb2
import hello_pb2_grpc

class HelloServiceServicer(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        name = request.name
        return hello_pb2.HelloResponse(message=f"Hola, {name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC corriendo en puerto 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()