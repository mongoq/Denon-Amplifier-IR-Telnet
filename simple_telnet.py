# TODO: Connect to Wifi before you run this code !!!

import usocket as socket

def telnet_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 23))
    server_socket.listen(1)

    while True:
        print('Waiting for Telnet connection...')
        client_socket, client_address = server_socket.accept()
        print('Telnet connection from:', client_address)
        client_socket.sendall(b'\nWelcome to the Denon Amplifier IR Telnet Server!\r\n\n')
        #client_socket.sendall(b'Set Volume absolute: "setvabs(xyz)" ...\r\n')
        #client_socket.sendall(b'Set Volume relative: "setvrel(xyz)" ...\r\n')
        client_socket.sendall(b'Power on: "setpon" ...\r\n')
        client_socket.sendall(b'Power off: "setpoff" ...\r\n')
        #client_socket.sendall(b'Switch Input Mode to Bluetooth: "bt" ...\r\n')
        #client_socket.sendall(b'Switch Input Mode to Xbox 360: "xbox" ...\r\n')
        client_socket.sendall(b'Exit: "quit" ...\r\n\r\n')
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            if str(data) == str(b'setpon\r\n'):
                client_socket.sendall(b'Powering Denon Amplifier up ...\r\n')
                print("Power up!")
                
            if str(data) == str(b'setpoff\r\n'):
                client_socket.sendall(b'Powering Denon Amplifier down ...\r\n')
                print("Power down!")
            if str(data) == str(b'quit\r\n'):
                break
        client_socket.close()

telnet_server()
