# QR Code Generator Telegram Bot

This is a Telegram bot that converts text to QR code.

## Author

JAYANTH RAJ G

## Date

01-02-2024

## Description

The bot takes a text input from the user and converts it into a QR code. It then sends the generated QR code back to the user as an image.

## Modules

The bot uses the following Python modules:

- `telegram`: For interacting with the Telegram API.
- `qrcode`: For generating QR codes.
- `io`: For handling byte streams.
- `os`: For interacting with the operating system.
- `dotenv`: For loading environment variables.

## Functions

The bot has two main functions:

- `start(update:Update, context: CallbackContext)`: This function is triggered when the `/start` command is sent to the bot. It sends a welcome message to the user and asks for the text to be converted to a QR code.

- `create_img(update:Update, context: CallbackContext)`: This function is triggered when the user sends a text message to the bot. It converts the text into a QR code and sends the QR code image back to the user.

## Running the Bot

To run the bot, you need to have a valid Telegram API token. You can get this token by creating a new bot on Telegram. Once you have the token, you can set it as an environment variable and run the bot.

You can interact with the bot by sending text messages to it on Telegram. The bot will convert the text into a QR code and send it back to you as an image.

Please note that you do not need to run the bot yourself to use it. You can simply interact with it on Telegram.

## Bot Link

You can access the bot using this link: [QR_craft_bot](https://t.me/QR_craft_bot)
