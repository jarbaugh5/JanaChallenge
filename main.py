import urllib
import praw

from twilio.rest import TwilioRestClient

from config.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, TWILIO_TO_NUMBER


def get_headline():
    """
    Get the headline of the top post from reddit
    :return:
    """
    r = praw.Reddit(user_agent='jana_challenge')
    page = r.get_front_page(limit=1)
    post = next(page)
    return post.title


def get_url_encoded_twiml():
    """
    Get the twiml xml file
    :return:
    """
    twiml = open('twiml.xml', 'r').read()
    twiml = twiml.format(name='Jon Arbaugh', headline=get_headline())
    twiml = urllib.parse.quote_plus(twiml)

    return twiml


def get_call_url():
    """
    Use the twimlets echo app with the result
    of get_url_encoded_twiml to create the call url
    :return:
    """
    return 'http://twimlets.com/echo?Twiml=' + get_url_encoded_twiml()


def main():
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(to=TWILIO_TO_NUMBER,
                               from_=TWILIO_FROM_NUMBER,
                               url=get_call_url())
    print(call.sid)


if __name__ == '__main__':
    main()