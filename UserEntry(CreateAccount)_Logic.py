A = open("User_Information.txt", "a")

username = input("")
password = input()
A.write(f"{username}~{password}\n")
A.close()
