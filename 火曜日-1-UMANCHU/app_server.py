from package import model
import socket
print("あなたのIPアドレスがP1として登録されました。続けて、他のユーザのIPアドレスもコピーアンドペーストで登録してください。")
model = model.Model([socket.gethostbyname(socket.gethostname()),input("P2のIPアドレスを登録してください"),input("P3のIPアドレスを登録してください"),input("P4のIPアドレスを登録してください")],[input("あなたを表すアルファベット3文字を入力してください"),input("P2を表すアルファベット3文字を入力してください"),input("P3を表すアルファベット3文字を入力してください"),input("P4を表すアルファベット3文字を入力してください")])
model.run()
