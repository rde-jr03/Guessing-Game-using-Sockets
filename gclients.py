import socket

host = "localhost"
port = 7777

while True:
    s = socket.socket()
    s.connect((host, port))  # Connect to the server

    # Received the banner
    data = s.recv(1024)
    # Print banner and get difficulty choice from user
    print(data.decode().strip())
    difficulty_choice = input("")

    # Send difficulty choice to the server
    s.sendall(difficulty_choice.encode())

    while True:
        user_input = input("").strip()
        s.sendall(user_input.encode())
        reply = s.recv(1024).decode().strip()
        if "Correct" in reply:
            print(reply)
            name = input("Enter your name: ")  # Ask for the user's name
            s.sendall(name.encode())  # Send the user's name to the server
            s.sendall(difficulty_choice.encode())  # Send the difficulty choice to the server
            break
        print(reply)
        continue

    s.close()

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
