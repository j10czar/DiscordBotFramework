v = 'V.1.0'

def handle_response(message) -> str:
    l_message = message.lower()

    if l_message == 'version':
        return v

    if l_message == 'help':
        return '**Help:** ```.version: Displays the current version of the bot```' 

    return 'Sorry, I dont know that command.'
