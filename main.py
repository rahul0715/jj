import subprocess
from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen
import asyncio
import logging
import time
import sys
import os

bot_token = os.environ.get("7361574071:AAFds5AYOFpqDizW660NPDqqrvExfOJ7zB0")

bot = Client(
    "bot",
    bot_token=bot_token,
    api_id=28426319,
    api_hash="b1e3ce7b9cc5d73e7c22c9e82ab3cbe9"
)
#Code written by @leo
@bot.on_message(filters.command(["start"]))
async def start(_,message):
  await message.reply_photo(photo="https://telegra.ph/file/1d0c6fe5961f466d596fa.jpg", caption="**𝙷𝚒!**\n\n**𝙶𝚒𝚟𝚎 /Leo ♌️ 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 T𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚛𝚘𝚖 A 𝚃𝚎𝚡𝚝 F𝚒𝚕𝚎.**🎓✨",
                            reply_markup=InlineKeyboardMarkup([
                           
                [
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/tigerxy09"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/tigerxy09")
                ]
                            ]))
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("**Restarted**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
#Code written by tiger
async def download_video(url, cmd, name):
    download_cmd = f'{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args "aria2c: -x 16 -j 32"'
    global failed_counter
    print(download_cmd)
    logging.info(download_cmd)
    k = subprocess.run(download_cmd, shell=True)
    if "visionias" in cmd and k.returncode != 0 and failed_counter <= 10:
        failed_counter += 1
        await asyncio.sleep(5)
        await download_video(url, cmd, name)
    failed_counter = 0
    try:
        if os.path.isfile(name):
            return name
        elif os.path.isfile(f"{name}.webm"):
            return f"{name}.webm"
        name = name.split(".")[0]
        if os.path.isfile(f"{name}.mkv"):
            return f"{name}.mkv"
        elif os.path.isfile(f"{name}.mp4"):
            return f"{name}.mp4"
        elif os.path.isfile(f"{name}.mp4.webm"):
            return f"{name}.mp4.webm"

        return name
    except FileNotFoundError as exc:
        return os.path.splitext(name)[0] + ".mp4"
#Code written by @St2Master    
async def send_vid(bot, m, cc, filename, name, prog):
    await prog.delete()
    xx = await bot.send_message(m.chat.id, f"**Generate Thumbnail** - {name}")
    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
    thumb = f"{filename}.jpg"
    logging.info("Default Thumb downloaded successfully!")
    
    duration_seconds = float(os.popen(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{filename}"').read())
    dur = int(duration_seconds)
    
    start_time = time.time()  
    await xx.delete()
    
    try:
        xxx = await bot.send_message(m.chat.id, f"**WaterMark Overlay on Video - ** {name}")
        subprocess.run(
            f'ffmpeg -i "{filename}" -i watermark.png -filter_complex '
            f'"[0][1]overlay=x=(W-w)*mod(n\,500)/500:y=(H-h)*mod(n\,1000)/1000" '
            f'"{filename}_watermark.mp4"',
            shell=True
        )
    except Exception as e:
        logging.error(f"Error Executing Command: {e}")
    
    watermark_video = f"{filename}_watermark.mp4"
    await xxx.delete()
#Code written by @St2Master    
    reply = await bot.send_message(m.chat.id, f"**Uploading :**\n\n**Name :** {name}\n\nCode By TiGer") 
 
    try:
        await bot.send_video(chat_id=m.chat.id, video=watermark_video, caption=cc, supports_streaming=True, height=720, width=1280, thumb=thumb, duration=dur, progress_args=(reply, start_time))
    except Exception as e:
        logging.error(f"Error while sending video: {e}")
        await bot.send_video(chat_id=m.chat.id, video=watermark_video, caption=cc, progress_args=(reply, start_time))
    
    os.remove(filename)
    os.remove(watermark_video)
    os.remove(thumb)
    await reply.delete()
#Code written by @St2Master
@bot.on_message(filters.command(["Leo"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('__Please Input Your Url __ \n\nEg: FileName: File Link or Send default any Video Url')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await input.delete()
        try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")
            links = [i.split("://", 1) for i in content]
            os.remove(x)
        except Exception as e:
            await m.reply_text(f"Error processing file: {e}")
            os.remove(x)
            return
    else:
        content = input.text
        content = content.split("\n")
        links = [i.split("://", 1) for i in content]
        await input.delete()
   
    await editable.edit(f"Total Links Found Are **{len(links)}**\n\nSend From Where You Want To Download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete()
    
    await editable.edit("**Enter Resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete()
    await editable.delete()
#Code written by @St2Master
    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)
    try:            
        for i in range(len(links)):
            name1 = links[i][0].replace(":", "Leo").replace("https", "").strip()
            name = f'{str(count).zfill(3)}){name1[:60]}'
            url = links[i][1]       
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
        
            elif "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"' 
            try:
                cc = f'**Vid_id  :** {str(count).zfill(3)}\n**Tɪᴛᴛʟᴇ :**__{name1}.mkv__\n'
                Show = f"** Downloading :**\n\n**Name :** {name}\nVideo Quality - {raw_text2}\n\n Code By TiGer"
                prog = await m.reply_text(Show)
                filename = await download_video(url, cmd, name)
                await prog.delete(True)
                await send_vid(bot, m, cc, filename, name, prog)
                count += 1
                time.sleep(1)
            except Exception as e:
                    await m.reply_text(f"**Downloading Interupted **\n\n**Name** : {name}\n**Link** : {url}\n\n ** Fail Reason :** {e}\n\n Code By TiGer")
                    continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**Done**🚦")

bot.run()

give me updated main.py
