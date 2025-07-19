# 🩸 Python Keylogger (with Screenshot Beacon)

A lightweight keylogging implant written entirely in Python, designed for educational red team use.  
Captures keystrokes, sends logs via HTTP, and emails screenshots from compromised systems.

Includes full .exe conversion flow from Linux using Wine for cross-platform payload generation.

## 🚨 Features

- 🔑 Keylogging (stored locally + exfiltrated via POST)
- 📸 Screenshot capture every minute (emailed)
- 📤 Email-based exfiltration with timestamped filenames
- 🖥 Works on target systems with **no elevated privileges**
- 📦 Full `.exe` conversion on Linux using **Wine + PyInstaller**
- 🧱 Modular: server-side listener included

It consists of two parts:
- a keylogger
- and a server


This is basically how it works.

Let's assume we have some sort of access to the target's  machine whether it'd be physical or remote.
That's usually when we get to install different kind of software for persistence, privilege escalation etc ...

We then get the keylogger.py script onto the target's machine preferably in a folder which we have writable rights to
in case we do not have higher privileges.

At that point we should have already started the server.py script that should be running on the attacker's box 
listening for incoming [POST] requests.


![Screenshot at 2024-06-30 20-11-05](https://github.com/sp3c1fic/keylogger/assets/80251840/7fa8c30c-e982-4758-a825-bdaffc965eb9)

Once the keylogger.py script is already running on the victim's box and keystrokes are captured they get sent back to the server on the attacker's machine. They also get saved into a .txt file



![Screenshot at 2024-06-30 20-12-08](https://github.com/sp3c1fic/keylogger/assets/80251840/28159171-20d1-4948-91b6-ecb3bf66a40a)

The image below shows precisely the entire POST request that has been received from the client i.e. keylogger.py and 
how the keystrokes are captured and sent in json format alongside the request itself. 

![Screenshot at 2024-06-30 20-15-01](https://github.com/sp3c1fic/keylogger/assets/80251840/46207240-47ee-4de3-b8e6-fd9bf052dfa8)


In the next image you can see that the image has also been sent via email. The name of the image contains the date and time of the caputre.

The images are captured and sent via email every minute.This could be changed in the code itself.

![Screenshot at 2024-06-30 20-15-08](https://github.com/sp3c1fic/keylogger/assets/80251840/1d92c4c9-9543-44bd-a06a-6b373e53a52e)


HOW TO USE IT:

You need two emails one to send the image from and another to receive it.

Required Libraries and versions.

- Python 3.x
- Pillow
- smtplib****

Update the email configuration in keylogger.py with your SMTP server details and login credentials.

Run the server.py on the attacker's machine

Run the keylogger.py on the victim's machine.

ENJOY.

DISCLAIMER

This project is for educational purposes only. I am not responsible for any unauthorized use of this software.
It is a proof of concept.


CONVERTING TO AN .EXE FROM A LINUX MACHINE

Typically if u want to convert a .py file to an executable for a corresponding OS you will need to do it on the exact OS itself.
However in a scenario where hyphotetically we will be "capturing keystrokes" on a WIN machine and only have access to the attacker's machine i.e ours, it'd be running Linux.

So here I will show you how to convert a .py file to an .exe straight up on a Linux machine using Wine

Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.

https://www.winehq.org/ 

I will not be going over the installation process of wine. All you need you can find on the wine website.

First thing's first.

We need to go https://www.python.org/downloads/windows/ and download a windows version of python.
For this I used python-3.11.4.exe

Once the installer is downloaded we need to run it using wine.

Before that however make sure u run the winecfg command and select an appropriate version of windows.
The default one is Windows 7 and this will throw an error when trying to open the installer 

![Screenshot at 2024-07-31 23-20-33](https://github.com/user-attachments/assets/2fc4c4c4-1a5a-4aec-b195-09978449b05a)

After that simply run the installer 

![Screenshot at 2024-07-31 23-19-43](https://github.com/user-attachments/assets/6055da33-7f53-4461-832c-91950d07ab43)

Next thing is to install pip in order to install pyinstaller afterwards.

PyInstaller is what will be used for the .exe conversion.

This is where get-pip.py can be downloaded from - https://bootstrap.pypa.io/get-pip.py

Once that's dealt with, it has to be run.

![Screenshot at 2024-07-31 23-31-36](https://github.com/user-attachments/assets/cb9f3e20-d5f5-46a3-8332-2f3ec01bd3b9)

Once pip is installed, next thing that needs to be done is the pyinstaller installation.


![Screenshot at 2024-07-31 23-34-26](https://github.com/user-attachments/assets/c39c864c-02bc-4a4f-ba30-940b6d531adb)


!!! In order to run these commands though you must be in the python directory of wine !!! - ./wine/drive_c/users/<your_username>/AppData/Local/Programs/Python/Python*version* !!!

Now that all of this is done only thing that's left is to convert the keylogger.py to .exe

!!! Before that however all the necessary dependencies must be installed otherwise the file will most likely throw errors upon execution !!!

The dependencies needed for this script are as follows:
  - pynput
  - pillow
  - screeninfo
  - requests

if there are any other dependencies that you might be missing or think that something else might be necessary make sure to install it.

![Screenshot at 2024-07-31 23-42-32](https://github.com/user-attachments/assets/c6688e74-7842-41ed-8756-7f991f53379e)

The last step is to actually convert the script to .exe:

After the conversion there will be two folders. build and dist. The .exe could be found inside the dist folder.

![Screenshot at 2024-07-31 23-45-15](https://github.com/user-attachments/assets/77ce9145-9a20-44ab-80b9-842a378db127)


From there on it is up to you and your social engineering skills to actually distribute the malware.

(Don't forget to make the neccessary tweaks in the script before all the previous step.)

Changing emails, credentials.
Also change the ip of the server depending on whether it'd be running on LAN or WAN (Port forwarding will be crucial for WAN)

> ⚠️ **DISCLAIMER**  
> This project is provided for **educational and authorized security research only**.  
> The developer is **not responsible** for any misuse, unauthorized deployment, or unethical application of this tool.

It can be extended upon.

Additional features like:

-Data encryption

-Obfuscation: Make the script undetectable

-Application Usage: Log which applications are in use and the duration of their usage.

-Website Monitoring: Track visited websites and browser activity.
