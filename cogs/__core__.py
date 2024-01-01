import json

import discord
from discord.ext import commands


with open("config.json") as json_file:
    data = json.load(json_file)
    community_server_id = data["community_server_id"]


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            status=discord.Status.online, activity=discord.Game("https://fumes.top")
        )

        await self.bot.tree.sync()
        await self.bot.tree.sync(guild=discord.Object(id=community_server_id))

        self.bot.log.info("FumeStop is ready")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if message.guild and message.guild.me in message.mentions:
            await message.reply(
                content="Hello there! I'm the FumeStop community manager bot."
            )


async def setup(bot):
    await bot.add_cog(Core(bot))
