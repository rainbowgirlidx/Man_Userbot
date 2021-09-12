class Text:
    need = "`Balas file mp3 atau simpan judul lagu!`"
    no_admin = "`Anda tidak memiliki izin untuk melakukan ini!`"
    download = "`Mendownload...`"
    uploading = "`Uploading...`"
    helper = """
**Perintah:**\n
  - `{x}alive` - __Periksa apakah asisten aktif.__
  - `{x}play <link / answer to mp3> - sounds music__
  - `{x}pause` - __Menjeda Lagu.__
  - `{x}resume` - __Melanjutkan Lagu.__
  - `{x}song <nama lagu> - __mengunduh musik.__
**Man UserBot**"""


async def startedsong(pycalls, message, song):
    try:
        await pycalls.stream(message.chat.id, song)
    except Exception as e:
        await message.reply_text(f"**Tidak dapat berbunyi!**\n\n**ERROR**\n{e}")
