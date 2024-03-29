#client ID : 1041608834755612742
#token : 
#permission integer : 256064, 137439471680

import discord

from discord.utils import get
from discord import FFmpegPCMAudio
import youtube_dl
import asyncio
from functools import partial
from async_timeout import timeout

from discord.ext import commands
from datetime import datetime, timedelta
import itertools

message_lastseen = datetime.now()
message_lastseen1 = datetime.now()
message_lastseen11 = datetime.now()
message_lastseen111 = datetime.now()
message2_lastseen = datetime.now()
message3_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5" ## song will end if no this line
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        await ctx.send(f'```ini\n[Added {data["title"]} to the Queue.]\n```') #delete after can be added

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source, **ffmpeg_options), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options), data=data, requester=requester)

class MusicPlayer:
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                del players[self._guild]
                return await self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'There was an error processing your song.\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.np = await self._channel.send(f'**Now Playing:** `{source.title}` requested by '
                                               f'`{source.requester}`')
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

            try:
                # We are no longer playing this song...
                await self.np.delete()
            except discord.HTTPException:
                pass

    async def destroy(self, guild):
        """Disconnect and cleanup the player."""
        del players[self._guild]
        await self._guild.voice_client.disconnect()
        return self.bot.loop.create_task(self._cog.cleanup(guild))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("You type {0}".format(par))

@bot.command()
async def help(ctx):
    #help
    #send
    #สวัสดีบอท
    #my user
    #บอทนายชื่ออะไร
    #บอกชื่อผมหน่อยครับ
    #My ID
    #!logout
    #play
    #stop
    #pause
    #resume
    #leave
    #queue
    #skip
    emBed = discord.Embed(title="DJ. Show Command list", description="All avaliable command", color= 0x51bf47)
    emBed.add_field(name="!help", value="Get help command", inline=False)
    emBed.add_field(name="!send", value="Say hello to user", inline=False)
    emBed.add_field(name="สวัสดีบอท", value="บอททักทายเรากลับ", inline=False)
    emBed.add_field(name="บอทนายชื่ออะไร", value="บอทบอกชื่อของบอทเอง", inline=False)
    emBed.add_field(name="My ID", value="บอทบอก ID ของ user", inline=False)
    emBed.add_field(name="!logout", value="บอทออฟไลน์", inline=False)
    emBed.add_field(name="!play [ลิ้งเพลง]", value="ใส่ลิ้งค์หลัง !play เพื่อเล่นเพลง", inline=False)
    emBed.add_field(name="!stop", value="หยุดเพลงนั้น เเละข้ามไปเลย", inline=False)
    emBed.add_field(name="!pause", value="หยุดเพลงนั้นชั่วคราว", inline=False)
    emBed.add_field(name="!resume", value="เพลงกลับมาเล่นใหม่", inline=False)
    emBed.add_field(name="!leave", value="บอทจะออกจาก Voice Channel นั้นๆ", inline=False)
    emBed.add_field(name="!queue", value="แสดงคิวเพลงทั้งหมด", inline=False)
    emBed.add_field(name="!skip", value="ข้ามเพลงที่กำลังเล่นอยู่ ณ ขนาดนั้น", inline=False)
    emBed.set_thumbnail(url="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png")
    emBed.set_footer(text="DJ Show.", icon_url="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png")
    await ctx.channel.send(embed=emBed)

@bot.command()
async def send(ctx):
    await ctx.channel.send("Hello")

@bot.event
async def on_message(message):
    global message_lastseen, message2_lastseen, message3_lastseen\
        , message_lastseen1, message_lastseen11, message_lastseen111

    bad_word = ["ไอ้สัตว์", "ควย", "เหี้ย", "พ่อมึงตาย"\
        , "แม่มึงตาย", "สัด", "ไอ้สัด", "พ่อมึงอะ", "แม่มึงอะ"\
            , "ไปตายซะ", "หำ", "หี", "ขี้", "ไอ้สาด", "มึง"\
                , "กู", "ห่า", "อีดอก", "อีสัตว์", "ห่าเหว", "เย็ด"\
                    , "สัส", "คุวย", "คาวย", "ควาย", "ไอควาย"\
                        , "ไอโง่", "เย็ดพ่อ", "ค ว ย", "พ่องตาย"\
                            , "แม่มึง", "พ่อมึง", "fuck", "Fuck"\
                                , "เ ย็ ด", "ชาติหมา", "หนังหมา"\
                                    , "ชาติสุนัข", "หนังสุนัข", "หมออ้อย"\
                                        , "หมอย", "หรรม", "หัม", "ตอแหล"\
                                            , "เดรัจฉาน", "สถุล", "เศษมนุษย์"\
                                                , "ส้นตีน", "แดก", "กาก", "แดกตีน"\
                                                    , "สันขวาน", "ไอระยำ", "ไอเปรต"\
                                                        , "อีร่าน", "ไอkวย", "คูไว", "ชาติชั่ว"\
                                                            , "อีเสเพล", "แตด", "ไอถ่อย", "shit"\
                                                                , "เสือก"\
                                                                    , "ส่อหล่อ"\
                                                                        , "สู่รู่"\
                                                                            , "นิกก้า"\
                                                                    , "ฟัค", "ร่าน"\
                                                                        , "ไอ้ถ่อย", "ครวย"\
                                                                        , "กระหรี่", "ห อ ม"\
                                                                            , "ถุย", "ทุย"\
                                                                            , "ตูด", "สำโต่ย"\
                                                                                , "ฆูวาย", "ฟวย"\
                                                                                , "ฆูไว", "ฮี้", "ษัส", "ษัศ", "ศัศ"\
                                                                                    , "ศัษ", "Hee", "hee"\
                                                                                        , "ควย", "สันดานหมา", "สันดานสุนัข"\
                                                                                            , "ชักว่าว", "แ ห ก H e e", "เงี่ยน"\
                                                                                                , "Pornhub", "พรฮับ", "บ้ากาม", "ห่วยแตก", "อีเหี้ย"]

    if message.content == "สวัสดีบอท"and datetime.now() >= message_lastseen1:
        message_lastseen1 = datetime.now() + timedelta(seconds=5)
        await message.channel.send('สวัสดี '+str(message.author.name))

    elif message.content == "my user" and datetime.now() >= message_lastseen11:
        message_lastseen11 = datetime.now() + timedelta(seconds=5)
        await message.channel.send(str(message.author.name) + ' คุณชื่อนี้นะครับ')

    elif message.content == "บอทนายชื่ออะไร" and datetime.now() >= message_lastseen111:
        message_lastseen111 = datetime.now() + timedelta(seconds=5)
        await message.channel.send("My name is : "+str(bot.user.name))
        print('{0} Has Used "บอทนายชื่ออะไร" Time : {1} And will Avaliable in {2}'\
            .format(message.author.name, datetime.now(), message_lastseen111))

    elif message.content == "บอกชื่อผมหน่อยครับ" and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send("คุณชื่อ : "+str(message.author.name))

    elif message.content == "My ID" and datetime.now() >= message3_lastseen:
        message3_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send("ID : "+str(message.author.discriminator))

    elif message.content == "!logout":
        await bot.close()

    for word000 in bad_word:
        if word000 in message.content:
            await message.delete()
            await message.channel.send("มีคำหยาบอยู่ในข้อความของคุณ กรุณาพิมพ์ใหม่ด้วยคำสุภาพอีกครั้งครับ", delete_after = 5)

    await bot.process_commands(message)

@bot.command()
async def play(ctx,* ,search: str):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if voice_client == None:
        await ctx.channel.send("Joined")
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)

    _player = get_player(ctx)
    source = await YTDLSource.create_source(ctx, search, loop=bot.loop, download=False)

    await _player.queue.put(source)

players = {}
def get_player(ctx):
    try:
        player = players[ctx.guild.id]
    except:
        player = MusicPlayer(ctx)
        players[ctx.guild.id] = player
    
    return player

@bot.command()
async def stop(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("Bot not in any Voice CHannel")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("The bot is not in your voice channel. Please connect to {0} for input command".format(voice_client.channel))
        return

    voice_client.stop()

@bot.command()
async def pause(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("Bot not in any Voice Channel", delete_after = 300)
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("The bot is not in your voice channel. Please connect to {0} for input command".format(voice_client.channel))
        return

    voice_client.pause()

@bot.command()
async def resume(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("Bot not in any Voice Channel", delete_after = 300)
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("The bot is not in your voice channel. Please connect to {0} for input command".format(voice_client.channel), delete_after = 300)
        return

    voice_client.resume()

@bot.command()
async def leave(ctx):
    del players[ctx.guild.id]
    await ctx.voice_client.disconnect()

@bot.command()
async def queue(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None or not voice_client.is_connected():
        await ctx.channel.send("Bot not in any Voice Channel", delete_after = 300)
        return

    player = get_player(ctx)
    if player.queue.empty():
        return await ctx.send("There are no song in queue", delete_after = 300)
    
    upcoming = list(itertools.islice(player.queue._queue,0,player.queue.qsize()))
    fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
    embed = discord.Embed(title=f'Upcoming - Next {len(upcoming)}', description=fmt)
    await ctx.send(embed=embed)

@bot.command()
async def skip(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None or not voice_client.is_connected():
        await ctx.channel.send("Bot not in any Voice Channel", delete_after = 300)
        return

    if voice_client.is_paused():
        pass
    elif not voice_client.is_playing():
        return

    voice_client.stop()
    await ctx.send(f'**`{ctx.author}`**: Skipped the song!')
@bot.command()
async def loop(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None or not voice_client.is_connected():
        await ctx.channel.send("Bot not in any Voice Channel", delete_after = 300)
        return

bot.run('')
