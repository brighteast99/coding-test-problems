import math

def solution(bandage, health, attacks):
    [duration, hps, bonus] = bandage
    cur_health = health
    time = 0

    for attack in attacks:
        [attack_time, damage] = attack
        heal_streak = attack_time - time - 1
        total_heal = hps * heal_streak + math.floor(heal_streak / duration) * bonus
        cur_health = min(health, cur_health + total_heal)
        cur_health -= damage
        if cur_health <= 0:
            return -1

        time = attack_time

    return cur_health
