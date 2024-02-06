import discord

async def handle_wn_command(message, text1_channel_id, text2_channel_id):
    if message.content.startswith("!wn"):
        message_content = message.content[3:].strip()

        # Get the text1 channel by ID
        text1_channel = message.guild.get_channel(text1_channel_id)
        # Get the text2 channel by ID
        text2_channel = message.guild.get_channel(text2_channel_id)

        if text1_channel and text2_channel:
            # Send the message content from text1 channel to text2 channel
            await text1_channel.send(message_content)
            await text2_channel.send(message_content)
        else:
            print("Text1 or Text2 channel not found. Make sure the channel IDs are correct.")
