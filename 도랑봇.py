import discord
import random
import os


client = discord.Client()



@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='도랑아 도움말', type=1))

@client.event
async def on_message(message):
    if message.content.startswith("도랑아 도움말"):
        await client.send_message(message.channel, "``프사``\n\n``투표``\n명령어 앞에 꼭 내이름 불러")

    if message.content.startswith("도랑아 안녕"):
        await client.send_message(message.channel, "안뇽")
        
    if message.content.startswith("도랑아 뭐해"):
        a = ["게임하고 있음", "공부하는중인데 방해금지", "잘꺼야 건들지마", "멍때리고 있음", "몰라"]
        b = random.choice(a)
        await client.send_message(message.channel, b)

    if message.content.startswith("도랑아 프사"):
        memberid = message.content[6:]
        memberid = memberid.replace("<", "")
        memberid = memberid.replace("@", "")
        memberid = memberid.replace("!", "")
        memberid = memberid.replace(">", "")
        memberid = str(memberid)
        if memberid == "":
            memberid = message.author.id
            member = message.server.get_member(memberid)
            a = member.avatar_url
            if a == "":
                a = member.default_avatar_url
            embed = discord.Embed(title="", description="", color=0x62bf42)
            embed.set_author(name="진짜 프로필 너같이 생겼다")
            embed.set_footer(text="By 도랑")
            embed.set_thumbnail(url=a)
            await client.send_message(message.channel, embed=embed)

client.run('NTQ4ODU3NzgzNTUwODY5NTI1.D1LbQQ.CG-9TQJcBlV54mVUJamLVc4Fgc0')
