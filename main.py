import ptbot
import os
from pytimeparse import parse

def notify():
    bot.send_message(my_id, 'Time is over')

def notify_progress(secs_left, message_id, total):
    bot.update_message(my_id, message_id, 
        "The timer stated on {} seconds\n".format(secs_left) +
        render_progressbar(total, iteration=secs_left))

def render_progressbar(total, iteration, prefix='', suffix='Complete', length=15, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def reply(text):
    message_id = bot.send_message\
        (my_id, "The timer stated on {} seconds!\n".format(parse(text)))
    bot.create_timer(parse(text), notify)
    bot.create_countdown(parse(text), notify_progress,
                         message_id=message_id, total=parse(text))

if __name__=='__main__':
    token = os.getenv('TOKEN_TG_COUNTER')
    my_id = os.getenv('MY_TG_ID')
    bot = ptbot.Bot(token)
    bot.send_message(my_id, 'Bot is running!\nHow much to start the timer?')
    bot.reply_on_message(reply)
    bot.run_bot()
