import socket
import json


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024).decode("utf-8").strip()
            if data:
                headers_dict: dict = {}
                headers = data.split(sep="\r\n")
                for i, header in enumerate(headers):
                    if i == 0:
                        continue
                    header_key = header.split(sep=":")[0].strip()
                    header_value = header.split(sep=":")[1].strip()
                    headers_dict[header_key] = header_value

                conn.send(f"HTTP/1.1 200 OK\n"
                          f"Content-Length: 100\n"
                          f"Connection: close\n "
                          f"Content-Type: application/json\n"
                          f"\n {json.dumps(headers_dict)}".encode("utf-8"))
                break
