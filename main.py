import telebot
import config
import tweepy
import webbrowser

bot = telebot.TeleBot(config.token)
auth = tweepy.OAuthHandler(config.API_key, config.API_secret)
auth_access_token =""
auth_secret_token=""
@bot.message_handler(commands=['reg'])
def reg_twiiter(message):

    auth_url = auth.get_authorization_url()
    bot.send_message(message.chat.id, auth_url)
   # verifier = raw_input("PIN: ").strip()
   ##auth.get_access_token(verifier)
    ## print(auth.access_token.key)
    bot.register_next_step_handler(message, next_twitter_step)

def next_twitter_step(message):
    auth.get_access_token(message.text)


@bot.message_handler(commands=['twi'])
def twi(message):
    bot.register_next_step_handler(message, send_twi)
def send_twi(message):
    auth.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message.text)


bot.polling()