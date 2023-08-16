import asyncio
from telethon import TelegramClient, events
import random
from telethon.errors import MessageIdInvalidError

api_id = 
api_hash = ''

async def main():
    client = TelegramClient(', , ')

    @client.on(events.MessageEdited(from_users=6149996968))
    async def handle_message_edited(event):
        if "CHARACTER" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+0.6 )  
                await event.click(0, 0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.NewMessage(from_users=6149996968))
    async def handle_new_message(event):
        if "level" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random()+0.6 )  
                await event.click(0)
            return

    @client.on(events.NewMessage(from_users=6149996968))
    async def handle_quota(event):
        if "QUOTA" in event.raw_text:
            await asyncio.sleep(random.random() + 1)  
            await event.client.send_message(6149996968, "/enter_dungeon")

    @client.on(events.NewMessage(from_users=6149996968))
    async def handle_hell(event):
        if "HELL" in event.raw_text:
            await asyncio.sleep(random.random() + 1)  
            await event.click(1, 2)
        return

    @client.on(events.NewMessage(from_users=6149996968))
    async def handle_defeated(event):
        if any(keyword in event.raw_text for keyword in ["DED", "defeated", "entered"]):
            await asyncio.sleep(random.random() + 0.5)  
            await event.client.send_message(6149996968, "/explore")

    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
