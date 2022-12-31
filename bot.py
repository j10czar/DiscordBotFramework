import discord
import responses

TOKEN = 'insert token here'

async def send_message(message, user_message, is_dm):
    try:

        response = responses.handle_response(user_message)
        await message.author.send(response) if is_dm else await message.channel.send(response)
    except Exception as e:
        print(e)





def run_bot():
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(client.user,'is now running!')
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return


        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel) 
        print(username+' in '+channel+': '+user_message)

        if user_message[0]=='.':
            user_message = user_message[1:]
            await send_message(message, user_message, is_dm=False)



    client.run(TOKEN)

    
