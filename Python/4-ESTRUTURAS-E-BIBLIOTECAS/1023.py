qnt_imoveis = 1

while qnt_imoveis != 0:
    qnt_imoveis = int(input())
    if qnt_imoveis == 0:
        continue
    
    cidade = 1
    dados = dict()
    dados_imovel = []
    soma_consumo = 0

    for _ in range(qnt_imoveis):
        moradores_imovel, consumo_imovel = map(int, input().split())

        media_consumo_imovel = consumo_imovel // moradores_imovel
        soma_consumo += media_consumo_imovel
        
        dados_imovel.append(f"{moradores_imovel}-{media_consumo_imovel}") 

    dados_ordenados = sorted(dados_imovel, key=lambda x: int(x.split("-")[0]))
    
    media_cidade = soma_consumo / qnt_imoveis

    print(f"Cidade# {cidade}:")
    print(" ".join(dados_ordenados))
    cidade += 1
