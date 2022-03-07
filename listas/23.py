# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

def byte_to_megabyte(bytes):
    return bytes/(1024*1024)


def disc_usage_percentage(user_usage, disc_space):
    return (100*user_usage)/disc_space


usuarios = list()
uso_disco = list()

try:
    usuarios_file = open('listas/usuarios.txt')

    usuario = ''
    espaco_ocupado = ''
    for line in usuarios_file:
        usuario = line[:15]
        usuario = usuario.strip()
        usuarios.append(usuario)

        espaco_ocupado = line[16:]
        espaco_ocupado = espaco_ocupado.strip()
        espaco_ocupado = float(espaco_ocupado)
        uso_disco.append(espaco_ocupado)
except FileNotFoundError:
    print('Arquivo não encontrado.')

uso_disco_mb = list()
k = 0
while k < len(uso_disco):
    aux = uso_disco[k]
    aux = byte_to_megabyte(aux)
    uso_disco_mb.append(aux)
    k += 1

total_disc_usage = 0
if len(usuarios) > 0:
    total_disc_usage = sum(uso_disco)
total_disc_usage_mb = byte_to_megabyte(total_disc_usage)

print()
print('ACME Inc.               Uso do espaço em disco pelos usuários')
print('------------------------------------------------------------------------')
print()
print('{:<5} {:<15} {:<20} {:<20}'.format(
    'Nr.', 'Usuário', 'Espaço utilizado', '% do uso'))

for count, usuario in enumerate(usuarios, start=1):
    user_disc_usage = byte_to_megabyte(uso_disco[count-1])

    percentage_usage = disc_usage_percentage(
        user_disc_usage, total_disc_usage_mb)
    print('{:<5} {:<15} {:<20} {:<20}'.format(count, usuario, '{:.2f}'.format(
        uso_disco_mb[count-1]), '{:.2f}'.format(percentage_usage)))
