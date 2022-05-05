import time
import pyautogui
import random


def follow(thefile):
    thefile.seek(0, 2)
    while True:
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
bet_win_data_red = ['red' for i in range(30)]
bet_win_data_black = ['black' for i in range(30)]
bet_win_data_zero = ['green' for i in range(2)]
bet_win_data = bet_win_data_zero + bet_win_data_red + bet_win_data_black

if __name__ == "__main__":
    while True:
        try:
            logfile = open("C:\\Users\\djako\\AppData\\Roaming\\.minecraft\\logs\\latest.log", "r")
            loglines = follow(logfile)
            for line in loglines:
                if "казино ставка" in line.lower():
                    casino_data = line.lower().split()
                    i = casino_data.index("казино")
                    bet_count = casino_data[i + 2]
                    bet_place = casino_data[i + 3]
                    bet_win = random.choice(bet_win_data)
                    i = casino_data.index("[игрок]") + 1
                    player = casino_data[i]
                    time.sleep(0.5)
                    if bet_place == bet_win and bet_place == "green":
                        pyautogui.press('t')
                        pyautogui.write(f"!Player: {player} win {int(bet_count)*5}, bet on Green!! Jackpot!! ", interval=0.01)
                        pyautogui.press('enter')
                        pyautogui.press('t')
                        pyautogui.write(
                            f"/pay {player} 0.02",
                            interval=0.01)
                        pyautogui.press('enter')
                    elif bet_place == bet_win:
                        pyautogui.press('t')
                        pyautogui.write(
                            f"!Player: {player} win {int(bet_count) * 2}, bet on {bet_place}!!",
                            interval=0.01)
                        pyautogui.press('enter')
                        pyautogui.press('t')
                        pyautogui.write(
                            f"/pay {player} 0.01",
                            interval=0.01)
                        pyautogui.press('enter')
                    else:
                        pyautogui.press('t')
                        pyautogui.write(
                            f"!{player}, try again!",
                            interval=0.01)
                        pyautogui.press('enter')
                time.sleep(1)
        except Exception:
            pass
