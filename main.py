import threading

from telegram_bot import bot
from GeneralManager.GeneralManager import GeneralManager


def main():
    manager = GeneralManager('resources/')
    t = threading.Thread(target=bot.polling)
    t.start()
    c = threading.Thread(target=manager.start)
    c.start()


if __name__ == "__main__":
    main()
