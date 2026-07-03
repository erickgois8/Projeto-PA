from classes.menu import Menu

# Criação da janela (interface) já configurada
janela = Menu()

# Deixando o menu interativo
janela.canva.bind('<ButtonPress-1>', janela.iniciar_figura_nova)
janela.canva.bind('<B1-Motion>', janela.atualizar_figura_nova)
janela.canva.bind('<ButtonRelease-1>', janela.incluir_figura_nova)

# Loop principal
janela.root.mainloop()