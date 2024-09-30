Bash Description:

In short, this piece of code or group of codes should install the Midori browser (an older version), MagicMirror, and Node.js on Armbian. At least I can confirm that it works for MagicMirror. With some minor adjustments, it can be adapted for other operating systems as well!

Python Description:

For the Python side, this was my last term project, and it worked on a Raspberry Pi. Unfortunately, I’ve forgotten some of the details over time. However, I wrote down the Python code, so here we are!

Known Issues/Things to Oversee:

I think there are some issues with Armbian, or maybe I have some misconfigurations. I can't change directories (cd) when using mm.sh, so I can't troubleshoot that.

MagicMirror-Configure:

For configuration, refer to the MagicMirror page.

Usage of Python Scripts:

Using the Python scripts is straightforward. The OpenCV functionality works well—detecting faces and triggering their corresponding MagicMirror-configured bash scripts. For this copy and use fdx.sh. 

Now, how does this work? And how does it stop?

Let’s assume you install everything and want to use it like a real magical mirror, as in the tales. We’re here for that, right? There will be many copy (cp) commands, which will take some time, but it’ll be fun—don’t worry!

First, get your pictures into the "friends" folder.
Second, copy and rename codes in face.py. (for each friend)
Third, copy and paste fdx.sh, renaming them as (fd1.sh, fd2.sh, etc.). 
Fourth, if you’re using different configs for MagicMirror, make sure the fdx.sh scripts are correct. (and used in face.py)
Fifth, since you have opened face detection, and MagicMirror and the browser are working, you may want to get the LCD working. For that, you’ll need GPIO code to control a relay (I think it's in reboot.py).
Sixth, where were we? Ah, I remember—closing. Let’s count fingers, right? There’s a .py for that, and I’ll change the names and organize them into folders for easy use.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

git clone https://github.com/mahmut26/mm-f

chmod +x mm-f

cd mm-f

sh browser1.sh ile çalışıyor

her birinde kabul gerekli

iei - midori yukler
node node yükler 
mm de sadece git clone var ! 
iei, node ve mm ile yükleme yapılıyor 


sistemi anlat ufaktan tamam burası !!

