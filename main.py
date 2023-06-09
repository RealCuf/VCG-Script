# GitHub : https://github.com/RealCuf

import base64
import datetime
import os
import random
import subprocess
import sys
import qrcode
import requests
from rich import print as rprint
from rich.progress import track
import argparse
import urllib.parse

# URLs for configs not encoded in a base64 string

DECODED_URLS = [
    "https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/trojan.txt",
    "https://raw.githubusercontent.com/learnhard-cn/free_proxy_ss/main/v2ray/v2raysub",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub1.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub2.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub3.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub3.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub5.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub6.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub7.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub8.txt",
]

# URLs for configs encoded in a base64 string

ENCODED_URLS = [
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
    "https://github.xiaoku666.tk/https://raw.githubusercontent.com/ripaojiedian/freenode/main/sub",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/ssr.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/ssr.txt",
    "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt",
    "https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/o/node.txt",
    "https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",    
    "https://raw.githubusercontent.com/AzadNetCH/Clash/main/V2Ray.txt",
    "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.fastgit.org/ripaojiedian/freenode/main/sub",
]

logo = r"""
____   _____________   ________ 
\   \ /   /\_   ___ \ /  _____/ 
 \   Y   / /    \  \//   \  ___ 
  \     /  \     \___\    \_\  \
   \___/    \______  /\______  /
                   \/        \/           
"""

COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
NOW = datetime.datetime.now()
config_folder = "./conf"
QR_DIR = "./qr"

def check_reality(urls):
    for url in urls:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"The link {url} is reachable and valid.")
        else:
            print(f"The link {url} is not reachable or invalid.")

def check_reality(link):
    parsed_url = urllib.parse.urlparse(link)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    if 'security' in query_params and 'encryption' in query_params:
        if query_params['security'][0] == 'reality' and query_params['encryption'][0] != 'none':
            return True
    
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--reality", action="store_true", help="Check reality of URLs")
    args = parser.parse_args()

    if args.check_reality:
        check_reality(DECODED_URLS + ENCODED_URLS)

def get_config(url):
    """Get config from URL."""

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def decode_base64(string):
    """Decode base64 encoded string."""

    try:
        decoded_string = base64.b64decode(string).decode()
        return decoded_string
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_cleaned_configs(vmess=False, vless=False, trojan=False, shadowsocks=False, shadowsocksr=False):
    """Get cleaned configs."""

    configs = []
    all_urls = DECODED_URLS + ENCODED_URLS
    for url in track(all_urls, description="Getting configs..."):
        if url in DECODED_URLS:
            config = get_config(url)
            if config:
                configs.extend(config.splitlines())
        elif url in ENCODED_URLS:
            decoded_config = decode_base64(get_config(url))
            if decoded_config:
                configs.extend(decoded_config.splitlines())

    if vmess:
        configs = [config for config in configs if "vmess" in config]
    elif vless:
        configs = [config for config in configs if "vless" in config]
    elif trojan:
        configs = [config for config in configs if "trojan" in config]
    elif shadowsocks:
        configs = [config for config in configs if "shadowsocks" in config]
    elif shadowsocks:
        configs = [config for config in configs if "shadowsocksr" in config]
    return configs


def save_configs(configs):
    """Save configs to file."""

    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    file_name = os.path.join(config_folder, f"configs_{NOW.strftime('%Y-%m-%d_%H-%M-%S')}.txt")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    rprint(f"[bold green]Config file saved to {file_name}[/bold green]")


def get_random_color(word):
    """Returns a random color wrapped around the given word."""

    random_color = random.choice(COLORS)
    return f"[{random_color}]{word}[/{random_color}]"


def get_random_config(configs, random_configs=5):
    """Returns a list of random configs from the given list of whole configs."""

    random_configs = random.sample(configs, random_configs)
    return random_configs


def save_qr_code(data):
    """Save QR codes to qr_codes directory."""

    for index, qr_data in enumerate(data, start=1):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        if not os.path.exists(QR_DIR):
            os.makedirs(QR_DIR)

        img = qr.make_image(fill_color="white", back_color="black")
        file_name = f"{QR_DIR}/{str(index).zfill(0000)}_qr_code_{NOW.strftime('%Y-%m-%d_%H-%M-%S')}.png"
        img.save(file_name)

    rprint(
        f"[bold yellow]{len(data)} QR code(s) saved to qr_codes directory.[/bold yellow]"
    )

if "-p" in sys.argv or "--ping" in sys.argv:
    subprocess.call(["python", "pingtester.py"])
    sys.exit()

def run_code():

    if len(sys.argv) == 1:
        rprint("[magenta]------------------------------------------------------------▶[/magenta]")
        rprint(logo)
        rprint("\n[bold cyan]V E R S I O N : [cyan][[/cyan][yellow]v 1.5.1[yellow][cyan]][/cyan] [bold green]GitHub : [cyan]https://github.com/RealCuf[/cyan][/bold green]\n")
        rprint("[bold cyan]U S A G E : [/bold cyan][bold magenta]python main.py[/bold magenta] [cyan][[/cyan][yellow]O P T I O N S[yellow][cyan]][/cyan]\n")
        rprint("[bold cyan]O P T I O N S : [/bold cyan]\n")
        rprint("• [yellow]-n[/yellow][blue]  --number[/blue]            〔 [green]Number of configs - Default : 5 [/green]")
        rprint("• [yellow]-v[/yellow][blue]  --vmess [/blue]            〔 [green]Vmess configs only[/green]")
        rprint("• [yellow]-l[/yellow][blue]  --vless [/blue]            〔 [green]Vless configs only[/green]")
        rprint("• [yellow]-t[/yellow][blue]  --trojan[/blue]            〔 [green]Trojan configs only[/green]")
        rprint("• [yellow]-h[/yellow][blue]  --shadowsocks[/blue]       〔 [green]ShadowSocks configs only[/green]")
        rprint("• [yellow]-r[/yellow][blue]  --shadowsocksr[/blue]      〔 [green]ShadowSocksR configs only[/green]")
        rprint("• [yellow]-s[/yellow][blue]  --save  [/blue]            〔 [green]Save configs to a file[/green]")
        rprint("• [yellow]-q[/yellow][blue]  --qr    [/blue]            〔 [green]Save QR codes[/green]")
        rprint("• [yellow]-e[/yellow][blue]  --reality    [/blue]       〔 [green]Check reality[/green]")
        rprint("• [yellow]-p[/yellow][blue]  --ping  [/blue]            〔 [green]Ping from configs[/green]\n")
        rprint("[bold cyan]E X A M P L E : [/bold cyan][bold magenta]python main.py[/bold magenta] [yellow]-n 5 -t -s -q[/yellow]")
        rprint("[bold cyan]P I N G : [/bold cyan][bold magenta]python main.py[/bold magenta] [yellow]-p[/yellow]\n")
        rprint("[magenta]------------------------------------------------------------▶[/magenta]")
        sys.exit(1)

    if "-v" in sys.argv or "--vmess" in sys.argv:
        configs = get_cleaned_configs(vmess=True)
    elif "-l" in sys.argv or "--vless" in sys.argv:
        configs = get_cleaned_configs(vless=True)
    elif "-t" in sys.argv or "--trojan" in sys.argv:
        configs = get_cleaned_configs(trojan=True)
    elif "-h" in sys.argv or "--shadowsocks" in sys.argv:
        configs = get_cleaned_configs(shadowsocks=True)
    elif "-r" in sys.argv or "--shadowsocksr" in sys.argv:
        configs = get_cleaned_configs(shadowsocksr=True)
    else:
        configs = get_cleaned_configs()

    configs_length = len(configs)
    rprint(f"[bold yellow]{configs_length} configs downloaded.[/bold yellow]\n")

    if configs_length == 0:
        rprint("[bold red]No configs found.[/bold red]\n")
        sys.exit(1)

    if "-n" in sys.argv or "--number" in sys.argv:
        try:
            config_number = int(sys.argv[sys.argv.index("-n") + 1])
        except ValueError:
            try:
                config_number = int(sys.argv[sys.argv.index("--number") + 1])
            except ValueError:
                config_number = 5
        if config_number > configs_length:
            config_number = configs_length

        random_configs = get_random_config(configs, config_number)

        if "--silent" not in sys.argv:
            for config in random_configs:
                rprint(get_random_color(config))
                rprint("")

        if "-s" in sys.argv or "--save" in sys.argv:
            save_configs(random_configs)

        if "-q" in sys.argv or "--qr" in sys.argv:
            save_qr_code(random_configs)

        rprint(f"[bold yellow]{config_number} random configs generated.[/bold yellow]\n")

if __name__ == "__main__":
    run_code()

# GitHub : https://github.com/RealCuf
