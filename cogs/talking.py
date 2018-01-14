import discord
from discord.ext import commands
from sys import argv

class Talking:
    """
    Talking as the bot.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.has_permissions(ban_members=True)
    @commands.command(hidden=True, pass_context=True)
    async def announce(self, ctx, *, inp):
        server = ctx.message.server
        await self.bot.send_message(discord.utils.get(server.channels, name='announcements'), inp)

    @commands.has_permissions(ban_members=True)
    @commands.command(hidden=True, pass_context=True)
    async def say(self, ctx, channel_destination: str, *, inp):
        channel = ctx.message.channel_mentions[0]
        await self.bot.send_message(channel, inp)

    @commands.has_permissions(administrator=True)
    @commands.command(hidden=True, pass_context=True)
    async def dm(self, ctx, channel_destination: str, *, inp):
        dest = ctx.message.mentions[0]
        dest2 = self.bot.get_channel('402196014485733387')
        await self.bot.send_message(dest, inp)
        await self.bot.send_message(dest2, inp)


def setup(bot):
    bot.add_cog(Talking(bot))
