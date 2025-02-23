import pandas as pd
import main

path = "S08_question_answer_pairs.txt"
df = pd.read_csv(path, delimiter='\t')
print(df.head())

length = df['ArticleTitle'].shape[0]

for i in range(int(length)): 
    question =  str(df.iloc[i,1])
    answer = str(df.iloc[i,2] )
    if not question.isspace() and not answer.isspace():
        if question != "NOTTTT  FOUND" and question != "NULL" and answer!= "nan":
            main.chat_bot_train(question, answer)

