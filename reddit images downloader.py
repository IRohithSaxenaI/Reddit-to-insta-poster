import praw
import urllib.request

# Create a Reddit instance and authenticate
reddit = praw.Reddit(client_id="your client id",client_secret="client secret",user_agent="testing_api",username= "your userame",password= "your password")


# Specify the subreddit and sort type
subreddit = reddit.subreddit('greentext')
# you can put day,week, year, all time in sort type
sort_type = 'day'

# Get the top 10 submissions in the subreddit
submissions = subreddit.top(limit=10, time_filter=sort_type)

# Iterate through the submissions and download any image posts
for submission in submissions:
    if submission.url.endswith('.jpg') or submission.url.endswith('.png'):
        image_url = submission.url
        image_filename = submission.title + '.' + image_url.split('.')[-1]
        urllib.request.urlretrieve(image_url, image_filename)
        print('Downloaded:', image_filename)