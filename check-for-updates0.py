import socket
import time
import threading

#boolean return of whether there is a valid internet connection currently
def is_connected(remote_server):
    try:
        host = socket.gethostbyname(remote_server)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        raise

#checks for internet and updates every (timeout) seconds
def looping_update_check(remote_server, timeout):
    connected = False
    while not connected:
        try:
            connected = is_connected(remote_server)
        except:
            print("GIVE ME INTERNET")
            time.sleep(timeout)

    # DO SOMETHING
    print('CHECK FOR DOWNLOAD HERE')

    time.sleep(timeout)
    looping_update_check(remote_server, timeout)

#chcecks for updates every 5 seconds as separate thread
def async_update(remote_server, timeout):
    def worker():
        looping_update_check(remote_server, timeout)
        return
    threading.Thread(target=worker).start()

async_update("www.google.com", 5) #replace with server target
print(4)
