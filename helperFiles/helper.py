import configparser

def init():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    data = {}

    data["api_id"] = config['Telegram']['api_id']
    data["api_hash"] = config['Telegram']['api_hash']
    data["username"] = config['Telegram']['username']
    data["phone"] = config['Telegram']['phone']
    data["channel_link"] = config['Telegram']['channel_link']

    return data