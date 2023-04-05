from telethon import TelegramClient, events, sync
from PySide6 import QtCore, QtWidgets, QtGui

# client.get_messages('username') to get messages from a specific user 
# client.download_profile_photo('me') get profile pic (mine & others)


class client:
    def __init__(self):
        self.TgCli = TelegramClient('Python Telegram Client', 999, ":(")
        self.TgCli.connect()
        self.GUI = gui(self)
        self.GUIapp = QtWidgets.QApplication([])
        widget = self.GUI()
        widget.resize(800, 600)
        widget.show()
        with open("style.css", "r") as css:
            self.GUIapp.setStyleSheet(css.read())
        self.GUIapp.exec()
        ###############################################################################################
    
    def newMessage(self, event: events.NewMessage):
        print(event.from_users)

class gui(QtWidgets.QTWidget):
    def __init__(self, client: client):
        self.TGcli = client
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    
    def CodeButton_clicked(self):
        self.TGcli.TgCli.send_code_request(self.PhoneInput.text())
        self.PinInput.setEnabled(True)
        self.PinInput.setObjectName("PinInput_enabled")
    
    def LoginButton_clicked(self):
        if(len(self.PasswordInput.text()) >1):
            self.TgCli.CLI = self.TgCli.TgCli.sign_in(self.PhoneInput.text(), self.PinInput.text(), password=self.PasswordInput.text())
        self.TgCli.CLI = self.TgCli.TgCli.sign_in(self.PhoneInput.text(), self.PinInput.text())
        self.TgCli.add_event_handler(self.TgCli.newMessage, events.NewMessage())
    
    def show_login_page(self):
        PhoneText = QtWidgets.QLabel("Phone Number")
        PhoneText.setObjectName("phoneText")
        ###
        horizontal1 = QtWidgets.QLBoxLayout(self)
        self.PhoneInput = QtWidgets.QLineEdit()
        self.PhoneInput.setValidator(QtCore.QRegularExpression("""^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"""))
        CodeButton = QtWidgets.QPushButton("Send Code")
        CodeButton.clicked.connect(self.CodeButton_clicked)
        horizontal1.addWidget(self.PhoneInput)
        horizontal1.addWidget(CodeButton)
        ###
        PinText = QtWidgets.QLabel("PinCode from Telegram")
        PinText.setObjectName("pinText")
        ###
        self.PinInput = QtWidgets.QLineEdit()
        self.PinInput.setEnabled(False)
        self.PinInput.setObjectName("PinInput_disabled")
        ###
        PasswordText = QtWidgets.QLabel("Telegram Password (only if you have)")
        PasswordText.setObjectName("passwordText")
        ###
        self.PasswordInput = QtWidgets.QLineEdit()
        self.PasswordInput.setObjectName("passwordInput")
        ###
        LoginButton = QtWidgets.QPushButton("Send Code")
        LoginButton.clicked.connect(self.LoginButton_clicked)
        


client()