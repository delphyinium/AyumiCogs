import aiohttp
import discord


from redbot.core import commands

class Animal(commands.Cog):
    """cog for showing you that you have no future!"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command()
    @commands.guild_only()
    async def femboy(self, ctx):
        """Fetch a random picture of bro moment!"""
        try:
            async with self.session.get("https://femboyapi.crispie.ovh/api/random") as response:
                data = await response.json()
                embed = discord.Embed(title="COOM", color=0x00ff00)
                embed.set_image(url=data[0]["url"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github") 

    
    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())