# coding: UTF-8
from distutils.cmd import Command
from email.mime import base
import tkinter as tk
from turtle import goto
import webbrowser
import platform
import os
import sys
from tkinter import messagebox

if not os.name == 'nt':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')

ur = platform.uname()
print(ur.system)
print(ur.release)
print(ur.version)
print(ur.processor)

if ur.release == 'xp':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '2000':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == 'me':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '98':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '95':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')

print('FxxkDocomoApps_V2.0')
print('Developer @wakanameko2')

baseGround = tk.Tk()

if ur.release == 'vista':baseGround.geometry('600x75')
if ur.release == '7':baseGround.geometry('600x75')
if ur.release == '8':baseGround.geometry('600x75')
if ur.release == '8.1':baseGround.geometry('600x75')
if ur.release == '2012ServerR2':baseGround.geometry('600x75')
if ur.release == '10':baseGround.geometry('525x60')
#Windows11
if ur.version == '10.0.22000':baseGround.geometry('575x70')
if ur.version == '10.0.22621':baseGround.geometry('575x70')

baseGround.title('FxxkDocomoApps')

baseGround.resizable(width = False, height = False)

data = '''R0lGODlhAAEAAffgAAAAADY2Njk5OTk2NjEvL1dXV15dXFhXVkZGRntGT3dLU2dY
        WnBQVl9gYGJjZGRqbGVoaWh1eXd3d3p6emVucW00PbkcNrIWMLciO7AsOZArOs8N
        Hs4FG9ASH88GJM8KJM8HK88LLcUNLtAMLtAGK9EaJdAUK9EbK9EVJc4OMccPMNAO
        McwTMsMZNsgYNdESNNIaNNIXOdIbPNgZOs8SJ9IjLMYkOdMnONUzO8c2NrxJNLBz
        N8NEM8BUO5c1Ro07SaYqQdQfQNQkQ9MqRdUsStcnS9Y3Sdg2U9c6VcwyToZATIhA
        TIJJU7ZIWdhFTNpCXdlJVdpUXM1GVNtGYNxMZtlMZt5VbdtYZd9act5XcMxUZt1k
        bN1seN5yesxwfuFle+Fpe+F2fOBfdoyqMZq9NZS1M5CsMpuONp7CNqTJNqPGOKXK
        OaLGOZ+uUbPSV6vMR7fVYr7YccLbemt/hNV2hOJsguN3iOZ+kW2DiXKOlnKPmXST
        m3ibpn2qtn2ptXqirXC+2G+92HTC3HjF33zK5HnG4IiIiJ2dnZaUlKioqLW1tbu7
        u4aqttqKleSGi+eDleaLmOeXnOqUpOqbpeubqueboOmPoNSutOyireuprO2kse2r
        te+tue61ufCyvvG7vdaao8jeh87ik9joqt7qttvnu4K0xIS7y4e/0fG8xPG3wu+9
        wc++worH2YfBz4HP6YfO5ITT7I3T6JLb75DW7I3b9IjX8JLc85Hf+Jbl/5jo/5Xi
        +cHBwcvLy9TU1Nzc3NfY19TNyvPEzPLGyPTM0/TH0PTR1ffV2/ba3Pja3+3FyOfx
        y+rx1Pjd4vfe4ePj4+vr6+jn5vnj5vrm6frr7fbj5e/w7/X56vzv8fXv8PDw8PHx
        8fPz8/Lz8vzz9f33+P////7+/v39/f////j69N/g37/AvwAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAAAQABAAj/AAEIHEiwoMGDCBMqXMiw
        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
        vOLbfDjGM67xjXO84x7/OMhDLnLZBAQAOw==
     ''' 
baseGround.tk.call('wm', 'iconphoto', baseGround._w, tk.PhotoImage(data=data))

def btn_click():    
    label1 = tk.Label(baseGround, text='Selected Uninstall').place(x=290,y=15)
    print('selected Uninstall.')
    OAU = messagebox.askyesno('確認','おサイフケータイ機能を残しますか？')
    
    if OAU == True:
        print('selected yes')
        import subprocess
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anmane2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.accountwipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.pf.dcmippushaggregator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.pf.dcmwappush')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.applicationmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.applicationmanagersub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.accountauthenticator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.initialization')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dhome')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nextbit.app')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.store')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dmenu2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.iconcier')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.iconcier_contents')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.rwpushcontroller')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.devicehelp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mascot')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.bugreport')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.atf')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.phonemotion')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.databackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.schedulememo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.omronsoft.android.decoemojimanager_docomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.docomoset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.carriermail')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.lcsapp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.lcsappsub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.voiceeditor')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dcmvoicerecognition')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mediaplayer')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.saigaiban')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.socialphonebook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.android.contacts')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.android.homezozo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.photocollection')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.wipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anmate2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.contentsheadline')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.android.incallui.product.res.overlay')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.screenlockservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.osv.res.overlay_305')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.toruca')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.msg')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mydocomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.dbook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anshinsecurity')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.voicetranslation')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.cloudstorageservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mymagazine')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.remotelock')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.dmapnavi.navi02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.rsupport.rs.activity.ntt')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.sha2.kids')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.local.guide02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.store.appssha2')
        subprocess.call(cmd)
        print('All_Done')
        label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)

    else:
        print('selected no')
        import subprocess
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anmane2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.accountwipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.pf.dcmippushaggregator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.pf.dcmwappush')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.applicationmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.applicationmanagersub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.accountauthenticator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.initialization')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dhome')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nextbit.app')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.store')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dmenu2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.iconcier')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.iconcier_contents')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.rwpushcontroller')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.devicehelp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mascot')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.bugreport')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.atf')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.phonemotion')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.databackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.schedulememo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.omronsoft.android.decoemojimanager_docomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.docomoset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.carriermail')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.lcsapp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.lcsappsub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.voiceeditor')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dcmvoicerecognition')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mediaplayer')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.saigaiban')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.socialphonebook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.android.contacts')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.android.homezozo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.photocollection')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.wipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anmate2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.contentsheadline')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.android.incallui.product.res.overlay')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.screenlockservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.osv.res.overlay_305')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.toruca')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.msg')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mydocomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.dbook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anshinsecurity')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.voicetranslation')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.cloudstorageservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mymagazine')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.remotelock')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.dmapnavi.navi02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.rsupport.rs.activity.ntt')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.sha2.kids')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.local.guide02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.store.appssha2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.felicaremotelock')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')   
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dpoint')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.tapandpay')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.dcard')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.keitai.payment')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.id_credit_sp.android')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.felicanetworks.mfm.main')
        subprocess.call(cmd)
        print('All_Done')
        label1 = tk.Label(baseGround, text='All Done                    ').place(x=290,y=15)

def btn2_click():
    label1 = tk.Label(baseGround, text='Selected Install   ').place(x=290,y=15)
    print('selected Install.')
    import subprocess
    
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.bridgelauncher')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.anmane2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.felicaremotelock')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.accountwipe')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.pf.dcmippushaggregator')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.pf.dcmwappush')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.applicationmanager')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.applicationmanagersub')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.accountauthenticator')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.initialization')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.dhome')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nextbit.app')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.idmanager')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.store')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.dmenu2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.iconcier')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.iconcier_contents')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.rwpushcontroller')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.anshinmode')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.devicehelp')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.osaifu.tsmproxy')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.mascot')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.bugreport')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.atf')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.phonemotion')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.databackup')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.schedulememo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.tapandpay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.omronsoft.android.decoemojimanager_docomo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.cloudset')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.docomoset')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.sdcardbackup')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.carriermail')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.lcsapp')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.lcsappsub')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.voiceeditor')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.dcmvoicerecognition')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.mediaplayer')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.saigaiban')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.socialphonebook')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.android.contacts')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.android.homezozo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.dpoint')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.photocollection')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.idmanager')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.cloudset')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.wipe')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.anmate2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.contentsheadline')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.android.incallui.product.res.overlay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.screenlockservice')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.osv.res.overlay_305')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.anshinmode')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.toruca')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.msg')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.tapandpay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.sdcardbackup')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.mydocomo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.dbook')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.dcard')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.keitai.payment')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.osaifu.tsmproxy')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.id_credit_sp.android')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.anshinsecurity')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.co.nttdocomo.anshinmode')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.felicanetworks.mfm.main')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.voicetranslation')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.cloudstorageservice')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.mymagazine')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.remotelock')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.dmapnavi.navi02')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.rsupport.rs.activity.ntt')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.sha2.kids')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.local.guide02')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.store.appssha2')
    subprocess.call(cmd)
    print('All_Done')
    label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)

def btn3_click():
    label1 = tk.Label(baseGround, text='Selected Disable  ').place(x=290,y=15)
    print('selected Disable.')    
    OAD = messagebox.askyesno('確認','おサイフケータイ機能を残しますか？')

    if OAD == True:
        print('Selected Yes')
        import subprocess
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.anmane2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.accountwipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.pf.dcmippushaggregator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.pf.dcmwappush')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.applicationmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.applicationmanagersub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.accountauthenticator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.initialization')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.dhome')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nextbit.app')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.store')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.dmenu2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.iconcier')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.iconcier_contents')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.rwpushcontroller')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.devicehelp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mascot')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.bugreport')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.atf')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.phonemotion')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.databackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.schedulememo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.omronsoft.android.decoemojimanager_docomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.docomoset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.carriermail')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.lcsapp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.lcsappsub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.voiceeditor')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.dcmvoicerecognition')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mediaplayer')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.saigaiban')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.socialphonebook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.android.contacts')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.android.homezozo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.photocollection')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.wipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.anmate2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.contentsheadline')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.android.incallui.product.res.overlay')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.screenlockservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.osv.res.overlay_305')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.toruca')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.msg')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mydocomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.dbook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.anshinsecurity')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.voicetranslation')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.cloudstorageservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mymagazine')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.remotelock')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.dmapnavi.navi02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.rsupport.rs.activity.ntt')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.sha2.kids')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.local.guide02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.store.appssha2')
        subprocess.call(cmd)
        print('All_Done')
        label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)

    else:
        print('Selected No')
        import subprocess
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.anmane2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.felicaremotelock')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.accountwipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.pf.dcmippushaggregator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.pf.dcmwappush')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.applicationmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.applicationmanagersub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.accountauthenticator')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.initialization')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.dhome')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nextbit.app')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.store')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.dmenu2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.iconcier')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.iconcier_contents')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.rwpushcontroller')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.devicehelp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mascot')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.bugreport')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.atf')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.phonemotion')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.databackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.schedulememo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.tapandpay')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.omronsoft.android.decoemojimanager_docomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.docomoset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.carriermail')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.lcsapp')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.lcsappsub')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.voiceeditor')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.dcmvoicerecognition')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mediaplayer')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.saigaiban')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.socialphonebook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.android.contacts')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.android.homezozo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.dpoint')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.photocollection')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.idmanager')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.cloudset')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.wipe')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.anmate2')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.contentsheadline')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.android.incallui.product.res.overlay')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.screenlockservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.osv.res.overlay_305')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.toruca')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.msg')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.tapandpay')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mydocomo')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.dbook')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.dcard')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.keitai.payment')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.id_credit_sp.android')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.anshinsecurity')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.co.nttdocomo.anshinmode')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.felicanetworks.mfm.main')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.voicetranslation')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.cloudstorageservice')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.mymagazine')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.remotelock')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'jp.dmapnavi.navi02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.rsupport.rs.activity.ntt')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.sha2.kids')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.local.guide02')
        subprocess.call(cmd)
        cmd = ('adb', 'shell', 'pm', 'disable-user', '--user', '0', 'com.nttdocomo.android.store.appssha2')
        subprocess.call(cmd)
        print('All_Done')
        label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)

def btn4_click():
    label1 = tk.Label(baseGround, text='Selected Enable   ').place(x=290,y=15)
    print('selected Enable.')
    import subprocess
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.anmane2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.felicaremotelock')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.accountwipe')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.pf.dcmippushaggregator')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.pf.dcmwappush')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.applicationmanager')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.applicationmanagersub')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.accountauthenticator')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.initialization')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.dhome')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nextbit.app')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.idmanager')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.store')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.dmenu2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.iconcier')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.iconcier_contents')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.rwpushcontroller')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.anshinmode')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.devicehelp')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.mascot')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.bugreport')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.atf')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.phonemotion')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.databackup')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.schedulememo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.tapandpay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.omronsoft.android.decoemojimanager_docomo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.cloudset')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.docomoset')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.carriermail')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.lcsapp')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.lcsappsub')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.voiceeditor')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.dcmvoicerecognition')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.mediaplayer')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.saigaiban')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.socialphonebook')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.android.contacts')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.android.homezozo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.dpoint')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.photocollection')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.idmanager')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.cloudset')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.wipe')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.anmate2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.contentsheadline')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.android.incallui.product.res.overlay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.screenlockservice')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.osv.res.overlay_305')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.anshinmode')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.toruca')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.msg')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.tapandpay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.mydocomo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.dbook')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.dcard')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.keitai.payment')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.id_credit_sp.android')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.anshinsecurity')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.co.nttdocomo.anshinmode')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.felicanetworks.mfm.main')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.voicetranslation')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.cloudstorageservice')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.mymagazine')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.remotelock')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'jp.dmapnavi.navi02')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.rsupport.rs.activity.ntt')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.sha2.kids')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.local.guide02')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'enable', '--user', '0', 'com.nttdocomo.android.store.appssha2')
    subprocess.call(cmd)
    print('All_Done')
    label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)
    
def btn_click_adb():
    webbrowser.open('https://dl.google.com/android/repository/platform-tools_r33.0.1-darwin.zip')

if ur.release == 'vista':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=253,y=48)
if ur.release == '7':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=253,y=48)
if ur.release == '8':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=290,y=48)
if ur.release == '8.1':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=290,y=48)
if ur.release == '2012ServerR2':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=290,y=48)
#Windows10
if ur.version == '10.0.10240':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.10586':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.14393':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.15063':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.16299':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.17134':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.17763':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.18362':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.18363':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.19041':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.19042':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.19043':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.19044':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
if ur.version == '10.0.19045':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)
#Windows11
if ur.version == '10.0.22000':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=270,y=43)
if ur.version == '10.0.22621':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=270,y=43)

if ur.release == 'vista':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 530, y=41)
if ur.release == '7':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 530, y=41)
if ur.release == '8':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 525, y=43)
if ur.release == '8.1':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 525, y=43)
if ur.release == '2012ServerR2':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 525, y=43)
#Windows10
if ur.version == '10.0.10240':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.10586':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.14393':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.15063':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.16299':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.17134':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.17763':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.18362':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.18363':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.19041':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.19042':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.19043':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.19044':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
if ur.version == '10.0.19045':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)
#Windows11
if ur.version == '10.0.22000':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 500, y=40)
if ur.version == '10.0.22621':button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 500, y=40)

button = tk.Button(
    baseGround, text='Uninstall', command=btn_click).place(x= 10, y=10)
button2 = tk.Button(
    baseGround, text='Install', command=btn2_click).place(x= 90, y=10)
button3 = tk.Button(
    baseGround, text='Disable', command=btn3_click).place(x= 155, y=10)
button4 = tk.Button(
    baseGround, text='Enable', command=btn4_click).place(x= 225, y=10)

baseGround.mainloop()