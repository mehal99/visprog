PROMPT = """Think step by step to carry out the instruction.

Instruction: Visualize this story: Fred lays in a hammock in the yard. Fred is laying outside in a hammock. Something moves past Fred. Fred sits on a hammock in the yard. Fred is outside sitting in a hammock.
Program:
IMAGE0=STORYIMG(image=IMAGE, src_prompt='Fred lays in a hammock in the yard', target_prompt='Fred is laying outside in a hammock', seed = 200, w1 = 1.5)
IMAGE1 = STORYIMG(image=IMAGE0, src_prompt='Fred is laying outside in a hammock', target_prompt='Something moves past Fred', seed = 200, w1 = 1.5)
IMAGE2 = STORYIMG(image=IMAGE1, src_prompt='Something moves past Fred', target_prompt='Fred sits on a hammock in the yard', seed = 200, w1 = 1.5)
IMAGE3 = STORYIMG(image=IMAGE2, src_prompt='Fred sits on a hammock in the yard', target_prompt='Fred is outside in a hammock', seed = 200, w1 = 1.5)
FINAL_RESULT=RESULT(var=[IMAGE0, IMAGE1, IMAGE2, IMAGE3])

Instruction: Visualize this story: man wearing purple plays an instrument next to a microphone on a stage. man with violet dress wearing glasses talks into a microphone on stage. man with violet dress wearing glasses looks away from the microphone on stage. man with violet dress wearing glasses is talking without microphone. He is speaking to someone on the phone while wearing a purple hat.
Program:
IMAGE0=STORYIMG(image=IMAGE, src_prompt='man wearing purple plays an instrument next to a microphone on a stage', target_prompt='man with violet dress wearing glasses talks into a microphone on stage.', seed = 200, w1 = 1.5)
IMAGE1 = STORYIMG(image=IMAGE0, src_prompt='man with violet dress wearing glasses talks into a microphone on stage.', target_prompt='man with violet dress wearing glasses looks away from the microphone on stage.', seed = 200, w1 = 1.5)
IMAGE2 = STORYIMG(image=IMAGE1, src_prompt='man with violet dress wearing glasses looks away from the microphone on stage.', target_prompt='man with violet dress wearing glasses is talking without microphone.', seed = 200, w1 = 1.5)
IMAGE3 = STORYIMG(image=IMAGE2, src_prompt='man with violet dress wearing glasses is talking without microphone.', target_prompt='He is speaking to someone on the phone while wearing a purple hat.', seed = 200, w1 = 1.5)
FINAL_RESULT=RESULT(var=[IMAGE0, IMAGE1, IMAGE2, IMAGE3])

Instruction: {instruction}
Program:
"""