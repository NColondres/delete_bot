import discord
import os
import logging

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents, max_messages=5000)


@bot.event
async def on_message_delete(message):
    async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
        deleter = entry.user
    await message.channel.send(f"{deleter.name} deleted message sent by {message.author.name}\nMessage:\n{message.content}")

if __name__ == "__main__":
    bot.run(BOT_TOKEN, log_level=logging.WARN)