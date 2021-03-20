import discord
import random
import urllib.request
from discord.ext import commands
from PIL import Image, ImageFilter

# Essa parte do código inicializa o bot
client = discord.Client()
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='~', intents=intents)
token = 'YOUR TOKEN GOES HERE'
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# O jogo usará uma lista com várias possíveis palavras
with open("Keywords.txt", 'r') as file:
    keys = file.read().split('\n')

@client.event
async def on_message(message):  # Quando uma mensagem for recebida

    if message.author == client.user:  # Evita que o bot responda a ele mesmo
        return

    # Se a mensagem for "~start" o bot inicia o jogo e envia a mensagem explicando
    if message.content.startswith('~start'):
        await message.channel.send(
            "Welcome to the game! \nHere are the rules:\nYou have 20 guesses.\nEvery incorrect guess will decrease the image's level of blur.\nGood luck!\n "
        )
        await message.channel.send('Guess what this image is:')

        # Essa função será usada depois e sempre retorna True
        def is_correct(m):
            return True

        answer = random.choice(
            keys)  # O bot escolhe uma palavra aleatória entre uma lista
        chances = 20  # Ele te dá 20 chances para acertar
        image = get_image(answer)  # E pega essa imagem da internet

        # A cada tentativa, o bot reduz o filtro aplicado
        while chances > 0:
            blurred = apply_filters(chances, image)
            blurred.save("imagem.png")

            # Envia a imagem no Discord
            await message.channel.send(file=discord.File('imagem.png'))

            # Espera por uma tentativa do usuário
            guess = await client.wait_for('message',
                                          check=is_correct,
                                          timeout=120.0)
            
            # Se a tentativa estiver correta ele define o vencedor
            if (guess.content == answer):
                await message.channel.send(
                    f'You are right! {guess.author.mention} is the winner.')
                break
            
            # Caso esteja errada, o jogo diminui uma chance e reduz o filtro
            else:
                await message.channel.send(f'{chances - 1} chances left')
                chances -= 1
            
            # Quando as chances acabarem ou alguém acertar, o jogo enviará a resposta com a imagem
            await message.channel.send(f'The answer was {answer}.')
            blurred = apply_filters(0, image)
            blurred.save("imagem.png")
            await message.channel.send(file=discord.File('imagem.png'))

# Essa função pega a imagem da internet
def get_image(key):
    raw_word = key
    word = raw_word.replace(' ', '+')
    chave = random.choice(range(20))
    f = urllib.request.urlopen(
        f"https://images.search.yahoo.com/search/images;_ylt=AwrJ7KDGUe1fhdgAUN5XNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZANDMDY3Ml8xBHNlYwNwaXZz?p={word}&fr2=piv-web&fr=yfp-search-sb"
    )
    page = f.read().decode("utf-8")
    f.close()

    index0 = page.index(f'resitem-{chave}')
    base0 = page[index0:]
    index1 = base0.index(f'img src')
    base1 = base0[index1:]
    index2 = base1.index("'")
    base2 = base1[index2 + 1:]
    index3 = base2.index("'")
    link = base2[:index3]

    return link

# Essa função aplica os filtros na imagem
def apply_filters(kernel, image):
    img = Image.open(urllib.request.urlopen(image))
    k = (50 / 960) * (1 / 20) * kernel * img.size[0]
    k = round(k)
    blurred = img.filter(ImageFilter.BoxBlur(k))
    return blurred

client.run(token)