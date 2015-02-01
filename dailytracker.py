import praw
import time

r = praw.Reddit(user_agent = "Gets the Daily General Thread from subreddit.")
print("Logging in...")
r.login()

words_to_match = ['daily general thread']

cache = []

def run_bot():
    print("Grabbing subreddit...")
    subreddit = r.get_subreddit("test")
    print("Grabbing thread titles...")
    threads = subreddit.get_hot(limit=20)
    for submission in threads:
        thread_title = submission.title.lower()
        isMatch = any(string in thread_title for string in words_to_match)
        if submission.id not in cache and isMatch:
            print("Match found! Thread ID is " + submission.id)
            r.send_message('FlameDraBot', 'DGT has been posted!', 'You are awesome!')
            print("Message sent!")
            cache.append(submission.id)
    print("Comment loop finished. Restarting...")


while True:
    run_bot()
    time.sleep(20)
