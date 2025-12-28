import pandas as pd

df = pd.read_csv('aprovados.csv', sep=';', skipinitialspace=True) 

def gerar_messagem(linha):
    nome = linha['NOME']
    resultado = linha['CLASSIFICAÇÃO']

    if resultado == 'Aprovado Classificado':
        return f'Olá {nome}, você foi aprovado e logo entraremos em contato contigo para finalizar sua matrícula. Parabéns'
    elif resultado== 'Aprovado Cadastro de Reserva':
        return f'Olá {nome}, você foi aprovado no cadatastro reserva, mas não perca as esperanças, em caso de desistência ou eliminação de possíveis aprovados podemos te chamar. Desde já, agradecemos pelo seu comprometimento.'
    else:
        return f'Agradecemos mas não foi dessa vez'
   

df['Resposta'] = df.apply(gerar_messagem, axis=1)

df.to_csv('resultado_final.csv', index= False)