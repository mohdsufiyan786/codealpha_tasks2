def chatbot():
    #Infinite loop to keep the chatbot running

    print("Hi! I am your chatbot.type something to chat. (Type 'bye' to exit)")
    while True:

        user_input=input("You:").lower()
    #Take user input and convert lowercase for asy matching
        #Greeting response
        if "hello" in user_input:
            print("Bot: Hi there! i'm excitd to talk with you")
        #asking about well being    
        elif "how are you" in user_input:
            print("Bot: I am doing great. thank you! what about you?")

        elif "i am fine" in user_input or "i am good" in user_input or "i am also fine" in user_input:
            print("Bot: That's wonderful to hear!")
        elif "your name" in user_input:

            print("Bot: My name is chatbuddy! What's your name?")
        elif "my name is" in user_input:
            print("Bot: Thaat's a beautiful name! Nice to meet you.")

        elif "hat can you do" in user_input or "what do you do" in user_input:
            print("Bot: I can chat with you, tell jokes, motivate you.")

        #telling a joke
        elif "tell me a joke" in user_input:
            print("Bot: Why don't scientists trust atom? Because they make up everything")
        #motivational msg
        elif "motivate me" in user_input or "motivation" in user_input:
            print("Bot: Believe in yourself! Evry day is a new chance to achieve your goal")

        elif "thank you" in user_input or "thanks" in user_input:
            print("Bot: You're always welcome")

            #Exit condition
        elif"bye"in user_input:
            print("Bot: Goodbye! it was nice chatting with you")
            break
        else:
            print("Bot: I did'nt understand...")
chatbot()