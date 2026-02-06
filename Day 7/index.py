import urllib.request
import threading
import time
def download_file():
    url='http://127.0.0.1:5500/jk.txt'

    filename='downloaded_test.txt'

    print("starting download...")
    urllib.request.urlretrieve(url,filename)
    time.sleep(2)
    print("download completed.")

t=threading.Thread(target=download_file)
t.start()
print("main program continues to run...")
