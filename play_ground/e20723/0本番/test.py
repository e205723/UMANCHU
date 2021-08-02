import model
import socket
model = model.Model([socket.gethostbyname(socket.gethostname()),socket.gethostbyname(socket.gethostname()),socket.gethostbyname(socket.gethostname()),socket.gethostbyname(socket.gethostname())],["a","b","c","d"])
model.run()
