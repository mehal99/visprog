PROMPT = """Think step by step to carry out the instruction.

Instruction: Visualize this story: Fred, Jenny, and Pebbles are sitting in the woods. Fred is daydreaming about curry rice. Jenny brings out delicious food and they are eating. A raven stoops down for the food. Fred, Jenny, and Pebbles run away. 
Program:
OBJ0=SEG(image=IMAGE)
OBJ1=SELECT(image=IMAGE,object=OBJ0,query='man on the left',category=None)
IMAGE0=BGBLUR(image=IMAGE, object=OBJ1)
IMAGE1=ADDCHAR(image=IMAGE0,object=OBJ1,char='cloud')
OBJ2=SEG(image=IMAGE1)
OBJ3=SELECT(image=IMAGE1,object=OBJ2, query='cloud',category=None)
IMAGE2=ADDCHAR(image=IMAGE1,object=OBJ3,char='curry_rice')
IMAGE3=IMGEDIT(image=IMAGE, src_prompt='Fred, jenny and the baby are talking in the woods', target_prompt='Fred, jenny and the baby are eating in the woods', seed = 7, w1 = 1)
IMAGE4=IMGEDIT(image=IMAGE3, src_prompt='Fred, jenny and the baby are eating in the woods', target_prompt='Fred, jenny and the baby getting attacked by scary crows in the woods', seed = 2, w1 = 1)
IMAGE5=IMGEDIT(image=IMAGE4, src_prompt='Fred, jenny and the baby getting attacked by scary crows in the woods', target_prompt='Fred, jenny and the baby are running away from the crows in the woods', seed = 12397, w1 = 1.2)
STORY=STORYTEXT(query="Fred, Jenny, and baby Pebbles are sitting in the woods. Fred is daydreaming about curry rice. Jenny brings out delicious food and they are eating. A raven stoops down for the food. Fred, Jenny and baby run Pebbles away.")
STORY_TEXT_RESULT=RESULT(var=STORY)
FINAL_RESULT=RESULT(var=IMAGE5)

Instruction: Visualize this story: Barney comes out from the cave hut. He sees a bear and runs away.
Program:
OBJ0=SEG(image=IMAGE)
OBJ1=SELECT(image=IMAGE,object=OBJ0,query='cave hut entry',category=None)
IMAGE1=ADDCHAR(image=IMAGE1,object=OBJ1,char='barney')
IMAGE2=IMGEDIT(image=IMAGE, src_prompt='Barney is outside the cave', target_prompt='Barney and bear are outside the cave', seed = 7, w1 = 1)
IMAGE3=IMGEDIT(image=IMAGE, src_prompt='Barney is standing outside the cave', target_prompt='Barney is running outside the cave', seed = 7, w1 = 1)
IMAGE4=REMOVE(image=IMAGE3, object="Barney man character")
STORY=STORYTEXT(query="Barney comes out from the cave hut. He sees a bear and runs away.")
STORY_TEXT_RESULT=RESULT(var=STORY)
FINAL_RESULT=RESULT(var=IMAGE4)

Instruction: Visualize this story: Pebbles is sitting in a baby chair and looking at her dinosaur toy. She tries to reach out to the toy but falls down. Wilma comes worried and picks her up.
Program:
IMAGE1=IMGEDIT(image=IMAGE, src_prompt='Pebbles is sitting in a baby chair', target_prompt='Pebbles is stretching out from her baby chair', seed = 7, w1 = 1)
IMAGE2=IMGEDIT(image=IMAGE1, src_prompt='Pebbles is stretching out from her baby chair', target_prompt='Pebbles is falling down from her baby chair', seed = 7, w1 = 1)
OBJ0=SEG(image=IMAGE2)
OBJ1=SELECT(image=IMAGE2,object=OBJ0,query='dinosaur toy',category=None)
IMAGE0=ADDCHAR(image=IMAGE2,object=OBJ1,char='wilma')
IMAGE4=IMGEDIT(image=IMAGE, src_prompt='Wilma is smiling', target_prompt='Wilma is worried', seed = 7, w1 = 1)
IMAGE5=IMGEDIT(image=IMAGE4, src_prompt='Wilma is worried', target_prompt='Wilma is picking up baby', seed = 7, w1 = 1)
STORY=STORYTEXT(query="Pebbles is sitting in a baby chair and looking at her dinosaur toy. She tries to reach out to the toy but falls down. Wilma comes worried and picks her up.")
STORY_TEXT_RESULT=RESULT(var=STORY)
FINAL_RESULT=RESULT(var=IMAGE5)

Instruction: Visualize this story: Pororo and his friends are dancing with a fairy in a rose garden. The fairy sprinkles magic dust on the roses and many butterflies appear. 
Program:
IMAGE1=IMGEDIT(image=IMAGE, src_prompt='Fairy is dancing', target_prompt='Fairy does magic', seed = 7, w1 = 1)
OBJ0=SEG(image=IMAGE1)
OBJ1=SELECT(image=IMAGE1,object=OBJ0,query='background',category=None)
IMAGE2=BGBLUR(image=IMAGE1, object=OBJ1)
IMAGE3=REPLACE(image=IMAGE1,object=OBJ1,prompt='magic dust')
OBJ2=SEG(image=IMAGE3)
OBJ1=SELECT(image=IMAGE3,object=OBJ2,query='flowers',category=None)
IMAGE4=REPLACE(image=IMAGE3,object=OBJ1,prompt='butterflies')
STORY = STORYTEXT(query="Pororo and his friends are dancing with a fairy in a rose garden. The fairy sprinkles magic dust on the roses and many butterflies appear.")
STORY_TEXT_RESULT=RESULT(var=STORY)
FINAL_RESULT=RESULT(var=IMAGE4)

Instruction: Visualize this story: Pororo and friends are dancing in the snow. Petty comes and joins them. They all make a snowman.
Program:
OBJ0=SEG(image=IMAGE)
OBJ1=SELECT(image=IMAGE,object=OBJ0,query='snow',category=None)
IMAGE1=ADDCHAR(image=IMAGE,object=OBJ1,char='petty')
IMAGE2=IMGEDIT(image=IMAGE, src_prompt='Pororo and friends are dancing in the snow', target_prompt='Pororo and friends are making a snowman', seed = 7, w1 = 1)
STORY = STORYTEXT(query="Pororo and friends are dancing in the snow. Petty comes and joins them. They all make a snowman.")
STORY_TEXT_RESULT=RESULT(var=STORY)
FINAL_RESULT=RESULT(var=IMAGE2)

Instruction: Visualize this story: Wilma, Barney and Betty are preparing for Fred's birthday. Wilma puts candles on the cake. Fred enters the room. He blows the candles.
Program:
IMAGE1=IMGEDIT(image=IMAGE, src_prompt='Everyone is around the cake', target_prompt='Everyone is around the cake with candles', seed = 7, w1 = 1)
OBJ0=SEG(image=IMAGE1)
OBJ1=SELECT(image=IMAGE1,object=OBJ0,query='cake',category=None)
IMAGE2=ADDCHAR(image=IMAGE1,object=OBJ1,char='fred')
IMAGE3=IMGEDIT(image=IMAGE, src_prompt='Fred enters the room', target_prompt='Fred is blowing the candles', seed = 7, w1 = 1)
STORY = STORYTEXT(query="Wilma, Barney and Betty are preparing for Fred's birthday. Wilma puts candles on the cake. Fred enters the room. He blows the candles.")
STORY_TEXT_RESULT=RESULT(var=STORY)
FINAL_RESULT=RESULT(var=IMAGE3)

Instruction: {instruction}
Program:
"""