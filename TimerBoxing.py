from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import TimerBoxing_codes as ideal
i = 0
class Ui_MainWindow(object):
    def __init__(self) -> None:
        super().__init__()
        self.media_player = QMediaPlayer()
        self.second10 = QMediaContent(QUrl.fromLocalFile(r"sounds/saniye_10.mp3"))
        self.second3 = QMediaContent(QUrl.fromLocalFile(r"sounds/3saniye.mp3"))
        self.secondEnd = QMediaContent(QUrl.fromLocalFile(r"sounds/sheypur.mp3"))
        self.secondStart = QMediaContent(QUrl.fromLocalFile(r"sounds/shuru.mp3"))
        self.waiter = QTimer()
        self.waiter.timeout.connect(self.update_daly)
        self.waite = QTime(0, 0, 0)
        self.round = 0
        self.repeat = 0
        self.rest = 0
    def play_second10(self):
        self.media_player.setMedia(self.second10)
        self.media_player.play()

    def play_second3(self):
        self.media_player.setMedia(self.second3)
        self.media_player.play()

    def play_secondstart(self):
        self.media_player.setMedia(self.secondStart)
        self.media_player.play()

    def play_secondend(self):
        self.media_player.setMedia(self.secondEnd)
        self.media_player.play()

    def play_sounds(self):
        if self.waite == QTime(0, 0, 11):
            self.play_second10()

    def showmassage_OK(self, caption):
        masssage = QMessageBox()
        masssage.setWindowTitle("Warning")
        masssage.setIcon(QMessageBox.Warning)
        masssage.setText(caption)
        masssage.setStandardButtons(QMessageBox.Ok)
        masssage.exec()

    def showmassage_Yes_No(self, caption):
        masssage = QMessageBox()
        masssage.setWindowTitle("Warning")
        masssage.setIcon(QMessageBox.Warning)
        masssage.setText(caption)
        masssage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = masssage.exec()
        return result

    def SendData(self):
        result = self.showmassage_Yes_No("Will the information be stored in the system?")
        if result == QMessageBox.Yes:
            numkey = int(self.ComboQuick.currentText())
            title = self.lineEditTitle.text()
            wait = self.comboWait.currentText()
            round = self.comboRound.currentText()
            fightminu = self.comboFightMinutes.currentText()
            fightsecs = self.comboFightSecond.currentText()
            restminu = self.comboRestMinutes.currentText()
            restsecs = self.comboRestSecond.currentText()
            ideal.GYM.save(numkey, title, round, fightminu, fightsecs, restminu, restsecs, wait)
            self.showmassage_OK("Saved successfully")
            self.Reset()
        else:
            self.showmassage_OK("The operation was canceled")

    def DeleteData(self):
        result = self.showmassage_Yes_No("Will the information be deleted?")
        if result == QMessageBox.Yes:
            numkey = int(self.ComboQuick.currentText())
            ideal.GYM.delete(numkey)
            self.showmassage_OK("Deleted successfully")
            self.Reset()
        else:
            self.showmassage_OK("The operation was canceled")

    def starttimer(self):
        global i
        i = 0
        self.btnStopTimer.setEnabled(True)
        self.btnPauseTimer.setEnabled(True)
        self.btnStart.setEnabled(False)
        self.waiter.start(1000)
        if self.waite == QTime(0, 0, 0):
            return self.waite

    def stoptimer(self):
        self.waiter.stop()
        self.waite = QTime(0, 0, 0)
        self.round = 0
        self.repeat = 0
        self.Reset()
        self.btnStart.setEnabled(True)
        self.btnPauseTimer.setEnabled(False)
        self.btnStopTimer.setEnabled(False)
        self.lblCountRound.setText("00")
        self.lblTimer.setText("00:00")

    def Pausetimer(self):
        self.waiter.stop()
        self.btnStart.setEnabled(True)
        self.btnStopTimer.setEnabled(True)
        self.btnPauseTimer.setEnabled(False)

    def Reset(self):
        self.lineEditTitle.setText("")
        self.comboFightMinutes.setCurrentText("0")
        self.comboFightSecond.setCurrentText("0")
        self.comboRestMinutes.setCurrentText("0")
        self.comboRestSecond.setCurrentText("0")
        self.comboRound.setCurrentText("1")
        self.comboWait.setCurrentText("0")
        self.ComboQuick.setCurrentText("0")

    def Quickbtns(self, numkey):
        line = ideal.GYM.select(self, numkey)
        self.ComboQuick.setCurrentText(str(line[0][0]))
        self.lineEditTitle.setText(line[0][1])
        self.comboRound.setCurrentText(line[0][2])
        self.comboFightMinutes.setCurrentText(line[0][3])
        self.comboFightSecond.setCurrentText(line[0][4])
        self.comboRestMinutes.setCurrentText(line[0][5])
        self.comboRestSecond.setCurrentText(line[0][6])
        self.comboWait.setCurrentText(line[0][7])

    def aboutus(self):
        self.showmassage_OK("©1402 farid najafi\n"
                            "All rights reserved.\n"
                            "Distribution, reproduction, or transmission of this program without the written permission of the copyright holder is prohibited.\n"
                            "You can contact the copyright holder by email at [faridnajafi.0037@gmail.com] or by phone at [+989045169009].")

    def update_daly(self):
        global i
        self.waite = self.waite.addSecs(-1)
        if self.waite == QTime(23, 59, 59):
            if i % 2 != 0 and self.round > 0:
                i += 1
                self.rest += 1
                restminu = int(self.comboRestMinutes.currentText())
                restsecs = int(self.comboRestSecond.currentText())
                self.waite = QTime(0, restminu, restsecs)
                self.lblTimer.setText(self.waite.toString("mm:ss"))
                self.frame_10.setStyleSheet("background: #03c508;"
                                            "border-radius: 30px;\n")  # سبز
                self.frame.setStyleSheet("background-color: #000000;\n"
                                         "border: 3px solid #03c508;\n"
                                         "border-radius: 10px;")
                self.lblTimer.setStyleSheet("font: 75 310pt 'Arial';\n"
                                            "color: white")
                self.labelRound.setStyleSheet("font: 75 55pt Tahoma;\n"
                                              "color: white;")
                self.lblCountRound.setStyleSheet("font: 75 80pt Arial;\n"
                                                 "margin: 0;\n"
                                                 "padding: 0;\n"
                                                 "margin-top: 8px;\n"
                                                 "color: white;")
            elif i % 2 == 0 and self.round > 0:
                self.play_secondstart()
                i += 1
                self.round -= 1
                self.repeat += 1
                fightminu = int(self.comboFightMinutes.currentText())
                fightsecs = int(self.comboFightSecond.currentText())
                self.waite = QTime(0, fightminu, fightsecs)
                self.lblTimer.setText(self.waite.toString("mm:ss"))
                self.frame_10.setStyleSheet("background-color: #0096ff;\n"  # آبی
                                            "color: white;"
                                            "border-radius: 30px;\n")
                self.frame.setStyleSheet("background-color: #000000;\n"
                                         "border: 3px solid #0096ff;\n"
                                         "border-radius: 10px;")
                self.lblTimer.setStyleSheet("font: 75 310pt 'Arial';")
                self.labelRound.setStyleSheet("font: 75 55pt Tahoma;\n"
                                              "color: white")
                self.lblCountRound.setStyleSheet("font: 75 80pt Arial;\n"
                                                 "margin: 0;\n"
                                                 "padding: 0;\n"
                                                 "margin-top: 8px;\n"
                                                 "color: white")
            else:
                self.waiter.stop()
                self.Reset()
                self.repeat = 0
                self.round = 0
                self.waite = QTime(0, 0, 0)
                self.showmassage_OK("Time is up")
                self.btnStart.setEnabled(True)
                self.btnPauseTimer.setEnabled(False)
                self.btnStopTimer.setEnabled(False)
        else:
            if self.repeat < 10:
                self.lblCountRound.setText(f"0{self.repeat}")
            else:
                self.lblCountRound.setText(str(self.repeat))
            self.lblTimer.setText(self.waite.toString("mm:ss"))
            if i % 2 == 0 and self.waite == QTime(0, 0, 3):
                self.play_second3()
            if i % 2 != 0 and self.waite == QTime(0, 0, 1):
                self.play_secondend()
            if self.waite == QTime(0, 0, 10):
                self.play_second10()
            self.change_bg_style()

    def change_bg_style(self):
        if i % 2 != 0 and self.waite == QTime(0, 0, 10):  # fight
            self.frame_10.setStyleSheet("background: #ff0000;\n"
                                        "border-radius: 30px;\n")  # قرمز
            self.lblTimer.setStyleSheet("font: 75 310pt 'Arial';\n"
                                        "color: white")
            self.labelRound.setStyleSheet("font: 75 55pt Tahoma;\n"
                                          "color: white")
            self.lblCountRound.setStyleSheet("font: 75 80pt Arial;\n"
                                             "margin: 0;\n"
                                             "padding: 0;\n"
                                             "margin-top: 8px;\n"
                                             "color: white")
            self.frame.setStyleSheet("background-color: #000000;\n"
                                     "border: 3px solid #ff0000;\n"
                                     "border-radius: 10px;")
        if i % 2 != 0 and self.waite == QTime(0, 0, 0):
            self.frame_10.setStyleSheet("background: #ff0000;"
                                        "border-radius: 30px;\n")  # قرمز
            self.lblTimer.setStyleSheet("font: 75 310pt 'Arial';\n"
                                        "color: white")
            self.labelRound.setStyleSheet("font: 75 55pt Tahoma;\n"
                                          "color: white")
            self.lblCountRound.setStyleSheet("font: 75 85pt 'Arial';\n"
                                             "margin: 0;\n"
                                             "padding: 0;\n"
                                             "margin-top: 8px;\n"
                                             "color: white")
            self.frame.setStyleSheet("background-color: #000000;\n"
                                     "border: 3px solid #ff0000;\n"
                                     "border-radius: 10px;")
        if i % 2 == 0 and self.waite == QTime(0, 0, 0):  # rest
            self.frame_10.setStyleSheet("background: #ff0000;"
                                        "border-radius: 30px;\n")  # قرمز
            self.lblTimer.setStyleSheet("font: 75 310pt 'Arial';\n"
                                        "color: white")
            self.labelRound.setStyleSheet("font: 75 55pt Tahoma;\n"
                                          "color: white")
            self.lblCountRound.setStyleSheet("font: 75 85pt 'Arial';\n"
                                             "margin: 0;\n"
                                             "padding: 0;\n"
                                             "margin-top: 8px;\n"
                                             "color: white")
            self.frame.setStyleSheet("background-color: #000000;\n"
                                     "border: 3px solid #ff0000;\n"
                                     "border-radius: 10px;")
        if i % 2 == 0 and self.waite == QTime(0, 0, 10):  # rest
            self.frame_10.setStyleSheet("background: #ff0000;"
                                        "border-radius: 30px;\n")  # قرمز
            self.lblTimer.setStyleSheet("font: 75 310pt 'Arial';\n"
                                        "color: white")
            self.labelRound.setStyleSheet("font: 75 55pt Tahoma;\n"
                                          "color: white")
            self.lblCountRound.setStyleSheet("font: 75 80pt Tahoma;\n"
                                             "margin: 0;\n"
                                             "padding: 0;\n"
                                             "margin-top: 8px;\n"
                                             "color: white")
            self.frame.setStyleSheet("background-color: #000000;\n"
                                     "border: 3px solid #ff0000;\n"
                                     "border-radius: 10px;")

    def set_timer_wait(self):
        dearly = int(self.comboWait.currentText())
        self.waite = QTime(0, 0, dearly)
        self.lblTimer.setText(self.waite.toString("mm:ss"))

    def set_timer_fight(self):
        fightminutes = int(self.comboFightMinutes.currentText())
        fightsecs = int(self.comboFightSecond.currentText())
        self.round = int(self.comboRound.currentText())
        if fightminutes or fightsecs:
            self.time = QTime(0, fightminutes, fightsecs)
            self.lblTimer.setText(self.time.toString("mm:ss"))

    def set_timer_rest(self):
        restminu = int(self.comboRestMinutes.currentText())
        restsecs = int(self.comboRestSecond.currentText())
        if restminu or restsecs:
            self.resttime = QTime(0, restminu, restsecs)
            self.lblTimer.setText(self.resttime.toString("mm:ss"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 700)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/AppIcon/Images/Icon/boxing.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(3, 5, 3, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: #000000;\n"
                                 "border: 3px solid #23A4E6;\n"
                                 "border-radius: 25px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_2.setStyleSheet("background-color:#000000;\n"
                                   "border: 0;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 190))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 190))
        self.frame_4.setStyleSheet("background-color:#000000;\n"
                                   "border-right: 0;\n"
                                   "")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbllogo = QtWidgets.QLabel(self.frame_4)
        self.lbllogo.setMaximumSize(QtCore.QSize(180, 160))
        self.lbllogo.setStyleSheet("border-radius: 10px;")
        self.lbllogo.setText("")
        self.lbllogo.setPixmap(QtGui.QPixmap(":/logo/Images/logo/IDEAL LOGO 1.jpg"))
        self.lbllogo.setScaledContents(True)
        self.lbllogo.setObjectName("lbllogo")
        self.gridLayout_2.addWidget(self.lbllogo, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setStyleSheet("background-color: #000000;\n"
                                   "border-right: 0;\n"
                                   "")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lblTitle = QtWidgets.QLabel(self.frame_8)
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 45))
        self.lblTitle.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_9.addWidget(self.lblTitle)
        self.lineEditTitle = QtWidgets.QLineEdit(self.frame_8)
        self.lineEditTitle.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEditTitle.setStyleSheet("font: 75 14pt \"B Nazanin\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 0;\n"
                                         "border-bottom:2px solid rgba(38, 179, 251,0.4);")
        self.lineEditTitle.setMaxLength(20)
        self.lineEditTitle.setFrame(True)
        self.lineEditTitle.setCursorPosition(0)
        self.lineEditTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.verticalLayout_9.addWidget(self.lineEditTitle)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("background-color: #000000;\n"
                                   "border-right: 0;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.frame_5)
        self.frame_14.setStyleSheet("background-color:#000000;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblTimeFight = QtWidgets.QLabel(self.frame_14)
        self.lblTimeFight.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                        "color: rgb(255, 255, 255);")
        self.lblTimeFight.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTimeFight.setObjectName("lblTimeFight")
        self.verticalLayout_6.addWidget(self.lblTimeFight)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_5)
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_15.setStyleSheet("background-color:#000000;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setStyleSheet("background-color:#000000;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblFightMinutes = QtWidgets.QLabel(self.frame_16)
        self.lblFightMinutes.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border: 0;\n"
                                           "")
        self.lblFightMinutes.setObjectName("lblFightMinutes")
        self.horizontalLayout_6.addWidget(self.lblFightMinutes)
        self.comboFightMinutes = QtWidgets.QComboBox(self.frame_16)
        self.comboFightMinutes.setMinimumSize(QtCore.QSize(67, 40))
        self.comboFightMinutes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboFightMinutes.setMouseTracking(True)
        self.comboFightMinutes.setTabletTracking(True)
        self.comboFightMinutes.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboFightMinutes.setStyleSheet("padding: 5px 6px 11px;\n"
                                             "color: white;\n"
                                             "font: 16pt \"Arial\";")
        self.comboFightMinutes.setObjectName("comboFightMinutes")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.comboFightMinutes.addItem("")
        self.horizontalLayout_6.addWidget(self.comboFightMinutes)
        self.horizontalLayout_4.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setStyleSheet("background-color:#000000;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_5.setContentsMargins(9, 0, 3, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblFightSecond = QtWidgets.QLabel(self.frame_17)
        self.lblFightSecond.setTabletTracking(False)
        self.lblFightSecond.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border: 0;\n"
                                          "")
        self.lblFightSecond.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFightSecond.setObjectName("lblFightSecond")
        self.horizontalLayout_5.addWidget(self.lblFightSecond)
        self.comboFightSecond = QtWidgets.QComboBox(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFightSecond.sizePolicy().hasHeightForWidth())
        self.comboFightSecond.setSizePolicy(sizePolicy)
        self.comboFightSecond.setMinimumSize(QtCore.QSize(67, 40))
        self.comboFightSecond.setMaximumSize(QtCore.QSize(16777215, 45))
        self.comboFightSecond.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboFightSecond.setMouseTracking(True)
        self.comboFightSecond.setTabletTracking(True)
        self.comboFightSecond.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboFightSecond.setStyleSheet("padding: 5px 6px 11px;\n"
                                            "color: white;\n"
                                            "font: 16pt \"Arial\";")
        self.comboFightSecond.setIconSize(QtCore.QSize(16, 16))
        self.comboFightSecond.setDuplicatesEnabled(False)
        self.comboFightSecond.setFrame(True)
        self.comboFightSecond.setModelColumn(0)
        self.comboFightSecond.setObjectName("comboFightSecond")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.comboFightSecond.addItem("")
        self.horizontalLayout_5.addWidget(self.comboFightSecond)
        self.horizontalLayout_4.addWidget(self.frame_17)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setStyleSheet("background-color:#000000;\n"
                                   "border-right: 0;\n"
                                   "")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_18 = QtWidgets.QFrame(self.frame_6)
        self.frame_18.setStyleSheet("background-color: #000000;\n"
                                    "border-right: 0;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setStyleSheet("background-color:#000000;")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblTimeRest = QtWidgets.QLabel(self.frame_19)
        self.lblTimeRest.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                       "color: rgb(255, 255, 255);")
        self.lblTimeRest.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTimeRest.setObjectName("lblTimeRest")
        self.verticalLayout_8.addWidget(self.lblTimeRest)
        self.verticalLayout_7.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_20.setStyleSheet("background-color:#000000;\n"
                                    "border-radius: 0;\n""")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_7.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        self.frame_21.setStyleSheet("background-color:#000000;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_8.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblRestMinutes = QtWidgets.QLabel(self.frame_21)
        self.lblRestMinutes.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border: 0;\n""")
        self.lblRestMinutes.setObjectName("lblRestMinutes")
        self.horizontalLayout_8.addWidget(self.lblRestMinutes)
        self.comboRestMinutes = QtWidgets.QComboBox(self.frame_21)
        self.comboRestMinutes.setMinimumSize(QtCore.QSize(67, 40))
        self.comboRestMinutes.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboRestMinutes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboRestMinutes.setMouseTracking(True)
        self.comboRestMinutes.setTabletTracking(True)
        self.comboRestMinutes.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboRestMinutes.setStyleSheet("padding: 5px 6px 11px;\n"
                                            "color: white;\n"
                                            "font: 16pt \"Arial\";")
        self.comboRestMinutes.setObjectName("comboRestMinutes")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.comboRestMinutes.addItem("")
        self.horizontalLayout_8.addWidget(self.comboRestMinutes)
        self.horizontalLayout_7.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setStyleSheet("background-color:#000000;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setContentsMargins(5, 0, 3, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblRestSecond = QtWidgets.QLabel(self.frame_22)
        self.lblRestSecond.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 0;\n"
                                         "")
        self.lblRestSecond.setObjectName("lblRestSecond")
        self.horizontalLayout_9.addWidget(self.lblRestSecond)
        self.comboRestSecond = QtWidgets.QComboBox(self.frame_22)
        self.comboRestSecond.setMinimumSize(QtCore.QSize(67, 40))
        self.comboRestSecond.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboRestSecond.setMouseTracking(True)
        self.comboRestSecond.setTabletTracking(True)
        self.comboRestSecond.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboRestSecond.setStyleSheet("padding: 5px 6px 11px;\n"
                                           "color: white;\n"
                                           "font: 16pt \"Arial\";")
        self.comboRestSecond.setObjectName("comboRestSecond")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.comboRestSecond.addItem("")
        self.horizontalLayout_9.addWidget(self.comboRestSecond)
        self.horizontalLayout_7.addWidget(self.frame_22)
        self.verticalLayout_7.addWidget(self.frame_20)
        self.horizontalLayout_10.addWidget(self.frame_18)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_7.setStyleSheet("border: 0;\n"
                                   "border-top:2px solid rgba(38, 179, 251,0.4);\n"
                                   "margin-top: 4px;\n"
                                   "border-radius: 0;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblWait = QtWidgets.QLabel(self.frame_7)
        self.lblWait.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: 0;\n"
                                   "")
        self.lblWait.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWait.setObjectName("lblWait")
        self.horizontalLayout_11.addWidget(self.lblWait)
        self.comboWait = QtWidgets.QComboBox(self.frame_7)
        self.comboWait.setMinimumSize(QtCore.QSize(90, 40))
        self.comboWait.setMaximumSize(QtCore.QSize(70, 16777215))
        self.comboWait.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboWait.setMouseTracking(True)
        self.comboWait.setTabletTracking(True)
        self.comboWait.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboWait.setStyleSheet("padding: 0 20px;\n"
                                     "color: white;\n"
                                     "background-color: rgba(4, 4,2,0.4);\n"
                                     "font: 18pt \"Arial\";\n"
                                     "border-top: 0;\n"
                                     "")
        self.comboWait.setObjectName("comboWait")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.comboWait.addItem("")
        self.horizontalLayout_11.addWidget(self.comboWait)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_24 = QtWidgets.QFrame(self.frame_2)
        self.frame_24.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_24.setStyleSheet("border:0;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setContentsMargins(5, 0, 15, 0)
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lblRound = QtWidgets.QLabel(self.frame_24)
        self.lblRound.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border: 0;\n"
                                    "")
        self.lblRound.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRound.setObjectName("lblRound")
        self.horizontalLayout_17.addWidget(self.lblRound)
        self.comboRound = QtWidgets.QComboBox(self.frame_24)
        self.comboRound.setMinimumSize(QtCore.QSize(90, 40))
        self.comboRound.setMaximumSize(QtCore.QSize(70, 16777215))
        self.comboRound.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboRound.setMouseTracking(True)
        self.comboRound.setTabletTracking(True)
        self.comboRound.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboRound.setStyleSheet("padding: 0 20px;\n"
                                      "color: white;\n"
                                      "background-color: rgba(4, 4,2,0.4);\n"
                                      "font: 18pt \"Arial\";\n"
                                      "border-top: 0;\n"
                                      "")
        self.comboRound.setObjectName("comboRound")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.comboRound.addItem("")
        self.horizontalLayout_17.addWidget(self.comboRound)
        self.verticalLayout_2.addWidget(self.frame_24)
        self.frame_23 = QtWidgets.QFrame(self.frame_2)
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_23.setStyleSheet("border-right:0;\n"
                                    "")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_12.setSpacing(8)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblQuick = QtWidgets.QLabel(self.frame_23)
        self.lblQuick.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border: 0;\n"
                                    "")
        self.lblQuick.setAlignment(QtCore.Qt.AlignCenter)
        self.lblQuick.setObjectName("lblQuick")
        self.horizontalLayout_12.addWidget(self.lblQuick)
        self.ComboQuick = QtWidgets.QComboBox(self.frame_23)
        self.ComboQuick.setMinimumSize(QtCore.QSize(90, 40))
        self.ComboQuick.setMaximumSize(QtCore.QSize(70, 37))
        self.ComboQuick.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboQuick.setMouseTracking(True)
        self.ComboQuick.setTabletTracking(True)
        self.ComboQuick.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ComboQuick.setStyleSheet("padding: 0 20px;\n"
                                      "color: white;\n"
                                      "background-color: rgba(4, 4,2,0.4);\n"
                                      "font: 18pt \"Arial\";\n"
                                      "border-top: 0;\n"
                                      "")
        self.ComboQuick.setIconSize(QtCore.QSize(15, 15))
        self.ComboQuick.setObjectName("ComboQuick")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.ComboQuick.addItem("")
        self.horizontalLayout_12.addWidget(self.ComboQuick)
        self.verticalLayout_2.addWidget(self.frame_23)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setStyleSheet("background-color: #000000;\n"
                                   "border-right: 0;\n"
                                   "")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setStyleSheet("background-color: #000000;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setContentsMargins(8, 10, 8, 0)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btnSave = QtWidgets.QPushButton(self.frame_12)
        self.btnSave.setMinimumSize(QtCore.QSize(0, 36))
        self.btnSave.setMaximumSize(QtCore.QSize(95, 16777215))
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setMouseTracking(True)
        self.btnSave.setTabletTracking(True)
        self.btnSave.setStyleSheet("QPushButton {\n"
                                   "    color:WHITE;\n"
                                   "    border: 5px solid #555;\n"
                                   "    border-radius: 13px;\n"
                                   "    border-style: outset;\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                   "        );\n"
                                   "    padding-bottom: 2px;\n"
                                   "    padding-top: 3px;\n"
                                   "    background-color: #0045A8;\n"
                                   "    font: 75 18pt \"Tahoma\";\n"
                                   "    }\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                   "        );\n"
                                   "    background-color: #00327A;\n"
                                   "    }\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    border-style: inset;\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                   "        );\n"
                                   "background-color: #001C45;\n"
                                   "    }QPushButton {\n"
                                   "    color:WHITE;\n"
                                   "    border: 5px solid #555;\n"
                                   "    border-radius: 13px;\n"
                                   "    border-style: outset;\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                   "        );\n"
                                   "    padding-bottom: 2px;\n"
                                   "    padding-top: 3px;\n"
                                   "    background-color: #0045A8;\n"
                                   "    font: 75 18pt \"Tahoma\";\n"
                                   "    }\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                   "        );\n"
                                   "    background-color: #00327A;\n"
                                   "    }\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    border-style: inset;\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                   "        );\n"
                                   "background-color: #001C45;\n"
                                   "    }")
        self.btnSave.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Images/Icon/save-svgrepo-com.png.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btnSave.setIcon(icon1)
        self.btnSave.setIconSize(QtCore.QSize(24, 25))
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_13.addWidget(self.btnSave)
        self.btnDelete = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setMinimumSize(QtCore.QSize(0, 36))
        self.btnDelete.setMaximumSize(QtCore.QSize(95, 36))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnDelete.setFont(font)
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelete.setMouseTracking(True)
        self.btnDelete.setTabletTracking(True)
        self.btnDelete.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 75 18pt \"Tahoma\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnDelete.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Images/Icon/delete-white-2.png.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btnDelete.setIcon(icon2)
        self.btnDelete.setIconSize(QtCore.QSize(22, 22))
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_13.addWidget(self.btnDelete)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setStyleSheet("background-color: #000000;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout.setContentsMargins(8, 0, 8, 5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_29 = QtWidgets.QFrame(self.frame_13)
        self.frame_29.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btnPauseTimer = QtWidgets.QPushButton(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPauseTimer.sizePolicy().hasHeightForWidth())
        self.btnPauseTimer.setSizePolicy(sizePolicy)
        self.btnPauseTimer.setMinimumSize(QtCore.QSize(0, 36))
        self.btnPauseTimer.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPauseTimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPauseTimer.setMouseTracking(True)
        self.btnPauseTimer.setTabletTracking(True)
        self.btnPauseTimer.setStyleSheet("QPushButton {\n"
                                         "    color:WHITE;\n"
                                         "    border: 5px solid #555;\n"
                                         "    border-radius: 13px;\n"
                                         "    border-style: outset;\n"
                                         "    background: qradialgradient(\n"
                                         "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                         "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                         "        );\n"
                                         "    padding-bottom: 2px;\n"
                                         "    padding-top: 3px;\n"
                                         "    background-color: #0045A8;\n"
                                         "    font: 75 18pt \"Tahoma\";\n"
                                         "    }\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background: qradialgradient(\n"
                                         "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                         "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                         "        );\n"
                                         "    background-color: #00327A;\n"
                                         "    }\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    border-style: inset;\n"
                                         "    background: qradialgradient(\n"
                                         "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                         "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                         "        );\n"
                                         "background-color: #001C45;\n"
                                         "    }")
        self.btnPauseTimer.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Images/Icon/media-pause-svgrepo-com.png.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btnPauseTimer.setIcon(icon3)
        self.btnPauseTimer.setIconSize(QtCore.QSize(22, 25))
        self.btnPauseTimer.setObjectName("btnPauseTimer")
        self.horizontalLayout_14.addWidget(self.btnPauseTimer)
        self.btnStopTimer = QtWidgets.QPushButton(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStopTimer.sizePolicy().hasHeightForWidth())
        self.btnStopTimer.setSizePolicy(sizePolicy)
        self.btnStopTimer.setMinimumSize(QtCore.QSize(0, 36))
        self.btnStopTimer.setMaximumSize(QtCore.QSize(100, 36))
        self.btnStopTimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStopTimer.setMouseTracking(True)
        self.btnStopTimer.setTabletTracking(True)
        self.btnStopTimer.setStyleSheet("QPushButton {\n"
                                        "    color:WHITE;\n"
                                        "    border: 5px solid #555;\n"
                                        "    border-radius: 13px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                        "        );\n"
                                        "    padding-bottom: 2px;\n"
                                        "    padding-top: 3px;\n"
                                        "    background-color: #0045A8;\n"
                                        "    font: 75 18pt \"Tahoma\";\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                        "        );\n"
                                        "    background-color: #00327A;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "background-color: #001C45;\n"
                                        "    }")
        self.btnStopTimer.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Images/Icon/media-stop-svgrepo-com.png.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btnStopTimer.setIcon(icon4)
        self.btnStopTimer.setIconSize(QtCore.QSize(18, 18))
        self.btnStopTimer.setObjectName("btnStopTimer")
        self.horizontalLayout_14.addWidget(self.btnStopTimer)
        self.gridLayout.addWidget(self.frame_29, 0, 0, 1, 1)
        self.btnStart = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        self.btnStart.setMinimumSize(QtCore.QSize(0, 43))
        self.btnStart.setMaximumSize(QtCore.QSize(200, 60))
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStart.setMouseTracking(True)
        self.btnStart.setTabletTracking(True)
        self.btnStart.setStyleSheet("QPushButton {\n"
                                    "    color:#D1D1D1;\n"
                                    "    border: 5px solid #555;\n"
                                    "    border-radius: 13px;\n"
                                    "    border-style: outset;\n"
                                    "    background: qradialgradient(\n"
                                    "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                    "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                    "        );\n"
                                    "    padding-bottom: 1px;\n"
                                    "    background-color: #0045A8;\n"
                                    "    font: 87 16pt \"Arial Black\";\n"
                                    "    }\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background: qradialgradient(\n"
                                    "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                    "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                    "        );\n"
                                    "    background-color: #00327A;\n"
                                    "    }\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    border-style: inset;\n"
                                    "    background: qradialgradient(\n"
                                    "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                    "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                    "        );\n"
                                    "background-color: #001C45;\n"
                                    "    }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Images/Icon/boxing-white.png.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon5)
        self.btnStart.setIconSize(QtCore.QSize(34, 33))
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_13)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border:0;\n"
                                   "background-color: #000000;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(4, 8, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setStyleSheet("background-color: #23A4E6;\n"
                                    "border-radius: 30px;\n"
                                    "color: white")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_26 = QtWidgets.QFrame(self.frame_10)
        self.frame_26.setStyleSheet("")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_28 = QtWidgets.QFrame(self.frame_26)
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.formLayout = QtWidgets.QFormLayout(self.frame_28)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(260, 0, 45, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelRound = QtWidgets.QLabel(self.frame_28)
        self.labelRound.setMaximumSize(QtCore.QSize(503, 130))
        self.labelRound.setSizeIncrement(QtCore.QSize(0, 0))
        self.labelRound.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelRound.setStyleSheet("font: 75 55pt \"Tahoma\";")
        self.labelRound.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelRound.setIndent(-1)
        self.labelRound.setObjectName("labelRound")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelRound)
        self.lblCountRound = QtWidgets.QLabel(self.frame_28)
        self.lblCountRound.setMinimumSize(QtCore.QSize(502, 130))
        self.lblCountRound.setMaximumSize(QtCore.QSize(502, 130))
        self.lblCountRound.setAutoFillBackground(False)
        self.lblCountRound.setStyleSheet("font: 87 80pt \"Arial\";\n"
                                         "margin: 0;\n"
                                         "padding: 0;\n"
                                         "margin-top: 8px;\n"
                                         "font-weight: bold;\n"
                                         "")
        self.lblCountRound.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblCountRound.setObjectName("lblCountRound")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblCountRound)
        self.verticalLayout_13.addWidget(self.frame_28)
        self.lblTimer = QtWidgets.QLabel(self.frame_26)
        self.lblTimer.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(310)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lblTimer.setFont(font)
        self.lblTimer.setMouseTracking(False)
        self.lblTimer.setTabletTracking(False)
        self.lblTimer.setAcceptDrops(False)
        self.lblTimer.setStyleSheet("font: 75 310pt \"Arial\";\n"
                                    "margin: 5px 5px 5px 5px;")
        self.lblTimer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTimer.setScaledContents(True)
        self.lblTimer.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTimer.setObjectName("lblTimer")
        self.verticalLayout_13.addWidget(self.lblTimer)
        self.verticalLayout_12.addWidget(self.frame_26)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frame_11.setStyleSheet("background-color:#000000;\n"
                                    "padding: 0 20px;\n"
                                    "")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnQuick1 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick1.setMouseTracking(True)
        self.btnQuick1.setTabletTracking(True)
        self.btnQuick1.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick1.setObjectName("btnQuick1")
        self.horizontalLayout_2.addWidget(self.btnQuick1)
        self.btnQuick2 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick2.setMouseTracking(True)
        self.btnQuick2.setTabletTracking(True)
        self.btnQuick2.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick2.setObjectName("btnQuick2")
        self.horizontalLayout_2.addWidget(self.btnQuick2)
        self.btnQuick3 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick3.setMouseTracking(True)
        self.btnQuick3.setTabletTracking(True)
        self.btnQuick3.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick3.setObjectName("btnQuick3")
        self.horizontalLayout_2.addWidget(self.btnQuick3)
        self.btnQuick4 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick4.setMouseTracking(True)
        self.btnQuick4.setTabletTracking(True)
        self.btnQuick4.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick4.setObjectName("btnQuick4")
        self.horizontalLayout_2.addWidget(self.btnQuick4)
        self.btnQuick5 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick5.setMouseTracking(True)
        self.btnQuick5.setTabletTracking(True)
        self.btnQuick5.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick5.setObjectName("btnQuick5")
        self.horizontalLayout_2.addWidget(self.btnQuick5)
        self.btnQuick6 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick6.setMouseTracking(True)
        self.btnQuick6.setTabletTracking(True)
        self.btnQuick6.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick6.setObjectName("btnQuick6")
        self.horizontalLayout_2.addWidget(self.btnQuick6)
        self.btnQuick7 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick7.setMouseTracking(True)
        self.btnQuick7.setTabletTracking(True)
        self.btnQuick7.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick7.setObjectName("btnQuick7")
        self.horizontalLayout_2.addWidget(self.btnQuick7)
        self.btnQuick8 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick8.setMouseTracking(True)
        self.btnQuick8.setTabletTracking(True)
        self.btnQuick8.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick8.setObjectName("btnQuick8")
        self.horizontalLayout_2.addWidget(self.btnQuick8)
        self.btnQuick9 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick9.setMouseTracking(True)
        self.btnQuick9.setTabletTracking(True)
        self.btnQuick9.setStyleSheet("QPushButton {\n"
                                     "    color:WHITE;\n"
                                     "    border: 5px solid #555;\n"
                                     "    border-radius: 13px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding-bottom: 2px;\n"
                                     "    padding-top: 3px;\n"
                                     "    background-color: #0045A8;\n"
                                     "    font: 87 18pt \"Arial\";\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    background-color: #00327A;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "background-color: #001C45;\n"
                                     "    }")
        self.btnQuick9.setObjectName("btnQuick9")
        self.horizontalLayout_2.addWidget(self.btnQuick9)
        self.btnQuick10 = QtWidgets.QPushButton(self.frame_11)
        self.btnQuick10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick10.setMouseTracking(True)
        self.btnQuick10.setTabletTracking(True)
        self.btnQuick10.setStyleSheet("QPushButton {\n"
                                      "    color:WHITE;\n"
                                      "    border: 5px solid #555;\n"
                                      "    border-radius: 13px;\n"
                                      "    border-style: outset;\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                      "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                      "        );\n"
                                      "    padding-bottom: 2px;\n"
                                      "    padding-top: 3px;\n"
                                      "    background-color: #0045A8;\n"
                                      "    font: 87 18pt \"Arial\";\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                      "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                      "        );\n"
                                      "    background-color: #00327A;\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border-style: inset;\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                      "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                      "        );\n"
                                      "background-color: #001C45;\n"
                                      "    }")
        self.btnQuick10.setObjectName("btnQuick10")
        self.horizontalLayout_2.addWidget(self.btnQuick10)
        self.btnQuick10_2 = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQuick10_2.sizePolicy().hasHeightForWidth())
        self.btnQuick10_2.setSizePolicy(sizePolicy)
        self.btnQuick10_2.setMinimumSize(QtCore.QSize(0, 0))
        self.btnQuick10_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.btnQuick10_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuick10_2.setMouseTracking(True)
        self.btnQuick10_2.setTabletTracking(True)
        self.btnQuick10_2.setStyleSheet("QPushButton {\n"
                                        "    color:WHITE;\n"
                                        "    border: 5px solid #555;\n"
                                        "    border-radius: 13px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                        "        );\n"
                                        "    background-color: #0045A8;\n"
                                        "    font: 87 10pt \"Arial\";\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                        "        );\n"
                                        "    background-color: #00327A;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "background-color: #001C45;\n"
                                        "    }")
        self.btnQuick10_2.setObjectName("btnQuick10_2")
        self.horizontalLayout_2.addWidget(self.btnQuick10_2)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.lblFightMinutes.setBuddy(self.comboFightMinutes)
        self.lblFightSecond.setBuddy(self.comboFightSecond)
        self.retranslateUi(MainWindow)
        self.comboFightSecond.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnQuick1.clicked.connect(lambda: self.Quickbtns(1))
        self.btnQuick2.clicked.connect(lambda: self.Quickbtns(2))
        self.btnQuick3.clicked.connect(lambda: self.Quickbtns(3))
        self.btnQuick4.clicked.connect(lambda: self.Quickbtns(4))
        self.btnQuick5.clicked.connect(lambda: self.Quickbtns(5))
        self.btnQuick6.clicked.connect(lambda: self.Quickbtns(6))
        self.btnQuick7.clicked.connect(lambda: self.Quickbtns(7))
        self.btnQuick8.clicked.connect(lambda: self.Quickbtns(8))
        self.btnQuick9.clicked.connect(lambda: self.Quickbtns(9))
        self.btnQuick10.clicked.connect(lambda: self.Quickbtns(10))
        self.btnSave.clicked.connect(self.SendData)
        self.btnDelete.clicked.connect(self.DeleteData)
        self.btnStart.clicked.connect(self.starttimer)
        self.btnPauseTimer.clicked.connect(self.Pausetimer)
        self.btnStopTimer.clicked.connect(self.stoptimer)
        self.btnQuick10_2.clicked.connect(self.aboutus)
        self.btnPauseTimer.setEnabled(False)
        self.btnStopTimer.setEnabled(False)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Title:"))
        self.lineEditTitle.setPlaceholderText(_translate("MainWindow", "Please enter title"))
        self.lblTimeFight.setText(_translate("MainWindow", "Time:"))
        self.lblFightMinutes.setText(_translate("MainWindow", "Min: "))
        for fighminu in range(0, 60):
            self.comboFightMinutes.setItemText(fighminu, _translate("MainWindow", f"{fighminu}"))
        self.lblFightSecond.setText(_translate("MainWindow", "sec: "))
        for fightsecs in range(0, 60):
            self.comboFightSecond.setItemText(fightsecs, _translate("MainWindow", f"{fightsecs}"))
        self.lblTimeRest.setText(_translate("MainWindow", "Rest:"))
        self.lblRestMinutes.setText(_translate("MainWindow", "Min:"))
        for restminu in range(0, 60):
            self.comboRestMinutes.setItemText(restminu, _translate("MainWindow", f"{restminu}"))
        self.lblRestSecond.setText(_translate("MainWindow", "sec: "))
        for restsecs in range(0, 60):
            self.comboRestSecond.setItemText(restsecs, _translate("MainWindow", f"{restsecs}"))
        self.lblWait.setText(_translate("MainWindow", "Wait:"))
        for wait in range(0, 60):
            self.comboWait.setItemText(wait, _translate("MainWindow", f"{wait}"))
        self.lblRound.setText(_translate("MainWindow", "Round:"))
        for round in range(0, 100):
            self.comboRound.setItemText(round, _translate("MainWindow", f"{round + 1}"))
        self.lblQuick.setText(_translate("MainWindow", "Quick:"))
        for quick in range(0, 10):
            self.ComboQuick.setItemText(quick, _translate("MainWindow", f"{quick + 1}"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.labelRound.setText(_translate("MainWindow", "Round:"))
        self.lblCountRound.setText(_translate("MainWindow", "00"))
        self.lblTimer.setText(_translate("MainWindow", "00:00"))
        self.btnQuick1.setText(_translate("MainWindow", "1"))
        self.btnQuick2.setText(_translate("MainWindow", "2"))
        self.btnQuick3.setText(_translate("MainWindow", "3"))
        self.btnQuick4.setText(_translate("MainWindow", "4"))
        self.btnQuick5.setText(_translate("MainWindow", "5"))
        self.btnQuick6.setText(_translate("MainWindow", "6"))
        self.btnQuick7.setText(_translate("MainWindow", "7"))
        self.btnQuick8.setText(_translate("MainWindow", "8"))
        self.btnQuick9.setText(_translate("MainWindow", "9"))
        self.btnQuick10.setText(_translate("MainWindow", "10"))
        self.btnQuick10_2.setText(_translate("MainWindow", "about us"))
        self.comboFightMinutes.currentIndexChanged.connect(self.set_timer_fight)
        self.comboFightSecond.currentIndexChanged.connect(self.set_timer_fight)
        self.comboRestMinutes.currentIndexChanged.connect(self.set_timer_rest)
        self.comboRestSecond.currentIndexChanged.connect(self.set_timer_rest)
        self.comboRound.currentIndexChanged.connect(self.set_timer_fight)
        self.comboWait.currentIndexChanged.connect(self.set_timer_wait)
import TimerBoxingicon_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())