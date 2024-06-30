This is a basic kelogger that I have created purely in python.

It consists of two parts:
- a keylogger
- and a server

This is basically how it works.

Let's assume we have some sort of access to the target's  machine whether it'd be physical or remote.
That's usually when we get to install different kind of software for persistence, privilege escalation etc ...

We then get the keylogger.py script onto the target's machine preferably in a folder wheich we have writable rights to
in case we do not have higher privileges.

At that point we should have already started the server.py script that should be running on the attacker's box 
listening for incoming post requests.


![Screenshot at 2024-06-30 20-11-05](https://github.com/sp3c1fic/keylogger/assets/80251840/7fa8c30c-e982-4758-a825-bdaffc965eb9)
