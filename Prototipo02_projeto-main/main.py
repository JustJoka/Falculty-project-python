import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import font
from PIL import Image, ImageTk

#validando apenas números para Quantidade
def validar_numeros(texto):
    return texto.isdigit()


#criando a janela principal
janela_principal = tk.Tk()
janela_principal.geometry("900x600")
janela_principal.title("controle_de_pedidos")
janela_principal.configure(bg="#F2F2F2")
janela_principal.resizable(False, False)

#registrando a função
vcmd = janela_principal.register(validar_numeros)

#carregando imagem
img = Image.open("images/kufc.png")
img = img.resize((80, 80))
img_tk = ImageTk.PhotoImage(img)

#exibindo a imagem
label_img = tk.Label(janela_principal, image=img_tk)
label_img.pack(pady=8)
label_img.image = img_tk


#criando label e entry do cliente
label_cliente = tk.Label(janela_principal, text="Cliente", bg="#F2F2F2", font=("Century Gothic", 12))
label_cliente.pack()

entry_cliente = tk.Entry(janela_principal, width=30, font=("Century Gothic", 10))
entry_cliente.pack(pady=5)


#criando label e combobox dos itens
label_item = tk.Label(janela_principal, text="Item", bg ="#F2F2F2", font=("Century Gothic", 12))
label_item.pack()

#criando a lista de opções dos itens
opcoes_itens = [
    "Hambúrguer com queijo e maionese",
    "Hambúrguer com queijo e BBQ",
    "Hambúrguer com salada e maionese",
    "Batata frita com cheddar e bacon",
    "Sorvete de chocolate",
    "Sorvete de baunilha",
    "Guaraná Coca-Cola",
    "Guaraná Antártica",
    "Guaraná Fanta-Uva",
]

combobox_item = ttk.Combobox(janela_principal, values= opcoes_itens,width=35, font=("Century Gothic", 10))
combobox_item.pack(pady=5)
combobox_item.set("Escolha um item")


#criando label e spinbox da quantidade
label_quantidade = tk.Label(janela_principal, text="Quantidade", bg="#F2F2F2", font=("Century Gothic", 12))
label_quantidade.pack()

spinbox_quantidade = tk.Spinbox(janela_principal, from_=1, to=100, width=28, font=("Century Gothic", 10), validate="key", validatecommand=(vcmd, "%P"))
spinbox_quantidade.pack(pady=5)


#criando label e entry para observacoes no pedido
label_observacao = tk.Label(janela_principal, text="Observações", bg="#F2F2F2", font=("Century Gothic", 12))
label_observacao.pack()

entry_observacao = tk.Text(janela_principal, height=2, width=35, font=("Century Gothic", 10))
entry_observacao.pack(pady=(0,20))



#criando um frame para os botões
frame_botoes = tk.Frame(janela_principal)
frame_botoes.pack()



#criando botoes
btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar pedido", bg="#D41C00", fg= "white", font=("Verdana", 12, "bold"))
btn_cadastrar.pack(side="left", padx=5)

btn_editar = tk.Button(frame_botoes, text="Editar pedidos", bg="#D41C00", fg="white", font=("Verdana", 12, "bold"))
btn_editar.pack(side="left", padx=5)

btn_excluir = tk.Button(frame_botoes, text="Excluir pedido", bg="red", fg="white", font=("Verdana", 12, "bold"))
btn_excluir.pack(side="left", padx=5)



#criando a lista de pedidos
tree_lista = ttk.Treeview(janela_principal, columns=("ID", "Cliente", "Item", "Quantidade", "Observação"), show="headings")

#configurando os cabeçalhos
tree_lista.heading("ID", text="ID")
tree_lista.heading("Cliente", text="Cliente")
tree_lista.heading("Item", text="Item")
tree_lista.heading("Quantidade", text="Quantidade")
tree_lista.heading("Observação", text="Observação")

#configurando as colunas
tree_lista.column("ID", width=50, stretch=False)
tree_lista.column("Cliente", width=150)
tree_lista.column("Item", width=250)
tree_lista.column("Quantidade", width=50)
tree_lista.column("Observação", width=250)

#adicionando o widget à interface
tree_lista.pack(expand=True, fill="both", pady=15)











janela_principal.mainloop()