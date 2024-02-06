import random

import discord
from discord.ext import commands, tasks

import aitext
import config
import voice
from keep_alive import keep_alive
from ticket_system import handle_tickets
from topics import discussion_topics
from voice_event_handler import handle_voice_state_update

keep_alive()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Store channel IDs in a dictionary
channel_ids = {
    "text1": 990239842531156000,
    "text2": 1145542152978448485,
    "text3": 935070314575065109,
    "text4": 1141993006099083335,
    "text5": 1165583033303322674,
    "text6": 763115297904263220,
    "dm_category": 1165593221347414057,
}

# Define the statuses
statuses = ["DM Open 🗯️", "Contact for Staff 📧", "Report📝"]
status_index = 0

@tasks.loop(seconds=5)
async def change_status():
    global status_index
    await bot.change_presence(activity=discord.Game(name=statuses[status_index]), status=discord.Status.online)
    status_index = (status_index + 1) % len(statuses)

@bot.event
async def on_ready():
    print("Bot is ready!")
    change_status.start()

@bot.command()
async def dmt(ctx, *, args):
    if ctx.channel.id == channel_ids["text1"]:
        try:
            message_content, channel_id = args.rsplit(" ", 1)
            channel_id = channel_id.strip('"')
            target_channel = bot.get_channel(int(channel_id))

            if target_channel:
                await target_channel.send(f"{message_content}")
                await ctx.send(f"Your message has been forwarded to {target_channel.mention}.")
            else:
                await ctx.send("Invalid channel ID. Please check the channel ID and try again.")
        except ValueError:
            await ctx.send("Invalid command format. Please use the format: `!dmt <message> <channel_id>`.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

@bot.command()
async def dm(ctx, *, args):
    if ctx.channel.id == channel_ids["text1"]:
        category = bot.get_channel(channel_ids["dm_category"])
        if category:
            mentioned_user = ctx.message.mentions[0] if ctx.message.mentions else None
            staff_talk_channels = [channel for channel in category.channels if channel.name.startswith("Staff Talk")]
            new_channel_name = f"Staff Talk {len(staff_talk_channels) + 1}"

            role = ctx.guild.get_role(1166239893375156264)
            if role:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                }

                new_channel = await category.create_text_channel(new_channel_name, overwrites=overwrites)

                if mentioned_user:
                    await mentioned_user.add_roles(role)
                    await new_channel.send(f"{mentioned_user.mention}: {args}")
                else:
                    await new_channel.send(args)

                await ctx.send(f"Your message has been forwarded to {new_channel.mention}.")
        else:
            await ctx.send("Category not found. Please check the category ID.")
    else:
        await ctx.send("This command can only be used in text1 channel.")

 








@bot.command()
async def remove_empty_channels(ctx):
    await voice.remove_empty_channels(ctx)

bot.add_listener(voice.on_voice_state_update)


@bot.command()
async def at(ctx, *, message):
    if ctx.channel.id == text1_channel_id:
        text3_channel = bot.get_channel(text3_channel_id)

        if text3_channel:
            # Send the message to text3 channel
            await text3_channel.send(message)

@bot.command()
async def talk(ctx, *, message):
    if ctx.channel.id == text1_channel_id:
        text3_channel = bot.get_channel(text4_channel_id)

        if text3_channel:
            # Send the message to text3 channel
            await text3_channel.send(message)
          
@bot.command()
async def talkg(ctx, *, message):
    if ctx.channel.id == text1_channel_id:
        text6_channel = bot.get_channel(text6_channel_id)

        if text6_channel:
            # Send the message to text6 channel
            await text6_channel.send(message)
        else:
            await ctx.send("Text channel not found. Please check the channel ID.")
    else:
        await ctx.send("This command can only be used in text1 channel.")


@bot.command()
async def wn(ctx, *, message):
    # Check if the command was sent in text1 channel
    if ctx.channel.id != text1_channel_id:
        await ctx.send("This command can only be used in bot-commad.")
        return

    # Get the mentioned role
    role = ctx.guild.get_role(1131920263487963216)

    # Check if the message contains a mention
    if ctx.message.mentions:
        member = ctx.message.mentions[0]  # Get the mentioned member
        await member.add_roles(role)  # Add the specified role to the mentioned member

    # Send the message to text2 channel
    text2_channel = bot.get_channel(text2_channel_id)
    if text2_channel:
        await text2_channel.send(message)

    # Send a confirmation message to the original channel
    await ctx.send("Message sent to text2 channel and role added to the mentioned user.")


@bot.event
async def on_voice_state_update(member, before, after):
    await handle_voice_state_update(member, before, after)  # Call the function from voice_event_handler.py


@bot.command()
async def topic(ctx):
    discussion_topic = random.choice(discussion_topics)
    user_mention = ctx.author.mention  # Mention the user who used the command
    await ctx.send(f'{user_mention}, here is your discussion topic: **{discussion_topic}**')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.tree.command()
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message("This is Mr A!")


@bot.event
async def on_message(message: discord.Message):
    # Call both on_message functions
    await aitext.on_message(message, bot)  # Call the on_message function from aitext.py
    await handle_tickets(bot, message)  # Call the handle_tickets function from ticket_system.py
    await bot.process_commands(message)


bot.run(config.TOKEN)
