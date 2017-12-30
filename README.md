# EOT
Have you ever tried to look the contents of an image without any graphical software or a GUI without succeeding? Yes, me too. Through the history of humankind have the humans been unable to perform these kind of actions without a GUI. Well, this is about to change.
Introducing: 
## The EOT
### Who is He?
The EOT is a python script created by Kaappo Raivio in 2017. He can look for an image and, display its contents using unicode block characters for luminance control and ASCII escape sequences for color control.
### How Does one exploit Him?
Basically, you download the script shown in the master branch, and exploit him with the same care as shown in the following illustration:
```bash
$ python3 /path/to/the/script.py <width> /path/to/the/image.png
```
The ```<width>``` can be set first to 100, that should work fine with a full-screen terminal. He can process all kinds of path notations: /home/user/foo.png; ~/Desktop/asd.jpg; foo/goo/image.jpg
I'd suggest for creating an alias for ease of operation:
```bash
$ sudo apt install tput
```
```
alias eot='width=$(tput cols); python3 /path/to/the/script $width'
```
