import socket
import sys
import os
from datetime import datetime

Server_time_ends = ['09:05','10:05','11:20','12:20','13:20','15:05','16:05','03:37']

def main():
    pass
    s = socket.socket()
    host = ''#socket.gethostname()
    s.bind((host,5000))
    s.listen(10)
    img_counter = 0
    while True:
        try:
            s.settimeout(300)
            print("WILL accept")
            sc, address = s.accept()
            print("DID  accept")
            print(address)
            f = open(os.path.join(os.getcwd(),'test', str(img_counter) + '.png'),'wb')
            img_counter += 1
            l = sc.recv(1024)
            while (l):
                f.write(l)
                l = sc.recv(1024)
            f.close()
            sc.close()



        except Exception as e:
            print ("Server DONE")
            s.close()
            raise


        # if current_time in Server_time_ends:
        #     print("###############Time_out ho gya##########")
        #     break


if __name__ == '__main__':
    main()
