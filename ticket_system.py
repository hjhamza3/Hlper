import discord

user_to_channel = {}  # Dictionary to store user IDs as keys and ticket channel IDs as values

async def handle_tickets(bot, message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself

    if isinstance(message.channel, discord.DMChannel):
        user_id = message.author.id

        # Check if the user already has a ticket channel
        if user_id not in user_to_channel:
            # Get the category
            category = bot.get_channel(1165593221347414057)
            if category:
                # Create a new channel with a unique name
                channel_name = f"Ticket{len(user_to_channel) + 1}"
                new_channel = await category.create_text_channel(channel_name)

                # Store the user's ID and ticket channel ID in the dictionary
                user_to_channel[user_id] = new_channel.id

            # Send an automatic reply to the user who sent the first DM
            reply_message = "Thank you for your message! We have received it and will contact you very soon."
            await message.author.send(reply_message)

        # Forward the DM message to the user's ticket channel
        user_channel_id = user_to_channel.get(user_id)
        if user_channel_id:
            user_channel = bot.get_channel(user_channel_id)
            if user_channel:
                await user_channel.send(f"DM from {message.author.display_name}: {message.content}")

    else:
        # Check if the message was sent in a ticket channel
        if isinstance(message.channel, discord.TextChannel) and message.channel.category_id == 1165593221347414057:
            original_sender_id = None

            # Find the original sender's ID based on the ticket channel ID
            for user_id, channel_id in user_to_channel.items():
                if channel_id == message.channel.id:
                    original_sender_id = user_id
                    break

            if original_sender_id:
                # Get the original sender's channel object
                original_sender_channel = bot.get_user(original_sender_id)
                if original_sender_channel:
                    # Send the reply message back to the original sender's DM
                    await original_sender_channel.send(f" {message.content}")
