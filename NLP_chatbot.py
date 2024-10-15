from textblob import TextBlob

#Defining chatbot class for interacting with user
class Chatbot:
    #initializer
    def __init__(self):
        self.sentiment_analyzer = TextBlob("")

    def start_chat(self):
        print("Hello, Welcome to chat bot, please Type in your question")
        
        while True:
            user_prompt = input("Q: ").strip()
            
            self.sentiment_analyzer = TextBlob(user_prompt)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity
            
            #Analyzing the Score
            if sentiment_score > 0:
                chatbot_message = f"Great to hear that! \n  sentiment score : {sentiment_score} \n "
            elif sentiment_score < 0:
                chatbot_message = f"So sorry to hear that! would you like me to transfer to a live agent?. \n sentiment score : {sentiment_score} \n"
            else:
                chatbot_message = f"Can you please provide more information? \n sentiment score: {sentiment_score}"
                
            print(chatbot_message)
                
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()