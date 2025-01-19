import discord
from discord.ext import commands
from model import get_class
from discord_components import DiscordComponents, Button, ButtonStyle

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!! bot is ready, I am a bot {bot.user}!')

@bot.command()
async def pindai_sampah(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'Kardus\n' and hasil[1] >= 0.6:
                await ctx.send('ini adalah sampah kardus')
            elif hasil[0] == 'Kertas\n' and hasil[1] >= 0.6:
                await ctx.send('ini adalah sampah kertas')
            elif hasil[0] == 'Botol Kaca\n' and hasil[1] >= 0.6:
                await ctx.send('ini adalah sampah kaca')
            elif hasil[0] == 'Kaleng\n' and hasil[1] >= 0.6:
                await ctx.send('ini adalah sampah logam')
            elif hasil[0] == 'Botol Plastik\n' and hasil[1] >= 0.6:
                await ctx.send('ini adalah sampah plastik')
            else:
                await ctx.send('Gambarmu eror tidak terdeteksi! Kemungkinan :Salah Format, Blur/Kurang Jelas')
                await ctx.send('Kirim ulang gambarmu!')
    else:
        await ctx.send('Gaada gambarnya:<')


bot.run("MTI1NzMxOTA1Nzk4ODkxNTIzMA.GNXhLT.wFUAV2RVSck5kgFugN-xsmnKJpCkqziCVNp128")