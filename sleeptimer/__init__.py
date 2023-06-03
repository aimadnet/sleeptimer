#        .__                        __  .__                      
#   _____|  |   ____   ____ _______/  |_|__| _____   ___________ 
#  /  ___/  | _/ __ \_/ __ \\____ \   __\  |/     \_/ __ \_  __ \
#  \___ \|  |_\  ___/\  ___/|  |_> >  | |  |  Y Y  \  ___/|  | \/
# /____  >____/\___  >\___  >   __/|__| |__|__|_|  /\___  >__|   
#      \/          \/     \/|__|                 \/     \/       
#            by t.me/aimadnet - contact@aimadnet.com

import datetime
import sys
import time
import termios
import tty

def enable_input_blocking():
    tty.setcbreak(sys.stdin.fileno())

def disable_input_blocking():
    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, termios.tcgetattr(sys.stdin))

def sleep(seconds, title="😴 Sleep", message="Time remaining: ", show_progress_bar=True):
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(seconds=seconds)

    previous_line_length = 0

    enable_input_blocking()

    while datetime.datetime.now() < end_time:
        remaining_time = (end_time - datetime.datetime.now()).total_seconds()
        remaining_ms = int(remaining_time * 1000)

        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
        progress = elapsed_time / seconds
        progress_percent = int(progress * 100)

        bar_length = 20
        filled_length = int(progress * bar_length)
        if progress_percent == 100:
            filled_length = bar_length
        bar = '\033[93m' + '█' * filled_length + '\033[0m' + '-' * (bar_length - filled_length)

        sys.stdout.write('\r' + ' ' * previous_line_length)

        line = ""
        if title and title != "":
            line += "\033[96m[" + title + "]\033[0m "

        if message and message != "":
            line += message

        line += "\033[93m{} ms\033[0m".format(remaining_ms)

        if show_progress_bar:
            line += " [{}] {}%".format(bar, progress_percent)

        sys.stdout.write('\r' + line)
        sys.stdout.flush()
        previous_line_length = len(line)

        time.sleep(0.1)

    sys.stdout.write('\r' + ' ' * previous_line_length)
    sys.stdout.write('\r')
    sys.stdout.flush()

    disable_input_blocking()

