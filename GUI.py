import tkinter as tk
from tkinter import messagebox

#CRIANDO PAGINA DE LOGIN

#USUARIO E SENHA CORRETOS E FUNCAO PRA VERIFICAR
usuario_correto = "Work123"
senha_correta = "1234"

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == usuario_correto and senha == senha_correta:
        messagebox.showinfo("Logado!", "Logado com sucesso!")
    elif not usuario or not senha:
        messagebox.showwarning("Erro ao logar!", "Todos os campos são obrigatórios!")
    else:
        messagebox.showerror("Erro ao logar!", "Usuário ou senha incorretos!")

def abrir_tela_registro():
    janela.withdraw() #PARA ESCONDER A JANELA DE LOGIN
    janela_registro = tk.Toplevel()#CRIA UMA JANELA INDEPENDENTE NO PROGRAMA
    janela_registro.title("Registro")
    janela_registro.geometry("800x600")
    janela_registro.configure(bg="lightgrey")

    entrada_usuario = tk.StringVar()
    entrada_senha = tk.StringVar()

    def registrar_usuario():
        usuario = entrada_usuario.get().strip()
        senha = entrada_senha.get().strip()

        if not usuario or not senha:
            messagebox.showwarning("Erro ao registrar!", "Todos os campos são obrigatórios")
        elif usuario != usuario_correto or senha != senha_correta:
            messagebox.showerror("Erro ao registrar!", "Preencha os campos corretamente")
        else:
            messagebox.showinfo("Registrado!", "Registrado com sucesso!")
            entrada_usuario.set("")
            entrada_senha.set("")



    def voltar_tela_login():
        janela_registro.destroy()#PARA FAZER A TELA DE REGISTRO SUMIR
        janela.deiconify()#PARA MOSTRAR A PAGINA DE LOGIN DE NOVO

           
    #VERIFICA O FECHAMENTO PELO X (SEM ESSE COMANDO, SE VOCE FECHAR A JANELA REGISTRO PELO X
    #QUANDO VOCE TENTAR EXECUTAR O PROGRAMA DE NOVO, ELE NAO ABRE)
    janela_registro.protocol("WM_DELETE_WINDOW", voltar_tela_login)


    #TITULO DA PAGINA REGISTRO
    lbl_titulo = tk.Label(janela_registro, text="Registrar-se", bg="lightgrey", fg="black", font=("Comfortaa", 30))
    lbl_titulo.pack(pady=50)


    #CRIANDO LABEL E ENTRY DO USUARIO DA PAGINA REGISTRO
    lbl_usuario_registro = tk.Label(janela_registro, text="Usuário", bg="lightgrey", fg="#4682B4", font=("Comfortaa", 15))
    lbl_usuario_registro.pack(pady=20)
    entry_usuario_registro = tk.Entry(janela_registro, width=50, textvariable=entrada_usuario)
    entry_usuario_registro.pack()


    #CRIANDO LABEL E ENTRY DA SENHA DA PAGINA REGISTRO
    lbl_senha_registro = tk.Label(janela_registro, text="Senha", bg="lightgrey", fg="#4682B4", font=("Comfortaa", 15))
    lbl_senha_registro.pack(pady=20)

    entry_senha_registro = tk.Entry(janela_registro, width=50, show="*", textvariable=entrada_senha)
    entry_senha_registro.pack()


    #CRIANDO O BOTAO DE REGISTRAR DA PAGINA REGISTRO
    btn_registrar_registro = tk.Button(janela_registro, text="Registrar", command=registrar_usuario, bg="white", fg="#4682B4", font=("Comfortaa", 15))
    btn_registrar_registro.pack(pady=20)


    #CRIANDO BOTAO DE VOLTAR PARA PAGINA DO LOGIN
    btn_voltar_login_registro = tk.Button(janela_registro, text="Voltar para o Login", command=voltar_tela_login, fg="green", bg="white", font=("Confortaa", 15))
    btn_voltar_login_registro.pack()

    
#CRIANDO A JANELA
janela = tk.Tk()
janela.title("Minha Window")
janela.geometry("800x600")
janela.configure(bg="lightgrey")
janela.resizable(False, False)


#CRIANDO A PALAVRA DESTAQUE DA PAGINA
plv_destaque = tk.Label(janela, text="Login", font=("Comfortaa", 30), bg="lightgrey")
plv_destaque.grid(padx=15, pady=10)
plv_destaque.place(relx=0.5, rely=0.2, anchor="center")


#CRIANDO O LABEL E O ENTRY 1
#CAMPO USUARIO
label1 = tk.Label(janela, text="Usuario", font=("Comfortaa", 15), bg="lightgrey", fg="#006400")
label1.grid(column=0, row=0)
label1.place(relx=0.5, rely=0.35, anchor="center")

entry_usuario = tk.Entry(janela, width=50, fg="red")
entry_usuario.grid(row=1, column=0, padx=15, pady=10)
entry_usuario.place(relx=0.5, rely=0.4, anchor="center")


#CRIANDO O LABEL E O ENTRY 2
#CAMPO DO USUARIO
label2 = tk.Label(janela, text="Senha", font=("Comfortaa", 15), bg="lightgrey", fg="#006400")
label2.grid(column=0, row=7)
label2.place(relx=0.5, rely=0.55, anchor="center")

entry_senha = tk.Entry(janela, width=50, show="*", fg="red")
entry_senha.grid(column=0, row=10, padx=15, pady=10)
entry_senha.place(relx=0.5, rely=0.6, anchor="center")


#CRIANDO FUNCAO PRA ALTERAR O HOVER DO BOTAO
def em_cima_botao(event):
    btn["background"] = "lightblue"

def sair_cima_botao(event):
    btn["background"] = "white"


#CRIANDO O BOTÃO PRA LOGAR
btn = tk.Button(janela, text="LOGAR", command=verificar_login, fg="#006400", bg="white", font=("Arial", 15), activebackground="#98FB98")
btn.grid(column=0, row=13, padx=15, pady=5)
btn.place(relx=0.5, rely=0.68, anchor="center")
btn.bind("<Enter>", em_cima_botao)
btn.bind("<Leave>", sair_cima_botao)


#CRIANDO BOTAO PRA REGISTRAR-SE
btn_registrar = tk.Button(janela, text="REGISTRAR-SE", command=abrir_tela_registro, bg="white", fg="#4682B4", font=("Comfortaa", 15))
btn_registrar.grid(column=0, row=15, padx=15, pady=5)
btn_registrar.place(relx=0.5, rely=0.76, anchor="center")
btn_registrar.bind("<Enter>", em_cima_botao)
btn_registrar.bind("<Leave>", sair_cima_botao)


janela.mainloop()

