# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

import enum


def calculates_percentage(player_votes, total_votes):
    percentage = 0

    try:
        percentage = (100*player_votes)/total_votes
        fmt_percentage = '{:.2f}'.format(percentage)
        fmt_percentage = float(fmt_percentage)
        percentage = fmt_percentage
    except (ZeroDivisionError, TypeError):
        print('Não foi possível calcular a porcentagem.')

    return percentage


def calculates_most_voted(votes_list):
    most_voted_index = 0
    bigger_amount_votes = 0

    for count, votes in enumerate(votes_list):
        if votes > bigger_amount_votes:
            bigger_amount_votes = votes
            most_voted_index = count

    return most_voted_index


players = list(range(1, 24))
votes = list()


while True:

    vote = None
    try:
        vote = int(input('Para quem vai o seu voto? '))

        if vote < 0 or vote > 23:
            print('Voto inválido. Por favor, tente novamente.')
            continue

        if vote == 0:
            print('Votação encerrada.')
            break
        # pylint: disable = bare-except
    except:
        print('Formato invalido. Por favor, tente novamente.')
        continue

    votes.append(vote)

total_votes = len(votes)

votes_per_player = list()
for player in players:
    vote_aux = votes.count(player)
    votes_per_player.append(vote_aux)

votes_percentages = list()
for vote in votes_per_player:
    percentage = calculates_percentage(vote, total_votes)
    votes_percentages.append(percentage)

most_voted_index = calculates_most_voted(votes_per_player)


print('Resultado da votação:\n')
print(f'Foram computados {total_votes} votos.\n')
print('{:<10} {:<20} {:<30}'.format('Jogador', 'Votos', '%'))

index = 0
while index < len(players):

    print('{:<10}{:<20}{:<30}'.format(
        players[index], votes_per_player[index], votes_percentages[index]))

    index += 1

if total_votes == 0:
    print('Não houveram votos. Eleição anulada.')
else:
    print(
        f'O melhor jogador foi o número {players[most_voted_index]}, com {votes_per_player[most_voted_index]} votos, correspondendo a {votes_percentages[most_voted_index]}%')
