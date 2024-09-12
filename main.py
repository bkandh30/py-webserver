import socket

def parse_request(request_data):
    lines = request_data.split('\r\n')
    start_line = lines[0]
    method, path, version = start_line(' ')
    return method, path, version

def get_response(path):
    responses = {
        "/": "HTTP/1.1 200 OK\r\n\r\n"
    }
    default_response = "HTTP/1.1 404 Not Found\r\n\r\n"

    return responses.get(path, default_response)


def handle_request(client_socket):
    client_socket.recv(1024)

    response = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.send(response.encode())

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server is running on port 4221...")

    try:
        while True:
            print("Waiting for connection")
            client_socket, addr = server_socket.accept()

            print(f"Connection from {addr} has been established")

            handle_request(client_socket)
            client_socket.close()
    except KeyboardInterrupt:
        print("\nServer is shutting down")
    finally:
        server_socket.close()
        print("Server has been shut down")

if __name__ == "__main__":
    main()
