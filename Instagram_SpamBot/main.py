import Bot_blueprint
from selenium.common.exceptions import ElementClickInterceptedException
from colorama import *


with open("User_pass.env", "r") as person_info:

    username = person_info.readline()
    password = person_info.readline()

commence = Bot_blueprint.Auto_Spam_Bot(username, password)
LOGIN_ERROR = Fore.RED + "Login failed, check internet connection " + Fore.RESET


def main():

    print(Fore.RED + " \n-->[LOGGING IN...]" + Fore.RESET)

    try:

        commence.login_with_these()

    except ElementClickInterceptedException:

        print(Fore.GREEN + "Login successful \u2713 \n" + Fore.RESET)

    except ConnectionError:

        print(LOGIN_ERROR)

    try:
        commence.say_no_to_save_info()
        commence.click_on_the_dms()
        commence.enter_first_chat_from_dms()
        commence.start_spam_procedure()

    except:
        print("\x1B[3m Unexpected error occurred \x1B[0m")


if __name__ == '__main__':
    main()
