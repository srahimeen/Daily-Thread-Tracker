import praw
import time
#import numpy
#import pickle

r = praw.Reddit(user_agent = "Gets the Daily General Thread from subreddit.")
print("Logging in...")
r.login()

#open file
config_file_name = "config.txt"
config_file = open(config_file_name).read().splitlines()

#set up config array
config = []

#input values from file into config array
for line in config_file:
    config.append(line)

#assign all variables from file
subreddit_name = config[0]
message_recipient = config[2]
message_title = config[3]
message_body = config[4]

#print each variable for testing purposes
print("Subreddit name: " + subreddit_name)
print("Message recipient: " + message_recipient)
print("Message title: " + message_title)
print("Message body: " + message_body)

#set up query string
words_to_match = ['potato']

#cache to keep track of searched threads
cache = []

#main function
def run_bot():
    print("Grabbing subreddit...")
    subreddit = r.get_subreddit(subreddit_name) #gets subreddit list
    print("Grabbing thread titles...")
    threads = subreddit.get_hot(limit=10) #gets assigned thread ids from selected subreddit
    for submission in threads:
        thread_title = submission.title.lower() #change to lowercase to avoid discrepancy
        isMatch = any(string in thread_title for string in words_to_match)
        if submission.id not in cache and isMatch: #to make sure we're not checking it twice
            print("Match found! Thread ID is " + submission.id)
            r.send_message(message_recipient, message_title, message_body)
            print("Message sent!")
            cache.append(submission.id)
    print("Comment loop finished. Restarting...")


# Run the script
while True:
    run_bot()
    time.sleep(20)

