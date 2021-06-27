from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("Logo.jpg", caption='"Feel Like a King"')

######  follow someone #######
bot.follow("TechiEmpire")

######  send a message #######
bot.send_message("Hello from TechiEmpire", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("TechiEmpire")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()
