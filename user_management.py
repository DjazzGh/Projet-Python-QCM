import json
def load_questions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def is_user_exist(name,password):
    users= load_questions('users.json')
    found=False
    i=1
    for i in range(len(users["users"])):
       if users["users"][i]["name"] == name and users["users"][i]["password"] == password:
          found = True
    return found 
def create_new_profile(name,password):
   new_user = {
    "name": name,
    "password":password,
    "scores":[]



}
   users= load_questions('users.json') 
   users['users'].append(new_user)
  

   with open('users.json', 'w') as file:
      json.dump(users,file, indent=4)




def save_score_and_questions(date, score, name, password,questions):
     users = load_questions('users.json')
    
     for user in users["users"]:
        if user["name"] == name and user["password"] == password:
           
         new_scores={
                    "score":score,
                    "date":date,
                    "questions": [
                     questions
                    ]
                }   
         break
     user['scores'].append(new_scores)

     with open('users.json', 'w') as file:
                json.dump(users, file, indent=4)






def display_scores_and_questions(name, password):
    users = load_questions('users.json')
    
    for user in users["users"]:
       
        if user["name"] == name and user["password"] == password:
           
            print("{name}'s score historic ")
            
            for score in user["scores"]:
                print(f"Date : {score['date']}, Score : {score['score']}")
                print("Questions and answers :")
                
            
                if isinstance(score["questions"], list):
                    for question in score["questions"]:
                        # Check if the item is a list or dictionary
                        if isinstance(question, list):
                            for q in question:  
                                print(f"- Question: {q.get('question', '').strip()}")
                                print(f"  Answer: {q.get('answer', '')}")
                        elif isinstance(question, dict):
                            print(f"- Question: {question.get('question', '').strip()}")
                            print(f"  Answer: {question.get('answer', '')}")
            
    
   


