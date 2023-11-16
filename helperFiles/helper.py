import configparser

def init():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    data = {}

    data["api_id"] = config['telegram']['api_id']
    data["api_hash"] = config['telegram']['api_hash']
    data["username"] = config['telegram']['username']
    data["phone"] = config['telegram']['phone']
    data["channel_link"] = config['telegram']['phone']

    return data