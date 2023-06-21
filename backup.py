# GitHub : https://github.com/RealCuf

import argparse
import datetime
import pysftp
import os
import sys
from rich import print as rprint

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--backup", action="store_true")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.backup:
        # Prompt user for SFTP server information
        data = []
        while True:
            host = input("\n[ ] Enter S.Host (or 'q' to quit) :\n>>>> ")
            if host.lower() == 'q':
                break
            port = int(input("[ ] Enter S.Port:\n>>>> "))
            user = input("[ ] Enter S.Username:\n>>>> ")
            password = input("[ ] Enter S.Password:\n>>>> ")
            remote_path = input("[ ] Enter remote file path (Default : /etc/x-ui/x-ui.db):\n>>>> ")
            if not remote_path:
                remote_path = '/etc/x-ui/x-ui.db'

            data.append({
                "host": host,
                "port": port,
                "user": user,
                "pass": password,
                "remote": remote_path
            })

        # solar date
        date_str = datetime.datetime.now().strftime('%Y/%m/%d')

        # Work !!
        for i in data:
            # Information required to connect to the SFTP server
            hostname = i["host"]
            port = i["port"]
            username = i['user']
            password = i['pass']
            remote_path = i['remote']

            # Disable hostkey checking
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None

            try:
                # Connect to the SFTP server
                with pysftp.Connection(host=hostname, username=username, password=password, port=port,
                                       cnopts=cnopts) as sftp:
                    # Change directory to the root
                    sftp.cwd('/')

                    # Create the 'database' directory if it doesn't exist
                    if not os.path.exists('database'):
                        os.makedirs('database')

                    # Generate a unique local file name based on timestamp
                    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                    local_filename = f'x-ui_{timestamp}.db'

                    # Download the remote file
                    sftp.get(remote_path, localpath=f'database/{local_filename}')

                    rprint("[yellow]------------------------------------------------------------[/yellow]\n")
                    rprint("[green]Downloaded successfully.[/green]")
                    rprint(f"[green]Local file path[/green] : [magenta]database/{local_filename}[/magenta]")
                    rprint("\n[cyan]You can find them in the 'database' directory.[/cyan] [magenta](type : start database)[/magenta]")
                    rprint("\n[yellow]------------------------------------------------------------[/yellow]")

                    os.system("start database")


            except pysftp.AuthenticationException:
                rprint("\n[red]Incorrect login credentials.[/red]")
            except pysftp.CredentialException:
                rprint("\n[red]Missing or invalid login credentials.[/red]")
            except pysftp.SSHException as e:
                rprint("\n[red]An SSH error occurred :[/red]", str(e))
            except pysftp.ConnectionException as e:
                rprint("\n[red]Could not connect to the server :[/red]", str(e))
            except Exception as e:
                rprint("\n[red]An error occurred :[/red]\n", str(e))

            

if __name__ == '__main__':
    main()


# GitHub : https://github.com/RealCuf