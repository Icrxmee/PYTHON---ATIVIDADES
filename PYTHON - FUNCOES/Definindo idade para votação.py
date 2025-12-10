from datetime import datetime 

def voto(a): 

    ano_atual = datetime.now().year # Puxando o ano atual 
    idade = ano_atual - a # Calculando a idade do usuário
    
    if idade >= 18: 
        return f'Com {idade} anos: VOTO OBRIGATÓRIO' # A formatação pode ficar solta.

    if idade < 18 and idade >= 16:
        return  f"Com {idade} anos: VOTO OPICIONAL"

    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    
    
ano = int (input("Digite qual ano você nasceu: "))
print(voto(ano)) # Não precisa armazenar o return em uma variável, ele poder ser puxado diretamente pro print.