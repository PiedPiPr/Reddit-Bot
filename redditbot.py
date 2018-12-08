##A bot that auto replies to comments in reddit
##https://old.reddit.com/prefs/apps/   use this link for API
import praw

bot = praw.Reddit(user_agent='Name of Your Bot',
                  client_id='Get it from Reddit Left Upper personal use script',
                  client_secret='generated secret code here',
                  username='your username',
                  password='your password')


subreddit = bot.subreddit('space')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    author = comment.author
    if 'mars' in text.lower():
        message = "Have you ever been to Mars ?, u/{0}?".format(author)
        comment.reply(message)
