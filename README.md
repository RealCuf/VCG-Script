<p align="center">
  <a href="https://github.com/RealCuf/V2Ray-Config-Downloader" target="_blank" rel="noopener noreferrer">
    <picture>
      <img width="200" height="200" src="https://i.ibb.co/khZMnP5/R-Copy.png">
    </picture>
  </a>
</p>

<h1 align="center"/>Welcome to VCG Script</h1>

<p align="center">
Easy To Generat With <a href="https://github.com/RealCuf/V2Ray-Config-Downloader">VCD Script</a> Easy Install With Few Clicks
</p>

<p align="center">This Python script downloads free V2Ray configs , which are updated everyday and include vmess , Vless , and Trojan.</p>
<p align="center">اینترنت برای همه ؛ یا هیچ‌کس!</p>
<hr>

### فهرست
- [معرفی](#معرفی)<br>
- [امکانات](#امکانات)<br>
- [آموزش](#آموزش) <br>
# معرفی
اسکریپت وی سی جی پروژه ایی هست که از چندین URL سابسکرایبشن مختلف ، کانفیگ هایی را دریافت میکند و برای شما تعدادی کانفیگ تصادفی که نوع آن را از قبل مشخص کرده اید نمایش میدهد و شما میتونید آن‌ کانفیگ را در یک فایل ذخیره یا QR کد برای آن‌ ها بسازید


# امکانات
:green_circle: متن باز و قابل ویرایش <br>
:green_circle: ایجاد کانفیگ بدون محدودیت <br>
:green_circle: اعمال محدودیت در تعداد ساخت کانفیگ<br>
:green_circle: امکان ذخیره کانفیگ ها و ساخت QR Code<br>
:green_circle: تغییر لینک سابسکرایبشن به لینک دلخواه شما<br>
:green_circle: پشتیبانی از Vmess , Vless , Trojan<br>
:orange_circle: اضافه شدن ShadowSocks (به زودی)<br>
:orange_circle: گرفتن پینگ از لینک ها (به زودی)<br>

### Telegram Channel : [VCG Script](https://t.me/VCGScript)

# آموزش


- فایل ZIP دانلود شده را در دسکتاپ استخراج کنید
- نصب Python3
- نصب VsCode
## پیش نیاز مرحله اول
- وارد CMD شوید و برای استفاده کافیست دستورات زیر را وارد کنید
```
$ cd desktop/VCG-Script
$ pip install -r Requirements.txt
```
## اجرای اسکریپت مرحله دوم
- پس از نصب کتابخانه ها دستور پایین را وارد کنید
```
$ python3 main.py
```
## آشنایی با محیط مرحله سوم
<a><img alt="VCG" src="https://i.ibb.co/khjHZfH/image.png"></a>
- وارد محیط اسکریپت شدید ، جدول زیر را مطالعه کنید
> میتونید برای ساخت کانفیگ ها از دستور زیر و در قسمت OPTIONS از توضیحات جدول استفاده کنید 
````
$ python3 main.py [OPTIONS]
````
<br>

|Number of configs|Vmess configs only|Vless configs only|Trojan configs only|Save configs to a file|Save QR codes|
|:---:|:---:|:---:|:---:|:---:|:---:|
|-n| -v| -l| -t| -s| -q|
|-number| -vmess| -vless| -trojan| -save| -qr|

<br>

- بطور مثال
> معنی دستور : 10 عدد کانفیگ تروجان به همراه ذخیره کانفیگ ها + ساخت QR Code 

````
$ python3 main.py -n 10 -t -s -q
$ python3 main.py -number 10 -trojan -save -qr
````
## ساخت کانفیگ مرحله چهارم
- سپس اطلاعات خواسته شده را وارد کنید و اینتر کنید تا مراحل ساخت انجام شود (فیلترشکن باید روشن باشد)

<a><img alt="VCG" src="https://i.ibb.co/H7fYhvM/image-2023-05-18-18-35-54.png"></a>
- پس از تکمیل ساخت کانفیگ ها وارد فایل VCG-Script بشید 
- در فایل Config سرور ها در فایل txt ذخیره شدند
- در فایل QR-Code کیو آر کد کانفیگ ها ذخیره شدند
- حالا میتونید به راحتی ازشون استفاده کنید 🎁

## ویرایش سورس مرحله پنجم
- در بخش های DECODED_URLS , ENCODED_URLS میتونید لینک سابسکرایبشن دلخواه خودتون رو قرار بدید
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
<br>
<br>

## Contact Developer

💎 Discord : [Cuf#5566](http://discordapp.com/users/767770096319201290)

💎 Channel  [VCG Script](https://t.me/VCGScript)

![myImage](https://media.giphy.com/media/XRB1uf2F9bGOA/giphy.gif)

<br>
<br>



## Stargazers over time

[![Stargazers over time](https://starchart.cc/RealCuf/V2Ray-Config-Generator.svg)](https://starchart.cc/RealCuf/V2Ray-Config-Generator)

