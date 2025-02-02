from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Say some shit, mf'
    elif 'hello' in lowered or 'hi' in lowered:
        return 'Hello there!'
    elif 'random number' in lowered:
        return randint(1,69)
    elif 'what can you do' in lowered:
        return 'Teach you languages!'
    elif 'how are you' in lowered:
        return 'I\'m fine, thanks for asking!'
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])