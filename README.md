<p align="center">
  <a href="https://github.com/RealCuf/VCG-Script" target="_blank" rel="noopener noreferrer">
    <picture>
      <img width="200" height="200" src="https://i.postimg.cc/kXh9Y0TD/v-logo-yellow.png">
    </picture>
  </a>
</p>

<h1 align="center"/>Welcome to VCG Scrpit</h1>

<p align="center">
Easy To Generat With <a href="https://github.com/RealCuf/VCG-Script">V2Ray Config Generator</a> Easy Install With Few Clicks
</p>

<p align="center">This Python script downloads free V2Ray configs , which are updated everyday and include <br>( Vmess & Vless & Trojan & ShadowSocks )</p>
<p align="center">اینترنت برای همه ؛ یا هیچ‌کس!</p>
<div align=center>
  
<!-- ![GitHub all releases](https://img.shields.io/github/downloads/iDehghan/VCG-Script/total?color=white&style=for-the-badge) -->
![GitHub release (latest by date)](https://img.shields.io/github/v/release/RealCuf/VCG-Script?color=white&style=for-the-badge)
![GitHub](https://img.shields.io/github/license/RealCuf/VCG-Script?color=white&style=for-the-badge)

</div>
<hr>

### فهرست
- [معرفی](#معرفی)<br>
- [امکانات](#امکانات)<br>
- [آموزش](#آموزش) <br>
# معرفی
اسکریپت وی سی جی پروژه ایی هست که از چندین URL سابسکرایبشن مختلف ، کانفیگ هایی را دریافت میکند و برای شما تعدادی کانفیگ تصادفی که نوع آن را از قبل مشخص کرده اید نمایش میدهد و شما میتونید آن‌ کانفیگ را در یک فایل ذخیره یا QR کد برای آن‌ ها بسازید


# امکانات
:green_circle: متن باز و قابل ویرایش <br>
:green_circle: اعمال محدودیت در تعداد ساخت کانفیگ<br>
:green_circle: امکان ذخیره کانفیگ ها و ساخت QR Code<br>
:green_circle: تغییر لینک سابسکرایبشن به لینک دلخواه شما<br>
:green_circle: پشتیبانی از Vmess , Vless , Trojan , ShadowSocks<br>
:green_circle: گرفتن پینگ و تست کانفیگ ها<br>


### Telegram Channel : [VCG Script](https://t.me/VCGScript)

# آموزش

## پیش نیاز مرحله اول
- نصب داشتن Git , Python
- وارد ترمینال شوید و برای دانلود اسکریپت کافیست دستور زیر را وارد کنید
```
git clone https://github.com/RealCuf/VCG-Script.git
```
- در C:\Users\System.name میتونید به سورس کد دسترسی داشته باشید
>  
## نصب کتابخانه مرحله دوم
- پس از نصب ، دستورات پایین را وارد کنید
```
cd VCG-Script
```
```
pip install -r requirements.txt
```
## اجرای اسکریپت مرحله سوم
- پس از نصب کامل کتابخانه ها ، برای اجرای اسکریپت دستور پایین رو وارد کنید
```
python main.py
```
## آشنایی با محیط مرحله چهارم
<a><img alt="VCG" src="https://i.ibb.co/fvSQGfW/image.png"></a>
- وارد محیط اسکریپت شدید ، جدول زیر رو مطالعه کنید
- میتونید برای ساخت کانفیگ ها از دستور مورد نظر و در قسمت OPTIONS از توضیحات جدول / اسکریپت استفاده کنید
<br>

|Number of configs|Vmess configs only|Vless configs only|Trojan configs only|Save configs to a file|Save QR codes|
|:---:|:---:|:---:|:---:|:---:|:---:|
|-n| -v| -l| -t| -s| -q|
|-number| -vmess| -vless| -trojan| -save| -qr|

<br>

- بطور مثال
- معنی دستور : 10 عدد کانفیگ تروجان به همراه ذخیره کانفیگ ها + ساخت QR Code 
````
python main.py -n 10 -t -s -q
````
## ساخت کانفیگ مرحله پنجم
- سپس اطلاعات خواسته شده را وارد کنید و اینتر کنید تا مراحل ساخت انجام شود (فیلترشکن باید روشن باشد)

<a><img alt="VCG" src="https://i.ibb.co/Fxz0Jsp/Screenshot-2023-06-05-110312.png"></a>

## استفاده از Config و QRCODE ها مرحله ششم
- پس از تکمیل ساخت برای دیدن کانفیگ ها از دستورات زیر استفاده کنید
````
start conf
````
````
start qr
````
- در فولدر Conf ، کانفیگ ها در فایل txt ذخیره شدند
- در فولدر QR ، کیو آر کد کانفیگ ها ذخیره شدند
- حالا میتونید به راحتی ازشون استفاده کنید 🎁

## پینگ گرفتن مرحله هفتم
- برای پینگ گرفتن از فایل txt که حاوی تعدادی کانفیگ هست ، از دستور زیر استفاده کنید
````
python pingtester.py
````
- سپس روی Select File بزنید و در فولدر conf ، فایل txt مورد نظرتون رو انتخاب کنید

## آپدیت مرحله هشتم
- برای آپدیت اسکریپت وارد محل نصب شوید (C:\Users\System.name) و سپس فولدر VCG-Script را پاک کنید
- مجدد از دستور نصب استفاده کنید
> قبل از آپدیت از فولدر های conf و qr بک اپ بگیرید
```
git clone https://github.com/RealCuf/VCG-Script.git
``` 
## ویرایش سورس مرحله نهم
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
<br>
<br>

## Contact Developer

💎 Discord : [Cuf#5566](http://discordapp.com/users/767770096319201290)

<a href="http://www.coffeete.ir/RealCuf"><img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:180px;" /></a>

![myImage](https://media.giphy.com/media/XRB1uf2F9bGOA/giphy.gif)


## Stargazers over time

[![Stargazers over time](https://starchart.cc/iDehghan/VCG-Script.svg)](https://starchart.cc/iDehghan/VCG-Script)
