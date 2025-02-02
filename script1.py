from random import randint
from database import russian_a1_possible_questions, russian_a2_possible_questions, russian_b1_possible_questions, french_a1_possible_questions, french_a2_possible_questions, french_b1_possible_questions,spanish_a1_possible_questions, spanish_a2_possible_questions, spanish_b1_possible_questions , chinese_a1_possible_questions, chinese_a2_possible_questions, chinese_b1_possible_questions

russian_arrayIndex_a1 = randint(0, len(russian_a1_possible_questions))
russian_arrayIndex_a2 = randint(0, len(russian_a2_possible_questions))
russian_arrayIndex_b1 = randint(0, len(russian_b1_possible_questions))

french_arrayIndex_a1 = randint(0, len(french_a1_possible_questions))
french_arrayIndex_a2 = randint(0, len(french_a2_possible_questions))
french_arrayIndex_b1 = randint(0, len(french_b1_possible_questions))

spanish_arrayIndex_a1 = randint(0, len(spanish_a1_possible_questions))
spanish_arrayIndex_a2 = randint(0, len(spanish_a2_possible_questions))
spanish_arrayIndex_b1 = randint(0, len(spanish_b1_possible_questions))

chinese_arrayIndex_a1 = randint(0, len(chinese_a1_possible_questions))
chinese_arrayIndex_a2 = randint(0, len(chinese_a2_possible_questions))
chinese_arrayIndex_b1 = randint(0, len(chinese_b1_possible_questions))

isLearning = False

ttsActivated = False