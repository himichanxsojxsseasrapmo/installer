import subprocess
import sys
import os
import winreg
import requests
import sys

import ctypes
import os
import sys
import shutil
import os
import gdown
os.system('cls')
dcnmwxdr = r'C:\Windows\System32\HLTN'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

result = check_string_in_url("https://raw.githubusercontent.com/xxjsdaesoisadfsimgjomwpp/installer/refs/heads/main/uniqueid_3.0.txt", file_contentsx1)
os.system('cls')
def check_service_status(service_name):
    try:
        # Run the 'sc query' command to check the service status
        result = subprocess.run(
            ["sc", "query", service_name],
            capture_output=True,
            text=True
        )

        # Check if the command was successful
        if result.returncode != 0:
            return f""

        # Analyze the output to determine the service state
        output = result.stdout
        if "RUNNING" in output:
            state = "running"
            os.system('cls')
            print("Error, valorant anti-cheat is running.")
            input()
            exit()
        elif "STOPPED" in output:
            state = "stopped"
        else:
            state = "unknown"

        # Check the start type (manual, automatic, disabled)
        config_result = subprocess.run(
            ["sc", "qc", service_name],
            capture_output=True,
            text=True
        )

        if config_result.returncode != 0:
            start_type = f""
        else:
            config_output = config_result.stdout
            if "AUTO_START" in config_output:
                start_type = "automatic"
                os.system('cls')
                print("Error, VGC service is set to automatic.")
                input()
                exit()
            elif "DEMAND_START" in config_output:
                start_type = "manual"
            elif "DISABLED" in config_output:
                start_type = "disabled"
            else:
                start_type = "unknown"

        return f""

    except Exception as e:
        return f""


service_name = "vgc"
status = check_service_status(service_name)
print("")
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\HLTN\aespr-01232025.py"
    files_to_delete = [
        r"C:\Windows\System32\HLTN\aespr-jan-10-2025.py",
        r"C:\Windows\System32\HLTN\aespremium_nogui.bat",
        r"C:\Windows\System32\HLTN\pyarmor_runtime_000000"
    ]

    aesv3_exists = os.path.exists(aesv3_path)

    if not aesv3_exists:
        for item in files_to_delete:
            if os.path.exists(item):
                if os.path.isfile(item):
                    os.remove(item)
                    print("")
                elif os.path.isdir(item):
                    shutil.rmtree(item)
                    os.system('cls')
                    print("")
                    print("PREMIUM is updating, please don't close the window.")
                    print("")
                    print("")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\HLTN\\aespr-01232025.py"):
    print("")
    print("")
    print("")
    print("> INSTALLING PREMIUM...PLEASE WAIT...")
    print("")
    print("")
    print("")
    print("> INSTALLING PREMIUM...PLEASE WAIT...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1f5F0cv5rjrnV_zvyB27DZIqhyommyiAx", "C:\\Windows\\System32\\HLTN\\pr23.zip")
    zip_file = r'C:\Windows\System32\HLTN\pr23.zip'
    extract_dir = r'C:\Windows\System32\HLTN'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


import os
import shutil
os.system('cls')
def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")

os.system('cls')
def create_batch_file(python_command, script_name):
    directory = r"C:\Windows\System32\HLTN"
    filename = "aespremium_nogui.bat"
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        batch_content = f"@echo off\n{python_command} {script_name} || echo errorwithpath"
        os.makedirs(directory, exist_ok=True)
        with open(filepath, 'w') as file:
            file.write(batch_content)
        print(f"")
    else:
        print("")

create_batch_file("py -3.11", r"C:\Windows\System32\HLTN\aespr-01232025.py")
batch_file_path = r"C:\Windows\System32\HLTN\aespremium_nogui.bat"
os.system('cls')
import time

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print("")
        print("")
        print("")
        print("")
        print("Be patient, PREM is encrypting data to avoid ban/detection.")
        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    

countdown(5)

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")
os.system('cls')

os._exit(0)
sys.exit()
