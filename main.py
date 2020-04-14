from typing import List

MAX_SUM_BEFORE_LOSS = 31


def print_model(model):
    # print(model)
    for j in range(len(model)):
        for i in range(len(model[0])):
            print("%s\t" % model[j][i], end='')
        print()


def update_model(model, player_sum, dealer_sum, deck):
    print("player: %d, dealer: %d" % (player_sum, dealer_sum))
    try:
        card = next(iter(deck))
    except StopIteration:
        return
    card_count = deck[card]
    if card_count is 1:
        del deck[card]
    else:
        deck[card] -= 1

    if dealer_sum + card < MAX_SUM_BEFORE_LOSS and player_sum < MAX_SUM_BEFORE_LOSS:
        model[dealer_sum + card][player_sum] += 1
        update_model(model, player_sum + card, dealer_sum, deck)

    if player_sum + card < MAX_SUM_BEFORE_LOSS and dealer_sum < MAX_SUM_BEFORE_LOSS:
        model[dealer_sum][player_sum + card] += 1
        update_model(model, player_sum, dealer_sum + card, deck)


def make_model(player_sum, deal_card_val, player_aces):
    model: List[List[int]] = [[0 for i in range(MAX_SUM_BEFORE_LOSS)] for j in range(MAX_SUM_BEFORE_LOSS)]
    if deal_card_val is 11:
        dealer_aces = 1
    else:
        dealer_aces = 0
    # deck = {"1": 4 - player_aces - dealer_aces, "2": 4, "3": 4, "4": 4, "5": 4, "6": 4, "7": 4, "8": 4, "9": 4,
    # "10": 16}
    deck = {1: 4 - player_aces - dealer_aces, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}
    update_model(model, player_sum, deal_card_val, deck)
    return model


def should_hit(player_sum, deal_card_val, player_aces):
    model = make_model(player_sum, deal_card_val, player_aces)
    print_model(model)

print_model(make_model(0, 0, 0))
