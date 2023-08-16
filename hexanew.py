import asyncio
from telethon import TelegramClient, events
import random
from telethon.errors import MessageIdInvalidError

api_id = 22217626
api_hash = 'bfe14a2a0e0444f762db88231a463508'
is_poke_found = False

async def main():
    global is_poke_found
    client = TelegramClient('Aayu2809', api_id, api_hash)

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_hunting(event):
        global is_poke_found
        if any(keyword in event.raw_text for keyword in ["Slakoth", "Slaking", "Vigoroth" ,"Mankey","Machop","Dragonair","Scyther"]):
            await event.client.send_message(-860590576, "boys ur dad here")
            is_poke_found = True

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_new_message(event):
        global is_poke_found
        if not is_poke_found and "has appeared" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random()+0.75)
                await event.click(0, 0)

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_new_message(event):
        global is_poke_found
        if not is_poke_found and "challenged" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random()+0.75)
                await event.client.send_message(572621020, "/hunt")
                
    @client.on(events.NewMessage(from_users=572621020))
    async def handle_message_edited(event):
        if "HP" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+1)
                await event.click(0, 0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.MessageEdited(from_users=572621020))
    async def handle_message_edited(event):
        if "HP" in event.raw_text:
            try:
                await asyncio.sleep(random.random() +1)
                await event.click(0, 0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                
    @client.on(events.MessageEdited(from_users=572621020))
    async def handle_defeated(event):
        if "fainted" in event.raw_text:
            await asyncio.sleep(random.random() + 1)
            await event.client.send_message(572621020, "/hunt")

    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
