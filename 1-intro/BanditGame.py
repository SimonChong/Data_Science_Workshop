# -*- coding: utf-8 -*-
import sys
import random
import math

welcome_message = """
✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ 
$                                                                                   $
$                        Welcome to the BANDIT GAME!                                $ 
$                                                                                   $
$  Because you look so cute, we decide to give you $100 to start the game.          $
$  The bandit has 5 arms. Each arm has different (but fixed) odds and win ratio.    $ 
$  Choose one arm and put your luck there. Each play will cost you just $1.         $
$  You win the game when your money exceed $200, or lose it when you have no money. $
$  Have fun!                                                                        $ 
$                                                                                   $
✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ ✫ 

As promised, we added $100 into your account. Your current balance: $100
"""

money = 100
setting = [[0.26, 2.5], [0.6, 0.5], [0.4, 1], [0.05, 27], [0.8, 0.2]]

class BanditGame(object):
    def __init__(self):
        global setting, money, welcome_message
        random.seed()
        self._setting = random.shuffle(setting)
        self._size = len(setting)
        self._money = money
        self._celling = 200
        print(welcome_message)

    def arm_num(self):
        return self._size

    def money(self):
        return self._money

    def celling(self):
        return self._celling

    def _money_check(self):
        if self._money <= 0 or self._money > self._celling:
            return False
        return True

    def play(self, arm):
        if not self._money_check():
            exit()
        if arm in range(1, self._size+1):
            print("You pulled arm {0}".format(arm))
            value = random.random()
            win = True if value < setting[arm-1][0] else False
            gain = setting[arm-1][1] if win else -1
            self._money += gain
            if win:
                print("Contratulations! You win ${0}. Your current balence: {1}\n".format(gain, self._money))
            else:
                print("Oops You lose... Your current balence: {}\n".format(self._money))
            if self._money <= 0:
                print("GAME OVER! You lost all your money...")
            if self._money > self._celling:
                print("Congratulations! You earned too much money. OMG! \nThe Casino has finally gone bankrupt. \nGAME OVER...")
            return True, gain, self._money
        else:
            print('Kidding me??? There is no arm {0} exists.\n'.format(arm))
            return False, 0, self._money

    def continuous_play(self):
        while True:
            arm = raw_input("Which arm do you like to pull (1-{0} to choose an arm, or exit with 0)?".format(self._size))
            if arm.strip() == '0':
                print('Thanks for playing. See you next time ~')
                break
            try:
                arm = int(arm.strip())
            except:
                print('Kidding me??? There is no arm {} exists.\n'.format(arm))
                continue
            self.play(arm)


def main():
    bandit = BanditGame()
    # bandit.continuous_play()
    cash = 100
    count = 1
    arm = 1
    model = [
        {'wins': 0, 'losses': 0, 'payout': 0},
        {'wins': 0, 'losses': 0, 'payout': 0},
        {'wins': 0, 'losses': 0, 'payout': 0},
        {'wins': 0, 'losses': 0, 'payout': 0},
        {'wins': 0, 'losses': 0, 'payout': 0}
    ]

    def odds(item):
        runs = (item['wins'] + item['losses'])
        if(runs > 0):
            ratio = item['wins'] / float(runs) * item['payout']
        else:
            ratio = 0
        return ratio

    def largest():
        temp_large = -1, 0
        for i in range(5):
            current_odds = odds(model[i])
            if(current_odds > temp_large[1]):
                temp_large = i, current_odds
        return temp_large[0] + 1

    def debug():
        for i in range(5):
            print(i+1, odds(model[i])*100, model[i]['payout'], model[i]['wins'], model[i]['losses'])

    def run(arm):
        working, won_ammount, cash = bandit.play(arm)
        # print(working, won_ammount, cash)
        if won_ammount > 0:
            model[arm - 1]['wins'] += 1
            model[arm - 1]['payout'] = won_ammount
        else:
            model[arm - 1]['losses'] += 1


    while True:
        print(count)
        run(arm)
        debug()
        if largest() == arm:
            for z in range(int(math.pow(2, (count / 80)))):
                run(arm)
        count += 1
        arm = count % 5 + 1
        # print(model)

    while True:
        print(count)
        bandit.play(largest[0]+1)
        count += 1


if __name__ == '__main__':
    main()