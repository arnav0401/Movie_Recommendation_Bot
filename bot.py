import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from model import recommend_movie
from model import random_recommendation
from model import genre_recommendation

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

logger = logging.getLogger(__name__)

COMPANY, DEGREE, COLOUR, MOOD, FINAL, FINAL_2 = range(6)
GENRE_2 = range(1)

def start(update: Update, _: CallbackContext) -> int:
    ''' Starts the conversation by introducing itself '''
    update.message.reply_text(
        "Hi there! Welcome onboard. My name is Just Watch Botter & I am excited to have you here with us. "
        "To get started, please select your choice of command to active the bot!"
    )

def random(update: Update, _: CallbackContext) -> int:
    ''' Recommends a completely random movie '''
    update.message.reply_text(
        "Here is a random movie recommendation for you: " + random_recommendation()
    )

def genre(update: Update, _: CallbackContext) -> int:
    ''' Asks User to select a specific Genre'''
    user = update.message.from_user
    update.message.reply_text(
        "From which Genre would you like to watch a movie?"
    )
    return GENRE_2

def genre_2(update: Update, _: CallbackContext) -> int:
    ''' Recommends a random movie from a selected Genre'''
    user = update.message.from_user
    logger.info("%s wants to watch a movie from Genre: %s", user.first_name, update.message.text)
    update.message.reply_text(
        "Here is a movie for you from " +  update.message.text + ": " +
         genre_recommendation(update.message.text)
    )
    return ConversationHandler.END


def recommend(update: Update, _: CallbackContext) -> int:
    ''' Starts the recommendation thread '''
    update.message.reply_text(
        "To recommend you the perfect movie, I would need you to answer few questions for me. "
        "So, let's get started. Type 'JustWatch' to begin!"
    ) 
    return COMPANY

def company(update: Update, _: CallbackContext) -> int:
    ''' Asks the user who would they be watching the movie with? '''    
    reply_keyboard = [['Alone', 'Friends', 'Family', 'S/O']]
    update.message.reply_text(
        'Who are you intending to watch the movie with?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return DEGREE

def degree(update: Update, _: CallbackContext) -> int:
    ''' Asks the user whether they would prefer a light or a heavy movie?'''
    reply_keyboard = [['Light', 'Heavy', 'No Preference']]
    user = update.message.from_user
    logger.info("%s is currently watching with: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Would you prefer to watch a Light or a Heavy movie?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return COLOUR

def colour(update: Update, _: CallbackContext) -> int:
    ''' Asks the user for their favourite colour'''
    reply_keyboard = [['Red', 'Blue', 'Black', 'Green', 'Yellow', 'White', 'Purple', 'No Preference']]
    user = update.message.from_user
    logger.info("%s prefers watching a %s degree movie" , user.first_name, update.message.text)
    update.message.reply_text(
        'What is your favourite colour?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return MOOD

def mood(update: Update, _: CallbackContext) -> int:
    ''' Asks the user for their current mood'''
    reply_keyboard =  [['Excited', 'Lonely', 'Depressed', 'Cheerful', 'Stressed']]
    user = update.message.from_user
    logger.info("The favourite colour of %s is %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Which word best describes your feeling now?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return FINAL
    
    # return ConversationHandler.END

def final(update: Update, _: CallbackContext) -> int:
    ''' recommends movie to the User '''
    user = update.message.from_user
    logger.info("%s is currently feeling: %s", user.first_name, update.message.text)
    if update.message.text == 'Excited':
        update.message.reply_text(
           "We recommend you: " + recommend_movie('Excited') + "!" + 
           " Are you happy with this recommendation?" + " y or n"
        )
    elif update.message.text == 'Lonely':
        update.message.reply_text(
            "We recommend you: " + recommend_movie('Lonely') + "!" + 
           " Are you happy with this recommendation?" + " y or n"
        )
    elif update.message.text == 'Depressed':
        update.message.reply_text(
           "We recommend you: " + recommend_movie('Depressed') + "!" +
           " Are you happy with this recommendation?" + " y or n"
        )
    elif update.message.text == 'Cheerful':
        update.message.reply_text(
           "We recommend you: " + recommend_movie('Cheerful') + "!" +
           " Are you happy with this recommendation?" + " y or n"
        )
    elif update.message.text == 'Stressed':
        update.message.reply_text(
           "We recommend you: " + recommend_movie('Stressed') + "!" + 
             " Are you happy with this recommendation?" + " y or n"
        )

    return FINAL_2

def final_2(update: Update, _: CallbackContext) -> int:
    ''' Thanking Note '''
    user = update.message.from_user
    logger.info("Did %s like the movie? : %s", user.first_name, update.message.text)
    update.message.reply_text(
            "Thank you for your feedback! This will allow us to constantly retrain our model for better results! " +
            " You can always get another recommendation by clicking on /cancel and then /start to reactive the bot!"
        )
        
    return ConversationHandler.END
    
def cancel(update: Update, _: CallbackContext) -> int:
    ''' Cancels and ends the conversation '''
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope I can help you again some day :)', reply_markup=ReplyKeyboardRemove()
        )

    return ConversationHandler.END

def main() -> None:
    ''' Run the bot '''
    updater = Updater("1824372052:AAGUSF-9ZSqC6bYAlEeiLqhMAz3LbwhHKBE")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("random", random))
    #dispatcher.add_handler(CommandHandler("genre", genre))

    # Add conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('recommend', recommend)],
        states={
            COMPANY: [MessageHandler(Filters.text & ~Filters.command, company)],
            DEGREE: [MessageHandler(Filters.text & ~Filters.command, degree)],
            COLOUR: [MessageHandler(Filters.text & ~Filters.command, colour)],
            MOOD: [MessageHandler(Filters.text & ~Filters.command, mood)],
            FINAL : [MessageHandler(Filters.text & ~Filters.command, final)],
            FINAL_2 : [MessageHandler(Filters.text & ~Filters.command, final_2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    conv_handler_2 = ConversationHandler(
        entry_points=[CommandHandler('genre', genre)],
        states={
            GENRE_2: [MessageHandler(Filters.text & ~Filters.command, genre_2)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(conv_handler_2)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()















