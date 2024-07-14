import os
from dotenv import load_dotenv
import telebot

# Load environment variables from .env file
load_dotenv()

# Get the BOT_TOKEN environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Check if BOT_TOKEN is set
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN provided. Please set the BOT_TOKEN environment variable.")

bot = telebot.TeleBot(BOT_TOKEN)

# Command to start or greet the user
@bot.message_handler(commands=['start', 'hello','hi'])
def send_welcome(message):
    bot.reply_to(message, "How, how are you doing?")

# Command to provide information about you
@bot.message_handler(commands=['about'])
def about_me(message):
    about_text = """
    Hi! I'm Shedrack. I'm a computer scientist specializing in AI and machine learning.
    I have experience with web development, data science, cybersecurity, and more.
    I'm currently studying for a computer science degree at Kabarak University and will be graduating in 2025.
    """
    bot.reply_to(message, about_text)

# Command to provide all details
@bot.message_handler(commands=['everything'])
def everything(message):
    everything_text = """
    **About Shedrack**

    Hi! I'm Shedrack. I'm a computer scientist specializing in AI and machine learning.
    I have experience with web development, data science, cybersecurity, and more.
    I'm currently studying for a computer science degree at Kabarak University and will be graduating in 2025.
    """
    bot.reply_to(message, everything_text)

# Command to provide learning material sites
@bot.message_handler(commands=['learn'])
def learning_materials(message):
    materials_text = """
    Here are some great platforms to find learning materials:

    **Free Resources**:
    - [Coursera](https://www.coursera.org) - Offers free courses from top universities.
    - [edX](https://www.edx.org) - Free online courses from MIT, Harvard, and more.
    - [Khan Academy](https://www.khanacademy.org) - Free educational resources for various subjects.
    - [MIT OpenCourseWare](https://ocw.mit.edu) - Free lecture notes, exams, and videos from MIT.

    **Paid Resources**:
    - [Udemy](https://www.udemy.com) - Offers paid courses on a wide range of topics.
    - [Pluralsight](https://www.pluralsight.com) - Tech and creative skills courses.
    - [LinkedIn Learning](https://www.linkedin.com/learning) - Professional development courses.
    - [DataCamp](https://www.datacamp.com) - Data science and programming courses.
    """
    bot.reply_to(message, materials_text)

# Default message handler to provide learning materials based on user queries
@bot.message_handler(func=lambda msg: True)
def provide_learning_materials(message):
    query = message.text.lower()

    response = "I'm sorry, I don't have information on that topic. Please try asking about AI, ML, data science, web development, cybersecurity, databases, algorithms, networking, software engineering, cloud computing, or any other tech topic."

    if "ai" in query or "machine learning" in query:
        response = """
        **AI and Machine Learning Resources**:
        - [Coursera](https://www.coursera.org) - Offers various AI and ML courses.
        - [edX](https://www.edx.org) - Learn from MIT and Harvard courses on AI.
        - [Udemy](https://www.udemy.com) - Paid courses on AI and ML.
        - [DataCamp](https://www.datacamp.com) - Data science and AI courses.
        """
    elif "data science" in query:
        response = """
        **Data Science Resources**:
        - [Coursera](https://www.coursera.org) - Data science courses.
        - [edX](https://www.edx.org) - Learn data science from top universities.
        - [DataCamp](https://www.datacamp.com) - Data science and analytics courses.
        - [Kaggle](https://www.kaggle.com/learn) - Free data science courses.
        """
    elif "web development" in query:
        response = """
        **Web Development Resources**:
        - [FreeCodeCamp](https://www.freecodecamp.org) - Free web development tutorials.
        - [Coursera](https://www.coursera.org) - Web development courses.
        - [Udemy](https://www.udemy.com) - Paid courses on web development.
        - [Mozilla Developer Network](https://developer.mozilla.org) - Free resources and documentation.
        """
        
    elif "hello" in query:
        response = """
        **hello**:
        - Hi! I'm Rack. I'm a computer scientist specializing in AI and machine learning.
        
        
         Please try asking about AI, ML, data science, web development, cybersecurity, databases, algorithms, networking, software engineering, cloud computing, or any other tech topic."
    I
    """
        
    elif "cybersecurity" in query:
        response = """
        **Cybersecurity Resources**:
        - [Cybrary](https://www.cybrary.it) - Free cybersecurity courses.
        - [Coursera](https://www.coursera.org) - Cybersecurity courses.
        - [edX](https://www.edx.org) - Cybersecurity courses.
        - [Udemy](https://www.udemy.com) - Paid courses on cybersecurity.
        """
    elif "databases" in query:
        response = """
        **Database Resources**:
        - [Coursera](https://www.coursera.org) - Courses on SQL and database management.
        - [edX](https://www.edx.org) - Learn about databases from top universities.
        - [Udemy](https://www.udemy.com) - Paid courses on database management and SQL.
        """
    elif "algorithms" in query:
        response = """
        **Algorithms Resources**:
        - [Coursera](https://www.coursera.org) - Courses on algorithms and data structures.
        - [edX](https://www.edx.org) - Learn algorithms from top universities.
        - [Udemy](https://www.udemy.com) - Paid courses on algorithms and problem-solving.
        """
    elif "networking" in query:
        response = """
        **Networking Resources**:
        - [Coursera](https://www.coursera.org) - Networking courses.
        - [edX](https://www.edx.org) - Learn computer networking from top universities.
        - [Udemy](https://www.udemy.com) - Paid courses on networking.
        - [Cisco Networking Academy](https://www.netacad.com) - Free networking courses.
        """
    elif "software engineering" in query:
        response = """
        **Software Engineering Resources**:
        - [Coursera](https://www.coursera.org) - Software engineering courses.
        - [edX](https://www.edx.org) - Learn software engineering from top universities.
        - [Udemy](https://www.udemy.com) - Paid courses on software engineering.
        """
    elif "cloud computing" in query:
        response = """
        **Cloud Computing Resources**:
        - [Coursera](https://www.coursera.org) - Cloud computing courses.
        - [edX](https://www.edx.org) - Learn cloud computing from top universities.
        - [Udemy](https://www.udemy.com) - Paid courses on cloud computing.
        - [AWS Training](https://aws.amazon.com/training) - Free and paid cloud computing courses.
        """

    bot.reply_to(message, response)

# Start the bot
bot.infinity_polling()
