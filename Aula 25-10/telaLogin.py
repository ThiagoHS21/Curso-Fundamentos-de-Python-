# Tela de Login com customtkinter
#streamlit
#Flash
#Django
import customtkinter as ctk

# Criando a Função de Validação
def validacao():
    email = box_email.get()
    senha = box_senha.get()

    if not email or not senha:
        print('Preencha todos os campos!!')
        txt_msg.configure(text='Preencha todos os campos!!', text_color='#F29F05')
    elif email == 'eu@eu' and senha == '1234':
        print('Dados Validado com Sucesso!!')
        txt_msg.configure(text='Dados Validado com Sucesso!!', text_color='green')
    else:
        print('Dados não Confere!!')
        txt_msg.configure(text='Dados não Confere!!', text_color ='red')

# Definir a Tela
tela = ctk.CTk()

# Definir Tamanho da Tela
tela.geometry('300x400+1000+100')
#nome Jenela
tela.title('Tela de Login')

#Desbloquear alinhamento de Elementos

tela.columnconfigure(0, weight=1)

# Criando os Widgets (elemento de tela)
# - Grid
# - Pack
txt_login = ctk.CTkLabel(tela, text= 'Faça seu Login', font=('Verdana', 25))
txt_login.grid(row=0, column=0, padx=50, pady= 15)

txt_email= ctk.CTkLabel(tela, text='Digite Seu Email:', font= ('Verdana', 18))
txt_email.grid(row=1, column=0, padx=50, pady= (10,3), sticky= 'w')

box_email =  ctk.CTkEntry(tela,width=250, placeholder_text='Coloque email')
box_email.grid(row=2, column=0, padx=50, pady= 5)

txt_senha = ctk.CTkLabel(tela, text= 'Digite sua Senha:', font=('Verdana', 18))
txt_senha.grid(row=3, column=0, padx=50, pady= (10,3), sticky='w')

box_senha =  ctk.CTkEntry(tela,width=250, placeholder_text='Coloque a senha', show='*')
box_senha.grid(row=4, column=0, padx=50, pady= 5)

btn_enviar= ctk.CTkButton(tela,text='Enviar', font=('Verdana', 10), command=validacao)
btn_enviar.grid (row=5,column=0, padx=50, pady=15)

txt_msg = ctk.CTkLabel(tela, text='', font=('Verdana', 10))
txt_msg.grid(row=6, column=0, padx=50, pady=(10,3))

# Função Para Manter a Janela Aberta
tela.mainloop()