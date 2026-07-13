import pickle
from tkinter import filedialog, messagebox
from dataclasses import dataclass

from model.figuras import Figuras
from view.desenho import Desenho


@dataclass
class Arquivos:
    figuras: Figuras
    desenho: Desenho

    def salvar(self):
            file_path = filedialog.asksaveasfilename(
                defaultextension=".pickle",
                filetypes=[("Arquivos Pickle", "*.pickle"),
                        ("Todos os arquivos", "*.*")],
                title="Escolha onde salvar seus dados",
            )

            if file_path:
                try:
                    with open(file_path, "wb") as arquivo:
                        pickle.dump(self.figuras.acessar, arquivo)
                    messagebox.showinfo(
                        "Sucesso", "Todos os seus dados foram salvos com sucesso!")
                except Exception as e:
                    messagebox.showerror(
                        "Erro", f"Não foi possível salvar: \n{e}")

    def abrir(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos Pickle", "*.pickle"),
                       ("Todos os arquivos", "*.*")],
            title="Selecione o arquivo para carregar",
        )

        if file_path:
            try:
                with open(file_path, "rb") as arquivo:
                    loaded_data = pickle.load(arquivo)

                    for figura in loaded_data:
                        self.desenho.desenhar_figura(figura)

                messagebox.showinfo(
                    "Dados carregados", "Os seus dados foram importados com sucesso na sua área de trabalho."
                )
            except Exception as e:
                print(e)