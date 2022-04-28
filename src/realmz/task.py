import schedule
import time
from factory                                    import GetInput
from settings                                   import Settings


# Gets settings and kwargs it with crontab
SETTINGS = Settings(crontab='Y')
SETTINGS.get_settings()


def get_input(selection):
    """
    Accepts the selection to schedule run the App as if called from main.py
    :param selection:
    :return:
    """
    GetInput(selection, crontab='Y').get_input_redirect()
    return

schedule.every().day.at("09:00").do(get_input, selection='1')
schedule.every().day.at("09:02").do(get_input, selection='2')

while True:
    schedule.run_pending()
    time.sleep(1)
