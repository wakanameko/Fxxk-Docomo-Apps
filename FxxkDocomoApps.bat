@echo off
echo =========================
echo  = FxxkDocomoApps v1.9 =
echo  =   by @wakanameko2   =
echo =========================
pause

::Select Menu
cls
echo ============= Docomo_Apps ==============
echo Uninstall:1 Install:2 Disable:3 Enable:4
echo ========================================
echo.
set errorlevel=
set /p errorlevel=Enter Number and press Enter:
if "%errorlevel%"=="1" goto :Uninstall
if "%errorlevel%"=="2" goto :Install
if "%errorlevel%"=="3" goto :Disable
if "%errorlevel%"=="4" goto :Enable

:Uninstall
::Osaifu_uninstall
cls
echo ============ Osaihu keitai =============
echo       Uninstall:1         Leave:2
echo ========================================
echo.
set osaihuun=
set /p osaihuun=Enter Number and press Enter:
if "%osaihuun%"=="1" goto :Uninstallosaihu
if "%osaihuun%"=="2" goto :Leaveosaihu

:Uninstallosaihu
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.bridgelauncher
adb shell pm uninstall -k --user 0 com.nttdocomo.android.anmane2
adb shell pm uninstall -k --user 0 com.nttdocomo.android.felicaremotelock
adb shell pm uninstall -k --user 0 com.nttdocomo.android.accountwipe
adb shell pm uninstall -k --user 0 com.nttdocomo.android.pf.dcmippushaggregator
adb shell pm uninstall -k --user 0 com.nttdocomo.android.pf.dcmwappush
adb shell pm uninstall -k --user 0 com.nttdocomo.android.applicationmanager
adb shell pm uninstall -k --user 0 com.nttdocomo.android.accountauthenticator
adb shell pm uninstall -k --user 0 com.nttdocomo.android.initialization
adb shell pm uninstall -k --user 0 com.nttdocomo.android.dhome
adb shell pm uninstall -k --user 0 com.nextbit.app
adb shell pm uninstall -k --user 0 com.nttdocomo.android.idmanager
adb shell pm uninstall -k --user 0 com.nttdocomo.android.store
adb shell pm uninstall -k --user 0 com.nttdocomo.android.dmenu2
adb shell pm uninstall -k --user 0 com.nttdocomo.android.iconcier
adb shell pm uninstall -k --user 0 com.nttdocomo.android.iconcier_contents
adb shell pm uninstall -k --user 0 com.nttdocomo.android.rwpushcontroller
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.anshinmode
adb shell pm uninstall -k --user 0 com.nttdocomo.android.devicehelp
adb shell pm uninstall -k --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mascot
adb shell pm uninstall -k --user 0 com.nttdocomo.android.bugreport
adb shell pm uninstall -k --user 0 com.nttdocomo.android.atf
adb shell pm uninstall -k --user 0 com.nttdocomo.android.phonemotion
adb shell pm uninstall -k --user 0 com.nttdocomo.android.databackup
adb shell pm uninstall -k --user 0 com.nttdocomo.android.schedulememo
adb shell pm uninstall -k --user 0 com.nttdocomo.android.tapandpay
adb shell pm uninstall -k --user 0 jp.co.omronsoft.android.decoemojimanager_docomo
adb shell pm uninstall -k --user 0 com.nttdocomo.android.cloudset
adb shell pm uninstall -k --user 0 com.nttdocomo.android.docomoset
adb shell pm uninstall -k --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.carriermail
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.lcsapp
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.lcsappsub
adb shell pm uninstall -k --user 0 com.nttdocomo.android.voiceeditor
adb shell pm uninstall -k --user 0 com.nttdocomo.android.dcmvoicerecognition
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mediaplayer
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.saigaiban
adb shell pm uninstall -k --user 0 com.nttdocomo.android.socialphonebook
adb shell pm uninstall -k --user 0 com.android.contacts
adb shell pm uninstall -k --user 0 com.android.homezozo
adb shell pm uninstall -k --user 0 com.nttdocomo.android.dpoint
adb shell pm uninstall -k --user 0 com.nttdocomo.android.photocollection
adb shell pm uninstall -k --user 0 com.nttdocomo.android.idmanager
adb shell pm uninstall -k --user 0 com.nttdocomo.android.cloudset
adb shell pm uninstall -k --user 0 com.nttdocomo.android.wipe
adb shell pm uninstall -k --user 0 com.nttdocomo.android.anmate2
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.contentsheadline
adb shell pm uninstall -k --user 0 com.android.incallui.product.res.overlay
adb shell pm uninstall -k --user 0 com.nttdocomo.android.screenlockservice
adb shell pm uninstall -k --user 0 com.nttdocomo.android.osv.res.overlay_305
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.anshinmode
adb shell pm uninstall -k --user 0 com.nttdocomo.android.toruca
adb shell pm uninstall -k --user 0 com.nttdocomo.android.msg
adb shell pm uninstall -k --user 0 com.nttdocomo.android.tapandpay
adb shell pm uninstall -k --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mydocomo
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.dbook
adb shell pm uninstall -k --user 0 com.nttdocomo.dcard
adb shell pm uninstall -k --user 0 com.nttdocomo.keitai.payment
adb shell pm uninstall -k --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm uninstall -k --user 0 com.mobisystems.office
adb shell pm uninstall -k --user 0 jp.id_credit_sp.android
adb shell pm uninstall -k --user 0 com.nttdocomo.android.anshinsecurity
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.anshinmode
adb shell pm uninstall -k --user 0 com.felicanetworks.mfm.main
adb shell pm uninstall -k --user 0 com.nttdocomo.android.voicetranslation
adb shell pm uninstall -k --user 0 com.nttdocomo.android.cloudstorageservice
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mymagazine
adb shell pm uninstall -k --user 0 jp.dmapnavi.navi02
adb shell pm uninstall -k --user 0 com.rsupport.rs.activity.nttS
goto :alldone

:Leaveosaihu
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.bridgelauncher
adb shell pm uninstall -k --user 0 com.nttdocomo.android.anmane2
adb shell pm uninstall -k --user 0 com.nttdocomo.android.accountwipe
adb shell pm uninstall -k --user 0 com.nttdocomo.android.pf.dcmippushaggregator
adb shell pm uninstall -k --user 0 com.nttdocomo.android.pf.dcmwappush
adb shell pm uninstall -k --user 0 com.nttdocomo.android.applicationmanager
adb shell pm uninstall -k --user 0 com.nttdocomo.android.accountauthenticator
adb shell pm uninstall -k --user 0 com.nttdocomo.android.initialization
adb shell pm uninstall -k --user 0 com.nttdocomo.android.dhome
adb shell pm uninstall -k --user 0 com.nextbit.app
adb shell pm uninstall -k --user 0 com.nttdocomo.android.idmanager
adb shell pm uninstall -k --user 0 com.nttdocomo.android.store
adb shell pm uninstall -k --user 0 com.nttdocomo.android.dmenu2
adb shell pm uninstall -k --user 0 com.nttdocomo.android.iconcier
adb shell pm uninstall -k --user 0 com.nttdocomo.android.iconcier_contents
adb shell pm uninstall -k --user 0 com.nttdocomo.android.rwpushcontroller
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.anshinmode
adb shell pm uninstall -k --user 0 com.nttdocomo.android.devicehelp
adb shell pm uninstall -k --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mascot
adb shell pm uninstall -k --user 0 com.nttdocomo.android.bugreport
adb shell pm uninstall -k --user 0 com.nttdocomo.android.atf
adb shell pm uninstall -k --user 0 com.nttdocomo.android.phonemotion
adb shell pm uninstall -k --user 0 com.nttdocomo.android.databackup
adb shell pm uninstall -k --user 0 com.nttdocomo.android.schedulememo
adb shell pm uninstall -k --user 0 jp.co.omronsoft.android.decoemojimanager_docomo
adb shell pm uninstall -k --user 0 com.nttdocomo.android.cloudset
adb shell pm uninstall -k --user 0 com.nttdocomo.android.docomoset
adb shell pm uninstall -k --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.carriermail
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.lcsapp
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.lcsappsub
adb shell pm uninstall -k --user 0 com.nttdocomo.android.voiceeditor
adb shell pm uninstall -k --user 0 com.nttdocomo.android.dcmvoicerecognition
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mediaplayer
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.saigaiban
adb shell pm uninstall -k --user 0 com.nttdocomo.android.socialphonebook
adb shell pm uninstall -k --user 0 com.android.contacts
adb shell pm uninstall -k --user 0 com.android.homezozo
adb shell pm uninstall -k --user 0 com.nttdocomo.android.photocollection
adb shell pm uninstall -k --user 0 com.nttdocomo.android.idmanager
adb shell pm uninstall -k --user 0 com.nttdocomo.android.cloudset
adb shell pm uninstall -k --user 0 com.nttdocomo.android.wipe
adb shell pm uninstall -k --user 0 com.nttdocomo.android.anmate2
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.contentsheadline
adb shell pm uninstall -k --user 0 com.android.incallui.product.res.overlay
adb shell pm uninstall -k --user 0 com.nttdocomo.android.screenlockservice
adb shell pm uninstall -k --user 0 com.nttdocomo.android.osv.res.overlay_305
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.anshinmode
adb shell pm uninstall -k --user 0 com.nttdocomo.android.toruca
adb shell pm uninstall -k --user 0 com.nttdocomo.android.msg
adb shell pm uninstall -k --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mydocomo
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.dbook
adb shell pm uninstall -k --user 0 com.mobisystems.office
adb shell pm uninstall -k --user 0 com.nttdocomo.android.anshinsecurity
adb shell pm uninstall -k --user 0 jp.co.nttdocomo.anshinmode
adb shell pm uninstall -k --user 0 com.nttdocomo.android.voicetranslation
adb shell pm uninstall -k --user 0 com.nttdocomo.android.cloudstorageservice
adb shell pm uninstall -k --user 0 com.nttdocomo.android.mymagazine
adb shell pm uninstall -k --user 0 jp.dmapnavi.navi02
adb shell pm uninstall -k --user 0 com.rsupport.rs.activity.ntt
goto :alldone

:Install
adb shell cmd package install-existing jp.co.nttdocomo.bridgelauncher
adb shell cmd package install-existing com.nttdocomo.android.anmane2
adb shell cmd package install-existing com.nttdocomo.android.felicaremotelock
adb shell cmd package install-existing com.nttdocomo.android.accountwipe
adb shell cmd package install-existing com.nttdocomo.android.pf.dcmippushaggregator
adb shell cmd package install-existing com.nttdocomo.android.pf.dcmwappush
adb shell cmd package install-existing com.nttdocomo.android.applicationmanager
adb shell cmd package install-existing com.nttdocomo.android.accountauthenticator
adb shell cmd package install-existing com.nttdocomo.android.initialization
adb shell cmd package install-existing com.nttdocomo.android.dhome
adb shell cmd package install-existing com.nextbit.app
adb shell cmd package install-existing com.nttdocomo.android.idmanager
adb shell cmd package install-existing com.nttdocomo.android.store
adb shell cmd package install-existing com.nttdocomo.android.dmenu2
adb shell cmd package install-existing com.nttdocomo.android.iconcier
adb shell cmd package install-existing com.nttdocomo.android.iconcier_contents
adb shell cmd package install-existing com.nttdocomo.android.rwpushcontroller
adb shell cmd package install-existing jp.co.nttdocomo.anshinmode
adb shell cmd package install-existing com.nttdocomo.android.devicehelp
adb shell cmd package install-existing com.nttdocomo.osaifu.tsmproxy
adb shell cmd package install-existing com.nttdocomo.android.mascot
adb shell cmd package install-existing com.nttdocomo.android.bugreport
adb shell cmd package install-existing com.nttdocomo.android.atf
adb shell cmd package install-existing com.nttdocomo.android.phonemotion
adb shell cmd package install-existing com.nttdocomo.android.databackup
adb shell cmd package install-existing com.nttdocomo.android.schedulememo
adb shell cmd package install-existing com.nttdocomo.android.tapandpay
adb shell cmd package install-existing jp.co.omronsoft.android.decoemojimanager_docomo
adb shell cmd package install-existing com.nttdocomo.android.cloudset
adb shell cmd package install-existing com.nttdocomo.android.docomoset
adb shell cmd package install-existing com.nttdocomo.android.sdcardbackup
adb shell cmd package install-existing jp.co.nttdocomo.carriermail
adb shell cmd package install-existing jp.co.nttdocomo.lcsapp
adb shell cmd package install-existing jp.co.nttdocomo.lcsappsub
adb shell cmd package install-existing com.nttdocomo.android.voiceeditor
adb shell cmd package install-existing com.nttdocomo.android.dcmvoicerecognition
adb shell cmd package install-existing com.nttdocomo.android.mediaplayer
adb shell cmd package install-existing jp.co.nttdocomo.saigaiban
adb shell cmd package install-existing com.nttdocomo.android.socialphonebook

adb shell cmd package install-existing com.android.contacts
adb shell cmd package install-existing com.android.homezozo
adb shell cmd package install-existing com.nttdocomo.android.dpoint
adb shell cmd package install-existing com.nttdocomo.android.photocollection
adb shell cmd package install-existing com.nttdocomo.android.idmanager
adb shell cmd package install-existing com.nttdocomo.android.cloudset
adb shell cmd package install-existing com.nttdocomo.android.wipe
adb shell cmd package install-existing com.nttdocomo.android.anmate2
adb shell cmd package install-existing jp.co.nttdocomo.contentsheadline
adb shell cmd package install-existing com.android.incallui.product.res.overlay
adb shell cmd package install-existing com.nttdocomo.android.screenlockservice
adb shell cmd package install-existing com.nttdocomo.android.osv.res.overlay_305
adb shell cmd package install-existing jp.co.nttdocomo.anshinmode
adb shell cmd package install-existing com.nttdocomo.android.toruca
adb shell cmd package install-existing com.nttdocomo.android.msg
adb shell cmd package install-existing com.nttdocomo.android.tapandpay
adb shell cmd package install-existing com.nttdocomo.android.sdcardbackup
adb shell cmd package install-existing com.nttdocomo.android.mydocomo
adb shell cmd package install-existing jp.co.nttdocomo.dbook
adb shell cmd package install-existing com.nttdocomo.dcard
adb shell cmd package install-existing com.nttdocomo.keitai.payment
adb shell cmd package install-existing com.nttdocomo.osaifu.tsmproxy
adb shell cmd package install-existing com.mobisystems.office
adb shell cmd package install-existing jp.id_credit_sp.android
adb shell cmd package install-existing com.nttdocomo.android.anshinsecurity
adb shell cmd package install-existing jp.co.nttdocomo.anshinmode
adb shell cmd package install-existing com.felicanetworks.mfm.main
adb shell cmd package install-existing com.nttdocomo.android.voicetranslation
adb shell cmd package install-existing com.nttdocomo.android.cloudstorageservice
adb shell cmd package install-existing com.nttdocomo.android.mymagazine
adb shell cmd package install-existing jp.dmapnavi.navi02
adb shell cmd package install-existing com.rsupport.rs.activity.ntt
goto :alldone

:Disable
::Osaifu_Disable
cls
echo ============ Osaihu keitai =============
echo        Disable:1         Leave:2
echo ========================================
echo.
set osaihudi=
set /p osaihudi=Enter Number and press Enter:
if "%osaihudi%"=="1" goto :disableosaihu
if "%osaihudi%"=="2" goto :Leaveosaihudi

:disableosaihu
adb shell pm disable-user --user 0 jp.co.nttdocomo.bridgelauncher
adb shell pm disable-user --user 0 com.nttdocomo.android.anmane2
adb shell pm disable-user --user 0 com.nttdocomo.android.felicaremotelock
adb shell pm disable-user --user 0 com.nttdocomo.android.accountwipe
adb shell pm disable-user --user 0 com.nttdocomo.android.pf.dcmippushaggregator
adb shell pm disable-user --user 0 com.nttdocomo.android.pf.dcmwappush
adb shell pm disable-user --user 0 com.nttdocomo.android.applicationmanager
adb shell pm disable-user --user 0 com.nttdocomo.android.accountauthenticator
adb shell pm disable-user --user 0 com.nttdocomo.android.initialization
adb shell pm disable-user --user 0 com.nttdocomo.android.dhome
adb shell pm disable-user --user 0 com.nextbit.app
adb shell pm disable-user --user 0 com.nttdocomo.android.idmanager
adb shell pm disable-user --user 0 com.nttdocomo.android.store
adb shell pm disable-user --user 0 com.nttdocomo.android.dmenu2
adb shell pm disable-user --user 0 com.nttdocomo.android.iconcier
adb shell pm disable-user --user 0 com.nttdocomo.android.iconcier_contents
adb shell pm disable-user --user 0 com.nttdocomo.android.rwpushcontroller
adb shell pm disable-user --user 0 jp.co.nttdocomo.anshinmode
adb shell pm disable-user --user 0 com.nttdocomo.android.devicehelp
adb shell pm disable-user --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm disable-user --user 0 com.nttdocomo.android.mascot
adb shell pm disable-user --user 0 com.nttdocomo.android.bugreport
adb shell pm disable-user --user 0 com.nttdocomo.android.atf
adb shell pm disable-user --user 0 com.nttdocomo.android.phonemotion
adb shell pm disable-user --user 0 com.nttdocomo.android.databackup
adb shell pm disable-user --user 0 com.nttdocomo.android.schedulememo
adb shell pm disable-user --user 0 com.nttdocomo.android.tapandpay
adb shell pm disable-user --user 0 jp.co.omronsoft.android.decoemojimanager_docomo
adb shell pm disable-user --user 0 com.nttdocomo.android.cloudset
adb shell pm disable-user --user 0 com.nttdocomo.android.docomoset
adb shell pm disable-user --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm disable-user --user 0 jp.co.nttdocomo.carriermail
adb shell pm disable-user --user 0 jp.co.nttdocomo.lcsapp
adb shell pm disable-user --user 0 jp.co.nttdocomo.lcsappsub
adb shell pm disable-user --user 0 com.nttdocomo.android.voiceeditor
adb shell pm disable-user --user 0 com.nttdocomo.android.dcmvoicerecognition
adb shell pm disable-user --user 0 com.nttdocomo.android.mediaplayer
adb shell pm disable-user --user 0 jp.co.nttdocomo.saigaiban
adb shell pm disable-user --user 0 com.nttdocomo.android.socialphonebook

adb shell pm disable-user --user 0 com.android.contacts
adb shell pm disable-user --user 0 com.android.homezozo
adb shell pm disable-user --user 0 com.nttdocomo.android.dpoint
adb shell pm disable-user --user 0 com.nttdocomo.android.photocollection
adb shell pm disable-user --user 0 com.nttdocomo.android.idmanager
adb shell pm disable-user --user 0 com.nttdocomo.android.cloudset
adb shell pm disable-user --user 0 com.nttdocomo.android.wipe
adb shell pm disable-user --user 0 com.nttdocomo.android.anmate2
adb shell pm disable-user --user 0 jp.co.nttdocomo.contentsheadline
adb shell pm disable-user --user 0 com.android.incallui.product.res.overlay
adb shell pm disable-user --user 0 com.nttdocomo.android.screenlockservice
adb shell pm disable-user --user 0 com.nttdocomo.android.osv.res.overlay_305
adb shell pm disable-user --user 0 jp.co.nttdocomo.anshinmode
adb shell pm disable-user --user 0 com.nttdocomo.android.toruca
adb shell pm disable-user --user 0 com.nttdocomo.android.msg
adb shell pm disable-user --user 0 com.nttdocomo.android.tapandpay
adb shell pm disable-user --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm disable-user --user 0 com.nttdocomo.android.mydocomo
adb shell pm disable-user --user 0 jp.co.nttdocomo.dbook
adb shell pm disable-user --user 0 com.nttdocomo.dcard
adb shell pm disable-user --user 0 com.nttdocomo.keitai.payment
adb shell pm disable-user --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm disable-user --user 0 com.mobisystems.office
adb shell pm disable-user --user 0 jp.id_credit_sp.android
adb shell pm disable-user --user 0 com.nttdocomo.android.anshinsecurity
adb shell pm disable-user --user 0 jp.co.nttdocomo.anshinmode
adb shell pm disable-user --user 0 com.felicanetworks.mfm.main
adb shell pm disable-user --user 0 com.nttdocomo.android.voicetranslation
adb shell pm disable-user --user 0 com.nttdocomo.android.cloudstorageservice
adb shell pm disable-user --user 0 com.nttdocomo.android.mymagazine
adb shell pm disable-user --user 0 jp.dmapnavi.navi02
adb shell pm disable-user --user 0 com.rsupport.rs.activity.ntt
goto :alldone

:leaveosaihusdi
adb shell pm disable-user --user 0 jp.co.nttdocomo.bridgelauncher
adb shell pm disable-user --user 0 com.nttdocomo.android.anmane2
adb shell pm disable-user --user 0 com.nttdocomo.android.accountwipe
adb shell pm disable-user --user 0 com.nttdocomo.android.pf.dcmippushaggregator
adb shell pm disable-user --user 0 com.nttdocomo.android.pf.dcmwappush
adb shell pm disable-user --user 0 com.nttdocomo.android.applicationmanager
adb shell pm disable-user --user 0 com.nttdocomo.android.accountauthenticator
adb shell pm disable-user --user 0 com.nttdocomo.android.initialization
adb shell pm disable-user --user 0 com.nttdocomo.android.dhome
adb shell pm disable-user --user 0 com.nextbit.app
adb shell pm disable-user --user 0 com.nttdocomo.android.idmanager
adb shell pm disable-user --user 0 com.nttdocomo.android.store
adb shell pm disable-user --user 0 com.nttdocomo.android.dmenu2
adb shell pm disable-user --user 0 com.nttdocomo.android.iconcier
adb shell pm disable-user --user 0 com.nttdocomo.android.iconcier_contents
adb shell pm disable-user --user 0 com.nttdocomo.android.rwpushcontroller
adb shell pm disable-user --user 0 jp.co.nttdocomo.anshinmode
adb shell pm disable-user --user 0 com.nttdocomo.android.devicehelp
adb shell pm disable-user --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm disable-user --user 0 com.nttdocomo.android.mascot
adb shell pm disable-user --user 0 com.nttdocomo.android.bugreport
adb shell pm disable-user --user 0 com.nttdocomo.android.atf
adb shell pm disable-user --user 0 com.nttdocomo.android.phonemotion
adb shell pm disable-user --user 0 com.nttdocomo.android.databackup
adb shell pm disable-user --user 0 com.nttdocomo.android.schedulememo
adb shell pm disable-user --user 0 com.nttdocomo.android.tapandpay
adb shell pm disable-user --user 0 jp.co.omronsoft.android.decoemojimanager_docomo
adb shell pm disable-user --user 0 com.nttdocomo.android.cloudset
adb shell pm disable-user --user 0 com.nttdocomo.android.docomoset
adb shell pm disable-user --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm disable-user --user 0 jp.co.nttdocomo.carriermail
adb shell pm disable-user --user 0 jp.co.nttdocomo.lcsapp
adb shell pm disable-user --user 0 jp.co.nttdocomo.lcsappsub
adb shell pm disable-user --user 0 com.nttdocomo.android.voiceeditor
adb shell pm disable-user --user 0 com.nttdocomo.android.dcmvoicerecognition
adb shell pm disable-user --user 0 com.nttdocomo.android.mediaplayer
adb shell pm disable-user --user 0 jp.co.nttdocomo.saigaiban
adb shell pm disable-user --user 0 com.nttdocomo.android.socialphonebook
adb shell pm disable-user --user 0 com.android.contacts
adb shell pm disable-user --user 0 com.android.homezozo
adb shell pm disable-user --user 0 com.nttdocomo.android.photocollection
adb shell pm disable-user --user 0 com.nttdocomo.android.idmanager
adb shell pm disable-user --user 0 com.nttdocomo.android.cloudset
adb shell pm disable-user --user 0 com.nttdocomo.android.wipe
adb shell pm disable-user --user 0 com.nttdocomo.android.anmate2
adb shell pm disable-user --user 0 jp.co.nttdocomo.contentsheadline
adb shell pm disable-user --user 0 com.android.incallui.product.res.overlay
adb shell pm disable-user --user 0 com.nttdocomo.android.screenlockservice
adb shell pm disable-user --user 0 com.nttdocomo.android.osv.res.overlay_305
adb shell pm disable-user --user 0 jp.co.nttdocomo.anshinmode
adb shell pm disable-user --user 0 com.nttdocomo.android.toruca
adb shell pm disable-user --user 0 com.nttdocomo.android.msg
adb shell pm disable-user --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm disable-user --user 0 com.nttdocomo.android.mydocomo
adb shell pm disable-user --user 0 jp.co.nttdocomo.dbook
adb shell pm disable-user --user 0 com.mobisystems.office
adb shell pm disable-user --user 0 com.nttdocomo.android.anshinsecurity
adb shell pm disable-user --user 0 jp.co.nttdocomo.anshinmode
adb shell pm disable-user --user 0 com.nttdocomo.android.voicetranslation
adb shell pm disable-user --user 0 com.nttdocomo.android.cloudstorageservice
adb shell pm disable-user --user 0 com.nttdocomo.android.mymagazine
adb shell pm disable-user --user 0 jp.dmapnavi.navi02
adb shell pm disable-user --user 0 com.rsupport.rs.activity.ntt
goto :alldone

:Enable
adb shell pm enable --user 0 jp.co.nttdocomo.bridgelauncher
adb shell pm enable --user 0 com.nttdocomo.android.anmane2
adb shell pm enable --user 0 com.nttdocomo.android.felicaremotelock
adb shell pm enable --user 0 com.nttdocomo.android.accountwipe
adb shell pm enable --user 0 com.nttdocomo.android.pf.dcmippushaggregator
adb shell pm enable --user 0 com.nttdocomo.android.pf.dcmwappush
adb shell pm enable --user 0 com.nttdocomo.android.applicationmanager
adb shell pm enable --user 0 com.nttdocomo.android.accountauthenticator
adb shell pm enable --user 0 com.nttdocomo.android.initialization
adb shell pm enable --user 0 com.nttdocomo.android.dhome
adb shell pm enable --user 0 com.nextbit.app
adb shell pm enable --user 0 com.nttdocomo.android.idmanager
adb shell pm enable --user 0 com.nttdocomo.android.store
adb shell pm enable --user 0 com.nttdocomo.android.dmenu2
adb shell pm enable --user 0 com.nttdocomo.android.iconcier
adb shell pm enable --user 0 com.nttdocomo.android.iconcier_contents
adb shell pm enable --user 0 com.nttdocomo.android.rwpushcontroller
adb shell pm enable --user 0 jp.co.nttdocomo.anshinmode
adb shell pm enable --user 0 com.nttdocomo.android.devicehelp
adb shell pm enable --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm enable --user 0 com.nttdocomo.android.mascot
adb shell pm enable --user 0 com.nttdocomo.android.bugreport
adb shell pm enable --user 0 com.nttdocomo.android.atf
adb shell pm enable --user 0 com.nttdocomo.android.phonemotion
adb shell pm enable --user 0 com.nttdocomo.android.databackup
adb shell pm enable --user 0 com.nttdocomo.android.schedulememo
adb shell pm enable --user 0 com.nttdocomo.android.tapandpay
adb shell pm enable --user 0 jp.co.omronsoft.android.decoemojimanager_docomo
adb shell pm enable --user 0 com.nttdocomo.android.cloudset
adb shell pm enable --user 0 com.nttdocomo.android.docomoset
adb shell pm enable --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm enable --user 0 jp.co.nttdocomo.carriermail
adb shell pm enable --user 0 jp.co.nttdocomo.lcsapp
adb shell pm enable --user 0 jp.co.nttdocomo.lcsappsub
adb shell pm enable --user 0 com.nttdocomo.android.voiceeditor
adb shell pm enable --user 0 com.nttdocomo.android.dcmvoicerecognition
adb shell pm enable --user 0 com.nttdocomo.android.mediaplayer
adb shell pm enable --user 0 jp.co.nttdocomo.saigaiban
adb shell pm enable --user 0 com.nttdocomo.android.socialphonebook

adb shell pm enable --user 0 com.android.contacts
adb shell pm enable --user 0 com.android.homezozo
adb shell pm enable --user 0 com.nttdocomo.android.dpoint
adb shell pm enable --user 0 com.nttdocomo.android.photocollection
adb shell pm enable --user 0 com.nttdocomo.android.idmanager
adb shell pm enable --user 0 com.nttdocomo.android.cloudset
adb shell pm enable --user 0 com.nttdocomo.android.wipe
adb shell pm enable --user 0 com.nttdocomo.android.anmate2
adb shell pm enable --user 0 jp.co.nttdocomo.contentsheadline
adb shell pm enable --user 0 com.android.incallui.product.res.overlay
adb shell pm enable --user 0 com.nttdocomo.android.screenlockservice
adb shell pm enable --user 0 com.nttdocomo.android.osv.res.overlay_305
adb shell pm enable --user 0 jp.co.nttdocomo.anshinmode
adb shell pm enable --user 0 com.nttdocomo.android.toruca
adb shell pm enable --user 0 com.nttdocomo.android.msg
adb shell pm enable --user 0 com.nttdocomo.android.tapandpay
adb shell pm enable --user 0 com.nttdocomo.android.sdcardbackup
adb shell pm enable --user 0 com.nttdocomo.android.mydocomo
adb shell pm enable --user 0 jp.co.nttdocomo.dbook
adb shell pm enable --user 0 com.nttdocomo.dcard
adb shell pm enable --user 0 com.nttdocomo.keitai.payment
adb shell pm enable --user 0 com.nttdocomo.osaifu.tsmproxy
adb shell pm enable --user 0 com.mobisystems.office
adb shell pm enable --user 0 jp.id_credit_sp.android
adb shell pm enable --user 0 com.nttdocomo.android.anshinsecurity
adb shell pm enable --user 0 jp.co.nttdocomo.anshinmode
adb shell pm enable --user 0 com.felicanetworks.mfm.main
adb shell pm enable --user 0 com.nttdocomo.android.voicetranslation
adb shell pm enable --user 0 com.nttdocomo.android.cloudstorageservice
adb shell pm enable --user 0 com.nttdocomo.android.mymagazine
adb shell pm enable --user 0 jp.dmapnavi.navi02
adb shell pm enable --user 0 com.rsupport.rs.activity.ntt
goto :alldone

:alldone
cls
echo ===============
echo  = All_Done! =
echo ===============
pause
