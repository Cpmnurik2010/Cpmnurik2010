debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')



import os,sys,random,requests



def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        


try:
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    
#text = """
#< [ Telegram Ewan_Ali ] > X < [ TikTok Ewan.Shex.Ali ] >"""[1:]


banner = r"""



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠶⠶⠚⠛⠛⠛⠛⠛⠛⠛⠷⠶⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⣀⠄⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⡤⠤⠤⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠏⠀⢀⣀⣠⣶⠟⠁⠀⠀⠀⣠⠴⠀⢀⠔⠋⢁⠎⠀⡇⠘⡄⠉⠲⣍⠑⠢⢄⡀⠀⠀⠀⠙⣷⣦⣤⡀⠀⠙⣷⡀⠀⠀⠀
⠀⠀⢀⣾⠃⠀⣴⠏⣼⡿⣣⠀⠀⢀⡴⠋⠠⢄⡴⠃⠀⠀⡞⠀⠀⠃⠀⠹⡄⠀⠈⢳⡀⠤⠘⠢⡀⠀⠀⢾⢻⣷⡘⣦⡀⠈⢿⡄⠀⠀
⠀⠀⣾⠁⣠⢺⣿⢘⣭⣾⠃⠀⡰⠋⠀⠀⢀⡜⠁⠁⠀⢺⠀⣴⣞⡳⣶⡄⠁⠀⠉⠀⠱⡄⠀⠀⠈⠢⡀⠈⢷⣬⡓⢻⣷⢦⠈⢿⡄⠀
⠀⣼⠃⢰⡇⢸⣷⡿⢻⠁⢀⠞⠀⠀⠀⠀⡜⠀⠀⠀⠀⠈⠀⠈⠁⣷⠿⠃⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠱⡄⠀⢿⢿⣾⡿⢸⣧⠈⣷⠀
⢠⡟⠀⣾⣿⢸⣫⣶⠇⠀⡞⠀⠀⠒⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠃⠠⠀⠀⠀⢹⡀⠘⣷⣌⠧⢸⣿⠀⢸⡇
⣼⡇⣰⢻⣿⣸⡿⠋⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⢸⣿⣧⣼⡿⢀⠀⣷
⣿⠀⣿⡀⢿⡟⢡⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠸⣆⠻⣿⠃⣼⠀⢿
⣿⠀⢿⣷⠘⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡟⠀⣹⣯⡁⢸⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⢿⣦⠙⣼⣿⠀⢸
⣿⠀⠘⣿⣇⣿⡏⡄⠀⣄⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⠃⠀⢰⣇⠀⠀⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⢸⠁⢀⠸⣿⢰⣿⠇⠀⣾
⢻⡇⣷⡈⢻⣿⢀⣿⠀⢸⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⠀⢠⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⡾⠀⣼⡆⢿⡿⠃⣼⠀⣿
⠘⣧⠘⣿⣦⡙⢸⣿⣦⡀⢣⠀⡠⠤⠒⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⠒⠢⠤⣀⣰⠁⡰⣿⡇⢚⣴⣾⠏⢸⡇
⠀⢻⡄⢈⠻⣿⣼⣿⡇⣷⡈⢦⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⡰⢃⣼⠁⣿⣧⣾⡿⡃⢀⡿⠀
⠀⠈⢿⡀⢷⣌⠛⢿⣧⢸⣷⡀⠑⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠜⠁⣼⡟⢸⡿⠟⣉⡴⠃⣼⠃⠀
⠀⠀⠈⢿⡄⠻⢿⣶⣬⣁⢿⣧⢳⣄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⡖⣹⣿⢃⣥⣴⣾⠟⢁⣼⠃⠀⠀
⠀⠀⠀⠈⢻⣆⠀⢝⠻⠿⢿⣿⣦⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿⡿⠿⠟⣋⠁⢠⡾⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⡀⠙⠶⣶⣤⣤⣥⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣼⣥⣤⣶⡶⠛⢁⣴⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⢦⣀⠀⢭⣉⣙⣉⣉⣁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⣉⣉⣋⣉⡩⠁⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣤⡈⠙⠛⠻⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⢉⣠⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣄⣀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀


⠀⠀
                   █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
                   █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄
                       
                   𝙲𝙰𝚁 𝙿𝙰𝚁𝙺𝙸𝙽𝙶 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙰𝚈𝙴𝚁
                         𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁                                 
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.red_to_yellow, pyColorate.Vertical, enter=True)


#pyAnime.Fade(pyCenter.Center(text), pyColors.purple_to_red, pyColorate.Vertical, enter=True)
#print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))

pySystem.Clear()

#print("\n"*2    )
#print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
#print("\n"*2)





#پرسیار و وەڵام 
#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#print("Hello "+name)
#print("You are "+str(age)+" years old")
#print("You are "+str(height)+"cm tall")




from pystyle import Box
import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate
from pystyle import Center
import datetime

from cpmewan1999 import CPMEwan1999

__CHANNEL_USERNAME__ = "Ewan1999Kurd"
__GROUP_USERNAME__   = "Ewan19_99Kurd"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "       ▄████▄   ██▓███   ███▄ ▄███▓▓█████  █     █░ ▄▄▄       ███▄    █ \n"
    brand_name += "       ▒██▀ ▀█  ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓█░ █ ░█░▒████▄     ██ ▀█   █ \n"
    brand_name += "       ▒▓█    ▄ ▓██░ ██▓▒▓██    ▓██░▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██  ▀█ ██▒\n"
    brand_name += "       ▒▓▓▄ ▄██▒▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██▒  ▐▌██▒\n"
    brand_name += "       ▒ ▓███▀ ░▒██▒ ░  ░▒██▒   ░██▒░▒████▒░░██▒██▓  ▓█   ▓██▒▒██░   ▓██░\n"
    brand_name += "       ░ ░▒ ▒  ░▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ▒ ▒ \n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '─══════════════════════════════════════☆☆══════════════════════════════════════─'))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.DoubleCube("𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋"))))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃")))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f" 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}")))
    
    print(Colorate.Horizontal(Colors.rainbow, '─══════════════════════════════════════☆☆══════════════════════════════════════─'))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '─══════════[ 𝙿𝙻𝙰𝚈𝙴𝚁 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 ]══════════─'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'📍Name   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'📍LocalID: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'📍Money  : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'📍Coins  : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '─═════════════[ 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 ]══════════════─'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Access Key : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Telegram ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Balance $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} CANNOT BE EMPTY OR JUST SPACES, PLEASE TRY AGAIN'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '─═════════════[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]═════════════─'))
    now = datetime.datetime.now()
    print(Colorate.Horizontal(Colors.rainbow, (now.strftime("📍DateTime: %d-%m-%Y %H:%M:%S"))))
    print(Colorate.Horizontal(Colors.rainbow, f'📍Country : {data.get("country")}.'))    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Region  : {data.get("regionName")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'📍City    : {data.get("city")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '─═══════════════[ 𝐌𝐄𝐍𝐔 ]═══════════════─'))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] ACCOUNT EMAIL[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] ACCOUNT PASSWORD[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] ACCESS KEY[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] TRYING TO LOGIN[/bold cyan]: ", end=None)
        cpm = CPMEwan1999(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN'))
                print(Colorate.Horizontal(Colors.rainbow, '! NOTE: MAKE SURE YOU FILLED OUT THE FIELDS'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]
            print(Colorate.Horizontal(Colors.rainbow, '➩{01}: Increase Money            1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{02}: Increase Coins            3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{03}: King Rank                 3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{04}: Change ID                 2.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{05}: Change Name               1.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{06}: Change Name (Rainbow)     1.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{07}: Number Plates             2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{08}: Account Delete            FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{09}: Account Register          FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{10}: Delete Friends            5.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{11}: Unlock Paid Cars          3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{12}: Unlock all Cars           4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{13}: Unlock all Cars Siren     3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{14}: Unlock w16 Engine         3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{15}: Unlock All Horns          3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{16}: Unlock Disable Damage     2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{17}: Unlock Unlimited Fuel     2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{18}: Unlock All Wheels         2.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{19}: Unlock House 3            2.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{20}: Unlock Smoke              2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{21}: Change Race Wins          7.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{22}: Change Race Loses         7.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{23}: Speed Car Hack (Car_ID)   1.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{24}: Speed All Cars Hack       2.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '➩{25}: Chrome All Cars           3.500K'))            
            print(Colorate.Horizontal(Colors.rainbow, '➩{26}: All Cars Max Milage       2.000K'))                        
            print(Colorate.Horizontal(Colors.rainbow, '➩{27}: Clone Account             5.000K'))            
            print(Colorate.Horizontal(Colors.rainbow, '➩{00}: Exit'))
            
            print(Colorate.Horizontal(Colors.rainbow, '─═══════════════[ 𝐂𝐏𝐌☆ ]═══════════════─'))
            
            service = IntPrompt.ask(f"[bold][?] SELECT A SERVICE[red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '================[ 𝐂𝐏𝐌☆ ]================'))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))



            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH MONEY DO YOU WANT'))
                amount = IntPrompt.ask("[?] AMOUNT")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)



                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH COINS DO YOU WANT'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)



                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] NOTE:[/bold red]: IF THE KING RANK DOESN'T APPEAR IN GAME, CLOSE IT AND OPEN FEW TIMES", end=None)
                console.print("[bold red] [!] NOTE:[/bold red]: PLEASE DON'T DO KING RANK ON SAME ACCOUNT TWICE", end=None)
                sleep(2)
                console.print("[%] GIVING YOU A KING RANK: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)



                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW ID'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID ID'))
                    sleep(2)
                    continue



            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW NAME'))
                new_name = Prompt.ask("[?] NAME")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW RAINBOW NAME'))
                new_name = Prompt.ask("[?] NAME")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 7: # Number Plates
                console.print("[%] GIVING YOU A NUMBER PLATES: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] AFTER DELETING YOUR ACCOUNT THERE IS NO GOING BACK'))
                answ = Prompt.ask("[?] DO YOU WANT TO DELETE THIS ACCOUNT", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                else: continue



            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] REGISTRING NEW ACCOUNT'))
                acc2_email = prompt_valid_value("[?] ACCOUNT EMAIL", "Email", password=False)
                acc2_password = prompt_valid_value("[?] ACCOUNT PASSWORD", "Password", password=False)
                console.print("[%] CREATING NEW ACCOUNT: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFO: IN ORDER TO TWEAK THIS ACCOUNT WITH Ewan_Kurdish.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'YOU MOST SIGN-IN TO THE GAME USING THIS CCOUNT'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'THIS EMAIL IS ALREADY EXISTS'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 10: # Delete Friends
                console.print("[%] DELETING FRIENDS: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 11: # Unlock All Paid Cars
                console.print("[!] NOTE: THIS FUNCTION TAKES A WHILE TO COMPLETE, PLEASE DON'T CANCEL", end=None)
                console.print("[%] UNLOCKING ALL PAID CARS: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 12: # Unlock All Cars
                console.print("[%] UNLOCKING ALL CARS: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 13: # Unlock All Cars Siren
                console.print("[%] UNLOCKING ALL CARS SIREN: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 14: # Unlock w16 Engine
                console.print("[%] UNLOCKING W16 ENGINE: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 15: # Unlock All Horns
                console.print("[%] UNLOCKING ALL HORNS: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 16: # Disable Engine Damage
                console.print("[%] UNLOCKING DISABLE DAMAGE: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 17: # Unlimited Fuel
                console.print("[%] UNLOCKING UNLIMITED FUEL: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 18: # Unlock Car Wheels
                console.print("[%] UNLOCKING All Wheels: ", end=None)
                if cpm.unlock_car_wheel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                  



            elif service == 19: # Unlock House 3
                console.print("[%] UNLOCKING HOUSE 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 20: # Unlock Smoke
                console.print("[%] UNLOCKING SMOKE: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 21: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you win.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] CHANGING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 22: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] INSERT HOW MUCH RACES YOU LOSE'))
                amount = IntPrompt.ask("[?] AMOUNT")
                console.print("[%] CHANGING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE USE VALID VALUES'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 23: # Hack Car Speed (299hp)
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[?] CAR ID")
                console.print("[%] HACKING CAR SPEED: ", end=None)
                if cpm.hack_car_speed(car_id):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    console.print("==================================")
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[!] THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 24: # Hack All Car Speed 99hp
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))            
                console.print("[%] HACKING ALL CARS SPEED: ", end=None)
                if cpm.hack_car_sexo():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 25: # Chrome All Cars
                print(Colorate.Horizontal(Colors.rainbow, '[!] CHROME'))            
                console.print("[%] HACKING All CARS CHROME: ", end=None)
                if cpm.chrome_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue               



            elif service == 26: # ALL CARS MAX MILAGE
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL MILAGE CAN NOT BE RESTORED'))            
                console.print("[%] HACKING MILAGE: ", end=None)
                if cpm.hack_car_milage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                           



            elif service == 27: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE ENTER ACCOUNT DETALIS'))
                to_email = prompt_valid_value("[?] ACCOUNT EMAIL", "Email", password=False)
                to_password = prompt_valid_value("[?] ACCOUNT PASSWORD", "Password", password=False)
                console.print("[%] CLONING YOU ACCOUNT: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            else: continue
            break
        break
