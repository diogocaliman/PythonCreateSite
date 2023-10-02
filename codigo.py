# PapoPeople

#  Botão para Iniciar um Chat
# PoPup para Entrar no Chat
# Quando entrar no Chat: (Aparece para todo mundo ao vivo)
    # A Mensagem que você entrou no chat
    # O campo e o botão de enviar mensagem   
# A cada mensagem que o usuário enviar: (Aparece para todo mundo ao vivo)
    # Nome: Texto da Mensagem


import flet

def main(pagina):
    texto = flet.Text("PapoPeople")

    chat = flet.Column()

    nome_usuario = flet.TextField(label="Digite seu Nome")

    def enviar_mensagem_tunel(infos):
        tipo = infos["tipo"]
        if tipo == "infos":
            texto_mensagem = infos["texto"]
            usuario_mensagem = infos["usuario"]
            #adicionar a mensagem no chat
            chat.controls.append(flet.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = infos["usuario"]    
            chat.controls.append(flet.Text(f"{usuario_mensagem} entrou no chat", 
                                           size=10, italic=True, color=flet.colors.LIGHT_BLUE_500))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo" : "infos"})
        # limpar o campo de mensagem 
        campo_mensagem.value = ""
        pagina.update() 
    
    campo_mensagem = flet.TextField(label = "Digite uma Mensagem", on_submit = enviar_mensagem)
    botao_enviar_msg = flet.ElevatedButton("Enviar", on_click = enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo" : "entrada"})
        #adicionar o chat
        pagina.add(chat)
        #fechar o popup 
        popup.open = False
        #remover o botão iniciar chat
        pagina.remove(botao_start)
        pagina.remove(texto)
        #criar o campo de mensagem do usuario
        #criar o botao de enviar mensagem
        pagina.add(flet.Row(
            [campo_mensagem, botao_enviar_msg]
        ))
        pagina.update()


    popup = flet.AlertDialog(
        open = False,
        modal = True,
        title= flet.Text("Welcome ao PapoPeople"),
        content=nome_usuario,
        actions=[flet.ElevatedButton("Iniciar", on_click = entrar_popup)],
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_start = flet.ElevatedButton("Iniciar Chat", on_click = entrar_chat)

    pagina.add(texto)
    pagina.add(botao_start)


flet.app(target = main, view = flet.WEB_BROWSER)

#--- deploy ---