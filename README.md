<p align="center">
  <a href="https://github.com/RealCuf/VCG-Script" target="_blank" rel="noopener noreferrer">
    <picture>
      <img width="200" height="200" src="https://i.postimg.cc/kXh9Y0TD/v-logo-yellow.png">
    </picture>
  </a>
</p>

<h1 align="center"/>Welcome to VCG Script</h1>

<p align="center">
	<a href="./README.md">
	English
	</a>
	/
	<a href="./README-fa.md">
	فارسی
	</a>

</p>

<p align="center">
Easy To Generat With <a href="https://github.com/RealCuf/VCG-Script">V2Ray Config Generator</a> Easy Install With Few Clicks
</p>

<p align="center">This Python script downloads free V2Ray configs , which are updated everyday and include <br>( Vmess & Vless & Trojan & ShadowSocks & ShadowSocksR )</p>
<p align="center">اینترنت برای همه ؛ یا هیچ‌کس!</p>
<div align=center>
  
<!-- ![GitHub all releases](https://img.shields.io/github/downloads/iDehghan/VCG-Script/total?color=white&style=for-the-badge) -->
![GitHub release (latest by date)](https://img.shields.io/github/v/release/RealCuf/VCG-Script?color=white&style=for-the-badge)
![GitHub](https://img.shields.io/github/license/RealCuf/VCG-Script?color=white&style=for-the-badge)

</div>

<br>
<div align="center"> 
  <img src="https://s6.uplod.ir/i/01098/mweuncjsrnst.png" alt="screenshot" width="800" height="auto"/>
</div>  
<br>

<br>

# Introduction

**The VCG script is a project that receives the config from several different share URLs and displays some random config whose profile you specified earlier, and you can save that configuration in a file or create a QR code for them.**

**If you think this project is helpful to you, you may wish to give a** :star2:

**Buy Me a Coffee :**

- Tron USDT (TRC20) : `TDZccmYTC8AwK5vxwgbc9qPQ4VZHMkFgY4`

### Telegram Channel : [VCG Script](https://t.me/VCGScript)

<br>

# Features

- Support vless - vmess - trojan - ss - ssr
- Support for - xtls - tls - reality - Grpc - ws - tcp
- Apply limits in the number of config
- Save Configs & QR Code
- Change the subs link
- Pingtester
- Open Source
- Reality Checker
- x-ui Backup
- Upload File to Host

<br>

# Clone and Install Script

Installing Python , Git

```
git clone https://github.com/RealCuf/VCG-Script.git
cd VCG-Script
pip install -r requirements.txt
python main.py
```
> In C:\Users\System.name you can access the Source Code

<br>

# Familiarity with the environment

Read the table below!
You can use the desired command to create configs and in the OPTIONS section of the table / script description

|Number of configs|Vmess configs only|Vless configs only|Trojan configs only|Save configs to a file|Save QR codes|Reality Checker|Pingtester|x-ui Backup|Upload File
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|-n| -v| -l| -t| -s| -q| -e| -p| -b| -o|

Example :

````
python main.py -n 10 -t -s -q
````
> Command Meaning : 10 Trojan Configs with Config Save + QR Code Creation

<br>

## All Command

<details>
  <summary>Click for Command details</summary>

<br>

Usage :  `python main.py [Options]`

| Command | Alternative command               | Action                           |
| :----: | ---------------------------------- | -------------------------------- |
| `-n`  | `--number`                          | Number of Configs - Default : 5  |
| `-v`  | `--vmess`                           | Vmess Configs only               |
| `-l`  | `--vless`                           | Vless Configs only               |
| `-t`  | `--trojan`                          | Trojan Configs only              |
| `-h`  | `--shadowsocks`                     | ShadowSocks Configs only         |
| `-a`  | `--shadowsocksr`                    | ShadowSocksR Configs only        |
| `-r`  | `--reality`                         | Reality Checker                  |
| `-s`  | `--save`                            | Save Configs                     |
| `-q`  | `--qr`                              | Save QR codes                    |
| `-b`  | `--backup`                          | x-ui Backup                      |
| `-p`  | `--ping`                            | Pingtester                       |
| `-o`  | `--host`                            | Upload File to Host              |
| `-u`  | `--update`                          | Update Script                    |

</details>

<br>

## Reality Checker

<details>
  <summary>Click for  Reality details</summary>

  <br>
  
   - You can extract the config that has a Reality by adding a -r or --reality command.
   ```
   python main.py -n 10 -l -r -s -q
   ```
   > Command Meaning : 10 vless Configs with Config Save + QR Code Creation + Reality

  <br>
   
</details>

<br>

## Ping Tester

<details>
  <summary>Click for Pingtester details</summary>

  <br>
  
   - To ping a txt file that contains a number of config, use the following command
   ```
   python main.py -p
   ```
   - Then tap Select File and in the conf folder, select the txt file you want

  <br>

  <a><img alt="VCG" src="https://i.ibb.co/8M8xx38/image.png"></a>
   
</details>

<br>

## Update Script

<details>
  <summary>Click for Update details</summary>

  <br>
  
   ```
   python main.py -u
   ```
   > Backup conf and qr and database folders before updating
   
</details>

<br>

## X-ui Backup

<details>
  <summary>Click for  XuiBackup details</summary>

  <br>
  
   - Use the following command to back up the panel
   ```
   python main.py -b
   ```
   - In the data section, write your server information
> ip , port , user , password , remote_path

  <br>
   
</details>

<br>

## Edit Source

<details>
  <summary>Click for Edit details</summary>

  <br>

- In the DECODED_URLS sections, ENCODED_URLS you can choose your favorite Subscribtion link!
  
```python
# URLs for configs not encoded in a base64 string
DECODED_URLS = [
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.fastgit.org/ripaojiedian/freenode/main/sub",
]

# URLs for configs encoded in a base64 string
ENCODED_URLS = [
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/trojan.txt",
]
```
   
</details>

<br>

# Libraries used in the project

- Base64 - Datetime - OS - Random - Subprocess - Sys
- Qrcode - Requests - Rich - Argparse - Time - Git
- Tkinter - Ping3 - Threading - Pyperclip - Pysftp
- PySimpleGUI - Ftplib - Webbrowser - Shutil

<br>

# Contact Developer
### Be sure to join the channel and support us

😶‍🌫️ Twitter : [CybrDriver](https://twitter.com/CybrDriver) -
Channel : [Telegram](https://t.me/VCGScript)

![myImage](https://media.giphy.com/media/XRB1uf2F9bGOA/giphy.gif)

<br>

# Stargazers over time
![GitHub View](https://views.whatilearened.today/views/github/RealCuf/VCG-Script.svg)
[![Stargazers over time](https://starchart.cc/RealCuf/VCG-Script.svg)](https://starchart.cc/RealCuf/VCG-Script)
