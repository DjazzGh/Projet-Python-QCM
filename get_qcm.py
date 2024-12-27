import json
import random

from user_management import save_score ,display_history
# Fonction pour charger les questions depuis un fichier JSON
def load_questions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)



# Fonction pour obtenir les questions d'une catégorie spécifique
def get_category_questions(file_path, category_name):
    data = load_questions(file_path)  # Charge les données depuis le fichier
    return data.get(category_name, None)  # Récupère les questions de la catégorie demandée, ou None si la catégorie n'existe pas

# Fonction pour afficher les catégories disponibles
def show_categories(file_path):
    data = load_questions(file_path)  
    return list(data.keys())  # Récupère toutes les clés (noms des catégories) et les retourne sous forme de liste

# Function pour filtrer les difficultes par questions
def filter_questions_by_difficulty(questions, difficulty):
    return [q for q in questions if q['difficulty'] == difficulty]

# Function pour choisir des questions au hasard
def select_random_questions(questions, num_questions):
    return random.sample(questions, num_questions)

# Fonction pour manipuler les questions
def getscore(questions,username,password,category_name,numb_question, difficulty):
    correct =0
    if difficulty != "random":
        questions = filter_questions_by_difficulty(questions, difficulty)

    if difficulty == "random":
        questions = select_random_questions(questions, numb_question)
        
    for question in questions[:numb_question]:
        print(f"  Question: {question['question']}")
        for option in question['options']:  
            print(f"    - {option}")
        while True:
            choice = input("Choose answer (a, b, c, or d): ").lower()
            if choice in ['a', 'b', 'c', 'd']:
                break  # Valid input, exit the loop
            else:
                print("Invalid choice. Please enter 'a', 'b', 'c', or 'd'.")
        if choice == question['answer']:
            print("Correst answer!")
            correct +=1
        else:
            print(f"wrong answer the correst one is {question['answer']}")
    save_score( correct, username, password,questions,numb_question,category_name)
    print(f"your total correct answer {correct}/{numb_question}")


users = load_questions('users.json')
username = input("\nEnter your username: ")
password = input("\nEnter your password: ")

if  username in users:
    display_history(username)
else:
    print("\nWelcome new user!")
 
# Afficher les catégories disponibles
categories = show_categories('qcm.json')  
print("The categories available :")
for i, category in enumerate(categories, start=1):  # Affiche les catégories avec un index
    print(f"{i}. {category.capitalize()}")  # Affiche chaque catégorie avec une numérotation


# Demander à l'utilisateur de choisir une catégorie
while True:
    try:
        category_index = int(input("Choose the number of the category: ")) - 1  
        if 0 <= category_index < len(categories): 
            category_name = categories[category_index]  
            break  
        else:
            print("Invalid number. Please choose a valid category number.")  
    except ValueError:
        print("Invalid input. Please enter a number.") 
# Récupérer les questions de la catégorie choisie
questions = get_category_questions('qcm.json', category_name)

# Afficher les questions si elles ont été trouvées
if questions:
    difficulty_options = ["easy", "medium", "hard", "random"]
    print("Choose difficulty level:")
    for i, level in enumerate(difficulty_options, start=1):
        print(f"{i}. {level.capitalize()}")
    while True:
        try:
            difficulty_choice = int(input("Choose the number for difficulty level: ")) - 1
            if 0 <= difficulty_choice < len(difficulty_options):
                difficulty = difficulty_options[difficulty_choice]
                break
            else:
                print("Invalid number. Please choose a valid difficulty.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask for the number of questions based on difficulty
    if difficulty == "random":
        while True:
            try:
                numb_question = int(input("How many random questions would you like to answer (1-15)? "))
                if 1 <= numb_question <= 15:
                    break
                else:
                    print("Please choose between 1 and 15.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        while True:
            try:
                numb_question = int(input(f"How many questions would you like to answer (1-5) for {difficulty} difficulty? "))
                if 1 <= numb_question <= 5:
                    break
                else:
                    print("Please choose between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    print(f"Questions for the category '{category_name.capitalize()}' and difficulty '{difficulty.capitalize()}':"")
    getscore(questions,username,password,category_name,numb_question, difficulty)
else:
    print(f"The category '{category_name}' doesn't exist.")  # Si la catégorie n'existe pas, affiche un message d'erreur

