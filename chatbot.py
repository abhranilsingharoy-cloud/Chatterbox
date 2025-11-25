import sys

def simple_chatbot():
    """
    A simple rule-based chatbot using if-elif-else logic.
    """
    
    # 1. Print a welcome message
    print("Chatbot: Hello! I'm a simple bot. Type 'bye' to exit.")
    print("Chatbot: What's on your mind today?")

    # 2. Start an infinite loop to keep the conversation going
    while True:
        # Get user input
        try:
            user_input = input("You: ")
        except EOFError:
            # Handle case where input stream closes unexpectedly
            break
            
        # 3. Normalize the input to make matching easier
        # .strip() removes spaces from start/end
        # .lower() converts text to lowercase so "Hello" matches "hello"
        text = user_input.strip().lower()

        # Check if the input is empty
        if not text:
            continue

        # 4. Use if-elif-else logic to determine the response
        
        # --- Greetings ---
        if "hello" in text or "hi" in text or "hey" in text:
            print("Chatbot: Hi there! How can I help you?")

        # --- Asking about the bot ---
        elif "how are you" in text:
            print("Chatbot: I'm just a computer program, but I'm functioning perfectly! How are you?")
        
        elif "your name" in text or "who are you" in text:
            print("Chatbot: I am a Python Chatbot created for Task 8.")

        elif "what can you do" in text:
            print("Chatbot: I can answer simple questions, greet you, or say goodbye!")

        # --- General Conversation ---
        elif "weather" in text:
            print("Chatbot: I can't check the live weather, but it's always sunny in the digital world!")
        
        elif "joke" in text:
            print("Chatbot: Why did the Python programmer needing glasses? Because he couldn't C# (see sharp)!")

        # --- Exit Commands ---
        elif "bye" in text or "exit" in text or "quit" in text:
            print("Chatbot: Goodbye! Have a great day!")
            break  # This stops the loop and ends the program

        # --- Fallback (Default Response) ---
        else:
            print("Chatbot: I'm not sure I understand that. Can you try asking something else?")

if __name__ == "__main__":
    simple_chatbot()
