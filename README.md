# About
This is a module to retrieve the user agent from the website https://useragentstring.com/pages/Browserlist/.

# How to install in termux
```
pkg install git python
pip install git+https://github.com/zelvdsk/random-ua/
```
# How to use?
```py
# Import modules
import random_ua

# Acces class
ugent = random_ua.ugent()

# Get useragent random ( can choose the number of user agents )
# print(ugent.random(amount))
# amount only integer
print(ugent.random(5))
# Output is a string in the list. Example output : ['Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20021115)', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.59.12) Gecko/20160044 Firefox/52.59.12', 'Opera/9.20 (Windows NT 5.1; U; en)', 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9', 'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.7 (KHTML, like Gecko) Iron/16.0.950.0 Chrome/16.0.950.0 Safari/535.7']

# Get the useragent by browser name ( cannot select the number of user agents )
# print(ugent.browser('browserName'))
# browserName only string
# list browserName is below
print(ugent.browser('Chrome'))
# Output is a string. Example output : Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1

```

# Browser list!
- ABrowse
- America Online Browser
- AmigaVoyager
- AOL
- Arora
- Avant Browser
- Beonex
- Browzar
- Camino
- Chimera
- Chrome
- CometBird
- Crazy Browser
- Cyberdog
- DeskBrowse
- Dillo
- Dooble
- Edge
- Elinks
- Enigma Browser
- Epiphany                              
- Firebird           
- Firefox                   
- Fireweb Navigator                 
- Flock
- Fluid
- Galeon
- HotJava
- IBrowse
- iCab
- IceCat
- Iceweasel
- Internet Explorer
- iRider
- Iron
- K-Meleon
- K-Ninja
- Kapiko
- Kazehakase
- KKman
- Konqueror
- Links
- Lobo
- Lunascape
- Lynx
- Madfox
- Maxthon
- Midori
- Minefield
- Mozilla
- NCSA_Mosaic
- NetNewsWire
- NetPositive
- Netscape
- NetSurf
- OmniWeb
- Opera
- Orca
- Oregano
- Phoenix
- Prism
- Rekonq
- Safari
- SeaMonkey
- Shiira
- SlimBrowser
- Stainless
- Sunrise
- uzbl
- w3m
- Wyzo
