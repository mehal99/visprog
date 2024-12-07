PROMPT = """Think step by step to carry out the instruction.

Instruction: Visualize this story: Fred is sleeping and snoring in a hammock in the yard. Fred sits on a hammock in the yard, turning around happily.
Program:
IMG0=STORYIMG(image=IMAGE, src_prompt='Fred is sleeping and snoring in a hammock in the yard', target_prompt='Fred sits on a hammock in the yard, turning around happily', seed = 200, w1 = 1.5)
FINAL_RESULT=RESULT(var=IMAGE0)

Instruction: Visualize this story: Fred sits on a hammock in the yard, turning around happily. Something moves past Fred while Fred lays in a hammock outside. Fred watches it pass, then speaks.
Program:
IMG0=STORYIMG(image=IMAGE, src_prompt='Fred sits on a hammock in the yard, turning around happily', target_prompt='Something moves past Fred while Fred lays in a hammock outside. Fred watches it pass, then speaks.', seed = 200, w1 = 1.5)
FINAL_RESULT=RESULT(var=IMAGE0)

Instruction: Visualize this story: Barney is inside a brown room. Barney is walking in the desert.
Program:
IMG0=STORYIMG(image=IMAGE, src_prompt='Barney is inside a brown room', target_prompt='Barney is walking in the desert.', seed = 200, w1 = 1.5)
FINAL_RESULT=RESULT(var=IMAGE0)

Instruction: Visualize this story: Barney is looking in the window and speaking. Fred is in the room talking and his eyes are rolling.
Program:
IMG0=STORYIMG(image=IMAGE, src_prompt='Barney is looking in the window and speaking.', target_prompt='Fred is in the room talking and his eyes are rolling.', seed = 200, w1 = 1.5)
FINAL_RESULT=RESULT(var=IMAGE0)

Instruction: {instruction}
Program:
"""