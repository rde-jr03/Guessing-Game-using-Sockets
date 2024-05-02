import socket

host = "localhost"
port = 7777

while True:
    s = socket.socket()
    s.connect((host, port)) 

    data = s.recv(1024)

    print(data.decode().strip())
    difficulty_choice = input("")

    s.sendall(difficulty_choice.encode())

    while True:
        user_input = input("").strip()
        s.sendall(user_input.encode())
        reply = s.recv(1024).decode().strip()
        if "Correct" in reply:
            print(reply)
            name = input("Enter your name: ") 
            s.sendall(name.encode()) 
            s.sendall(difficulty_choice.encode())  
            break
        print(reply)
        continue

    s.close()

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
