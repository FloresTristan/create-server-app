import os
import subprocess


def get_latest_file(folder_path):
    # List all files in the folder
    files = [
        os.path.join(folder_path, f) for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    # If no files are found, return None
    if not files:
        return None

    # Get the file with the latest modification time
    latest_file = max(files, key=os.path.getmtime)
    return latest_file


def getLatestWheel():
    cwd = os.getcwd()
    wheelFolder = cwd + '\\dist'
    latestFile = get_latest_file(wheelFolder)
    return latestFile


process = subprocess.run('pip uninstall ' + getLatestWheel() + ' -y',
                         shell=True,
                         check=True,
                         text=True)
process = subprocess.run('pip install ' + getLatestWheel(),
                         shell=True,
                         check=True,
                         text=True)
