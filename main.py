from telethon import TelegramClient, events, sync

# client.get_messages('username') to get messages from a specific user 
# client.download_profile_photo('me') get profile pic (mine & others)

class client:
    def __init__(self):
        TgCli = TelegramClient('Python Telegram Client', 999, ":(")
        TgCli.connect()
        phone_num = input("Phone number here: ")
        TgCli.send_code_request(phone_num)
        pin = input("Account password (if you don't have, leave blank)")
        if(len(pin) >1):
            self.CLI = TgCli.sign_in(phone_num, input("Enter the code you recived: "), password=pin)
        self.CLI = TgCli.sign_in(phone_num, input("Enter the code you recived: "))
        TgCli.add_event_handler(self.newMessage, events.NewMessage())
    
    def newMessage(self, event: events.NewMessage):
        print(event.from_users)

client()