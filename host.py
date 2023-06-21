import PySimpleGUI as sg
import ftplib
import webbrowser
import argparse


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--host", action="store_true")
    return parser.parse_args()

def upload_file_to_ftp(file_path, ftp_host, ftp_user, ftp_password, upload_path):
    try:
        ftp = ftplib.FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)

        file = open(file_path, 'rb')

        ftp.storbinary('STOR {}/{}'.format(upload_path, file_path.split('/')[-1]), file)

        ftp.quit()
        file.close()

        return 'http://{}/{}'.format(ftp_host, file_path.split('/')[-1])
    except Exception as e:
        print('Error uploading file to FTP:', str(e))
        return None

def open_default_browser(url):
    webbrowser.open(url)

sg.theme('TealMono')
font = ('Calibri', 11)


layout = [
    [sg.Column([
        [sg.Text('IP/Domin Host:', font=font)],
        [sg.Text('Username:', font=font)],
        [sg.Text('Password:', font=font)],
        [sg.Text('Upload Path:', font=font)]
    ]),
    sg.Column([
        [sg.FileBrowse(key='-FILE-', font=font)],
        [sg.Input(key='-HOST-', size=(40, 1), font=font)],
        [sg.Input(key='-USER-', size=(20, 1), font=font)],
        [sg.Input(key='-PASS-', size=(20, 1), password_char='*', font=font)],
        [sg.Input(key='-PATH-', size=(40, 1), default_text='/home/(example)/public_html', font=font)],
        [sg.Button('Upload', key='-UPLOAD-', font=font), sg.Text('', key='-URL-', size=(20, 1), font=font)]
    ])]
]


window = sg.Window('Upload File to Host', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-UPLOAD-':
        file_path = values['-FILE-']
        ftp_host = values['-HOST-']
        ftp_user = values['-USER-']
        ftp_password = values['-PASS-']
        upload_path = values['-PATH-']

        result = upload_file_to_ftp(file_path, ftp_host, ftp_user, ftp_password, upload_path)
        if result:
            window['-URL-'].update('File link: {}'.format(result))
            open_default_browser(result)
        else:
            window['-URL-'].update('Error uploading file.')

window.close()
