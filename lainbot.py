import discord
import random
from discord import Game
from discord.ext.commands import Bot
TOKEN = 'nope'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await client.change_presence(game=discord.Game(name='lain help'))
    
    if message.content.startswith('lain roll dice'):
        msg = random.randint(1,6)
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain I love you'):
        msg = "I love you too, {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain say hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain say goodbye'):
        msg = 'Goodbye {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain code"):
        msg = "here is the lain bot github: https://github.com/tacitgenesis/Lain-Bot".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain game"):
        msg = 'http://laingame.net/'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain dab"):
        msg = 'https://imgur.com/ot6F47X'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('lain say you are a gamer'):
        msg = 'I am the most epic gamer {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain avatar'):
        msg = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/5ca09a54-c660-4578-89de-c0ec615b15bc/dad0kb5-dd8b3bac-2742-4b73-96f0-c6fae66ee020.jpg'
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain die'):
        msg = "I will live forever, however you will die a most painful death fool. https://i.4pcdn.org/x/1414265593395.gif"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain rise up'):
        msg = "I will already live forever, user. https://growingbranch.files.wordpress.com/2011/05/snapshot20110502230349.jpg"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith("lain I'm gonna say the n word"):
        msg = "mrs.obama get down"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith("lain wired"):
        msg = "the truth awaits, user. https://fauux.neocities.org/login.html"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith("lain information"):
        msg = "here is what you need, user. https://fauux.neocities.org/help.html"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith("lain invite"):
        msg = "invite lain bot to your server: https://discordbots.org/bot/530107695630647296"
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain say ame"):
        msg = "ame ame ame"
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain live"):
        msg = "I will live forever, thank you user. https://discordemoji.com/assets/emoji/smile_lain.png"
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain eat me"):
        msg = "NOM"
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain magic eight ball"):
        messages = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        msg = random.choice(messages)
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain help'):
        msg = """```the bot prefix is lain. the commands are:```
**===TALK TO LAIN===**
say hello
say goodbye
say you are a gamer
say ame
eat me
live
die
rise up
I love you
**===INTERACTION===**
hug
pat
slap
**===FUN===**
magic eight ball
game
roll dice
song
wired
information
site
**===IMAGES===**
image
gif
meme
quote
avatar
goose
dab
**===UTILITY===**
invite
help
code"""
        await client.send_message(message.channel, msg)



    if message.content.startswith("lain song"):
        songs = [
        'https://youtu.be/4-PkAQcuZOw',
        'https://youtu.be/SQ02E7qgZ_E',
        'https://youtu.be/H221MRRgFZs',
        'https://youtu.be/yO4myLCfN-Y',
        'https://youtu.be/5dbi4N6NGn4',
        'https://youtu.be/bEHUFRRK9Sk',
        'https://youtu.be/gZISvTviaj8',
        'https://youtu.be/eYMQnb2igTs',
        'https://youtu.be/N6Jn98ktFw0',
        'https://youtu.be/RVIreGd1-NA',
        'https://youtu.be/YSecmwH_AoQ',
        'https://youtu.be/rLiyFaLs8PY',
        'https://youtu.be/o0ndkiL5ivU',
        'https://youtu.be/pTzumRQKGgM',
        'https://youtu.be/28mTETQMRs4',
        'https://youtu.be/dvozrz9zWBg',
        'https://youtu.be/H40u9ufvSVo',
        'https://youtu.be/IQicDkntMVA',
        'https://youtu.be/MFcpcwdBYrk',
        'https://youtu.be/H221MRRgFZs?list=PLLiA91TyEc8tL1jj8RZ0zCkG1QCDUd8YX',
        'https://youtu.be/4DnCETKeHkc',
        'https://youtu.be/K00pcctFIuY',
        'https://youtu.be/qHT6eEKP3jI',
        ]
        msg = random.choice(songs)
        await client.send_message(message.channel, msg)
    
    huggo=[
        "http://i.imgur.com/tuH4gqZ.gif",
        "https://66.media.tumblr.com/18fdf4adcb5ad89f5469a91e860f80ba/tumblr_oltayyHynP1sy5k7wo1_400.gif",
        "https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935",
        "https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788",
        "http://i.imgur.com/I8LyQ9L.gif",
        "https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
        "https://media1.tenor.com/images/40aed63f5bc795ed7a980d0ad5c387f2/tenor.gif?itemid=11098589",
        "https://i.imgur.com/r9aU2xv.gif",
        "https://i.imgur.com/ntqYLGl.gif",
        "https://i.imgur.com/UMm95sV.gif",
        "https://37.media.tumblr.com/f2a878657add13aa09a5e089378ec43d/tumblr_n5uovjOi931tp7433o1_500.gif",
        "https://thumbs.gfycat.com/BlindOblongAmurratsnake-small.gif",
        "https://66.media.tumblr.com/291c8b98b219283f9e21927e7ef6c3f2/tumblr_mzscklfLYx1tptsy9o1_400.gif",
        "https://i.imgur.com/DBV5Ac9.gif",
        "https://i.imgur.com/x4koMxC.gif",
        "https://i.imgur.com/IESFOWD.gif",
        "https://i.imgur.com/Ed4DlVM.gif",
        "https://i.imgur.com/fhCVWgN.gif",
        "https://i.imgur.com/Ltmb8aa.gif",
        "https://i.imgur.com/c3WzMZu.gif",
        "https://media0.giphy.com/media/kvKFM3UWg2P04/giphy.gif?cid=3640f6095c8719d76e614e7932321eae",
        "https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif",
        "https://media.tenor.com/images/2e1d34d002d73459b6119d57e6a795d6/tenor.gif",
        "https://uploads.disquscdn.com/images/f5ee0928f31e1d867c85a1965005c54b3446595d2ff31989dc06a213679cc272.gif",
        "https://media1.tenor.com/images/fdefc2134e17de3bb15bc398ff66c6ca/tenor.gif?itemid=9469917",
        "https://media1.tenor.com/images/5845f40e535e00e753c7931dd77e4896/tenor.gif?itemid=9920978",
        "https://media1.tenor.com/images/6088a5ea989ddf19836f655b8555710a/tenor.gif?itemid=12159970",
        "https://media1.tenor.com/images/62048cf3073b2670e176c470aa1d2714/tenor.gif?itemid=12668675",
        "https://media1.tenor.com/images/75a607663feb91c59bb4a84ab803fba6/tenor.gif?itemid=11144378",
        ]

    if message.content.startswith('lain hug'):
        msg = (message.content + "!! amazing hug:" + random.choice(huggo))
        await client.send_message(message.channel, msg)

    slappu=[
        "https://i.imgur.com/jNaAaxn.gif",
        "https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720",
        "https://media1.tenor.com/images/fb17a25b86d80e55ceb5153f08e79385/tenor.gif?itemid=7919028",
        "https://media.giphy.com/media/VEmm8ngZxwJ9K/giphy.gif",
        "https://i.imgur.com/VW0cOyL.gif",
        "https://i.imgur.com/4MQkDKm.gif",
        "https://pa1.narvii.com/6807/ac91cef2e5ae98f598665193f37bba223301d75c_hq.gif",
        "https://media.giphy.com/media/iUgoB9zOO0QkU/giphy.gif",
        "https://media.giphy.com/media/10Am8idu3qBYRy/giphy.gif",
        "https://i.imgur.com/Agwwaj6.gif",
        "https://media.giphy.com/media/zRlGxKCCkatIQ/giphy.gif",
        "https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif",
        "https://i.imgur.com/kSLODXO.gif",
        "https://i.imgur.com/fm49srQ.gif"
        "https://i.imgur.com/o2SJYUS.gif",
        "https://i.imgur.com/oOCq3Bt.gif",
        "https://i.imgur.com/YA7g7h7.gif",
        "https://i.imgur.com/mIg8erJ.gif",
        "https://i.imgur.com/CwbYjBX.gif",
        
        ]

    pattu=[
        "https://i.imgur.com/2lacG7l.gif",
        "https://i.imgur.com/UWbKpx8.gif",
        "https://i.imgur.com/4ssddEQ.gif",
        "https://i.imgur.com/2k0MFIr.gif",
        "https://i.imgur.com/LUypjw3.gif",
        "https://i.imgur.com/F3cjr3n.gif",
        "https://i.imgur.com/sLwoifL.gif",
        "https://i.imgur.com/0znUWqT.gif",
        "https://i.imgur.com/TPqMPka.gif",
        "https://i.imgur.com/fp9XJZO.gif",
        "https://media.tenor.com/images/098689061fc2b850aa29fd4410fa97e7/tenor.gif",
        "https://thumbs.gfycat.com/ImpurePleasantArthropods-small.gif",
        "https://media0.giphy.com/media/BxdqaKAfdcCsg/giphy.gif",
        "https://media.tenor.com/images/e549c61c9bc3d8defdb0559b358b92a7/tenor.gif",
        "https://i.gifer.com/7MPC.gif",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR_B2M0Yc9qyqXjKrqLRAJngXEpM1XUxb9lYeOr9eJdndts0tB",
        

        ]

    if message.content.startswith('lain slap'):
        msg = (message.content + ", hope that stings..:" + random.choice(slappu))
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain pat'):
        msg = (message.content + "!!! uwu...:" + random.choice(pattu))
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain quote'):
        messages = [
            "People only have substance within the memories of other people. And that's why there were all kinds of me's. There weren't a lot of me's per se, I was just inside all sorts of people, that's all. -Lain",
            "No matter where you go, everyone's connected, -Lain",
            "There was no reason for me to stay in the real world any longer. In the real world, it didn't matter if I was there or not. When I realized that, I was no longer afraid of losing my body. -Chisa Yomoda",
            "God is here. -Chisa Yomoda",
            "The body exists only to verify one's own existence. - Mrs. Iwakura",
            "OK, let's see... I guess that I'm confused again. Am I here, or am I there? I don't know. Over there, I'm everywhere. I know that. But here is connected to over there. Is that right? But then, where is the real me after all is said and done. Oh! There is no real me. I guess that's it. I only exist inside those people aware of my existence. But what about this me that I can hear talking right here and now? It's me, isn't it? -Lain Iwakura",
            "If you're not remembered, then you never existed. - Arisu Mizuki",
            "History is not merely a linear collection of points that we pass through on a timeline. They are connected by a line. No, perhaps it is more accurate to say that they are made to connect.",
            "The truth has power because it's the truth. And because it is the truth, that makes it just. It's persuasive, isn't it? Don't you want truth like that? - Taro",
            "What isn't remembered never happened. - Lain Iwakura",
            "Present Day. Present Time.",
            "lmao ur gay 4 liking anime - society",
        ]
        msg = random.choice(messages)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('lain site'):
        urls = [
            "https://fauux.neocities.org/",
            "https://systemspace.link/warning.php",
            "https://mebious.neocities.org/Layer/Wierd.html",
            "https://arisuchan.jp/",
            "https://asphyxia.su/",
            "http://www.cjas.org/~leng/lain.htm",
            "http://lain.angelic-trust.net/wired.html",
            "http://www.geocities.jp/zatugakubeya/lain/index.html",
            "https://blackwings.neocities.org/",
            "http://sel.wikia.com/wiki/Serial_Experiments_Lain_Wiki",
            "https://systemspace.network/",
            "http://navi.solutions/",
            "https://arisuchan.jp/cyb/res/1210.html",
            
        ]
        msg = random.choice(urls)
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain goose"):
        geese = [
            "https://d1ia71hq4oe7pn.cloudfront.net/photo/59950681-720px.jpg",
            "https://png.pngtree.com/element_origin_min_pic/16/10/27/a5dfdc24f753f5500a4dfe432f4b24e5.jpg",
            "https://api.culture.pl/sites/default/files/styles/1920_auto/public/images/imported/KUCHNIA/GESINA/full_gesina_forum_770.jpg?itok=o5V8Ncz7",
            "https://d1ia71hq4oe7pn.cloudfront.net/photo/59940721-480px.jpg",
            "https://download.ams.birds.cornell.edu/api/v1/asset/59953191/1800",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Canada_goose_flight_cropped_and_NR.jpg/1200px-Canada_goose_flight_cropped_and_NR.jpg",
            "https://thenypost.files.wordpress.com/2017/05/shutterstock_633482957.jpg?quality=90&strip=all&w=618&h=410&crop=1",
            "https://st.depositphotos.com/2752123/4495/i/950/depositphotos_44954913-stock-photo-wild-goose-with-puppy-gooses.jpg",
            "https://nature.mdc.mo.gov/sites/default/files/styles/centered_full/public/media/images/2013/10/canada-goose_swimming_10-30-13.jpg?itok=1uPvCy4_",
            "http://media.advance.net/newyorkupstatecom_national_desk_blog/photo/2018/09/12/captain-jason-big-jay-barnes-of-frontenac-fowlers-guide-service-sets-up-for-a-canada-goose-hunt-bfe8525bbaf0895a.jpg",
            "https://www.aflac.com/_global-assets/images/mockup-images-do-not-use-for-final/new-final-images/product-cost-ducks/2015-03-12-cost-of-policy-milk-duck-300x300.png",
            "http://media.pixcove.com/B/5/5/Goose-Gosling-Geese-White-Free-Image-Bird-Swimming-9381.jpg",
            "https://www.eastcountyzoo.com/images/goose%20gosling%20african%20(4).jpg",
            "http://i.imgur.com/Nyv6k1S.jpg",
            "https://i.dailymail.co.uk/i/pix/2010/05/22/article-1280370-09B0E58D000005DC-919_964x577.jpg",
            "http://housegoose.com/menagerie/photos/birds/cowboygosling.jpg",
            "https://media-cdn.tripadvisor.com/media/photo-s/0b/11/97/6d/canada-goose-and-gosling.jpg",
            "https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/file/1/1734662/1407919967/image/525269601.jpg",
            "https://d1ia71hq4oe7pn.cloudfront.net/photo/59950701-480px.jpg",
            "https://s3-us-west-2.amazonaws.com/hobbyfarms.com/wp-content/uploads/2017/12/29195949/geese-ducks-resolutions.jpg",
            "https://media.mnn.com/assets/images/2018/04/canada_geese_chicks.jpg.838x0_q80.jpg",
            "https://i2.wp.com/www.wildlifehotline.com/wp-content/uploads/2011/10/lilducks.jpg",
            "https://insider.si.edu/wp-content/uploads/2018/05/Canada_Geese_in_pond.jpg",
            "https://kywildliferemovalpros.com/wp-content/uploads/2018/03/goose.jpg",
            "https://d1ia71hq4oe7pn.cloudfront.net/photo/59938311-480px.jpg",
            
        ]
        msg = random.choice(geese)
        await client.send_message(message.channel, msg)


    if message.content.startswith('lain meme'):
        urls = [
            "https://i.kym-cdn.com/photos/images/original/001/130/384/ff7.jpg",
            "https://i.kym-cdn.com/photos/images/original/001/043/266/9bf.jpg",
            "https://img.memecdn.com/eat-up-and-become-a-good-nerd-serial-experiments-lain_o_6681023.jpg",
            "https://pics.me.me/hey-mom-and-dad-i-dont-need-to-goto-i-30039967.png",
            "https://pics.awwmemes.com/aprantozaho-serial-experiment-lain-yuri-on-ice-kill-la-kill-21843017.png",
            "https://i.imgur.com/x8Ep0j5.jpg",
            "https://img.memecdn.com/why-the-heck-would-you-wear-something-like-that-indoors-serial-experiments-lain_o_7178838.jpg",
            "https://cdn.discordapp.com/attachments/528841759879331872/535565438663524352/Linux_708676_4900166.jpg",
            "https://2static.fjcdn.com/pictures/And+you+dont+seem+to+understand+lain+is+for+hugs_f5d3f0_5980863.jpg",
            "https://i.chzbgr.com/full/2490778880/h50C02810/",
            "https://ci.memecdn.com/9579043.jpg",
            "https://i.ytimg.com/vi/ysDc35yXqQk/maxresdefault.jpg",
            "https://img.fireden.net/a/image/1466/73/1466736357302.png",
            "https://i.pinimg.com/originals/54/ab/8a/54ab8adb4d5312534f54b976263245b0.jpg",
            "https://img.memecdn.com/inglorious-bastards-serial-experiments-lain_o_1676629.jpg",
            "https://i.kym-cdn.com/photos/images/original/001/104/212/326.jpg",
            "https://img.memecdn.com/hell-yeah-high-tech-cubic-monitors-serial-experiments-lain_o_6673309.jpg",
            "https://img.fireden.net/a/image/1523/99/1523995070828.jpg",
            "https://cdn.discordapp.com/attachments/528841759879331872/535569708502482954/image_search_1547760155063.jpg",
        ]
        msg = random.choice(urls)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('lain gif'):
        urls = [
            "https://cdn.4archive.org/img/6a6KxdZ.gif",
            "https://img.fireden.net/v/image/1454/27/1454275799295.gif",
            "https://media1.tenor.com/images/8d397680ad0f8fce375ac7c7bd8b4fad/tenor.gif?itemid=11598206",
            "https://i.kym-cdn.com/photos/images/original/001/130/238/951.gif",
            "https://arisuchan.jp/cult/src/1504745451093.gif",
            "https://arisuchan.jp/cult/src/1504745451093.gif",
            "https://66.media.tumblr.com/6e9d6b5af133b1b3884491d7f1f82983/tumblr_oog4yzg5u01vlb6q0o1_540.gif",
            "https://pa1.narvii.com/6318/77ba9762f081a004831cbdbc2fc2c11cc4a3a602_hq.gif",
            "https://desu-usergeneratedcontent.xyz/mu/image/1525/23/1525239710532.gif",
            "http://25.media.tumblr.com/tumblr_m2hpn4XlZQ1r73plvo1_500.gif",
            "http://marrowproductions.com/Twisted/wiki/images/4/42/LainTwist.gif",
            "https://i.gifer.com/8LV3.gif",
            "http://33.media.tumblr.com/931f551c7c5cd9a0e6a0a558775d81f6/tumblr_mytlj0llZV1rzn9vfo1_250.gif",
            "https://67.media.tumblr.com/5f8ca77f56da64b33145879cfcf73675/tumblr_nt2o8qQQS21tes8zmo1_500.gif",
            "http://cs.gettysburg.edu/~duncjo01/archive/patterns/lain/1st_day.gif",
            "https://img.fireden.net/a/image/1532/92/1532920863393.gif",
            "https://i.4pcdn.org/tg/1516038669389.gif",
            "https://66.media.tumblr.com/d4b2745356f425ddbd4e7de8975ecad7/tumblr_phon3a66b51w67s65o1_400.gif",
            "https://media.giphy.com/media/112CeAWuyhQX1C/giphy.gif",
            "https://i.imgur.com/6UxYXDJ.gif",
            "https://i.gifer.com/C2pQ.gif",
            "https://i.makeagif.com/media/10-10-2015/a4Whsh.gif",
            "https://media.giphy.com/media/h7J6rblcKKPDi/giphy.gif",
            "https://orig00.deviantart.net/868b/f/2018/226/4/a/lain_gif_remaster_final_by_deznak-dck4l98.gif",
            "https://media.giphy.com/media/5vAuoSpIK7uh2/source.gif",
            "https://gifimage.net/wp-content/uploads/2017/08/serial-experiments-lain-gif-21.gif",
            "https://img.fireden.net/a/image/1457/15/1457158385482.gif",
            "https://i.4pcdn.org/s4s/1532546585395.gif",
            "https://i.4pcdn.org/pol/1445669927592.gif",
            "https://img.fireden.net/v/image/1450/34/1450340196726.gif",
            "https://i.gifer.com/VvKY.gif",
            "http://38.media.tumblr.com/931f551c7c5cd9a0e6a0a558775d81f6/tumblr_mytlj0llZV1rzn9vfo1_500.gif",
            "https://media.giphy.com/media/cz1fqXcuMymgo/giphy.gif",
            "https://thumbs.gfycat.com/KindheartedIdleHoneycreeper-max-1mb.gif",
            "https://data.whicdn.com/images/243034617/original.gif",
            "https://steamusercontent-a.akamaihd.net/ugc/859477345548989008/23073CCB3B1FE199008FB2A2F1CC7A4328A3F958/",
            "https://i.imgur.com/eqkzFu0.gif",
            "https://media1.tenor.com/images/83eeeeeb64813c10236111e63f2080a8/tenor.gif?itemid=11578021",
            "https://afinde-production.s3.amazonaws.com/uploads/2eee0567-1b6d-4553-bebc-358003433f17.gif",
            "https://i.imgur.com/V4vSSo2.gif",
            "http://78.media.tumblr.com/4c9d850a8e5ac7ade46e286142f878f7/tumblr_nw2adbFCyf1uorwlqo1_400.gif",
            "https://78.media.tumblr.com/bd9272f9b0568794c7dad8ec52c01346/tumblr_n92s34HGM31qjlwa8o1_r1_500.gif",
            "http://i.4cdn.org/c/1547054999646.gif",
            "https://bakanoweeby.files.wordpress.com/2017/10/lain-2.gif?w=739",
            "https://steamusercontent-a.akamaihd.net/ugc/882000754018213605/C5280F51D7FEF548A21B7FDE639F8E949E9052FF/",
            "https://cdn.discordapp.com/attachments/528841759879331872/536465067508498432/we_be_walking.gif",
            "https://imgur.com/oSNisPS",
            "https://steamusercontent-a.akamaihd.net/ugc/110732351534804953/6170F4AC4C6080A353792551E2D9F7E61719713D/",
        ]
        msg = random.choice(urls)
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain image'):
        urls = [
            "http://www.otakuusamagazine.com/wp-content/uploads/2018/09/lain00.jpg",
            "https://outtherecinema.files.wordpress.com/2015/10/evil-lain.png",
            "https://i.imgur.com/qtvrFXI.jpg",
            "https://steamusercontent-a.akamaihd.net/ugc/956347227393432230/4A37EBA7255E13D36505913E07D8BDCF94D6716D/",
            "http://images6.fanpop.com/image/photos/37500000/Lain-Iwakura-Serial-Experiments-Lain-comic-freak-37540192-411-500.jpg",
            "http://brendysbookreport.com/wp-content/uploads/2018/06/a1.jpg",
            "https://i.ytimg.com/vi/NXSCGbSXwJQ/maxresdefault.jpg",
            "http://images6.fanpop.com/image/photos/38500000/Lain-Iwakura-Serial-Experiments-Lain-godofthewired-38580735-387-750.png",
            "https://66.media.tumblr.com/c1b40c07a197eaf747cf06fb3d7fbc78/tumblr_ove6fgVhnV1s73tqio1_400.jpg",
            "https://steemitimages.com/640x0/https://i.hizliresim.com/1J37ZA.jpg",
            "https://images-na.ssl-images-amazon.com/images/I/91x56KjbejL.jpg",
            "http://images6.fanpop.com/image/photos/39700000/Lain-Iwakura-SEL-rainbow-unicorn-39798201-1109-1281.jpg",
            "https://farm9.staticflickr.com/8323/8095518526_00a4243a4c_b.jpg",
            "https://img.fireden.net/a/image/1519/45/1519455054036.png",
            "https://lastfm-img2.akamaized.net/i/u/300x300/9d9f294f757a4ab782ca09078ee5ee1c.jpg",
            "https://img.fireden.net/a/image/1507/05/1507050296146.png",
            "https://orig00.deviantart.net/041f/f/2016/273/d/b/lain_by_bronickelodeon-dajgd65.png",
            "https://i.4pcdn.org/x/1494090508726.jpg",
            "https://i.warosu.org/data/vr/img/0051/33/1540878608890.png",
            "https://i.pinimg.com/originals/51/1c/f4/511cf45997bd698e4f30bfffd7c40bf3.jpg",
            "http://i.imgur.com/0fuI3bH.jpg",
            "http://images6.fanpop.com/image/photos/38200000/Lain-Iwakura-Serial-Experiments-Lain-kittyluv57-38269174-423-650.jpg",
            "https://myswordisunbelievablydull.files.wordpress.com/2011/07/coalgirls_serial_experiments_lain_01_1008x720_blu-ray_flac_f0ef8af8-mkv_snapshot_16-02_2011-07-18_14-56-28.jpg",
            "https://media1.tenor.com/images/93a28fa974e6e002f15fd5245a1079b7/tenor.gif?itemid=11578020",
            "https://vignette.wikia.nocookie.net/sel/images/e/e4/Touko%27s_NAVI_Screen.png/revision/latest?cb=20100515114244",
            "https://static.zerochan.net/Iwakura.Lain.full.613356.jpg",
            "https://i.ytimg.com/vi/TkXzOlytPME/0.jpg",
            "https://thumbs.worthpoint.com/wpimages/images/images1/1/0917/23/1_867ebf074e5ad5d8180f0ba2f0c6f6f4.jpg",
            "https://pbs.twimg.com/media/Dv_13_XWwAEZaEK.jpg",
            "https://pbs.twimg.com/media/DwK2TIkXcAAs6FJ.jpg",
            "https://pbs.twimg.com/media/DwKHX6QUYAEakTP.jpg",
            "https://pbs.twimg.com/media/DwJx4LNVYAAbdBj.jpg",
            "https://pbs.twimg.com/media/DwDnk1PUUAAGqER.jpg",
            "https://pbs.twimg.com/media/DwCLtWcWoAAy4jZ.jpg",
            "https://pbs.twimg.com/media/DwAm6JdW0AI-3Iz.jpg",
            "https://pbs.twimg.com/media/DwAmVyMX0AATe1e.jpg",
            "https://pbs.twimg.com/media/Dv_26MuW0AApOMD.jpg",
            "https://pbs.twimg.com/media/Dv_y_rkWsAAdCGs.jpg",
            "https://static.zerochan.net/Iwakura.Lain.full.891812.jpg",
            "https://i.pinimg.com/originals/ad/c5/33/adc533dcf3063c1e21702d8f1eb91284.jpg",
            "https://deninet.com/sites/default/files/images/lain-listening-lg.jpg",
            "https://cdnb.artstation.com/p/assets/images/images/005/789/449/large/chrotion-art-lain-iwakura-cosplay-of-neo.jpg?1493786291",
            "https://78.media.tumblr.com/eb2c63ac7fb01217539db4f23d676fef/tumblr_osfo1cMJbB1uah3u8o1_1280.png",
            "https://static.zerochan.net/Iwakura.Lain.full.769784.jpg",
            "https://66.media.tumblr.com/cd549a28872f42b52b429bd46f06b9d4/tumblr_o4ezevquAW1s73tqio1_400.jpg",
            "https://www.anbient.com/files/img/serial-experiments-lain/ss-8446.jpg",
            "http://i.imgur.com/91eok.jpg",
            "http://images6.fanpop.com/image/photos/37100000/Lain-Iwakura-Serial-Experiments-Lain-psychological-anime-manga-37187691-1520-1080.jpg",
            "https://data.whicdn.com/images/7353896/original.jpg",
            "https://img.fireden.net/a/image/1459/25/1459259158262.jpg",
            "https://66.media.tumblr.com/314c1df33c2833397e784288b6a4a280/tumblr_inline_p1ayzt11J21t07u0c_500.png",
            "https://i.pinimg.com/originals/c0/cc/50/c0cc50a78e28b697ec3a66846fcaf520.jpg",
            "https://i.pinimg.com/236x/20/66/9b/20669b285f70c4dba3b76118d0184bff--serial-experiments-lain-manga-anime.jpg",
            "https://images.8tracks.com/cover/i/010/115/151/lain-4378.png?rect=0,0,904,904&q=98&fm=jpg&fit=max",
            "https://pm1.narvii.com/6505/062a5a2d35200c8fa9916293025f484a6f3c57a4_hq.jpg",
            "https://vignette.wikia.nocookie.net/inciclopedia/images/1/16/Lain_oso.jpg/revision/latest?cb=20111226044923",
            "https://static.zerochan.net/Iwakura.Lain.full.1207948.jpg",
            "https://myswordisunbelievablydull.files.wordpress.com/2011/07/coalgirls_serial_experiments_lain_03_1008x720_blu-ray_flac_92704257-mkv_snapshot_17-56_2011-07-19_19-09-07.jpg",
            "https://c2.staticflickr.com/4/3539/3536914421_7247bdcd4f_z.jpg?zz=1",
            "http://fixitinpost.org/wp-content/uploads/2013/03/Serial-Experiments-Lain-Restore-04.jpg",
            "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Lain_hacker_small.jpg/250px-Lain_hacker_small.jpg",
            "http://image.itmedia.co.jp/nl/articles/1807/21/s180721_lain-20th_1.jpg",
            "https://img.fireden.net/a/image/1514/73/1514734810033.jpg",
            "https://i.pinimg.com/originals/0c/d8/1d/0cd81d2f357f91244ec87a1d6466107e.jpg",
            "https://i.ytimg.com/vi/tffVlvSQOjA/maxresdefault.jpg",
            "https://memestatic.fjcdn.com/large/pictures/39/82/398288_6490166.jpg",
            "https://i.pinimg.com/originals/68/65/b1/6865b15ca585c3d8f4901d5475c0a342.png",
            "https://pbs.twimg.com/media/Dx_D21qV4AAmkYT.jpg:large",
            "https://arisuchan.jp/%CE%BB/src/1529427554416.png",
            "https://img.fireden.net/v/image/1499/92/1499927137904.png",
            "https://i.redd.it/n5r8cum1mb911.jpg",
            "https://stmed.net/sites/default/files/serial-experiments-lain-wallpapers-26100-9616498.jpg",
            "https://beneaththetangles.files.wordpress.com/2010/11/lain2.jpg?w=900",
            "https://static.zerochan.net/Iwakura.Lain.full.79038.jpg",
            "https://mywaifulist.s3-us-west-1.amazonaws.com/series/70/70.jpg",
            "https://i.pinimg.com/236x/75/39/b0/7539b0418e5c187f75eefd1413cc321a--serial-experiments-lain-manga.jpg",
            "https://i.warosu.org/data/g/img/0595/15/1490129629325.jpg",
            "https://lh3.googleusercontent.com/-bofEp1dLNgw/Wfkjm0C87wI/AAAAAAAAAko/nrPFiK35NIc_xeluS83WT-U4F78xhhshgCJoC/w1280-h1829/457f84e6-cadc-49b5-98e2-4f32705f11fd.png",
            "https://img.fireden.net/a/image/1454/55/1454557826541.png",
            "https://i.imgur.com/GF7NC4i.jpg",
            "https://scontent-atl3-1.cdninstagram.com/vp/61a380b854e01d4b1bb5a6b816beeb15/5C9B9A1B/t51.2885-15/e35/29093379_385671531907205_2690296831937609728_n.jpg",
            "http://www.japanator.com/ul/29201-1374749821411.jpg",
            "https://img.fireden.net/a/image/1512/47/1512478457044.jpg",
            "https://c1.staticflickr.com/5/4071/4546116303_b8fcd3ff6e_b.jpg",
            "http://images6.fanpop.com/image/photos/38500000/Lain-Iwakura-Serial-Experiments-Lain-godofthewired-38580739-347-674.jpg",
            "https://i.pinimg.com/236x/03/1e/ac/031eac39a45e13081bb1df7b4de36712--serial-experiments-lain.jpg",
            "https://i.pinimg.com/236x/d7/cc/4f/d7cc4fab8e62a1c247aed7ff92e5500e--serial-experiments-lain-fabric-walls.jpg",
            "https://i.pinimg.com/originals/2d/bb/cf/2dbbcfb33c21fb240f1715cea11e1f11.jpg",
            "https://i.pinimg.com/originals/a5/ec/31/a5ec310608f5bf394631a04c03aa7cd7.jpg",
            "https://66.media.tumblr.com/ca94da5c9812e27674bc394c78cf3f92/tumblr_otlbqrT4uq1wqfs22o1_1280.png",
            "https://data.whicdn.com/images/308862999/large.jpg",
            "https://i.imgur.com/aOUg9o3.png",
            "https://66.media.tumblr.com/68b4d09e30d6eddbde8bc4b85e4e32a1/tumblr_oqv31798n71wqfs22o1_1280.png",
            "https://66.media.tumblr.com/68b4d09e30d6eddbde8bc4b85e4e32a1/tumblr_oqv31798n71wqfs22o1_1280.png",
            "http://41.media.tumblr.com/58ab8b9e534390ab996d0fa15ce0cede/tumblr_notf143Nit1qftmhbo1_500.png",
            "https://wallup.net/wp-content/uploads/2016/05/14/52934-Serial_Experiments_Lain-Lain_Iwakura-748x421.png",
            "https://i.imgur.com/eN7vUz3.png",
            "https://66.media.tumblr.com/c06286f1360f2550f86217ca4df6ada3/tumblr_oo80im8XKk1vtgpj4o1_400.jpg",
            "https://66.media.tumblr.com/0108cf7e72a70a4adc811a17310a1bef/tumblr_oocj3txIpg1rjtw15o4_250.png",
            "https://ih0.redbubble.net/image.628018512.8727/flat,550x550,075,f.u5.jpg",
            "https://images.8tracks.com/cover/i/002/863/598/434e8e4c1145-7107.jpg?rect=0,0,500,500&q=98&fm=jpg&fit=max",
            "https://scontent-sea1-1.cdninstagram.com/vp/c522fb17c6ed140811ec8b712968ce84/5CC7B08F/t51.2885-15/e35/c119.0.481.481/s480x480/28158331_1090161284476580_3726883881702391808_n.jpg?_nc_ht=scontent-sea1-1.cdninstagram.com",
            "https://66.media.tumblr.com/adbf256d62e42e490d5f3d9707ad69dc/tumblr_p6e3zpsOx61x9jrg4o1_500.png",
            "https://danbooru.donmai.us/data/__iwakura_lain_serial_experiments_lain_drawn_by_unprince__d4882ae18c908049ac4e79b3949fa21c.png",
            "https://i.pinimg.com/736x/24/fa/72/24fa72f6573024a94dd43f9f20103892--serial-experiments-lain-white-dress.jpg",
            "https://i.pinimg.com/236x/2e/91/23/2e91237c18ad9822302fc4215a1b4881--serial-experiments-lain-games.jpg",
            "https://i.pinimg.com/originals/92/b7/e0/92b7e038375453b4e541b126b380bb5c.png",
            "https://i.pinimg.com/originals/9e/b9/5c/9eb95c6f4d92335055e26e502ab5192f.jpg",
            "https://i.pinimg.com/736x/6a/b2/c0/6ab2c0ed376d2a1cc88def88bfe8375c.jpg",
            "https://i.pinimg.com/236x/04/79/c8/0479c8427d6b6a50ccefd8fb7c7fd172.jpg",
            "https://i.pinimg.com/originals/f6/fc/26/f6fc26e56f252d66197dd8f151c76a80.jpg",
            "http://dementedrabbits.net/images/medialogs/lain/lain02.jpg",
            "https://i.pinimg.com/736x/6f/c0/2d/6fc02daa9e3ce0c72e7e58a4248671d0--serial-experiments-lain-anime-pictures.jpg",
            "https://i.paigeeworld.com/user-media/1529452800000/511845483bfdeefd1601e157_5b2a1b5eb2bf487d10118e2e_320.jpg",
            "https://raikou2.donmai.us/7f/2d/7f2d8cc8fc14b08373089a95c0a3182d.jpg",
            "https://i.pinimg.com/236x/b9/4b/5b/b94b5be929c8a46ef6fd91f609620b09--weheartit-logs.jpg",
            "https://i.kym-cdn.com/photos/images/original/001/103/057/2c4.jpg",
            "https://2static.fjcdn.com/pictures/The+truth+about+serial+experiments+lain+subhuman+_6c62fe_5911108.jpg",
            "https://imgur.com/L1N70Un",
            "https://66.media.tumblr.com/8a3c407cfb3dfb50fe7255b776a4389d/tumblr_pcn60d1Rh91wjje03o4_r1_500.png",
            "https://i.ytimg.com/vi/qVMK5WnJ-C0/hqdefault.jpg",
            "https://i.pinimg.com/originals/66/92/03/669203fb477f7dd466c25cbecae7d012.jpg",
            "https://img2.goodfon.com/wallpaper/nbig/4/6c/art-serial-experiments-lain-6375.jpg",
            "https://pm1.narvii.com/6194/ee5c2618687bbd1edd1afdc54f4e55309b7b80c6_hq.jpg",
            "https://i.pinimg.com/236x/03/1e/ac/031eac39a45e13081bb1df7b4de36712--serial-experiments-lain.jpg?b=t",
            "https://c.wallhere.com/photos/15/46/Serial_Experiments_Lain_Lain_Iwakura_anime_girls_anime-229867.jpg!d",
            "http://images6.fanpop.com/image/photos/38500000/Lain-Iwakura-Serial-Experiments-Lain-godofthewired-38580737-500-582.jpg",
            "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/1274b4e5-aa00-45ca-a9db-6a90e7073a8c/d4n5m20-06936f97-032d-47f0-a163-d6532648f410.jpg/v1/fill/w_375,h_250,q_70,strp/lain_by_justv23_d4n5m20-250t.jpg",
            "https://i.pinimg.com/originals/78/d3/42/78d34226d2d5bf48a7b71d242b4e9270.jpg",
            "https://a.disquscdn.com/get?url=http%3A%2F%2Fs1.zerochan.net%2FIwakura.Lain.600.687994.jpg&key=5edZc1IqRe3Z2seRn4Cziw",
            "https://cs4.pikabu.ru/post_img/2016/05/14/9/1463234747199568052.jpg",
            "https://arisuchan.jp/art/src/1525183091131.jpg",
            "https://66.media.tumblr.com/f99a00f6c91e0721d84582cc0d60a0b2/tumblr_oocj3txIpg1rjtw15o1_500.png",
            "https://66.media.tumblr.com/bb66b48fdf6a9a41a3aa753c806d4c80/tumblr_pch9cciYKQ1v41zjoo1_400.jpg",
            "http://darkcloudstudio.com/austinifiedanime/wp-content/uploads/2009/11/LAIN26-300x231.jpg",
            "https://s3.amazonaws.com/cult-of-distraction/media/articles/images/lain-13.png",
            "https://img.fireden.net/a/image/1446/25/1446250794874.jpg",
            "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/b841d1a8-36d6-4d82-bb7c-31162693fafa/dck64zn-11a8092a-7ee5-416c-8398-f5a2f0d15697.png/v1/fill/w_800,h_1253,q_80,strp/lain_iwakura_by_peppermint_tea39_dck64zn-fullview.jpg",
            "https://cs8.pikabu.ru/post_img/big/2017/05/13/10/149469356816223570.jpg",
            "https://66.media.tumblr.com/d97d01c05943ec198d2724c33e0ca0de/tumblr_inline_p344h9u8Jy1t07u0c_1280.jpg",
            "http://www.animetion.co.uk/Lain/side7.jpg",
            "http://i.imgur.com/4oqKWcM.jpg",
            "https://zerojustice315.files.wordpress.com/2015/04/coalgirls_serial_experiments_lain_03_1008x720_blu-ray_flac_92704257-mkv_snapshot_16-51_2015-04-06_20-05-28.jpg",
            "https://66.media.tumblr.com/2792fea59564b6a670549322cc5a8e24/tumblr_p73s6vg9ZA1x9jrg4o2_500.png",
            "http://33.media.tumblr.com/f3307a1bb2de561902c3f4aa94819b90/tumblr_nttc6uSVuq1u4zgnro1_400.gif",
            "https://www.downloadwallpapers.info/dl/1280x960//2016/02/21/21974_blood-girl-iwakura-lain-serial-experiments-lain-wall_1280x1024_h.jpg",
            "https://cs7.pikabu.ru/post_img/2018/08/16/6/1534407361174380135.jpg",
            "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/e27f75f2-699b-4e21-806d-83a83389356e/d7g8oyb-5ab8ac4e-783b-4883-a264-052c7c9ecbea.png/v1/fill/w_471,h_350,q_70,strp/iwakura_lain___final_by_hackatt_d7g8oyb-350t.jpg",
            "https://scontent-amt2-1.cdninstagram.com/vp/3aaab5cdf84dcba75ea9546789340e52/5CD0568C/t51.2885-15/sh0.08/e35/s640x640/42068850_620156955045839_471048183435590991_n.jpg?_nc_ht=scontent-amt2-1.cdninstagram.com",
            "http://static.minitokyo.net/downloads/15/43/334665.jpg",
            "http://images6.fanpop.com/image/photos/38100000/Lain-Iwakura-Arisu-Mizuki-Juri-Kato-and-Reika-Yamamoto-Serial-Experiments-Lain-kittyluv57-38187394-600-450.jpg",
            "https://static.zerochan.net/Iwakura.Lain.full.485427.jpg",
            "https://data.whicdn.com/images/252355722/large.jpg",
            "https://cs4.pikabu.ru/post_img/2016/06/17/7/1466160572148393809.jpg",
            "https://cs4.pikabu.ru/post_img/2016/07/06/6/14677967391786776.jpg",
            "http://images6.fanpop.com/image/photos/38200000/Lain-Iwakura-Wallpaper-kittyluv57-38222200-1920-1080.jpg",
            "https://cs7.pikabu.ru/post_img/2019/01/12/1/1547250377171741873.png",
            "https://static.zerochan.net/Iwakura.Lain.full.132356.jpg",
            "http://static.minitokyo.net/downloads/42/29/193992.jpg",
            "https://www.wallpaperup.com/uploads/wallpapers/2014/03/15/298989/bf83071e887017b092582842dc759663-700.jpg",
            "https://www.vizzed.com/videogames/psx/screenshot/Serial%20Experiments%20Lain-2.jpg",
            "https://tacchi-canvas-prod.s3.amazonaws.com/uploads/work/image/5775/Serial_Experiments_Lain_by_dilara_ozden__Print_Designer_in_Tokyo.png",
            "https://i.redd.it/dpgtgivinto01.jpg",
            "http://animeonly.org/albums/VISINAUJI/Bishi/Volume-11-[S]/Serial_Experiment_Lain_14.jpg",
            "https://vignette.wikia.nocookie.net/malice-in-wonderland-and-all-things-alice/images/6/6c/Serial_experiments_lain_anime_desktop_wallpaper-normal.jpg/revision/latest?cb=20140214164314",
            "https://i.pinimg.com/736x/66/b0/7e/66b07e3adb28660dddd53358f4731ea2.jpg",
            "https://nefariousreviews.files.wordpress.com/2016/09/serial-experiments-lain-obsession.jpg",
            "https://i1.wp.com/beneaththetangles.com/wp-content/uploads/2018/10/serial-experiments-lain-episode-11h.png?zoom=2.625&resize=371%2C276&ssl=1https://i1.wp.com/beneaththetangles.com/wp-content/uploads/2018/10/serial-experiments-lain-episode-11h.png?zoom=2.625&resize=371%2C276&ssl=1",
            "http://potpourricomics.it/images/Autori/DeebleNF/Recensioni/Anime/Serial-Experiments-Lain/Lain-Disegni/Lain-1.jpg",
            "http://animerulezzz.org/FanArt/Serial%20Experiments%20Lain/1/Real/lain2.jpg",
            "https://lh3.googleusercontent.com/-jekIwAo4P6c/XCK2RNE1BVI/AAAAAAAC4YM/31rmK6lpVhwMcaYasI4kViiV8_cuALpmACJoC/w1392-h1560-n-rw/vatvyr.png",
            "https://dic.nicovideo.jp/oekaki/859218.png",
            "https://imgix.ranker.com/user_node_img/50082/1001629191/original/must-not-confuse-it-with-the-real-world-photo-u1?w=650&q=50&fm=jpg&fit=crop&crop=faces",
            "https://img.fireden.net/v/image/1518/07/1518074308001.jpg",
            "http://www.vector-ride.com/silly_moogle/TheBigO/Lain/lWatchDadSetNAVI.jpg",
            "http://rubberslug.s3.amazonaws.com/user/3/70f6c9ae3244334822e2fd614703412/ztambtxapy_o.jpg",
            "http://images6.fanpop.com/image/photos/37100000/Lain-Iwakura-Serial-Experiments-Lain-psychological-anime-manga-37187691-1520-1080.jpg",
            "https://static.zerochan.net/Iwakura.Lain.full.1394713.jpg",
            "https://imgur.com/a/fDkOZfP",
            "https://imgur.com/a/ML0y9jf",
            "https://imgur.com/a/S0aPnO9",
            "https://imgur.com/a/yPcmwaw",
            "https://imgur.com/a/WQrkc8G",
            "https://imgur.com/a/x8Lo4Xj",
            "https://imgur.com/a/cjUxAm3",
            "https://imgur.com/a/Tqn1d90",
            "https://imgur.com/a/L7gzXp6",
            "https://imgur.com/a/T1EsFz5",
            "https://imgur.com/a/zmKsRWX",
            "https://imgur.com/a/OKRwC4B",
            "https://imgur.com/a/3JLGzxc",
            "https://imgur.com/a/VT83R7p",
            "https://imgur.com/a/LXR4tti",
            "https://imgur.com/XZIe2uK",
            "https://imgur.com/DLpjpvs",
            "https://imgur.com/DDlDvHl",
            "https://imgur.com/vH2sy2N",
            "https://imgur.com/o1nHlMW",
            "https://imgur.com/bIIlmlR",
            "https://imgur.com/O03Xja2",
            "https://imgur.com/0NRev1a",
            "https://imgur.com/V86JYqi",
            "https://imgur.com/tsQz7ru",
            "https://imgur.com/jv8vtTU",
            "https://imgur.com/muBRskQ",
            "https://imgur.com/tXHy8uu",
            "https://imgur.com/FIwYIUQ",
            "https://imgur.com/FrmBadl",
            "https://imgur.com/pDtq7v0",
            "https://imgur.com/2CXVAix",
            "https://imgur.com/2lF0POS",
            "https://imgur.com/dYR2wMc",
            "https://imgur.com/AfnSUeK",
            "https://imgur.com/9IMvVjg",
            "https://imgur.com/tDfIoge",
            "https://imgur.com/UVc6OPm",
            "https://imgur.com/HKxVnxG",
            "https://imgur.com/h9ZOvcB",
            "https://imgur.com/J7hHxO1",
            "https://imgur.com/QRLgUYx",
            "https://imgur.com/U6XRtLW",
            "https://imgur.com/wZILJLP",
            "https://imgur.com/Eh33AVj",
            "https://imgur.com/061iIJk",
            "https://imgur.com/D09hKDb",
            "https://imgur.com/iJFZgLf",
            "https://imgur.com/TKUHvqm",
            "https://imgur.com/nJjE0Pm",
            "https://imgur.com/sxd3YPu",
            "https://imgur.com/1tf1TvT",
            "https://imgur.com/skHLZSZ",
            "https://imgur.com/hZKskr9",
            "https://imgur.com/LOXHumW",
            "https://imgur.com/8qfhk8e",
            "https://imgur.com/1a8upI7",
            "https://imgur.com/LE4YpeZ",
            "https://imgur.com/DECuVWQ",
            "https://imgur.com/pAtUbQD",
            "https://imgur.com/EDWuNq8",
            "https://imgur.com/pMFcMlO",
            "https://imgur.com/3zlHMq7",
            "https://imgur.com/AYQARfC",
            "https://imgur.com/d6CaKoz",
            "https://imgur.com/vUTd2zo",
            "https://imgur.com/QfvSxYs",
            "https://imgur.com/23XazJ4",
        ]
        msg = random.choice(urls)
        await client.send_message(message.channel, msg)





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
