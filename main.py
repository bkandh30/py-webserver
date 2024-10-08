import socket
import threading

def parse_request(request_data):
    lines = request_data.split('\r\n')
    start_line = lines[0]
    method, path, version = start_line(' ')
    return method, path, version

def get_response(path,headers):
    if path == "/":
        response = b"HTTP/1.1 200 OK\r\n\r\n"
    elif path.startswith("/echo/"):
        value = path.split("/echo/")[1]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(value)}\r\n\r\n{value}".encode()
    elif path.startswith("/files"):
        directory = sys.argv[2]
        filename = path[7:]
        print(directory, filename)
        try:
            with open(f"/{directory}/{filename}", "r") as f:
                body = f.read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(body)}\r\n\r\n{body}".encode()
        except Exception as e:
            response = f"HTTP/1.1 404 Not Found\r\n\r\n".encode()
    elif path == "/user-agent":
        user_agent = headers.get("User-Agent", "")
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    else:
        response = b"HTTP/1.1 404 Not Found\r\n\r\n"
    return response

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

            client_handler = threading.Thread(target=handle_request, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        print("\nServer is shutting down")
    finally:
        server_socket.close()
        print("Server has been shut down")

if __name__ == "__main__":
    main()
