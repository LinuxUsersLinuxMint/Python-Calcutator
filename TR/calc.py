#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

command=input('calc> ')
about= "Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
if command=="calc":
    print("calc> Girebileceğiniz işlemler: ")
    print("top\ncık\n\carp\nbol\nyuzde\nabout")
    sayi1=input('calc> 1.sayiyi giriniz: ')
    sayi2=input('calc> 2.sayiyi giriniz: ')
    islem=input('calc> Gerçekleştirmek istediğiniz işlemi giriniz: ')
    top=float(sayi1)+float(sayi2)
    cık=float(sayi1)-float(sayi2)
    carp=float(sayi1)*float(sayi2)
    bol=float(sayi1)/float(sayi2)
    yuzde=float(sayi1)%float(sayi2)
    if islem=="top": 
       print("{0} + {1} = {2}". format(sayi1,sayi2,top))  
    if islem=="cık":
       print("{0} - {1} = {2}". format(sayi1,sayi2,cık))
    if islem=="carp":
       print("{0} * {1} = {2}". format(sayi1,sayi2,carp))
    if islem=="bol":
       print("{0} / {1} = {2}". format(sayi1,sayi2,bol))
    if islem=="yuzde":
       print("{0} % {1} = {2}". format(sayi1,sayi2,yuzde))
if command=="about":
   print(about)
if command=="exit":
   exit()
if command=="help":
   print("Python calc Help")
   print("\n Command: calc , about , help , exit , git-address , web-site , ver , licence")
if command=="git-address":
   print("Github Link: https://github.com/LinuxUsersLinuxMint")
if command=="web-site":
   print("linuxuserslinuxmint.github.io")
if command=="ver":
   print("Sürüm: 0.1.5.2 (Son Güncellenme Tarihi 6 Eylül , 2023 , 18:10)")
if command=="licence":
   print("This Software is protected under the GPL2 license")