import socket

try:
    while True:
        hostname = input("Enter a hostname: ")
        try:
            ip_address = socket.gethostbyname(hostname)
            print(f"Hello! The IP address of {hostname} is {ip_address}.")
        except socket.error as e:
            print(f"Could not resolve hostname {hostname}: {e}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")