from itertools import product


def solution(users, emoticons):
    answer = [0, 0]

    for discount_rates in product([10, 20, 30, 40], repeat=len(emoticons)):
        new_subscribers, sales = 0, 0
        for [criteria, price_cap] in users:
            total_price = 0
            for [price, discount_rate] in zip(emoticons, discount_rates):
                if discount_rate >= criteria:
                    total_price += price * (100 - discount_rate) / 100

            sales += total_price if total_price < price_cap else 0
            new_subscribers += int(total_price >= price_cap)

        if new_subscribers > answer[0] or (new_subscribers == answer[0] and sales > answer[1]):
            answer = [new_subscribers, sales]

    return answer
