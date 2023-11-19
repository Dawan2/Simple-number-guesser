import random
import time
import os
from colorama import Fore, init, Style

os.system('clear')

init(autoreset=True)
randomnum = random.randint(1,1000)
tries = 0
lower_bound = 1
upper_bound = 1000

def clear_screen():
    os.system('clear')

while True:
  try:
    choice = int(input(f"{Fore.BLUE}PICK A NUMBER {lower_bound}-{upper_bound}{Style.RESET_ALL}: "))
    
    if choice < lower_bound or choice > upper_bound:
      print(f"{Fore.RED}CHOOSE A NUMBER BETWEEN {lower_bound}-{upper_bound}")
      time.sleep(1)
      clear_screen()
    elif choice == randomnum:
      tries += 1
      print(f"{Fore.GREEN}YOU WON YOU GUESSED {Style.RESET_ALL}{randomnum}{Fore.GREEN} IN {Style.RESET_ALL}{tries}{Fore.GREEN} TRIES!")
      break
    elif choice < randomnum:
      tries += 1
      lower_bound = choice + 1
      print(f"{Fore.RED}TOO LOW")
      time.sleep(1)
      clear_screen()
    elif choice > randomnum:
      tries += 1
      upper_bound = choice - 1
      print(f"{Fore.RED}TOO HIGH")
      time.sleep(1)
      clear_screen()
        
  except ValueError:
    print(f"{Fore.RED}WRONG INPUT")
    time.sleep(1)
    clear_screen()
  except KeyboardInterrupt:
    print(f"{Fore.RED}WRONG INPUT")
    time.sleep(1)
    clear_screen()
