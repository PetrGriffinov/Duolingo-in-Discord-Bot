import difflib
from random import choice, randint
from script1 import ttsActivated, french_arrayIndex_a1, french_arrayIndex_a2, french_arrayIndex_b1, russian_arrayIndex_a1, russian_arrayIndex_a2, russian_arrayIndex_b1, spanish_arrayIndex_a1, spanish_arrayIndex_a2, spanish_arrayIndex_b1, chinese_arrayIndex_a1, chinese_arrayIndex_a2, chinese_arrayIndex_b1 , isLearning
from database import russian_a1_possible_answers, russian_a1_possible_questions, russian_a2_possible_answers, russian_a2_possible_questions, russian_b1_possible_answers, russian_b1_possible_questions, french_a1_possible_answers, french_a1_possible_questions, french_a2_possible_answers, french_a2_possible_questions, french_b1_possible_answers, french_b1_possible_questions, spanish_a1_possible_answers, spanish_a1_possible_questions,spanish_a2_possible_answers, spanish_a2_possible_questions, spanish_b1_possible_answers, spanish_b1_possible_questions, chinese_a1_possible_answers, chinese_a1_possible_questions, chinese_a2_possible_answers, chinese_a2_possible_questions, chinese_b1_possible_answers, chinese_b1_possible_questions

def similar(a: str, b: str) -> bool:
    return difflib.SequenceMatcher(None, a, b).ratio() > 0.85

def almostCorrect(a: str, b: str) -> bool:
    return difflib.SequenceMatcher(None, a, b).ratio() > 0.5

def russian_a1(user_input: str) -> str:
    global russian_arrayIndex_a1
    global isLearning
    global ttsActivated
    ttsActivated = False
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not russian_a1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + russian_a1_possible_questions[russian_arrayIndex_a1] 
    elif lowered == 'speak out loud' and isLearning:
        ttsActivated = True
        return '' + russian_a1_possible_questions[russian_arrayIndex_a1]

    elif similar(lowered, russian_a1_possible_answers[russian_arrayIndex_a1]) and isLearning:
        russian_a1_possible_questions.pop(russian_arrayIndex_a1)
        russian_a1_possible_answers.pop(russian_arrayIndex_a1)
        if russian_a1_possible_questions:
            russian_arrayIndex_a1 = randint(0, len(russian_a1_possible_questions) - 1)
            print(russian_arrayIndex_a1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = russian_a1_possible_answers[russian_arrayIndex_a1]
        russian_a1_possible_questions.pop(russian_arrayIndex_a1)
        russian_a1_possible_answers.pop(russian_arrayIndex_a1)
        if russian_a1_possible_questions:
            russian_arrayIndex_a1 = randint(0, len(russian_a1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != russian_a1_possible_answers[russian_arrayIndex_a1] and isLearning:
        if almostCorrect(lowered, russian_a1_possible_answers[russian_arrayIndex_a1]):
            return choice([
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That was close! Try again!'
        ])
        return choice([
            'Wrong answer, try it again!',
            'That\'s completly wrong, please never try again',
            'Try harder! Don\'t give up!'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def russian_a2(user_input: str) -> str:
    global russian_arrayIndex_a2
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not russian_a2_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + russian_a2_possible_questions[russian_arrayIndex_a2] 
    elif similar(lowered, russian_a2_possible_answers[russian_arrayIndex_a2]) and isLearning:
        russian_a2_possible_questions.pop(russian_arrayIndex_a2)
        russian_a2_possible_answers.pop(russian_arrayIndex_a2)
        if russian_a2_possible_questions:
            russian_arrayIndex_a2 = randint(0, len(russian_a2_possible_questions) - 1)
            print(russian_arrayIndex_a2)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = russian_a2_possible_answers[russian_arrayIndex_a2]
        russian_a2_possible_questions.pop(russian_arrayIndex_a2)
        russian_a2_possible_answers.pop(russian_arrayIndex_a2)
        if russian_a2_possible_questions:
            russian_arrayIndex_a2 = randint(0, len(russian_a2_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != russian_a2_possible_answers[russian_arrayIndex_a2] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def russian_b1(user_input: str) -> str:
    global russian_arrayIndex_b1
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not russian_b1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + russian_b1_possible_questions[russian_arrayIndex_b1] 
    elif similar(lowered, russian_b1_possible_answers[russian_arrayIndex_b1]) and isLearning:
        russian_b1_possible_questions.pop(russian_arrayIndex_b1)
        russian_b1_possible_answers.pop(russian_arrayIndex_b1)
        if russian_b1_possible_questions:
            russian_arrayIndex_b1 = randint(0, len(russian_b1_possible_questions) - 1)
            print(russian_arrayIndex_b1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = russian_b1_possible_answers[russian_arrayIndex_b1]
        russian_b1_possible_questions.pop(russian_arrayIndex_b1)
        russian_b1_possible_answers.pop(russian_arrayIndex_b1)
        if russian_b1_possible_questions:
            russian_arrayIndex_b1 = randint(0, len(russian_b1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != russian_b1_possible_answers[russian_arrayIndex_b1] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def french_a1(user_input: str) -> str:
    global french_arrayIndex_a1
    global isLearning
    global ttsActivated
    ttsActivated = False
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not french_a1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + french_a1_possible_questions[french_arrayIndex_a1] 
    elif lowered == 'speak out loud' and isLearning:
        ttsActivated = True
        return '' + french_a1_possible_questions[french_arrayIndex_a1]
    elif similar(lowered, french_a1_possible_answers[french_arrayIndex_a1]) and isLearning:
        french_a1_possible_questions.pop(french_arrayIndex_a1)
        french_a1_possible_answers.pop(french_arrayIndex_a1)
        if french_a1_possible_questions:
            french_arrayIndex_a1 = randint(0, len(french_a1_possible_questions) - 1)
            print(french_arrayIndex_a1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = french_a1_possible_answers[french_arrayIndex_a1]
        french_a1_possible_questions.pop(french_arrayIndex_a1)
        french_a1_possible_answers.pop(french_arrayIndex_a1)
        if french_a1_possible_questions:
            french_arrayIndex_a1 = randint(0, len(french_a1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != french_a1_possible_answers[french_arrayIndex_a1] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def french_a2(user_input: str) -> str:
    global french_arrayIndex_a2
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not french_a2_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + french_a2_possible_questions[french_arrayIndex_a2] 
    elif similar(lowered, french_a2_possible_answers[french_arrayIndex_a2]) and isLearning:
        french_a2_possible_questions.pop(french_arrayIndex_a2)
        french_a2_possible_answers.pop(french_arrayIndex_a2)
        if french_a2_possible_questions:
            french_arrayIndex_a2 = randint(0, len(french_a2_possible_questions) - 1)
            print(french_arrayIndex_a2)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = french_a2_possible_answers[french_arrayIndex_a2]
        french_a2_possible_questions.pop(french_arrayIndex_a2)
        french_a2_possible_answers.pop(french_arrayIndex_a2)
        if french_a2_possible_questions:
            french_arrayIndex_a2 = randint(0, len(french_a2_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != french_a2_possible_answers[french_arrayIndex_a2] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def french_b1(user_input: str) -> str:
    global french_arrayIndex_b1
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not french_b1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + french_b1_possible_questions[french_arrayIndex_b1] 
    elif similar(lowered, french_b1_possible_answers[french_arrayIndex_b1]) and isLearning:
        french_b1_possible_questions.pop(french_arrayIndex_b1)
        french_b1_possible_answers.pop(french_arrayIndex_b1)
        if french_b1_possible_questions:
            french_arrayIndex_b1 = randint(0, len(french_b1_possible_questions) - 1)
            print(french_arrayIndex_b1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = french_b1_possible_answers[french_arrayIndex_b1]
        french_b1_possible_questions.pop(french_arrayIndex_b1)
        french_b1_possible_answers.pop(french_arrayIndex_b1)
        if french_b1_possible_questions:
            french_arrayIndex_b1 = randint(0, len(french_b1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != french_b1_possible_answers[french_arrayIndex_b1] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])
    
def spanish_a1(user_input: str) -> str:
    global spanish_arrayIndex_a1
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not spanish_a1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + spanish_a1_possible_questions[spanish_arrayIndex_a1] 
    elif similar(lowered, spanish_a1_possible_answers[spanish_arrayIndex_a1]) and isLearning:
        spanish_a1_possible_questions.pop(spanish_arrayIndex_a1)
        spanish_a1_possible_answers.pop(spanish_arrayIndex_a1)
        if spanish_a1_possible_questions:
            spanish_arrayIndex_a1 = randint(0, len(spanish_a1_possible_questions) - 1)
            print(spanish_arrayIndex_a1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = spanish_a1_possible_answers[spanish_arrayIndex_a1]
        spanish_a1_possible_questions.pop(spanish_arrayIndex_a1)
        spanish_a1_possible_answers.pop(spanish_arrayIndex_a1)
        if spanish_a1_possible_questions:
            spanish_arrayIndex_a1 = randint(0, len(spanish_a1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != spanish_a1_possible_answers[spanish_arrayIndex_a1] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def spanish_a2(user_input: str) -> str:
    global spanish_arrayIndex_a2
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not spanish_a2_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + spanish_a2_possible_questions[spanish_arrayIndex_a2] 
    elif similar(lowered, spanish_a2_possible_answers[spanish_arrayIndex_a2]) and isLearning:
        spanish_a2_possible_questions.pop(spanish_arrayIndex_a2)
        spanish_a2_possible_answers.pop(spanish_arrayIndex_a2)
        if spanish_a2_possible_questions:
            spanish_arrayIndex_a2 = randint(0, len(spanish_a2_possible_questions) - 1)
            print(spanish_arrayIndex_a2)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = spanish_a2_possible_answers[spanish_arrayIndex_a2]
        spanish_a2_possible_questions.pop(spanish_arrayIndex_a2)
        spanish_a2_possible_answers.pop(spanish_arrayIndex_a2)
        if spanish_a2_possible_questions:
            spanish_arrayIndex_a2 = randint(0, len(spanish_a2_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != spanish_a2_possible_answers[spanish_arrayIndex_a2] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def spanish_b1(user_input: str) -> str:
    global spanish_arrayIndex_b1
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not spanish_b1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + spanish_b1_possible_questions[spanish_arrayIndex_b1] 
    elif similar(lowered, spanish_b1_possible_answers[spanish_arrayIndex_b1]) and isLearning:
        spanish_b1_possible_questions.pop(spanish_arrayIndex_b1)
        spanish_b1_possible_answers.pop(spanish_arrayIndex_b1)
        if spanish_b1_possible_questions:
            spanish_arrayIndex_b1 = randint(0, len(spanish_b1_possible_questions) - 1)
            print(spanish_arrayIndex_b1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = spanish_b1_possible_answers[spanish_arrayIndex_b1]
        spanish_b1_possible_questions.pop(spanish_arrayIndex_b1)
        spanish_b1_possible_answers.pop(spanish_arrayIndex_b1)
        if spanish_b1_possible_questions:
            spanish_arrayIndex_b1 = randint(0, len(spanish_b1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != spanish_b1_possible_answers[spanish_arrayIndex_b1] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
   
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def chinese_a1(user_input: str) -> str:
    global chinese_arrayIndex_a1
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not chinese_a1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + chinese_a1_possible_questions[chinese_arrayIndex_a1] 
    elif similar(lowered, chinese_a1_possible_answers[chinese_arrayIndex_a1]) and isLearning:
        chinese_a1_possible_questions.pop(chinese_arrayIndex_a1)
        chinese_a1_possible_answers.pop(chinese_arrayIndex_a1)
        if chinese_a1_possible_questions:
            chinese_arrayIndex_a1 = randint(0, len(chinese_a1_possible_questions) - 1)
            print(chinese_arrayIndex_a1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = chinese_a1_possible_answers[chinese_arrayIndex_a1]
        chinese_a1_possible_questions.pop(chinese_arrayIndex_a1)
        chinese_a1_possible_answers.pop(chinese_arrayIndex_a1)
        if chinese_a1_possible_questions:
            chinese_arrayIndex_a1 = randint(0, len(chinese_a1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != chinese_a1_possible_answers[chinese_arrayIndex_a1] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def chinese_a2(user_input: str) -> str:
    global chinese_arrayIndex_a2
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not chinese_a2_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + chinese_a2_possible_questions[chinese_arrayIndex_a2] 
    elif similar(lowered, chinese_a2_possible_answers[chinese_arrayIndex_a2]) and isLearning:
        chinese_a2_possible_questions.pop(chinese_arrayIndex_a2)
        chinese_a2_possible_answers.pop(chinese_arrayIndex_a2)
        if chinese_a2_possible_questions:
            chinese_arrayIndex_a2 = randint(0, len(chinese_a2_possible_questions) - 1)
            print(chinese_arrayIndex_a2)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = chinese_a2_possible_answers[chinese_arrayIndex_a2]
        chinese_a2_possible_questions.pop(chinese_arrayIndex_a2)
        chinese_a2_possible_answers.pop(chinese_arrayIndex_a2)
        if chinese_a2_possible_questions:
            chinese_arrayIndex_a2 = randint(0, len(chinese_a2_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != chinese_a2_possible_answers[chinese_arrayIndex_a2] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])

def chinese_b1(user_input: str) -> str:
    global chinese_arrayIndex_b1
    global isLearning
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Say some shit, mf'
    elif 'start' in lowered:
        if not chinese_b1_possible_questions:
            return 'Nice! You completed every exercise. You can try the next level!'
        else:
            isLearning = True
            return 'Write this in english: ' + chinese_b1_possible_questions[chinese_arrayIndex_b1] 
    elif similar(lowered, chinese_b1_possible_answers[chinese_arrayIndex_b1]) and isLearning:
        chinese_b1_possible_questions.pop(chinese_arrayIndex_b1)
        chinese_b1_possible_answers.pop(chinese_arrayIndex_b1)
        if chinese_b1_possible_questions:
            chinese_arrayIndex_b1 = randint(0, len(chinese_b1_possible_questions) - 1)
            print(chinese_arrayIndex_b1)
        isLearning = False
        return 'Correct!'
    elif 'solution' in lowered and isLearning:
        solution = chinese_b1_possible_answers[chinese_arrayIndex_b1]
        chinese_b1_possible_questions.pop(chinese_arrayIndex_b1)
        chinese_b1_possible_answers.pop(chinese_arrayIndex_b1)
        if chinese_b1_possible_questions:
            chinese_arrayIndex_b1 = randint(0, len(chinese_b1_possible_questions) - 1)
        isLearning = False
        return 'The solution is: ' + solution
    elif lowered != chinese_b1_possible_answers[chinese_arrayIndex_b1] and isLearning:
        return choice([
            'Wrong answer, try it again!',
            'Almost there, try again!',
            'You almost got it, try one more time!',
            'That\'s completly wrong, please never try again'
        ])
    
    else:
        return choice([
            'I don\'t understand what you said...',
            'What you talking bout, fool?',
            'As of now, I don\'t understand yapanese, sorry!'
        ])