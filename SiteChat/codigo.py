#Título: Hashzap
#Botão de iniciar chat
    #clicou no botão: 
        #popup / modal
        #campo: escreva seu nome no chat
        #botão: entrar no chat
#chat
#embaixo do chat
    #campo de Digite sua mensagem
    #botão de enviar

#flet -> framework do Python

# 3 Passos
    # Importar o framework
import flet as ft
    # Criar a função principal
def main(pagina):
    texto = ft.Text("Sakai's Zap")

    chat = ft.Column()

    def enviarfall(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        campomensagem.value = ""
        pagina.update()

    pagina.pubsub.subscribe(enviarfall)

    def enviarmensagem(evento):
        pagina.pubsub.send_all(f"{nomeusuario.value} : {campomensagem.value}")
        campomensagem.value = ""
        pagina.update()


    campomensagem = ft.TextField(label= "Digite a sua mensagem aqui:", on_submit=enviarmensagem)
    enviarmen = ft.ElevatedButton("Enviar", on_click=enviarmensagem)
    linhaenv = ft.Row([campomensagem, enviarmen])

    def entrarchat(evento):
        pagina.pubsub.send_all(nomeusuario.value +  " entrou no chat")
        popup.open = False #Fechando o Popup
        pagina.remove(botãoiniciar) #Removendo o botão inicial
        pagina.add(chat)
        pagina.add(linhaenv)
        pagina.update()



    titulopopup = ft.Text("Bem vindo ao Chat!")
    nomeusuario = ft.TextField(label= "Digite o seu nome: ")
    botaoentry = ft.ElevatedButton("Entrar no chat", on_click=entrarchat)
    popup = ft.AlertDialog(
        open = False,
        modal = True,
        title = titulopopup,
        content = nomeusuario,
        actions = [botaoentry]
    )

    def abrirpopup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botãoiniciar = ft.ElevatedButton("Iniciar Chat", on_click= abrirpopup)

    pagina.add(texto)
    pagina.add(botãoiniciar)


# Criar o app chamando a def principal
ft.app(target=main, view=ft.WEB_BROWSER)