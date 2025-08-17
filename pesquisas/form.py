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
                pergunta_num = pergunta["pergunta"]
                if pergunta["tipo"] == "multipla_escolha":
                    self.fields[pergunta_num] = forms.ChoiceField(
                        label=pergunta["pergunta"],
                        choices=[(opcao, opcao) for opcao in pergunta["opcoes"]]
                    )
                    
                elif pergunta["tipo"] == "texto":
                    self.fields[pergunta_num] = forms.CharField(
                        label=pergunta["pergunta"], 
                        widget=forms.TextInput(attrs={"placeholder": "Digite aqui."}))
                    
                elif pergunta["tipo"] == "numero":
                    self.fields[pergunta_num] = forms.IntegerField(
                        label=pergunta["pergunta"], 
                        help_text="Digite somente números inteiros.", 
                        widget=forms.NumberInput(attrs={"placeholder": "Digite aqui.", "min":0, "max":100}))
                    
                elif pergunta["tipo"] == "radio":
                    self.fields[pergunta_num] = forms.ChoiceField(
                        label=pergunta["pergunta"], 
                        choices=[(opcao, opcao) for opcao in pergunta["opcoes"]],
                        help_text="Você pode marcar mais de um.",
                        widget=forms.CheckboxSelectMultiple)
                    
                elif pergunta["tipo"] == "checkbox":
                    self.fields[pergunta_num] = forms.ChoiceField(
                        label=pergunta["pergunta"],
                        choices=[("sim", "Sim"), ("não", "Não")],
                        widget=forms.RadioSelect
                    )
                else:
                    self.fields[pergunta_num] = forms.CharField(
                        label=pergunta["pergunta"]
                    )
        