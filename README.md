Jana Coding Challenge
===

Jon Arbaugh
---

My solution to the coding challenge for Jana.

A couple things of note about my implementation:

1) I used the Echo Twimlet to allow sending the Twiml document
content as a GET argument instead of uploading a file to S3 and
linked to it

2) I used the praw Reddit API wrapper to grab the top headline.
Alternatively, I could have manually fetched it using the REST API
or I could have used BeautifulSoup and Requests to parse it out if
need be.

3) The base XML is stored in the twiml.xml file

How I ran it:

I setup a cronjob on a DigitalOcean droplet with the following crontab entry:

```0 11 * * * cd /root/JanaChallenge && /opt/env/bin/python main.py >> cron.log 2>&1```

This entry will run the script every day at 11am EST/3pm UTC. Of course, I will disable after
its first run on Tuesday.



Thank you!!