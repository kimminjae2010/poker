

import random

# 카드 덱 만들기
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [rank + suit for suit in suits for rank in ranks]

# 카드 족보 순위 (간단화)
hand_rankings = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10
}

def deal_hand(deck):
    random.shuffle(deck)
    return [deck.pop() for _ in range(5)]

def get_rank_value(card):
    rank = card[:-1]
    if rank == 'A':
        return 14
    elif rank == 'K':
        return 13
    elif rank == 'Q':
        return 12
    elif rank == 'J':
        return 11
    return int(rank)

def evaluate_hand(hand):
    ranks = sorted([get_rank_value(card) for card in hand])
    suits = [card[-1] for card in hand]
    unique_ranks = set(ranks)

    is_flush = len(set(suits)) == 1
    is_straight = ranks == list(range(ranks[0], ranks[0] + 5))

    from collections import Counter
    counter = Counter(ranks)
    values = sorted(counter.values(), reverse=True)

    if is_flush and ranks == [10, 11, 12, 13, 14]:
        return "Royal Flush"
    elif is_flush and is_straight:
        return "Straight Flush"
    elif values == [4, 1]:
        return "Four of a Kind"
    elif values == [3, 2]:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif values == [3, 1, 1]:
        return "Three of a Kind"
    elif values == [2, 2, 1]:
        return "Two Pair"
    elif values == [2, 1, 1, 1]:
        return "One Pair"
    else:
        return "High Card"

# 게임 시작
print("🃏 파이썬 포커 게임 - 나 vs 컴퓨터")
deck = [rank + suit for suit in suits for rank in ranks]
player_hand = deal_hand(deck)
computer_hand = deal_hand(deck)

print(f"\n당신의 카드: {player_hand}")
player_rank = evaluate_hand(player_hand)
print(f"당신의 족보: {player_rank}")

print(f"\n컴퓨터의 카드: {computer_hand}")
computer_rank = evaluate_hand(computer_hand)
print(f"컴퓨터 족보: {computer_rank}")

# 승패 판별
def get_rank_score(rank):
    return hand_rankings[rank]

if get_rank_score(player_rank) > get_rank_score(computer_rank):
    print("\n🎉 당신이 이겼습니다!")
elif get_rank_score(player_rank) < get_rank_score(computer_rank):
    print("\n😢 컴퓨터가 이겼습니다.")
else:
    print("\n🤝 무승부입니다!")
