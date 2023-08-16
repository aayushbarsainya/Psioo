import asyncio
from telethon import TelegramClient, events
import random
from telethon.errors import MessageIdInvalidError

api_id = 22217626
api_hash = 'bfe14a2a0e0444f762db88231a463508'

async def main():
    client = TelegramClient('Aayu2809', 22217626, 'bfe14a2a0e0444f762db88231a463508')

    @client.on(events.MessageEdited(from_users=5416991774))
    async def handle_message_edited(event):
        if "shinobi" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+0.5)  
                await event.click(0, 1)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.MessageEdited(from_users=5416991774))
    async def handle_message_edited(event):
        if "next shinobi" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+0.5)  
                await event.click(0, 0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.MessageEdited(from_users=5416991774))
    async def handle_message_edited(event):
        if "| Choji Akimichi |" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+0.5)  
                await event.click(0, 0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                                                
    @client.on(events.NewMessage(from_users=5416991774))
    async def handle_message_edited(event):
        if "| Choji Akimichi |" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+0.5 )  
                await event.click(2,1)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                
    @client.on(events.MessageEdited(from_users=5416991774))
    async def handle_message_edited(event):
        if "| Sakura Haruno |" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+0.5 )  
                await event.click(2,1)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                
    @client.on(events.MessageEdited(from_users=5416991774))
    async def handle_message_edited(event):
        if "| Hinata Hyuga |" in event.raw_text:
            try:
                await asyncio.sleep(random.random()+0.5 )  
                await event.click(0, 0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass 
                
    @client.on(events.NewMessage(from_users=5416991774))
    async def handle_new_message(event):
        if "challenged" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random()+0.5)  
                await event.click(0)
            return
            
    @client.on(events.NewMessage(from_users=5416991774))
    async def handle_new_message(event):
        if "appeared" in event.raw_text:
            if event.buttons:
                await event.client.send_message(-860590576, "Yowai Mo")   
    @client.on(events.NewMessage(from_users=5416991774))
    async def handle_new_message(event):
        if "game" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random() +1)  
                await event.click(3,0)
            return
            
    @client.on(events.MessageEdited(from_users=5416991774))

    async def handle_defeated(event):
        if "exp" in event.raw_text:
            await asyncio.sleep(random.random() +1)  
            await event.client.send_message(5416991774, "/explore")

    @client.on(events.MessageEdited(from_users=5416991774))

    async def handle_defeated(event):
        if "fear" in event.raw_text:
            await asyncio.sleep(random.random()+1 )  
            await event.client.send_message(5416991774, "/explore")     
                                       
    @client.on(events.NewMessage(from_users=5416991774))
    async def handle_msgs(event):
        if any(keyword in event.raw_text for keyword in ["exp", "chest", "gems","masks" , 'fear','Timeout']):
            await asyncio.sleep(random.random()+0.6 )  
            await event.client.send_message(5416991774, "/explore")

    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
                