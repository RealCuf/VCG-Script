# GitHub : https://github.com/RealCuf

import os
import argparse
from git import Repo
import shutil
from rich import print as rprint

COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

def update_project(repo_url, project_dir):
    # Remove the previous project directory
    if os.path.exists(project_dir):
        rprint("\n[bold yellow][ ][/bold yellow] [bold white]Removing the previous project...[/bold white]")
        shutil.rmtree(project_dir, onerror=onerror)

    # Clone the new repository
    rprint("\n[bold yellow][ ][/bold yellow] [bold white]Cloning the new repository...[/bold white]")
    Repo.clone_from(repo_url, project_dir)

    rprint("\n[bold green][ ][/bold green] [bold white]Project successfully updated.[/bold white]\n")

def onerror(func, path, exc_info):
    """
    Error handler for `shutil.rmtree`.
    If the error is due to a permission issue (Access is denied),
    it will attempt to change the file permissions and retry the operation.
    """
    import stat
    import errno
    
    # Get the exception details
    exception_class, exception, traceback = exc_info

    # Check if the error is due to a permission issue (Access is denied)
    if exception.errno == errno.EACCES:
        # Change the file permissions to allow removal
        os.chmod(path, stat.S_IWRITE)

        # Retry the operation
        func(path)
    else:
        # Re-raise the exception for other errors
        raise exception

def main():
    parser = argparse.ArgumentParser(description='Update project')
    parser.add_argument('-u', '--update', action='store_true', help='Update the project')

    args = parser.parse_args()

    if args.update:
        # New repository information
        repo_url = "https://github.com/RealCuf/VCG-Script.git"  # New repo URL

        # Get the current user's home directory
        home_dir = os.path.expanduser("~")
        
        # Set the project directory
        project_dir = os.path.join(home_dir, "VCG-Script")

        # Update the project
        update_project(repo_url, project_dir)

        os.system("python main.py")

if __name__ == '__main__':
    main()

# GitHub : https://github.com/RealCuf