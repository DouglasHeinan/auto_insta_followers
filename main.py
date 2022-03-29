import os
from InstaFollower import InstaFollower

PASSWORD = os.environ["PASSWORD"]
EMAIL = os.environ["EMAIL"]
SIMILAR_ACCOUNT = "nytimes"


def main():

    follow_bot = InstaFollower()

    follow_bot.login(EMAIL, PASSWORD)
    follow_bot.find_followers(SIMILAR_ACCOUNT)
    follow_bot.follow()



if __name__ == '__main__':
    main()
