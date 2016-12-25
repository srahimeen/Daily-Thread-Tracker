# Daily-Thread-Tracker
### Tracks daily threads on reddit and notifies user when a daily thread has been posted

Implemented as a console application which allows one to select a subreddit and monitor it. Whenever a thread with the preset keywords is available, a message is sent to the user informing them about the post. Uses a .txt file to cache previous results to ensure only threads posted after application launch is used to generate notifications.

Set up the use config.txt file to initialize keywords. Config file is set up as follows:

[0] = subreddit name  
[1] = words to match  
[2] = message recipient  
[3] = message title  
[4] = message body  

Where [#] is the line number.
