import asyncio

import discord

original_voice_channel_id = 1136644728968978513
created_voice_channels = {}  # A dictionary to store the created voice channels

async def send_welcome_message(voice_channel, creator):
    speaking_partner_role_id = 990243328459173888
    role_mention = f'<@&{speaking_partner_role_id}>'  # Mention the role manually

    welcome_message = f"Hi, I am seeking a speaking partner!\nCreated by: {creator.mention}\nRoles: {role_mention}"
    await voice_channel.send(welcome_message)

async def delete_empty_channel(channel_id):
    await asyncio.sleep(10)  # Wait for 10 seconds
    voice_channel = discord.utils.get(bot.guilds[0].voice_channels, id=channel_id)
    if voice_channel and not voice_channel.members:
        await voice_channel.delete()
        del created_voice_channels[channel_id]

async def on_voice_state_update(member, old_state, new_state):
  if member.bot:
      return

  new_channel = new_state.channel
  old_channel = old_state.channel

  if old_channel != new_channel and new_channel and new_channel.id == original_voice_channel_id:
      await asyncio.sleep(2)  # Wait for 3 seconds before creating a new channel

      # Check if the user is still in the original channel after the sleep period
      if member.voice and member.voice.channel and member.voice.channel.id == original_voice_channel_id:
          overwrites = {
              member.guild.default_role: discord.PermissionOverwrite(connect=True, speak=True),
          }

          # Get the number of existing private voice channels
          speaking_pairs = sum(1 for channel in new_channel.category.channels if channel.name.startswith("Speaking Pair"))

          voice_channel = await new_channel.category.create_voice_channel(
              name=f"Speaking Pair {speaking_pairs + 1}",
              overwrites=overwrites,
              user_limit=2  # Set the user limit to 2 for the private voice channel
          )

          await member.move_to(voice_channel)

          created_voice_channels[voice_channel.id] = True
          await send_welcome_message(voice_channel, member)

          bot.loop.create_task(delete_empty_channel(voice_channel.id))



async def remove_empty_channels(ctx):
    empty_channels = [channel for channel in ctx.guild.voice_channels if len(channel.members) == 0 and channel.id in created_voice_channels]
    for channel in empty_channels:
        await channel.delete()
        del created_voice_channels[channel.id]
