# GitHub : https://github.com/RealCuf

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ping3 import ping
import json
import base64
import threading
import pyperclip


proxies = []
current_file = ""


def extract_proxy_info(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        proxies.clear()
        for line in lines:
            line = line.strip()
            if line.startswith('vmess://'):
                config_type = 'Vmess'
                proxy_info = line[8:]
                try:
                    proxy_info = base64.urlsafe_b64decode(proxy_info + '=' * (-len(proxy_info) % 4)).decode('utf-8')
                except Exception as e:
                    print(f'Error decoding Vmess proxy info: {str(e)}')
                    continue
            elif line.startswith('vless://'):
                config_type = 'Vless'
                proxy_info = line[8:]
            elif line.startswith('trojan://'):
                config_type = 'Trojan'
                proxy_info = line[9:]
            elif line.startswith('ss://'):
                config_type = 'SS'
                proxy_info = line[9:]
            elif line.startswith('ssr://'):
                config_type = 'SSR'
                proxy_info = line[9:]
            else:
                continue

            proxy_info_parts = proxy_info.split('@')
            if len(proxy_info_parts) == 2:
                address_port = proxy_info_parts[1].split('#')[0]
                address_parts = address_port.split(':')
                if len(address_parts) == 2:
                    address = address_parts[0]
                    port = address_parts[1]
                    proxies.append((config_type, address, port, line))
            elif config_type == 'Vmess':
                proxy_info_dict = json.loads(proxy_info)
                proxies.append((config_type, proxy_info_dict.get('add'), proxy_info_dict.get('port'), line))


def select_file():
    filepath = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if filepath:
        ping_proxy(filepath)


def ping_proxy(filepath=None):
    if filepath:
        extract_proxy_info(filepath)
        global current_file
        current_file = filepath

    root = tk.Tk()
    root.title('Ping Results v2.3.1')

    style = ttk.Style()
    style.theme_use('clam')

    refresh_button = ttk.Button(root, text='Refresh', command=lambda: refresh_results(root))
    refresh_button.pack(pady=10)

    result_frame = ttk.Frame(root)
    result_frame.pack(fill=tk.BOTH, expand=True)

    for index, proxy in enumerate(proxies):
        config_type, address, port, proxy_info = proxy

        result_label = ttk.Label(result_frame, text=f'{config_type} Config (Domain or IP: {address}): ')
        result_label.grid(row=index, column=0, sticky='w', padx=10, pady=5)

        response_label = ttk.Label(result_frame, text="Pinging...")
        response_label.grid(row=index, column=1, padx=10, pady=5)

        copy_button = ttk.Button(result_frame, text="Copy", command=lambda txt=proxy_info: copy_to_clipboard(txt))
        copy_button.grid(row=index, column=2, padx=10, pady=5)

        threading.Thread(target=ping_proxy_async, args=(address, response_label)).start()

    root.update_idletasks()
    root.mainloop()


    for proxy in proxies:
        config_type, address, port, proxy_info = proxy
        result = f'{config_type} Config (Domain or IP: {address}): '

        label = ttk.Label(result_frame, text=result)
        label.pack()

        response_label = ttk.Label(result_frame, text="Pinging...")
        response_label.pack()

        copy_button = ttk.Button(result_frame, text="Copy", command=lambda txt=proxy_info: copy_to_clipboard(txt))
        copy_button.pack()

        threading.Thread(target=ping_proxy_async, args=(address, response_label)).start()

    root.geometry('500x430')
    root.mainloop()


def ping_proxy_async(address, response_label):
    try:
        response_time = ping(address, timeout=1)
        if response_time is not None:
            response_time_str = '{:.0f} ms'.format(response_time * 1000)
            if response_time >= 100:
                response_time_str = '\033[91m{}\033[0m'.format(response_time_str, foreground='red')
            else:
                response_label.config(text=response_time_str, foreground='green')
        else:
            response_label.config(text="failed", foreground='red')
    except Exception as e:
        response_label.config(text="Error: {}".format(str(e)), foreground='red')


def refresh_results(root):
    root.destroy()
    ping_proxy(current_file)

def copy_to_clipboard(txt):
    pyperclip.copy(txt)

def create_gui():
    root = tk.Tk()
    root.title('VCG Pinger v2.3.1')

    style = ttk.Style()
    style.theme_use('clam')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 300
    window_height = 55
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    root.resizable(False, False)

    select_button = ttk.Button(root, text='Select File', command=select_file)
    select_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()

# GitHub : https://github.com/RealCuf
