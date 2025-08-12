from django import forms
import json

class PesquisaForm(forms.Form):

    def __init__(self, *args, pesquisa=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        if pesquisa:
            if isinstance(pesquisa, str):
                pesquisa = json.loads(pesquisa)
            for i, pergunta in enumerate(pesquisa):
                print(pergunta)
                pergunta_num = f"pergunta {i}"
                if pergunta["tipo"] == "multipla_escolha":
                    self.fields[pergunta_num] = forms.ChoiceField(
                        label=pergunta["pergunta"],
                        choices=[(opcao, opcao) for opcao in pergunta["opcoes"]]
                    )
                    
                elif pergunta["tipo"] == "texto":
                    self.fields[pergunta_num] = forms.CharField(label=pergunta["pergunta"])
                
                elif pergunta["tipo"] == "numero":
                    self.fields[pergunta_num] = forms.IntegerField(label=pergunta["pergunta"])
                    
                elif pergunta["tipo"] == "checkbox":
                    self.fields[pergunta_num] = forms.BooleanField(label=pergunta["pergunta"])
                else:
                    self.fields[pergunta_num] = forms.CharField(
                        label=pergunta["pergunta"]
                    )
        