import json
import random
import re
from pathlib import Path


def load_data():
    file_path = Path(__file__).with_name("chatbot_data.json")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("\nError: chatbot_data.json file was not found.")
        print("Keep both files in the same folder.")
        raise SystemExit(1)

    except json.JSONDecodeError:
        print("\nError: Please check your JSON file formatting.")
        raise SystemExit(1)

def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text

def show_welcome(data):
    bot_name = data.get("bot_name", "Nova")

    print("\n" + "=" * 50)
    print(f"          {bot_name.upper()} SUPPORT CHATBOT")
    print("       Your Friendly Customer Assistant")
    print("=" * 50)

    print("\nWelcome! I am here to help you.")
    print("You can ask me about:")

    print("  1- Business hours")
    print("  2- Product prices and availability")
    print("  3- Delivery and shipping")
    print("  4- Returns and refunds")
    print("  5- Payment methods")
    print("  6- Order tracking")

    print("\nType 'help' for examples.")
    print("Type 'bye' to end the conversation.")
    print("-" * 50)

def show_help():
    print("\n" + "-" * 45)
    print("              WHAT I CAN DO")
    print("-" * 45)

    examples = [
        "Hello",
        "How are you?",
        "What are your business hours?",
        "How much does a product cost?",
        "How long does delivery take?",
        "What is your return policy?",
        "Which payment methods do you accept?",
        "How can I track my order?",
        "How can I contact support?"
    ]

    for example in examples:
        print("  * " + example)

    print("-" * 45)

def identify_intent(message, patterns):
    for intent, regex_patterns in patterns.items():
        for pattern in regex_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                return intent

    return "fallback"

def get_response(user_message, data, conversation):
    message = normalize_text(user_message)

    if message in data.get("exit_commands", []):
        return random.choice(data["responses"]["goodbye"]), "exit"
    
    if message in data.get("help_commands", []):
        return "", "help"

    if conversation["awaiting_product"]:
        if message in [
            "no", "no thanks", "nothing",
            "cancel", "never mind"
        ]:
            conversation["awaiting_product"] = False
            return (
                "No problem! You can ask me about "
                "another topic whenever you like."
            ), "continue"

        conversation["awaiting_product"] = False

        return (
            f"Thanks for your interest in '{user_message.strip()}'.\n"
            "This demo does not have a live product catalogue "
            "or real-time prices.\n"
            "I can still help with delivery, payments and returns."
        ), "continue"

    greetings = [
        "hi", "hello", "hey", "salam",
        "assalamualaikum", "good morning",
        "good afternoon", "good evening"
    ]

    if message in greetings:
        return random.choice(data["responses"]["greeting"]), "continue"
    intent = identify_intent(message, data.get("patterns", {}))
    responses = data["responses"].get(
        intent,
        data["responses"]["fallback"]
    )

    response = random.choice(responses)
    if intent == "products" or (
        intent == "price"
        and message in ["price", "prices", "cost", "how much"]
    ):
        conversation["awaiting_product"] = True

    return response, "continue"

def run_chatbot():
    data = load_data()
    bot_name = data.get("bot_name", "Nova")

    conversation = {
        "state": "chatting",
        "awaiting_product": False
    }

    show_welcome(data)

    
    greeting = random.choice(data["responses"]["greeting"])

    print(f"\n{bot_name}: {greeting}")


    while conversation["state"] != "exit":

        try:
            user_message = input("\nYou: ").strip()

        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{bot_name}: Chat ended. Take care!")
            break

        if not user_message:
            print(f"{bot_name}: Please type a question.")
            continue

        response, action = get_response(
            user_message,
            data,
            conversation
        )

        if action == "help":
            show_help()
            continue


        print(f"\n{bot_name}: {response}")

        if action == "exit":
            conversation["state"] = "exit"

    print("\n" + "=" * 50)
    print("             CHAT SESSION FINISHED")
    print("=" * 50)

if __name__ == "__main__":
    run_chatbot()