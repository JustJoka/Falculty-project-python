import tkinter as tk
from tkinter import messagebox
import sqlite3

#CRIANDO PAGINA DE LOGIN

def criar_banco():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   usuario TEXT UNIQUE NOT NULL,
                   senha TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

criar_banco()


def verificar_login():
    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    if not usuario or not senha:
        messagebox.showwarning("Erro ao logar!", "Todos os campos são obrigatórios!")
        return
    
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE usuario = ?",(usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and resultado[0] == senha:
        messagebox.showinfo("Logado!", "Logado com sucesso!")
    else:
        messagebox.showerror("Erro ao logar!", "Usuário ou senha incorretos!")


def abrir_tela_registro():
    janela.withdraw() #PARA ESCONDER A JANELA DE LOGIN
    janela_registro = tk.Toplevel()#CRIA UMA JANELA INDEPENDENTE NO PROGRAMA
    janela_registro.title("Registro")
    janela_registro.geometry("800x600")
    janela_registro.configure(bg="#1E90FF")

    entrada_usuario = tk.StringVar()
    entrada_senha = tk.StringVar()

    def registrar_usuario():
        usuario = entrada_usuario.get().strip()
        senha = entrada_senha.get().strip()

        if not usuario or not senha:
            messagebox.showwarning("Erro ao registrar!", "Todos os campos são obrigatórios")
            return
        
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
            conn.commit()
            messagebox.showinfo("Registrado!", "Registrado com sucesso!")
            janela_registro.destroy()
            janela.deiconify()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro ao registrar!", "Usuário já existe!")
        finally:
            conn.close()

    #TITULO DA PAGINA REGISTRO
    lbl_titulo = tk.Label(janela_registro, text="Registrar-se", bg="#1E90FF", fg="black", font=("Comfortaa", 30))
    lbl_titulo.pack(pady=50)


    #CRIANDO LABEL E ENTRY DO USUARIO DA PAGINA REGISTRO
    lbl_usuario_registro = tk.Label(janela_registro, text="Usuário", bg="#1E90FF", fg="#000080", font=("Comfortaa", 15))
    lbl_usuario_registro.pack(pady=20)
    entry_usuario_registro = tk.Entry(janela_registro, width=50, textvariable=entrada_usuario, fg="#32CD32")
    entry_usuario_registro.pack()


    #CRIANDO LABEL E ENTRY DA SENHA DA PAGINA REGISTRO
    lbl_senha_registro = tk.Label(janela_registro, text="Senha", bg="#1E90FF", fg="#000080", font=("Comfortaa", 15))
    lbl_senha_registro.pack(pady=20)

    entry_senha_registro = tk.Entry(janela_registro, width=50, show="*", textvariable=entrada_senha, fg="#32CD32")
    entry_senha_registro.pack()


    #CRIANDO O BOTAO DE REGISTRAR DA PAGINA REGISTRO
    btn_registrar_registro = tk.Button(janela_registro, text="Registrar", command=registrar_usuario, bg="white", fg="#006400", font=("Comfortaa", 15))
    btn_registrar_registro.pack(pady=20)
    btn_registrar_registro.bind("<Enter>", em_cima_botao)
    btn_registrar_registro.bind("<Leave>", sair_cima_botao)



#CRIANDO FUNCAO PRA ALTERAR O HOVER DO BOTAO
def em_cima_botao(event):
    event.widget["background"] = "#4169E1"

def sair_cima_botao(event):
    event.widget["background"] = "white"


    
#CRIANDO A JANELA
janela = tk.Tk()
janela.title("Minha Window")
janela.geometry("800x600")
janela.configure(bg="#98FB98")
janela.resizable(False, False)


#CRIANDO A PALAVRA DESTAQUE DA PAGINA
plv_destaque = tk.Label(janela, text="Login", font=("Comfortaa", 30), bg="#98FB98")
plv_destaque.grid(padx=15, pady=10)
plv_destaque.place(relx=0.5, rely=0.2, anchor="center")


#CRIANDO O LABEL E O ENTRY 1
#CAMPO USUARIO
label1 = tk.Label(janela, text="Usuario", font=("Comfortaa", 15), bg="#98FB98", fg="#006400")
label1.grid(column=0, row=0)
label1.place(relx=0.5, rely=0.35, anchor="center")

entry_usuario = tk.Entry(janela, width=50, fg="#191970")
entry_usuario.grid(row=1, column=0, padx=15, pady=10)
entry_usuario.place(relx=0.5, rely=0.4, anchor="center")


#CRIANDO O LABEL E O ENTRY 2
#CAMPO DO USUARIO
label2 = tk.Label(janela, text="Senha", font=("Comfortaa", 15), bg="#98FB98", fg="#006400")
label2.grid(column=0, row=7)
label2.place(relx=0.5, rely=0.55, anchor="center")

entry_senha = tk.Entry(janela, width=50, show="*", fg="#191970")
entry_senha.grid(column=0, row=10, padx=15, pady=10)
entry_senha.place(relx=0.5, rely=0.6, anchor="center")


#CRIANDO FUNCAO PRA ALTERAR O HOVER DO BOTAO
def em_cima_botao(event):
    event.widget["background"] = "lightblue"

def sair_cima_botao(event):
    event.widget["background"] = "white"


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

