import tkinter as tk
 
baseGround = tk.Tk()

baseGround.geometry('500x50')
 
baseGround.title('FxxkDocomoApps')

def btn_click():    
    label1 = tk.Label(baseGround, text='Selected Uninstall').place(x=290,y=15)
    print('selected Uninstall.')
    import subprocess
    
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.bridgelauncher')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anmane2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.felicaremotelock')
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
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')
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
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.tapandpay')
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
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dpoint')
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
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.tapandpay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.sdcardbackup')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.mydocomo')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.dbook')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.dcard')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.keitai.payment')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.id_credit_sp.android')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.anshinsecurity')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.co.nttdocomo.anshinmode')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.felicanetworks.mfm.main')
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
    print('All_Done')
    label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)

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
    print('All_Done')
    label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)

def btn3_click():
    label1 = tk.Label(baseGround, text='Selected Disable  ').place(x=290,y=15)
    print('selected Disable.')
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
    print('All_Done')
    label1 = tk.Label(baseGround, text='All Done              ').place(x=290,y=15)
    
button = tk.Button(
    baseGround, text='Uninstall', command=btn_click).place(x= 10, y=10)

button2 = tk.Button(
    baseGround, text='Install', command=btn2_click).place(x= 90, y=10)
 
button3 = tk.Button(
    baseGround, text='Disable', command=btn3_click).place(x= 155, y=10)

button4 = tk.Button(
    baseGround, text='Enable', command=btn4_click).place(x= 225, y=10)
    
baseGround.mainloop()
