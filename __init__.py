from .FunnyAPI import FunnyAPI


def setup(bot):
    bot.add_cog(FunnyAPI(bot))
    return bot.add_cog(FunnyAPI(bot))