import urllib
import praw

from twilio.rest import TwilioRestClient

from config.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER


def get_headline():
    r = praw.Reddit(user_agent='jana_challenge')
    page = r.get_front_page(limit=1)
    post = next(page)
    return post.title

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

twiml = open('twiml.xml', 'r').read()

twiml = twiml.format(name='Jon Arbaugh', headline=get_headline())

# maybe not with the plus part, takes up a lot of space with white-space-plus-signs
twiml = urllib.parse.quote_plus(twiml)

print(twiml)

call = client.calls.create(to='+14438789292',
                           from_=TWILIO_FROM_NUMBER,
                           url='http://twimlets.com/echo?Twiml=' + twiml)

print(call.sid)