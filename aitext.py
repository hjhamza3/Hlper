import asyncio
import random

import discord

# Define a global variable to track whether the initial message has been sent
initial_hug_message_sent = False

async def on_message(msg: discord.Message, bot):
    content = msg.content.lower()

    if content == "hello":
        # Mention the user who sent the message
        user_mention = msg.author.mention
        await msg.reply(f"Hi {user_mention}, How can I assist you?")

    elif content == "hi":
        # Mention the user who sent the message
        user_mention = msg.author.mention
        await msg.reply(f"Hello there {user_mention}! How can I help?")

    elif content == "how are you":
        # Mention the user who sent the message
        user_mention = msg.author.mention
        await msg.reply(f"I'm just a bot, but I'm functioning well. {user_mention}! How about you?")

    elif any(word in content for word in ["i am good", "i'm good", "i am fine", "i'm fine"]):
        # Mention the user who sent the message
        user_mention = msg.author.mention
        await msg.reply(f"That's great to hear, {user_mention}!")

    # ... (previous code)

    elif "hug" in content:
        # List of hug gif links (local to the function)
        hug_gifs = [
            "https://media.giphy.com/media/9d3LQ6TdV2Flo8ODTU/giphy.gif",
            "https://media.giphy.com/media/qFmdpUKAFZ6rMobzzu/giphy.gif",
            "https://media.giphy.com/media/1JmGiBtqTuehfYxuy9/giphy.gif",
            "https://media.giphy.com/media/QbkL9WuorOlgI/giphy.gif",
            "https://media.giphy.com/media/P3CZolxd8DeRy4g4fM/giphy.gif",
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_hug_gif = random.choice(hug_gifs)
        response = await msg.reply(f"{sender_user_mention}, This is H.U.G for you {mentioned_user_mention}\n{random_hug_gif}")

        # Delete the message after 1 minute
        await asyncio.sleep(160)
        await response.delete()


    elif "kiss" in content:
        # List of kiss gif links (local to the function)
        kiss_gifs = [
            "https://media.giphy.com/media/frHK797nhEUow/giphy.gif",
            "https://media.giphy.com/media/udiIFmPkJQzkI/giphy.gif",
            "https://media.giphy.com/media/108M7gCS1JSoO4/giphy.gif",
            "https://media.giphy.com/media/l2Jhok92mZ2PZHjDG/giphy.gif",
            "https://media.giphy.com/media/124gj4XvM8f3fa/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_kiss_gif = random.choice(kiss_gifs)
        response=await msg.reply(f"{sender_user_mention}, This is a K.I.S.S for you {mentioned_user_mention}\n{random_kiss_gif}")

        # Delete the message after 1 minute
        await asyncio.sleep(160)
        await response.delete()
      
    elif "love" in content:
        # List of love gif links (local to the function)
        love_gifs = [
            "https://media.giphy.com/media/9d3LQ6TdV2Flo8ODTU/giphy.gif",
            "https://media.giphy.com/media/DorxfW5xBGSG8bVxRa/giphy.gif",
            "https://media.giphy.com/media/R6gvnAxj2ISzJdbA63/giphy.gif",
            "https://media.giphy.com/media/1hqb8LwPS2xCNCpWH8/giphy.gif",
            "https://media.giphy.com/media/iJa6kOfJ3qN7a/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_love_gif = random.choice(love_gifs)
        response=await msg.reply(f"{sender_user_mention}, Sending L.O.V.E to you {mentioned_user_mention}\n{random_love_gif}")
        # Delete the message after 1 minute
        await asyncio.sleep(160)
        await response.delete()
    elif "sorry" in content:
        # List of sorry gif links (local to the function)
        sorry_gifs = [
            "https://media.giphy.com/media/FaySkD6cBUOiKI9x8d/giphy.gif",
            "https://media.giphy.com/media/v1Tg74V7tHdEpaiJ0t/giphy.gif",
            "https://media.giphy.com/media/0W0HfVitWo61RlVbyD/giphy.gif",
            "https://media.giphy.com/media/3o7WIwkSmw32NgXvTG/giphy.gif",
            "https://media.giphy.com/media/9JLOGsEfPjpR1179HE/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_sorry_gif = random.choice(sorry_gifs)
        response=await msg.reply(f"{sender_user_mention}, I'm S.O.R.R.Y {mentioned_user_mention}\n{random_sorry_gif}")
        await asyncio.sleep(160)
        await response.delete()
    elif "cry" in content:
        # List of cry gif links (local to the function)
        cry_gifs = [
            "https://media.giphy.com/media/3fmRTfVIKMRiM/giphy.gif",
            "https://media.giphy.com/media/lk6AqFz5KRWPQaAxbk/giphy.gif",
            "https://media.giphy.com/media/OPU6wzx8JrHna/giphy.gif",
            "https://media.giphy.com/media/AOitRwIgx2wcOxZaIH/giphy.gif",
            "https://media.giphy.com/media/M28rUlcjueKUE/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_cry_gif = random.choice(cry_gifs)
        response=await msg.reply(f"{sender_user_mention}, Don't C.R.Y {mentioned_user_mention}\n{random_cry_gif}")
        await asyncio.sleep(160)
        await response.delete()
      
    elif "slap" in content:
        # List of slap gif links (local to the function)
        slap_gifs = [
            "https://media.giphy.com/media/Ql5voX2wAVUYw/giphy.gif",
            "https://media.giphy.com/media/Ql5voX2wAVUYw/giphy.gif",
            "https://media.giphy.com/media/3XlEk2RxPS1m8/giphy.gif",
            "https://media.giphy.com/media/vxvNnIYFcYqEE/giphy.gif",
            "https://media.giphy.com/media/gSIz6gGLhguOY/giphy.gif"
        ]
     
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_slap_gif = random.choice(slap_gifs)
        response=await msg.reply(f"{sender_user_mention}, That's a S.L.A.P for you {mentioned_user_mention}\n{random_slap_gif}")
        await asyncio.sleep(160)
        await response.delete()
      
    elif "kick" in content:
        # List of kick gif links (local to the function)
        kick_gifs = [
            "https://media.giphy.com/media/LICtqQ1K8ClIQ/giphy.gif",
            "https://media.giphy.com/media/Ur7br2RDlMlZQzuwUK/giphy.gif",
            "https://media.giphy.com/media/PipD5GTXYySWhF3V4j/giphy.gif",
            "https://media.giphy.com/media/l1J3AS8RShMebsmgU/giphy.gif",
            "https://media.giphy.com/media/u2LJ0n4lx6jF6/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_kick_gif = random.choice(kick_gifs)
        response=await msg.reply(f"{sender_user_mention}, That's a K.I.C.K for you {mentioned_user_mention}\n{random_kick_gif}")
        await asyncio.sleep(160)
        await response.delete()
      
    elif "punch" in content:
        # List of punch gif links (local to the function)
        punch_gifs = [
            "https://media.giphy.com/media/Lx8lyPHGfdNjq/giphy.gif",
            "https://media.giphy.com/media/kDfhTQgCt2brMKKfQd/giphy.gif",
            "https://media.giphy.com/media/P4l2ET85UuedO/giphy.gif",
            "https://media.giphy.com/media/d31wMAc5PUktQGpq/giphy.gif",
            "https://media.giphy.com/media/3M5J7yedLPCSs/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_punch_gif = random.choice(punch_gifs)
        response=await msg.reply(f"{sender_user_mention}, That's a P.U.N.C.H for you {mentioned_user_mention}\n{random_punch_gif}")

        await asyncio.sleep(160)
        await response.delete()

    elif "miss" in content:
          # List of miss gif links (local to the function)
          miss_gifs = [
              "https://media.giphy.com/media/5XHHIFJZpQsXS/giphy.gif",
              "https://media.giphy.com/media/l4HoaTxnFw3RH1p7y/giphy.gif",
              "https://media.giphy.com/media/WkNXHaiV9HLji/giphy.gif",
              "https://media.giphy.com/media/4tihbnVvOLER2/giphy.gif",
              "https://media.giphy.com/media/3ohhwhPn1rDiXH2rKM/giphy.gif",
              "https://media.giphy.com/media/Na7ESPm76gDTi/giphy.gif",
              "https://media.giphy.com/media/BZEXyZSAaDjwc/giphy.gif",
              "https://media.giphy.com/media/cTQlVCRG9xdpS/giphy.gif",
              "https://media.giphy.com/media/o1UKv4TutEOUo/giphy.gif",
              "https://media.giphy.com/media/4QFnFdfUTSBj25SwIB/giphy.gif",
              "https://media.giphy.com/media/jnEx4oDu2QpggdEWLZ/giphy.gif",
             "https://media.giphy.com/media/6nPrkULa3jj3Ps2Qsa/giphy.gif",
             "https://media.giphy.com/media/jrZCq2cBgPHFshAbav/giphy.gif",
             "https://media.giphy.com/media/qL6UVZcHLorC7pEXkh/giphy.gif",
            "https://media.giphy.com/media/vgyeei729llBazJNH8/giphy.gif",
             "https://media.giphy.com/media/OFQADHsQz56MLJquvg/giphy.gif",
             "https://media.giphy.com/media/KB8MW1UcbHP7TWhKH1/giphy.gif"
          ]
          # Mention the user who sent the message
          sender_user_mention = msg.author.mention
          mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
          random_miss_gif = random.choice(miss_gifs)
          response=await msg.reply(f"{sender_user_mention}, I M.I.S.S you {mentioned_user_mention}\n{random_miss_gif}")
          await asyncio.sleep(160)
          await response.delete()
    elif "angry" in content:
          # List of angry gif links (local to the function)
          angry_gifs = [
              "https://media.giphy.com/media/l49K2rm0Hjg7PmbUA/giphy.gif",
              "https://media.giphy.com/media/cKseZ404p9W8ygnNb5/giphy.gif",
              "https://media.giphy.com/media/GjR6RPcURgiL6/giphy.gif",
              "https://media.giphy.com/media/ZebTmyvw85gnm/giphy.gif",
              "https://media.giphy.com/media/eb4WGfjWeIsgM/giphy.gif"
          ]
          # Mention the user who sent the message
          sender_user_mention = msg.author.mention
          mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
          random_angry_gif = random.choice(angry_gifs)
          response=await msg.reply(f"{sender_user_mention}, Why are you A.N.G.R.Y {mentioned_user_mention}?\n{random_angry_gif}")
          await asyncio.sleep(160)
          await response.delete()
    elif "fight" in content:
          # List of fight gif links (local to the function)
          fight_gifs = [
              "https://media.giphy.com/media/c4t11obaChpu0/giphy.gif",
              "https://media.giphy.com/media/opmkDIybAEaju/giphy.gif",
              "https://media.giphy.com/media/Fw2PnsOvTu67m/giphy.gif",
              "https://media.giphy.com/media/3ohc0QQkTH6YK8g4zS/giphy.gif",
              "https://media.giphy.com/media/9CHKSOuWsTRok/giphy.gif"
          ]
          # Mention the user who sent the message
          sender_user_mention = msg.author.mention
          mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
          random_fight_gif = random.choice(fight_gifs)
          response=await msg.reply(f"{sender_user_mention}, Let's not F.I.G.H.T {mentioned_user_mention}\n{random_fight_gif}")
          await asyncio.sleep(160)
          await response.delete()
    elif "hate" in content:
          # List of hate gif links (local to the function)
          hate_gifs = [
              "https://media.giphy.com/media/7r8AnoSSqQBry/giphy.gif",
              "https://media.giphy.com/media/rPjYoncYgknGo/giphy.gif",
              "https://media.giphy.com/media/l1J9u3TZfpmeDLkD6/giphy.gif",
              "https://media.giphy.com/media/y1WDIwAZRSmru/giphy.gif",
              "https://media.giphy.com/media/sUzZwE9AgI8iA/giphy.gif"
          ]
          # Mention the user who sent the message
          sender_user_mention = msg.author.mention
          mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
          random_hate_gif = random.choice(hate_gifs)
          response=await msg.reply(f"{sender_user_mention}, Why do you H.A.T.E {mentioned_user_mention}?\n{random_hate_gif}")
    # ... (previous code)
          await asyncio.sleep(160)
          await response.delete()
    elif "sleep" in content:
        # List of sleep gif links (local to the function)
        sleep_gifs = [
            "https://media.giphy.com/media/Jap1tdjahS0rm/giphy.gif",
            "https://media.giphy.com/media/U7Lvtcuqh4WZy/giphy.gif",
            "https://media.giphy.com/media/Ta0WKhJcZ7skPJ1JbP/giphy.gif",
            "https://media.giphy.com/media/1Eac0nSYA78gfytMqh/giphy.gif",
            "https://media.giphy.com/media/dxasUAntwMPfaAAFDu/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_sleep_gif = random.choice(sleep_gifs)
        response=await msg.reply(f"{sender_user_mention}, Time to S.L.E.E.P {mentioned_user_mention}\n{random_sleep_gif}")
        await asyncio.sleep(160)
        await response.delete()
    elif "cuddle" in content:
      # List of cuddle gif links (local to the function)
      cuddle_gifs = [
          "https://media.giphy.com/media/2hgilyq37RtPyaF0pA/giphy.gif",
          "https://media.giphy.com/media/bw1zKcUa8Dkje/giphy.gif",
          "https://media.giphy.com/media/nTeeb8thSiS0U/giphy.gif",
          "https://media.giphy.com/media/U7E464W1x7bOkXU7tV/giphy.gif",
          "https://media.giphy.com/media/400JDxiFmkWid2turD/giphy.gif"
      ]

      sender_user_mention = msg.author.mention
      mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
      random_cuddle_gif = random.choice(cuddle_gifs)
      response=await msg.reply(f"{sender_user_mention}, Let's C.u.d.d.l.e {mentioned_user_mention}\n{random_cuddle_gif}")
      await asyncio.sleep(160)
      await response.delete()
    elif "high five" in content:
      # List of high-five gif links (local to the function)
      high_five_gifs = [
        "https://media.giphy.com/media/3oEjHV0z8S7WM4MwnK/giphy.gif",
        "https://media.giphy.com/media/cLzt6YaesfXR2MvkBS/giphy.gif",
        "https://media.giphy.com/media/DGXujBZlxNC6eWG4tY/giphy.gif",
        "https://media.giphy.com/media/fm4WhPMzu9hRK/giphy.gif",
        "https://media.giphy.com/media/w9mHi4xjefrAwpDJAT/giphy.gif"
         ]
       # Mention the user who sent the message
      sender_user_mention = msg.author.mention
      mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
      random_high_five_gif = random.choice(high_five_gifs)
      response=await msg.reply(f"{sender_user_mention}, H.i.g.h-f.i.v.e {mentioned_user_mention}\n{random_high_five_gif}")
      await asyncio.sleep(160)
      await response.delete()

    elif "handshake" in content:
      # List of handshake gif links (local to the function)
        handshake_gifs = [
       "https://media.giphy.com/media/oX8pSaFrQw3sJ0K5bk/giphy.gif",
       "https://media.giphy.com/media/xr7GE8l07Zw2Y/giphy.gif",
       "https://media.giphy.com/media/4BdaJ92wV9ciI/giphy.gif",
       "https://media.giphy.com/media/Dj8NIuXppqHAY/giphy.gif",
       "https://media.giphy.com/media/d1E2VyhFsxawRbeo/giphy.gif"
          ]
           # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_handshake_gif = random.choice(handshake_gifs)
        response=await msg.reply(f"{sender_user_mention}, Let's s.h.a.k.e h.a.n.d.s {mentioned_user_mention}\n{random_handshake_gif}")
        await asyncio.sleep(160)
        await response.delete()
    elif "dance" in content:
      # List of dance gif links (local to the function)
      dance_gifs = [
          "https://media.giphy.com/media/l4Ep3mmmj7Bw3adWw/giphy.gif",
          "https://media.giphy.com/media/l3vRlT2k2L35Cnn5C/giphy.gif",
          "https://media.giphy.com/media/14qb1Uhf40ndw4/giphy.gif",
          "https://media.giphy.com/media/Z9WQLSrsQKH3uBbiXq/giphy.gif",
          "https://media.giphy.com/media/Hicydpti7wG3vA8Zr4/giphy.gif",
          "https://media.giphy.com/media/10YWqUivkQPeeJWD3u/giphy.gif",
          "https://media.giphy.com/media/5xtDarIHieSzSJdmn0A/giphy.gif",
          "https://media.giphy.com/media/xUPGcIYm8zNwZ7xRIY/giphy.gif"
      ]
      # Mention the user who sent the message
      sender_user_mention = msg.author.mention
      mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
      random_dance_gif = random.choice(dance_gifs)
      response=await msg.reply(f"{sender_user_mention}, Let's D.A.N.C.E {mentioned_user_mention}\n{random_dance_gif}")

      await asyncio.sleep(160)
      await response.delete()
    elif "insult" in content:
       # List of insult gif links (local to the function)
       insult_gifs = [
           "https://media.giphy.com/media/3o6Ztbh0jSWVTIy080/giphy.gif",
           "https://media.giphy.com/media/oUS6u2rbjg4JD4Z9Lp/giphy.gif",
           "https://media.giphy.com/media/D5Xw2pE3BbKSw29xVi/giphy.gif",
           "https://media.giphy.com/media/CSRlrzDb0JX2w/giphy.gif",
           "https://media.giphy.com/media/13k0uUW3Aicx20/giphy.gif"
       ]
       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
       random_insult_gif = random.choice(insult_gifs)
       response=await msg.reply(f"{sender_user_mention}, That was an I.N.S.U.L.T, {mentioned_user_mention}!\n{random_insult_gif}")
       await asyncio.sleep(160)
       await response.delete()
    elif "tea" in content:
       # List of tea gif links (local to the function)
       tea_gifs = [
           "https://media.giphy.com/media/Wn74RUT0vjnoU98Hnt/giphy.gif",
           "https://media.giphy.com/media/BwStBxZnY7wkr8xltb/giphy.gif",
           "https://media.giphy.com/media/MDs5sQsX9LjscxOl8y/giphy.gif",
           "https://media.giphy.com/media/fD8gg1XymoTEhXhfCW/giphy.gif",
           "https://media.giphy.com/media/M1VL81pAxfj3y/giphy.gif"
       ]
       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
       random_tea_gif = random.choice(tea_gifs)
       response=await msg.reply(f"{sender_user_mention}, Time for T.E.A, {mentioned_user_mention}!\n{random_tea_gif}")
       await asyncio.sleep(160)
       await response.delete()

    elif "confuse" in content:
       # List of confuse gif links (local to the function)
       confuse_gifs = [
           "https://media.giphy.com/media/xT0xeuOy2Fcl9vDGiA/giphy.gif",
           "https://media.giphy.com/media/xRYZdfv3DgIQb1dvNA/giphy.gif",
           "https://media.giphy.com/media/9knlRYeSZ2wKBN7iEq/giphy.gif",
           "hhttps://media.giphy.com/media/hEs49vQtvBm2uESkrK/giphy.gif",
           "https://media.giphy.com/media/Sfm4egPjeaLSHatxUO/giphy.gif",
           "https://media.giphy.com/media/LomlRfu3doGd7Ki4nD/giphy.gif"
       ]
       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
       random_confuse_gif = random.choice(confuse_gifs)
       response=await msg.reply(f"{sender_user_mention}, I'm C.O.N.F.U.S.E.D, {mentioned_user_mention}!\n{random_confuse_gif}")
       await asyncio.sleep(160)
       await response.delete()
    elif "sad" in content:
       # List of sad gif links (local to the function)
       sad_gifs = [
           "https://media.giphy.com/media/7SF5scGB2AFrgsXP63/giphy.gif",
           "https://media.giphy.com/media/OPU6wzx8JrHna/giphy.gif",
           "https://media.giphy.com/media/NTY1kHmcLsCsg/giphy.gif",
           "https://media.giphy.com/media/BLJy2x6QwzgdrCfAlD/giphy.gif",
           "https://media.giphy.com/media/6gDSyjaOPwZ4A/giphy.gif"
       ]
       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
       random_sad_gif = random.choice(sad_gifs)
       response=await msg.reply(f"{sender_user_mention}, Feeling S.A.D, {mentioned_user_mention}!\n{random_sad_gif}")
       await asyncio.sleep(160)
       await response.delete()


    elif "nervous" in content:
      # List of nervous gif links (local to the function)
      nervous_gifs = [
          "https://media.giphy.com/media/GVKHEH8M5MLIWiqZVz/giphy.gif",
          "https://media.giphy.com/media/pDdzX4l9jqA80/giphy.gif",
          "https://media.giphy.com/media/lvzdeWk12qjmM/giphy.gif",
          "https://media.giphy.com/media/DUuyU3KyYGLNS/giphy.gif",
          "https://media.giphy.com/media/26DN5mTjpKEsumZqg/giphy.gif"
      ]
      # Mention the user who sent the message
      sender_user_mention = msg.author.mention
      mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
      random_nervous_gif = random.choice(nervous_gifs)
      response=await msg.reply(f"{sender_user_mention}, Feeling n.e.r.v.o.u.s, {mentioned_user_mention}!\n{random_nervous_gif}")
      await asyncio.sleep(160)
      await response.delete()


    elif "bored" in content:
       # List of bored gif links (local to the function)
       bored_gifs = [
           "https://media.giphy.com/media/tXL4FHPSnVJ0A/giphy.gif",
           "https://media.giphy.com/media/tmQrpA8zpG4a16SSxm/giphy.gif",
           "https://media.giphy.com/media/3o6Zt62PeJeFUDwBUI/giphy.gif",
           "https://media.giphy.com/media/l2JhpjWPccQhsAMfu/giphy.gif",
           "https://media.giphy.com/media/ZgqJGwh2tLj5C/giphy.gif"
       ]
       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
       random_bored_gif = random.choice(bored_gifs)
       response=await msg.reply(f"{sender_user_mention}, Feeling b.o.r.e.d, {mentioned_user_mention}!\n{random_bored_gif}")
       await asyncio.sleep(160)
       await response.delete()

    elif "wow" in content:
        # List of wow gif links (local to the function)
        wow_gifs = [
            "https://media.giphy.com/media/dSetRSJcR3PGqkvjRg/giphy.gif",
            "https://media.giphy.com/media/Sqfu14lSonVN219Zb6/giphy.gif",
            "https://media.giphy.com/media/7ziO8WTeXJCGZlq4mm/giphy.gif",
            "https://media.giphy.com/media/1ym5LJ17vp77BL8X5O/giphy.gif",
            "https://media.giphy.com/media/jrutBd1N7ZhsINAPzs/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_wow_gif = random.choice(wow_gifs)
        response=await msg.reply(f"{sender_user_mention}, That's a.m.a.z.i.n.g, {mentioned_user_mention}!\n{random_wow_gif}")
        await asyncio.sleep(160)
        await response.delete()



    elif "jealous" in content:
         # List of wow gif links (local to the function)
         wow_gifs = [
             "https://media.giphy.com/media/bTuGUzjm9Uru/giphy.gif",
             "https://media.giphy.com/media/oR0KiKwPmxWBG/giphy.gif",
             "https://media.giphy.com/media/5rrkafIbeVs5y/giphy.gif",
             "https://media.giphy.com/media/PmTWHSzTo53A4/giphy.gif",
             "https://media.giphy.com/media/qw5v8QkRYF42P7Lg8j/giphy.gif"
             
         ]
         # Mention the user who sent the message
         sender_user_mention = msg.author.mention
         mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
         random_wow_gif = random.choice(wow_gifs)
         response=await msg.reply(f"{sender_user_mention}, j.e.a.l.o.u.s, {mentioned_user_mention}!\n{random_wow_gif}")
         await asyncio.sleep(160)
         await response.delete()


    elif "welcome" in content:
        # List of wow gif links (local to the function)
        wow_gifs = [
            "https://media.giphy.com/media/XD9o33QG9BoMis7iM4/giphy.gif",
            "https://media.giphy.com/media/5UA8yzZgQeq3C02eA2/giphy.gif",
            "https://media.giphy.com/media/6pfEK1odbmcNi/giphy.gif",
            "https://media.giphy.com/media/qycX5IhwgIXSw/giphy.gif",
            "https://media.giphy.com/media/eoVusT7Pi9ODe/giphy.gif",
           "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif",
           "https://media.giphy.com/media/LpDmTYtmOJLXxkMB3H/giphy.gif",
          "https://media.giphy.com/media/oo2tEZ4bKu4s2dgSgI/giphy.gif",
           "https://media.giphy.com/media/X9MsWYVhRyNMY/giphy.gif",
          "https://media.giphy.com/media/Vg23LlVhBHM6V5JTyh/giphy.gif",
           "https://media.giphy.com/media/UtzyBJ9trryNO4R3Ee/giphy.gif",
          "https://media.giphy.com/media/QQyP7vl2S5g2mxF6Ed/giphy.gif",
           "https://media.giphy.com/media/H5OcJyyzY25aqofOiS/giphy.gif",
          "https://media.giphy.com/media/3oEhmOyl9YmGptHaoM/giphy.gif",
          "https://media.giphy.com/media/EqrIrilix4ysLpavlm/giphy.gif",
          "https://media.giphy.com/media/mBx7IUXlLx5MnnUGvD/giphy.gif",
          "https://media.giphy.com/media/BpS6k9mXoDiZa/giphy.gif",
          "https://media.giphy.com/media/TjB1MDpAsnqfOIYiy9/giphy.gif",
          "https://media.giphy.com/media/kZzY6eKKPdIjK/giphy.gif",

          "https://media.giphy.com/media/KMOzoSPDlQAhByLV3N/giphy.gif",
          "https://media.giphy.com/media/l3vRcE1YdbT9lPvDW/giphy.gif",
          "https://media.giphy.com/media/efekGoJMGlbpolOC1F/giphy.gif",
          "https://media.giphy.com/media/kmQREsvNQrhrHdkN7G/giphy.gif",
          "https://media.giphy.com/media/OvFMkVG5Z0cPhkhEeb/giphy.gif",
          "https://media.giphy.com/media/2x1jUYo8hIjdVg6Pqb/giphy.gif",
          "https://media.giphy.com/media/jCD6wQiUKQsYZlTAIG/giphy.gif",
          "https://media.giphy.com/media/5ceUVAtb1qTzN78Kbx/giphy.gif",
          "https://media.giphy.com/media/hTyWvPxBjJneYl7vJe/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_wow_gif = random.choice(wow_gifs)
        response=await msg.reply(f"{sender_user_mention},  W.E.L.C.O.M.E , {mentioned_user_mention}!\n{random_wow_gif}")
        await asyncio.sleep(160)
        await response.delete()



    elif "problem" in content:
        # List of wow gif links (local to the function)
        wow_gifs = [
            "https://media.giphy.com/media/GXKK71oMMtBPu8ffUW/giphy.gif",
            "https://media.giphy.com/media/caQCZus2yRmdc8YrLQ/giphy.gif",
            "https://media.giphy.com/media/Px7FQJqhWTGaA/giphy.gif",
            "https://media.giphy.com/media/h7yxbqC44jCYgWT2sV/giphy.gif",
            "https://media.giphy.com/media/eChf44Gyj2VrO/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_wow_gif = random.choice(wow_gifs)
        response=await msg.reply(f"{sender_user_mention}, That's a p.r.o.b.l.e.m , {mentioned_user_mention}!\n{random_wow_gif}")
        await asyncio.sleep(160)
        await response.delete()


    elif "sing" in content:
       # List of wow gif links (local to the function)
       wow_gifs = [
           "https://media.giphy.com/media/3o7qE897uzZjkm4hQA/giphy.gif",
           "https://media.giphy.com/media/7C0wCAyx9qoKPIeToi/giphy.gif",
           "https://media.giphy.com/media/fnk8VHOUlKBrY728zF/giphy.gif",
           "https://media.giphy.com/media/Y1GIle1Vv7jCsYqbi8/giphy.gif",
           "https://media.giphy.com/media/UIjDlOIr0nFH2uNFEN/giphy.gif"
       ]
       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
       random_wow_gif = random.choice(wow_gifs)
       response=await msg.reply(f"{sender_user_mention}, S.I.N.G for  , {mentioned_user_mention}!\n{random_wow_gif}")
       await asyncio.sleep(160)
       await response.delete()

    elif "thank you" in content:
         # List of wow gif links (local to the function)
         wow_gifs = [
             "https://media.giphy.com/media/ZfK4cXKJTTay1Ava29/giphy.gif",
             "https://media.giphy.com/media/FPDZV2JGkNGeUZdi7G/giphy.gif",
             "https://media.giphy.com/media/kLe9PygrSqB4oO4tYV/giphy.gif",
             "https://media.giphy.com/media/G5MDBwmdTrVMpuRJix/giphy.gif",
             "https://media.giphy.com/media/E8rJEUMGs9cyWEtNXT/giphy.gif"
         ]
         # Mention the user who sent the message
         sender_user_mention = msg.author.mention
         mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
         random_wow_gif = random.choice(wow_gifs)
         response=await msg.reply(f"{sender_user_mention}, t.h.a.n.k y.o.u  , {mentioned_user_mention}!\n{random_wow_gif}")
         await asyncio.sleep(160)
         await response.delete()

    elif "happy" in content:
         # List of wow gif links (local to the function)
         wow_gifs = [
             "https://media.giphy.com/media/chzz1FQgqhytWRWbp3/giphy.gif",
             "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
             "https://media.giphy.com/media/3NtY188QaxDdC/giphy.gif",
             "https://media.giphy.com/media/IoMkSXKHQIDVm/giphy.gif",
             "https://media.giphy.com/media/9Y6n9TR7U07ew/giphy.gif"
         ]
         # Mention the user who sent the message
         sender_user_mention = msg.author.mention
         mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
         random_wow_gif = random.choice(wow_gifs)
         response=await msg.reply(f"{sender_user_mention}, H.A.P.P.Y for  , {mentioned_user_mention}!\n{random_wow_gif}")
         await asyncio.sleep(160)
         await response.delete()

    elif "bye" in content:
        # List of wow gif links (local to the function)
        wow_gifs = [
            "https://media.giphy.com/media/xUySTVNHpdACknfKuc/giphy.gif",
            "https://media.giphy.com/media/lxQ53bXTjQtwpUItYB/giphy.gif",
            "https://media.giphy.com/media/5xtDarEgBDjEoWo6VRS/giphy.gif",
            "https://media.giphy.com/media/35EsMpEfGHkVoHbNTU/giphy.gif",
            "https://media.giphy.com/media/7DzlajZNY5D0I/giphy.gif"
        ]
        # Mention the user who sent the message
        sender_user_mention = msg.author.mention
        mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
        random_wow_gif = random.choice(wow_gifs)
        response=await msg.reply(f"{sender_user_mention}, B.Y.E  , {mentioned_user_mention}!\n{random_wow_gif}")
        await asyncio.sleep(160)
        await response.delete()


    elif "hey" in content:
       # List of wow gif links (local to the function)
       wow_gifs = [
           "https://media.giphy.com/media/SUtKUblVAvwMkTvaiT/giphy.gif",
           "https://media.giphy.com/media/xT39D7D1jX4ZjGK5EI/giphy.gif",
           "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif",
           "https://media.giphy.com/media/VdAvVcQLJDwKKDUDJR/giphy.gif",
           "https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif"
           "https://media.giphy.com/media/OnnUZxcHsbBN6/giphy.gif",
           "https://media.giphy.com/media/aDS4z67KKaumbMVanT/giphy.gif",
           "https://media.giphy.com/media/kZzY6eKKPdIjK/giphy.gif",
            "https://media.giphy.com/media/JsAXhnCEXr61PAHXc5/giphy.gif"
       ] 
       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
       random_wow_gif = random.choice(wow_gifs)
       response=await msg.reply(f"{sender_user_mention}, H.E.Y  , {mentioned_user_mention}!\n{random_wow_gif}")
       await asyncio.sleep(160)
       await response.delete()

    elif "cute" in content:
      # List of wow gif links (local to the function)
      wow_gifs = [
          "https://media.giphy.com/media/QynP1m2c4jt3STncEp/giphy.gif",
          "https://media.giphy.com/media/M9Nv3uS49YIz9pMO4h/giphy.gif",
          "https://media.giphy.com/media/33Uzuf6fquH0hoZXCh/giphy.gif",
          "https://media.giphy.com/media/UpE1MNOggKqh1xSeW1/giphy.gif",
          "https://media.giphy.com/media/bPWoQ2IASDffgLvvTL/giphy.gif"
      ]
      # Mention the user who sent the message
      sender_user_mention = msg.author.mention
      mentioned_user_mention = msg.mentions[0].mention if msg.mentions else ""
      random_wow_gif = random.choice(wow_gifs)
      response = await msg.reply(f"{sender_user_mention}, C.U.T.E, {mentioned_user_mention}!\n{random_wow_gif}")
      await asyncio.sleep(160)
      await response.delete()

    elif "okay" in content:
       # List of okay gif links (local to the function)
       okay_gifs = [
           "https://media.giphy.com/media/oOCbcGBJjlXJL8imGO/giphy.gif",
           "https://media.giphy.com/media/esVaNp1XK3h5vVwa1x/giphy.gif",
           "https://media.giphy.com/media/iOMSfTen1pZUPTx2QF/giphy.gif",
           "https://media.giphy.com/media/tIeCLkB8geYtW/giphy.gif",
           "https://media.giphy.com/media/Ge0Bt025YVlhXzOmuP/giphy.gif"
       ]

       # Mention the user who sent the message
       sender_user_mention = msg.author.mention
       random_okay_gif = random.choice(okay_gifs)

       response = await msg.reply(f"{sender_user_mention}, O.k.a.y!\n{random_okay_gif}")
       await asyncio.sleep(160)
       await response.delete()