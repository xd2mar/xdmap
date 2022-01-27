import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore

colorama.init()
print_lock = threading.Lock()

def xdmap():
    xdmap = """
 __   _______   __  __          _____  
 \ \ / /  __ \ |  \/  |   /\   |  __ \ 
  \ V /| |  | || \  / |  /  \  | |__) |
   > < | |  | || |\/| | / /\ \ |  ___/ 
  / . \| |__| || |  | |/ ____ \| |     
 /_/ \_\_____/ |_|  |_/_/    \_\_|     
"""
    hint="""
by xd2mar | Twitter:@QK9
    """       
    print(f'{Fore.CYAN+xdmap}{Fore.RED+hint}')                                                                                 

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(100)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " OPEN")
    except:
        pass

def main():
    xdmap()
    ip = input(f'{Fore.YELLOW}Enter the IP or Domain to scan : {Fore.GREEN}')
    print(f'{Fore.GREEN}[{Fore.RED}*{Fore.GREEN}]{Fore.BLUE}Checking from port {Fore.RED}1 {Fore.BLUE}to port{Fore.RED} 65535{Fore.GREEN}:')
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1,65535):
            executor.submit(scan, ip, port + 1)

if __name__ == "__main__":
     main()
print(f"""
                #<< SCAN FINISH! >>#
""")
    
