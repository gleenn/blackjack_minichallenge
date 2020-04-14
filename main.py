from typing import List

MAX_SUM_BEFORE_LOSS = 31
card_counts = {1: 4,
               2: 4,
               3: 4,
               4: 4,
               5: 4,
               6: 4,
               7: 4,
               8: 4,
               9: 4,
               10: 16,
               11: 4}


def print_model(model):
    # print(model)
    for j in range(len(model)):
        for i in range(len(model[0])):
            print("%s\t" % model[j][i], end='')
        print()


def make_model(player_sum, deal_card_val, player_aces):
    table: List[List[int]] = [[0 for i in range(MAX_SUM_BEFORE_LOSS)] for j in range(MAX_SUM_BEFORE_LOSS)]
    for i in range(player_sum - (player_aces * 10), MAX_SUM_BEFORE_LOSS):
        for j in range(deal_card_val, MAX_SUM_BEFORE_LOSS):
            for card in card_counts.keys():
                for num_of_card in range(1, card_counts[card] + 1):
                    # if card is 1 or card is 11:
                    #     num_of_card = num_of_card - player_aces
                    # Player takes card
                    if (num_of_card * card) + i < MAX_SUM_BEFORE_LOSS:
                        table[j][(num_of_card * card) + i] += 1
                    # Dealer takes card
                    if (num_of_card * card) + j < MAX_SUM_BEFORE_LOSS:
                        table[(num_of_card * card) + j][i] += 1
    return table


print_model(make_model(10, 2, 0))
