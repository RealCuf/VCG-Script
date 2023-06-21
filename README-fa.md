<p align="center">
  <a href="https://github.com/RealCuf/VCG-Script" target="_blank" rel="noopener noreferrer">
    <picture>
      <img width="200" height="200" src="https://i.postimg.cc/kXh9Y0TD/v-logo-yellow.png">
    </picture>
  </a>
</p>

<h1 align="center"/>خوش اومدید به اسکریپت وی سی جی</h1>

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

# معرفی

**اسکریپت وی سی جی پروژه ایی هست که از چندین URL سابسکرایبشن مختلف ، کانفیگ هایی را دریافت میکند و برای شما تعدادی کانفیگ تصادفی که نوع آن را از قبل مشخص کرده اید نمایش میدهد و شما میتونید آن‌ کانفیگ را در یک فایل ذخیره یا QR کد برای آن‌ ها بسازید.**

**اگر فکر می کنید این پروژه برای شما مفید است ، ممنون میشم یک ستاره بدهید** :star2:

**برای من قهوه بخر :**

- ترون USDT (TRC20) : `?`

### کانال تلگرام : [VCG Script](https://t.me/VCGScript)

<br>

# امکانات

- پشتیبانی از vless - vmess - trojan - ss - ssr
- پشتیبانی از for - xtls - tls - reality - Grpc - ws - tcp
- اعمال محدودیت در تعداد ساخت کانفیگ
- امکان ذخیره کانفیگ ها و ساخت QR Code
- تغییر لینک سابسکرایبشن به لینک دلخواه شما
- تست پینگ از کانفیگ ها
- متن باز و قابل ویرایش
- چک کردن ریالیتی در ساب ها
- پشتیبان گیری از x-ui
- اپلود فایل ها در هاست

<br>

# کلون و نصب اسکریپت

نصب داشتن Python , Git

```
git clone https://github.com/RealCuf/VCG-Script.git
cd VCG-Script
pip install -r requirements.txt
python main.py
```
> در C:\Users\System.name میتونید به سورس کد دسترسی داشته باشید

<br>

# آشنایی با محیط

جدول زیر رو مطالعه کنید!
میتونید برای ساخت کانفیگ ها از دستور مورد نظر و در قسمت OPTIONS از توضیحات جدول / اسکریپت استفاده کنید

|Number of configs|Vmess configs only|Vless configs only|Trojan configs only|Save configs to a file|Save QR codes|Reality Checker|Pingtester|x-ui Backup|Upload File
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|-n| -v| -l| -t| -s| -q| -e| -p| -b| -o|

مثال :

````
python main.py -n 10 -t -s -q
````
> معنی دستور : 10 عدد کانفیگ تروجان به همراه ذخیره کانفیگ ها + ساخت QR Code

<br>

## تمام دستورات

<details>
  <summary>برای جزئیات دستورات کلیک کنید</summary>

<br>

استفاده :  `python main.py [Options]`

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

## چک کردن ریالیتی

<details>
  <summary>برای جزئیات ریالیتی کلیک کنید</summary>

  <br>
  
   - میتوانید با افزودن یک دستور -r یا - -Reality ، کانفیگ هایی را که ریالیتی دارند ، استخراج کنید.
   ```
   python main.py -n 10 -l -r -s -q
   ```
   > معنی دستور : 10 عدد کانفیگ وی لس به همراه ذخیره کانفیگ ها + ساخت QR Code + ریالیتی

  <br>
   
</details>

<br>

## تست پینگ

<details>
  <summary>برای جزئیات پینگ کلیک کنید</summary>

  <br>
  
   - برای پینگ یک فایل txt که شامل تعدادی کانفیگ است ، از دستور زیر استفاده کنید
   ```
   python main.py -p
   ```
   - سپس روی File Select کلیک کنید و در پوشه Conf ، فایل txt مورد نظر خود را انتخاب کنید

  <br>

  <a><img alt="VCG" src="https://i.ibb.co/8M8xx38/image.png"></a>
   
</details>

<br>

## آپدیت اسکریپت

<details>
  <summary>برای جزئیات آپدیت کلیک کنید</summary>

  <br>
  
   ```
   python main.py -u
   ```
   > قبل از بروزرسانی از پوشه های Database و QR Backup و  QR بک آپ بگیرید
   
</details>

<br>

## بک اپ X-ui

<details>
  <summary>برای جزئیات X-ui کلیک کنید</summary>

  <br>
  
   - برای تهیه نسخه پشتیبان از پنل از دستور زیر استفاده کنید
   ```
   python main.py -b
   ```
   - در بخش داده ها ، اطلاعات سرور خود را بنویسید
> آیپی , پورت , یوزرنیم , پسورد , مسیر فایل

  <br>
   
</details>

<br>

## ویرایش کد

<details>
  <summary>برای جزئیات ویرایش کلیک کنید</summary>

  <br>

- در بخش های DECODED_URLS , ENCODED_URLS میتونید لینک سابسکرایبشن دلخواه خودتون رو قرار بدید!
  
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

# کتابخانه های استفاده شده در پروژه

- Base64 - Datetime - OS - Random - Subprocess - Sys
- Qrcode - Requests - Rich - Argparse - Time - Git
- Tkinter - Ping3 - Threading - Pyperclip - Pysftp
- PySimpleGUI - Ftplib - Webbrowser - Shutil

<br>

# ارتباط با من
### حتماً به کانال بپیوندید و از من حمایت کنید

😶‍🌫️ Twitter : [CybrDriver](https://twitter.com/CybrDriver) -
Channel : [Telegram](https://t.me/VCGScript)

![myImage](https://media.giphy.com/media/XRB1uf2F9bGOA/giphy.gif)

<br>

# Stargazers over time
<!---![GitHub View](https://views.whatilearened.today/views/github/RealCuf/VCG-Script.svg)--->
[![Stargazers over time](https://starchart.cc/RealCuf/VCG-Script.svg)](https://starchart.cc/RealCuf/VCG-Script)
