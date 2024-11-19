#!/usr/bin/env python
import sys
import argparse
from colorama import init, Fore
init()

def main():
    parser = argparse.ArgumentParser(description='Un semplice script di esempio per Skibidi')
    parser.add_argument('--name', '-n', default='World', help='Nome da salutare')
    parser.add_argument('--color', '-c', choices=['red', 'green', 'blue'], default='green', 
                        help='Colore del messaggio')
    
    args = parser.parse_args()
    
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'blue': Fore.BLUE
    }
    
    print(f"{colors[args.color]}Hello, {args.name}!{Fore.RESET}")

if __name__ == "__main__":
    main()
