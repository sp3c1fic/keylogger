This is a basic key-logger that I have created purely in python.

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

It can be extended upon.

Additional features like:

-Data encryption
-Obfuscation: Make the script undetectable
-Application Usage: Log which applications are in use and the duration of their usage.
-Website Monitoring: Track visited websites and browser activity.
-Convert to an executable.
