import tweepy
import qrcode
import os
from tweepy import OAuthHandler
from uuid import uuid4
from base64 import b64decode

consumer_key    = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token    = os.environ['TWITTER_ACCESS_TOKEN']
access_secret   = os.environ['TWITTER_ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def handle(event, context):
    payload = str(uuid4())
    qr_file = "/tmp/%s.jpg" % (payload)

    qr = qrcode.QRCode(version=None,
                       error_correction=qrcode.constants.ERROR_CORRECT_M,
                       box_size=20,
                       border=1)

    qr.add_data(payload)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(qr_file)

    api.update_with_media(qr_file)
    print(payload)
