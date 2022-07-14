pessoas = {'nome': 'Taigo', 'sexo': 'M','idade': 22}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k}={v}')