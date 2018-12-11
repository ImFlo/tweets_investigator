from twarc import Twarc
import tqdm
from datetime import datetime, timedelta

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

already_checked = []
pbar = tqdm.tqdm(desc='tweet analysed', unit='tweets')


def isSuspicious(user):
    created = datetime.strptime(user['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    now = datetime.now() - timedelta(days=90)
    if created > now:
        tqdm.tqdm.write("[!] Suspicious: "
                        "@{} ({}), created : {}".format(user["screen_name"], user["id"], created.strftime("%d/%m/%Y")))

if __name__ == "__main__":
    t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

    for tweet in t.filter(track="Strasbourg"):
        user = tweet["user"]
        if user["id"] not in already_checked:
            isSuspicious(user)
            already_checked.append(user["id"])
        pbar.update(1)