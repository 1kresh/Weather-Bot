from bot import bot


def report_error(e, other_info = ""):
    try:
        bot.send_message(450398500, f"Error:\n{e}")   
    except Exception as e:
        print(e)

