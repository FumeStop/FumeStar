from __future__ import annotations
from typing import TYPE_CHECKING

import math
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands

if TYPE_CHECKING:
    from bot import FumeStop


class General(commands.Cog):
    def __init__(self, bot: FumeStop):
        self.bot: FumeStop = bot

    @app_commands.command(name="ping")
    async def _ping(self, ctx: discord.Interaction):
        """Returns the API and bot latency."""
        # noinspection PyUnresolvedReferences
        await ctx.response.defer(thinking=True)

        embed = discord.Embed(colour=self.bot.embed_color)
        embed.description = "**Pong!**"

        ms = self.bot.latency * 1000

        embed.add_field(name="API latency (Heartbeat)", value=f"`{int(ms)} ms`")

        t1 = datetime.utcnow().strftime("%f")

        await ctx.edit_original_response(embed=embed)

        t2 = datetime.utcnow().strftime("%f")
        diff = int(math.fabs((int(t2) - int(t1)) / 1000))

        embed.add_field(name="Bot latency (Round-trip)", value=f"`{diff} ms`")

        await ctx.edit_original_response(embed=embed)


async def setup(bot: FumeStop):
    await bot.add_cog(General(bot))
