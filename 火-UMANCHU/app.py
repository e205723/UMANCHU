from package import client
from package import model
from time import sleep
import socket

print("これがあなたのIPアドレスです。\n" + socket.gethostbyname(socket.gethostname()))

userInterface = client.UserInterface(input("ホストのIPアドレスをコピーアンドペーストで入力してください。自分がホストの場合は自分のIPアドレスを入力してください。"))
print("あなたがホストの場合は、別にターミナルを開いて「app_server.py」を実行してください")
userInterface.run()
pygame.quit()
