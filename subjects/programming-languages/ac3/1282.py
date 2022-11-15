curated_channels_list = []
channel_number = int(input())
counter = 0

# Criação da classe do canal
class Channel:
    def __init__(self):
        self.nome = None
        self.inscritos = None
        self.monetizacao = None
        self.conteudo_premium = None
        self.bonus = None
        self.conteudo_value = None
    # Criando a função de calcular o bônus
    def calculate_bonus(self):
        if int(self.inscritos) >= 1000:
            bonus = self.bonus = float(self.monetizacao) + int((int(self.inscritos) / 1000)) * self.conteudo_value
            return bonus
        else:
            bonus = self.bonus = float(self.monetizacao)
            return bonus

# Pegando a entrada do usuário enquanto a variável acumuladora não é maior que a quantidade de canais definida
while counter < channel_number:
    channel = input()
    # Criando a instância do canal
    curated_channel = Channel()
    curated_channel.nome = channel.split(';')[0]
    curated_channel.inscritos = channel.split(';')[1]
    curated_channel.monetizacao = channel.split(';')[2]
    curated_channel.conteudo_premium = channel.split(';')[3]
    curated_channels_list.append(curated_channel)
    # Aumentando a variável acumuladora em 1
    counter += 1

# Pegando os valores da bonificação
valuePremium = float(input())
valueNonPremium = float(input())

# Definindo os valores de bonificação pra cada canal de acordo com o conteúdo
for x in curated_channels_list:
    if x.conteudo_premium == 'sim':
        x.conteudo_value = valuePremium
    else:
        x.conteudo_value = valueNonPremium


print('-----\n'
      'BÔNUS\n'
      '-----')

# Printando o nome e o bônus de cada canal que temos na lista
for x in curated_channels_list:
    print(f'{x.nome}: R$ {x.calculate_bonus():.2f}')

