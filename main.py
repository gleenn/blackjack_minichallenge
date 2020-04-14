from typing import List

MAX_SUM_BEFORE_LOSS = 31


def print_model(model):
    # print(model)
    for j in range(len(model)):
        for i in range(len(model[0])):
            print("%s\t" % model[j][i], end='')
        print()


def make_model(player_sum, deal_card_val, player_aces):
    table: List[List[int]] = [[0 for i in range(MAX_SUM_BEFORE_LOSS)] for j in range(MAX_SUM_BEFORE_LOSS)]
    for i in range(player_sum, MAX_SUM_BEFORE_LOSS):
        for j in range(deal_card_val, MAX_SUM_BEFORE_LOSS):
            for card in range(2, 11):
                if card is 10:
                    probability = 4
                else:
                    probability = 1
                new_i = i
                new_j = j
                while new_i + card < MAX_SUM_BEFORE_LOSS:
                    table[j][new_i + card] += probability
                    new_i += card
                while new_j + card < MAX_SUM_BEFORE_LOSS:
                    table[new_j + card][i] += probability
                    new_j += card
    return table


def should_hit(10, 2, 0):



print_model(make_model(10, 2, 0))
