from model import modelCola
from view import viewCola
import discord
import async_timeout



class ControllerCola():
    TOKEN = '68c32b2e584faf1f1b3c4855451a0a9934f5e5ab40f3c66b0f78245c44d45cd7'
    PREFIX = '!'
    INTENTS = discord.Intents.default()
    client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)
    
    
    @client.event
    async def on_ready():
        print(f'Logged in as: {client.user.name}')
        print(f'With ID: {client.user.id}')
    
    
    client.run(TOKEN)

    @client.event
    async def start():
        opcao = self.view.start

        while opcao != 0:
            materia = self.seleciona(opcao)
            self.view.selecionaMenu(materia)
            opcao = self.view.menu_materia()

    
        
    async def seleciona(self, opcao):
        x = self.view.selecionaMenu()
        if opcao == 1:
            return self.model.menu_matematica(x)
        elif opcao == 2:
            return self.model.menu_portugues(x)
        elif opcao == 3:
            return self.model.menu_historia(x)
        elif opcao == 4:
            return self.model.menu_geografia(x)
        elif opcao == 5:
            return self.model.menu_biologia(x)
        else:
            return self.model.menu_ingles(x)

    def __init__(self):
        self.model = modelCola
        self.view = viewCola

if __name__ == "__main__":
    main = ControllerCola
    main.start()