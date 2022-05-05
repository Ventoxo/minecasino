import time
import pyautogui
import random


def follow(thefile):
    thefile.seek(0, 2)
    timer = 0
    min3 = 1542857143
    while True:
        timer += 1
        if timer == 1800000:
            hey()
            timer = 0
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


'''
red
black
green
'''
bet_win_data_red = ['carrot' for _ in range(1)]
bet_win_data_black = ['potato' for _ in range(30)]
bet_win_data_zero = ['cactus' for _ in range(2)]
bet_win_data = bet_win_data_zero + bet_win_data_red + bet_win_data_black


def pay(player_name, bet_sum, coef=1.5):
    pyautogui.press('t')
    pyautogui.write(f"Player: {player_name} win {bet_sum * coef}! ", interval=0.01)
    if coef == 8:
        change_lang()
        change_lang()
        pyautogui.write(f"Gjcnfdbk yf rfrnec b dsquhfk l;trgjn!!", interval=0.01)
        change_lang()
    pyautogui.press('enter')

    pyautogui.press('t')
    pyautogui.write(
        f"/pay {player_name} {bet_sum * coef}",
        interval=0.01)
    pyautogui.press('enter')


def change_lang():
    pyautogui.keyDown('alt')
    pyautogui.press('shift')
    pyautogui.keyUp('alt')


def ah_sell(veg, cost):
    if veg == 'carrot':
        pyautogui.press('1')
    elif veg == 'potato':
        pyautogui.press('2')
    else:
        pyautogui.press('3')
    pyautogui.press('t')
    pyautogui.write(
        f"/ah sell {cost} 1",
        interval=0.01)
    pyautogui.press('enter')
    pyautogui.keyDown('space')
    time.sleep(1)
    pyautogui.keyUp('space')


def hey():
    pyautogui.write(f"Yf cthdtht hf,jnftn jykfqy-rfpbyj/ Lkz 'njuj regbnt yf ferwbjyt rfhnjire? vjhrjdm bkb rfrnec/,",
                    interval=0.02)
    time.sleep(1)
    pyautogui.write(
        f"rfrnec - l;trgjn (cnfdrf*8), vjhrjdm b rfhnjirf (cnfdrf*1.75)? yj b ifyc dsquhfnm ,jkmit/ Hbcreq b gj,t;lfq!",
        interval=0.02)


if __name__ == "__main__":
    while True:
        logfile = open("C:\\Users\\djako\\AppData\\Roaming\\.minecraft\\logs\\latest.log", "r")
        loglines = follow(logfile)
        for line in loglines:
            if "§r §fpurchased your auction of §" in line:
                line_data = line.lower().split('§')
                if "[игрок]" in line_data[0]:
                    print("Vjityybr!")
                else:
                    bet = 1
                    player_name = line_data[1][1::]
                    continue
            if "§fYou earned §b$" in line and bet == 1:
                bet_sum = int(line.lower().split('§')[-4].split('.')[0][2:])
                player_bet = str(line_data[-2][1::])
                random_bet = str(random.choice(bet_win_data))
                time.sleep(3)
                if player_bet == random_bet and random_bet == 'cactus':
                    pay(player_name, bet_sum, 8)
                elif player_bet == random_bet:
                    pay(player_name, bet_sum)
                else:
                    pass
                    pyautogui.press('t')
                    pyautogui.write(f"/m {player_name}",
                                    interval=0.02)
                    change_lang()
                    change_lang()
                    pyautogui.write(f" yt gjdtpkj? dfif cnfdrf - ",
                                    interval=0.02)
                    change_lang()
                    pyautogui.write(f"{player_bet},",
                                    interval=0.02)
                    change_lang()
                    change_lang()
                    pyautogui.write(f" f gj,tlbk - ",
                                    interval=0.02)
                    change_lang()
                    pyautogui.write(f"{random_bet},",
                                    interval=0.02)
                    change_lang()
                    change_lang()
                    pyautogui.write(f" gjghj,eqnt cyjdf/ ds j,zpfntkmyj dsquhftnt",
                                    interval=0.02)
                    pyautogui.press('enter')
                    change_lang()
                bet = 0
                ah_sell(player_bet, bet_sum)

