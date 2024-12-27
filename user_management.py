import json
from datetime import datetime

def load_questions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def is_user_exist(name,password):
    users= load_questions('users.json')
    found=False
    for i in range(1,len(users["users"])):
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
      
# fonction pour afficher l'historique
def display_history(username):
    users = load_questions('users.json')
    if username in users:
        print(f"\n{username}'s History:")
        for history in users[username]["history"]:
            print(f"- Date: {history['date']}, Score: {history['score']}/{history['total']} of category: {history['category_name']} ")
    print()

# fonction pour sauvgarder l'utilisateur dans le fichier json
def save_users(users):
    with open("users.json", 'w') as f:
        json.dump(users, f, indent=4)

# fonction pour sauvgarder l'historique
def save_score( score, username, password,questions,numb_question,category_name):
    users = load_questions('users.json')
    
    if username not in users:
        users[username] = {"password":password,"history": []}
        
    test_result = {
        "category_name":category_name,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "score": score,
        "total": numb_question,
    }
    users[username]["history"].append(test_result)
    save_users(users)







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
            
    
   

