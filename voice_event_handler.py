import asyncio
import random
import time

from topics import discussion_topics  # Import discussion_topics from topics.py

last_topic_time = {}  # Dictionary to store the last topic sending time for each member

async def handle_voice_state_update(member, before, after):
    voice_channels = {
        935529166625972254: "1 | Caffe ☕",
        1104337253439901808: "2 | Caffe ☕",
        1104337332259262564: "3 | Caffe ☕",
        1128553018669944833: "4 | Caffe ☕"
    }

    for channel_id, channel_name in voice_channels.items():
        if after.channel and after.channel.id == channel_id:
            current_time = time.time()
            member_id = member.id
            last_member_topic_time = last_topic_time.get(member_id, 0)

            # Send a new topic if it has been at least 300 seconds (5 minutes) since the last topic was sent for this member
            if current_time - last_member_topic_time >= 400:
                channel = after.channel
                welcome_message = await channel.send(f"Welcome {member.mention} to {channel_name}! Enjoy your discussion. You are a valued member of our English Community server. Did you know that spending time here earns you experience points (XP) to help you level up? We expect you to abide by our server rules <#1136889918518468658>. If someone is behaving toxically, please feel free to report them to us <#1136688228171268147>.")
                print(f"Sent welcome message with ID: {welcome_message.id}")  # Print the message ID
                await asyncio.sleep(60)  # Wait for 1 minute
                await welcome_message.delete()  # Delete the welcome message after 1 minute
                print(f"Deleted welcome message with ID: {welcome_message.id}")  # Print the message ID after deletion

                # Continue sending topics if there are 2 or more members in the channel
                while channel.members and len(channel.members) >= 2:
                    users_mention = ', '.join([member.mention for member in channel.members])
                    topic = random.choice(discussion_topics)
                    topic_message = await channel.send(f"H.e.y {users_mention}, here is your {channel_name} discussion topic: **{topic}**")
                    print(f"Sent topic message with ID: {topic_message.id}")  # Print the message ID
                    last_topic_time[member_id] = time.time()  # Update the last topic sending time for this member
                    await asyncio.sleep(900)  # Wait for 10 minutes (600 seconds) before sending the next topic
                    await topic_message.delete()  # Delete the topic message before sending a new one
                    print(f"Deleted topic message with ID: {topic_message.id}")  # Print the message ID after deletion

                break  # Exit the loop if the channel becomes empty or has less than 2 members

        # Check if someone left the channel
        if before.channel and before.channel.id == channel_id and not after.channel:
            channel = before.channel
            leave_message = f"Goodbye {member.mention}! Have a great day. We hope to see you again soon! I will miss you ❤"
            leave_msg = await channel.send(leave_message)
            print(f"Sent leave message with ID: {leave_msg.id}")  # Print the message ID
            await asyncio.sleep(60)  # Wait for 30 seconds
            await leave_msg.delete()  # Delete the leave message after 30 seconds
            print(f"Deleted leave message with ID: {leave_msg.id}")  # Print the message ID after deletion
            break  # Exit the loop when someone leaves the channel
