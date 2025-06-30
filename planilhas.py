import customtkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_excel('dados_vendas.xlsx')

#dados para os filtros
produtos = ['Sem Filtro']
categoria = ['Sem Filtro']
cidade = ['Sem Filtro']
pagamento = ['Sem Filtro']
for i in dados['Produto']:
    if i not in produtos:
        produtos.append(i)
for i in dados['Categoria']:
    if i not in categoria:
        categoria.append(i)
for i in dados['Cidade']:
    if i not in cidade:
        cidade.append(i)
for i in dados['Forma_Pagamento']:
    if i not in pagamento:
        pagamento.append(i)

#exibir gráfico da porcentagem de itens vendidos 
def mostrar_graph_vendas():
    if 'Sem Filtro' in produtos:
        produtos.remove('Sem Filtro')
    size_data = 0
    sizes = []
    labels = produtos
    for item in produtos:
        for i in range(len(dados['Produto'])):
            if dados['Produto'][i] == item:
                size_data += dados['Quantidade'][i]
        sizes.append(size_data)
        size_data = 0
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Gráfico de porcentagem de vendas')
    plt.show()

#exibir gráfico da porcentagem de lucro por item
def mostrar_graph_lucro():
    if 'Sem Filtro' in produtos:
        produtos.remove('Sem Filtro')
    size_data = 0
    sizes = []
    labels = produtos
    for item in produtos:
        for i in range(len(dados['Produto'])):
            if dados['Produto'][i] == item:
                size_data += dados['Valor_Total'][i]
        sizes.append(size_data)
        size_data = 0
    fig, ax = plt.subplots()
    
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Gráfico de porcentagem de lucro bruto')
    plt.show()  

#comandos para aplicar os filtros
def exibir_dados(nome):
    textbox_dados.configure(state='normal')
    exibir = pd.read_csv('dados_vendas.csv')
    #aplicação de filtro, checa um por um
    if optionmenu_var_prod.get() != 'Sem Filtro':
        exibir = exibir[exibir['Produto'] == f'{optionmenu_var_prod.get()}'].sort_values(by="Data_Pedido")
    if optionmenu_var_cat.get() != 'Sem Filtro':
        exibir = exibir[exibir['Categoria'] == f'{optionmenu_var_cat.get()}'].sort_values(by="Data_Pedido")
    if optionmenu_var_cit.get() != 'Sem Filtro':
        exibir = exibir[exibir['Cidade'] == f'{optionmenu_var_cit.get()}'].sort_values(by="Data_Pedido")
    if optionmenu_var_pag.get() != 'Sem Filtro':
        exibir = exibir[exibir['Forma_Pagamento'] == f'{optionmenu_var_pag.get()}'].sort_values(by="Data_Pedido")
    
    #inserir texto
    textbox_dados.delete('0.0', 'end')
    if len(exibir['Produto']) == 0:
        textbox_dados.insert('0.0', 'Sem dados disponíveis')
    else:
        textbox_dados.insert('0.0',exibir)
    textbox_dados.configure(state='disabled')

    #inserir valor bruto total de venda
    entrybox_total_venda.configure(state = 'normal')
    entrybox_total_venda.delete('0','end')
    entrybox_total_venda.insert('0',f'R$:{round(sum(exibir['Valor_Total']),2)}')
    entrybox_total_venda.configure(state = 'disabled')

    #inserir quantidade total vendida
    entrybox_total_quantidade.configure(state = 'normal')
    entrybox_total_quantidade.delete('0','end')
    entrybox_total_quantidade.insert('0',f'{sum(exibir['Quantidade'])}')
    entrybox_total_quantidade.configure(state = 'disabled')

cor_frame_1 = '#333333'
cor_texto_1 = '#ffffff'
cor_button_1 = "#707070"
#-------------------------------------------------------------------------------------------------------------------
#frontend aplicativo
app = tk.CTk()
app.geometry("730x420")
app.resizable(False,False)
app.configure(weight = 100, fg_color=cor_frame_1)
app.title('Organizador de dados Aste')

#-------------------------------------------------------------------------------------------------------------------
#frame dos filtros
frame = tk.CTkFrame(master=app, width=730, height=48, fg_color = cor_frame_1, corner_radius = 0)
frame.grid(row = 0, column = 0, columnspan = 6, rowspan=2 )

#texto dos títulos dos filtro 
#texto do filtro de produto
label_prod = tk.CTkLabel(app, text="Filtro Produto", fg_color= cor_frame_1, height= 12, text_color = cor_texto_1)
label_prod.grid(row = 0, column = 0,  padx = 1, pady = 0, sticky='sw')

#texto do filtro categoria
label_prod = tk.CTkLabel(app, text="Filtro Categoria", fg_color = cor_frame_1, height= 12, text_color = cor_texto_1)
label_prod.grid(row = 0, column = 1,  padx = 1, pady = 0, sticky='sw')

#filtro do filtro cidade
label_prod = tk.CTkLabel(app, text="Filtro Cidade", fg_color = cor_frame_1, height= 12, text_color = cor_texto_1)
label_prod.grid(row = 0, column = 2,  padx = 1, pady = 0, sticky='sw')

#texto do filtro método de pagamento
label_prod = tk.CTkLabel(app, text="Filtro Pagamento", fg_color = cor_frame_1, height= 12, text_color = cor_texto_1)
label_prod.grid(row = 0, column = 3, padx = 1, pady = 0, sticky='sw')

#Filtros dos produtos, categorias, cidades e métodos de pagamento
#frame do botão
frame = tk.CTkFrame(master=app, width=730, height=30, fg_color = cor_button_1, corner_radius = 0)
frame.grid(row = 1, column = 0, columnspan = 6, rowspan=1 )

#filtro produto
optionmenu_var_prod = tk.StringVar(value="Sem Filtro")
optionmenu_prod = tk.CTkOptionMenu(app,values=produtos, command=exibir_dados, variable= optionmenu_var_prod, corner_radius = 0, fg_color = cor_button_1, height = 30)
optionmenu_prod.grid(row = 1, column = 0, padx = 1, pady = 1, sticky='w')

#filtro categoria
optionmenu_var_cat = tk.StringVar(value="Sem Filtro")
optionmenu_cat = tk.CTkOptionMenu(app,values=categoria, command=exibir_dados, variable= optionmenu_var_cat, corner_radius = 0, fg_color = cor_button_1, height = 30)
optionmenu_cat.grid(row = 1, column = 1, padx = 1, pady = 1, sticky='w')

#filtro cidade
optionmenu_var_cit = tk.StringVar(value="Sem Filtro")
optionmenu_cit = tk.CTkOptionMenu(app,values=cidade, command=exibir_dados, variable= optionmenu_var_cit, corner_radius = 0, fg_color = cor_button_1, height = 30)
optionmenu_cit.grid(row = 1, column = 2, padx = 1, pady = 1, sticky='w')

#filtro método de pagamento
optionmenu_var_pag = tk.StringVar(value="Sem Filtro")
optionmenu_pag = tk.CTkOptionMenu(app,values=pagamento, command=exibir_dados, variable= optionmenu_var_pag, corner_radius = 0, fg_color = cor_button_1, height = 30)
optionmenu_pag.grid(row = 1, column = 3, padx = 1, pady = 1, sticky='w')

#-----------------------------------------------------------------------------------------------------------------
#caixa de texto para exibição de dados
textbox_dados = tk.CTkTextbox(app, width=730, height= 300, state='disabled', corner_radius = 0)
textbox_dados.grid (row = 2, column = 0, columnspan = 6)

#caixa de exibição para valores totais de venda
#total de valor bruto vendido
label_venda = tk.CTkLabel(app, text="Total de Vendas: ", fg_color = cor_frame_1, height= 12, text_color = cor_texto_1)
label_venda.grid(row = 3, column = 0,  padx = 1, pady = 1, sticky='w')

entrybox_total_venda = tk.CTkEntry(app, width=150, height= 12, state='disabled')
entrybox_total_venda.grid(row = 3, column = 1, padx = 1, pady = 1, sticky='w')

#total de quantidade vendida
label_prod = tk.CTkLabel(app, text="Quantidade Vendida: ", fg_color = cor_frame_1, height= 12, text_color = cor_texto_1)
label_prod.grid(row = 3, column = 2,  padx = 1, pady = 1, sticky='w', columnspan = 2)

entrybox_total_quantidade = tk.CTkEntry(app, width=150, height= 12, state='disabled')
entrybox_total_quantidade.grid(row = 3, column = 3, padx = 1, pady = 1, sticky='w')

#-----------------------------------------------------------------------------------------------------------------
#botão para exibir o gráfico das vendas
button_graph = tk.CTkButton(app, text = 'Gráfico de vendas', command = mostrar_graph_vendas)
button_graph.grid(row = 4, column = 0, sticky='w', padx = 1, pady = 1)

#botão para exibir o gráfico dos lucros
button_graph = tk.CTkButton(app, text = 'Gráfico de Lucro', command = mostrar_graph_lucro)
button_graph.grid(row = 4, column = 1, sticky='w', padx = 1, pady = 1)


app.mainloop()