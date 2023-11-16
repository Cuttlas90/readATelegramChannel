from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)

from helperFiles.helper import init
from helperFiles.csv_helper import add_a_row


def gettingTelegramData(data):
    client = TelegramClient(data["username"], data["api_id"], data["api_hash"])
    async def main(phone):
        await client.start()
        print("Client Created")
        # Ensure you're authorized
        if await client.is_user_authorized() == False:
            await client.send_code_request(phone)
            try:
                await client.sign_in(phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Password: '))

        me = await client.get_me()

        # user_input_channel = input('enter entity(telegram URL or entity id):')
        user_input_channel =  data["channel_link"]
        if user_input_channel.isdigit():
            entity = PeerChannel(int(user_input_channel))
        else:
            entity = user_input_channel

        my_channel = await client.get_entity(entity)

        offset_id = 0
        limit = 1000
        all_messages = []
        total_messages = 0
        # Read total_count_limit number of last messages
        while True:
            print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
            history = await client(GetHistoryRequest(
                peer=my_channel,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                if message.message != None:
                    add_a_row('asset/telegramRecords.csv',[message.date.timestamp(), message.message.encode('utf-8'), message.id])
            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            

    # write needed data in a file
    with client:
        client.loop.run_until_complete(main(data["phone"]))


if __name__ == "__main__":
    data = init()
    gettingTelegramData(data)
