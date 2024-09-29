import flet as ft
def main(page:ft.Page):
    def formulario_de_contato(e):
        contato=ft.Row([ft.Text(nome.value),
                ft.Text(email.value),
                ft.Text(mensagem.value),
                ft.Text(titulo.value)])
        lista.controls.append(contato)
        confirmacao.value="sua mensagem foi enviada!"
        nome.value=""
        email.value=""
        mensagem.value=""
        page.update()


    page.title="Pagina de formularios"
    page.window_width=500
    page.window_height=500

    nome=ft.TextField(label="digite o nome",width=300)
    email=ft.TextField(label="digite o email",width=300)
    mensagem=ft.TextField(label="digite a mensagem",width=300)
    botao=ft.ElevatedButton(text="enviar",on_click=formulario_de_contato)
    confirmacao=ft.Text(value="",size=20,color="green")
    titulo=ft.Text(value="Meu formulario",text_align="center",weight="bold",size=30)
    lista=ft.Column()

    page.add(titulo,nome,email,mensagem,botao,confirmacao,lista)

ft.app(target=main)

