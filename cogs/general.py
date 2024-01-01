import math
import json
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands


with open("config.json") as json_file:
    data = json.load(json_file)
    community_server_id = data["community_server_id"]


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Returns the API and bot latency")
    @app_commands.guilds(community_server_id)
    async def _ping(self, ctx: discord.Interaction):
        # noinspection PyUnresolvedReferences
        await ctx.response.defer(thinking=True)

        embed = discord.Embed(colour=self.bot.embed_colour)
        embed.description = "**Pong!**"

        ms = self.bot.latency * 1000

        embed.add_field(name="API latency (Heartbeat)", value=f"`{int(ms)} ms`")

        t1 = datetime.utcnow().strftime("%f")

        await ctx.edit_original_response(embed=embed)

        t2 = datetime.utcnow().strftime("%f")
        diff = int(math.fabs((int(t2) - int(t1)) / 1000))

        embed.add_field(name="Bot latency (Round-trip)", value=f"`{diff} ms`")

        await ctx.edit_original_response(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
