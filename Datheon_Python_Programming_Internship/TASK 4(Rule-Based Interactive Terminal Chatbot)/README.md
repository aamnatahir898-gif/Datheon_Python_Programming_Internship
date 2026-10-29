# Nova — Customer Support Chatbot 

Nova is a rule-based customer support chatbot built with Python 3. It helps users get answers to common customer service questions, including business hours, product information, prices, delivery, returns, payment methods, and order tracking.

The chatbot uses regular expressions (Regex) to identify user intents and retrieves contextual responses from a JSON dataset. It runs in the terminal and does not require an internet connection.

##  Features

-  Interactive console-based conversation
-  Friendly greetings and welcome messages
-  Answers questions about business hours
-  Handles product and price inquiries
-  Provides delivery and shipping information
-  Answers questions about returns and refunds
-  Explains accepted payment methods
-  Provides order-tracking guidance
-  Directs users to customer support when needed
-  Uses regular expressions to recognize user intents
-  Normalizes input by converting text to lowercase and removing extra whitespace
-  Provides varied responses for selected intents
-  Includes a help menu with example questions
-  Handles missing or invalid JSON data with error messages
-  Supports continuous conversations until the user exits
-  Supports `bye`, `exit`, and `quit` commands
-  Stores responses and intent patterns separately in a JSON file

##  Project Structure

```text
Nova-Customer-Support-Chatbot/
│
├── chatbot.py
├── chatbot_data.json
└── README.md
```

| File | Description |
|---|---|
| `chatbot.py` | Contains the chatbot logic, input processing, intent recognition, and conversation loop. |
| `chatbot_data.json` | Stores the bot name, responses, regex patterns, help commands, and exit commands. |
| `README.md` | Provides project documentation and usage instructions. |

##  Requirements

- Python 3.x
- No external libraries required

The project uses Python's built-in modules:

- `re` — matches keywords and patterns using regular expressions.
- `json` — loads chatbot responses and configuration data.
- `random` — selects responses from available response lists.
- `pathlib` — locates the JSON dataset relative to the Python script.

##  Installation and Setup

### 1. Install Python

Download Python from the official website if it is not already installed.

https://www.python.org/downloads/

### 2. Download the Project

Clone your GitHub repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Alternatively, download the repository as a ZIP file and extract it.

### 3. Check the Project Files

Make sure both files are present in the same directory:

- `chatbot.py`
- `chatbot_data.json`

The chatbot requires the JSON file to load its responses and configuration.

### 4. Run the Chatbot

Open a terminal in the project directory and execute:

```bash
python chatbot.py
```

On Windows, you can also use:

```bash
py chatbot.py
```

##  How to Use

1. Start the chatbot using the command above.
2. Nova displays a welcome message and introduces its supported topics.
3. Type your question in the terminal.
4. The chatbot processes your message and identifies a matching intent.
5. Nova displays a response based on the configured JSON data.
6. Type `help` to view example questions.
7. Type `bye`, `exit`, or `quit` to end the conversation.

##  Example Conversation

```text
==================================================
             NOVA SUPPORT CHATBOT
       Your Friendly Customer Assistant
==================================================

Welcome! I am here to help you.

Nova: Hi there! I am Nova, your friendly assistant.
What can I help you with?

You: What are your business hours?

Nova: Our business hours are Monday to Friday,
9 AM to 6 PM. On Saturday, we are open from
10 AM to 4 PM. Sunday is our day off.

You: How long does delivery take?

Nova: Good news! Standard delivery usually takes
3 to 5 business days. Delivery time may vary
by location.

You: bye

Nova: Thank you for chatting with Nova Store!
Have a wonderful day. Goodbye!
```

*Note: Actual responses may vary because the chatbot randomly selects from configured response lists.*

##  Supported Queries

| Category | Example Query |
|---|---|
| Greetings | `Hello` |
| General conversation | `How are you?` |
| Business hours | `What time do you open?` |
| Product prices | `How much does a product cost?` |
| Product inquiries | `Which products are available?` |
| Delivery | `How long does delivery take?` |
| Returns and refunds | `What is your return policy?` |
| Payment methods | `Which payment methods do you accept?` |
| Order tracking | `How can I track my order?` |
| Customer support | `How can I contact support?` |
| Thanks | `Thank you` |
| Help | `help` |
| Exit | `bye` |

##  working

The chatbot follows a rule-based processing workflow.

1. **Load configuration:** Reads responses, patterns, and commands from `chatbot_data.json`.
2. **Normalize input:** Converts user input to lowercase and removes leading, trailing, and repeated whitespace.
3. **Check commands:** Recognizes help and exit commands.
4. **Manage conversation state:** Handles situations such as waiting for a product name.
5. **Identify intent:** Uses regular expressions to match the user's message with a predefined intent.
6. **Generate response:** Selects a suitable response from the JSON configuration.
7. **Handle unknown queries:** Displays a fallback response when no matching intent is found.
8. **Continue or exit:** Keeps the conversation active until the user requests to leave.

##  JSON Dataset

The `chatbot_data.json` file separates chatbot content from the Python logic.

It contains:

- `bot_name` — the chatbot's name.
- `tagline` — the assistant's introductory description.
- `responses` — predefined answers for each intent.
- `patterns` — regular expressions used for intent recognition.
- `exit_commands` — commands used to end the conversation.
- `help_commands` — commands that display the help menu.

This structure makes it easier to update responses and add new intents without rewriting the main chatbot logic.

##  Code Structure

| Function | Purpose |
|---|---|
| `load_data()` | Loads the chatbot configuration from the JSON file and handles file or JSON errors. |
| `normalize_text()` | Converts text to lowercase and removes extra whitespace. |
| `show_welcome()` | Displays the welcome screen and supported topics. |
| `show_help()` | Shows example questions users can ask. |
| `identify_intent()` | Matches a message against predefined regular expression patterns. |
| `get_response()` | Processes commands, manages product-related conversation state, and selects a response. |
| `run_chatbot()` | Initializes the chatbot and manages the main conversation loop. |

##  Error Handling and Limitations

- If `chatbot_data.json` is missing, the chatbot displays an error and exits.
- If the JSON file contains invalid formatting, the chatbot displays an appropriate error message.
- Empty user messages are rejected with a prompt to enter a question.
- Unrecognized questions receive a fallback response.
- Keyboard interruption and end-of-input are handled to end the session gracefully.
- Product prices and availability are not retrieved from a live catalogue.
- Order tracking is not connected to a real order database.
- The chatbot does not use machine learning or an AI language model; intent recognition is based on predefined rules and regex patterns.

**Important:** Business hours, delivery estimates, return policies, and payment options are sample information configured in the JSON dataset. Update these values before using the chatbot for a real business.

## Learning Objectives

This project demonstrates practical Python concepts, including:

- Rule-based chatbot development
- Regular expressions and pattern matching
- JSON file handling
- Functions and modular programming
- Dictionaries and lists
- String normalization
- Random response selection
- Conversation state management
- Input validation and error handling

