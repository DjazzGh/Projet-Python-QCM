import json

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
# Fonction pour manipuler les questions
def getscore(questions):
    correct =0
    for question in questions:
        print(f"  Question: {question['question']}")
        for option in question['options']:  
            print(f"    - {option}")
        choice = input("Choose ansewer :").lower()
        if choice == question['answer']:
            print("Correst answer!")
            correct +=1
        else:
            print(f"worng answer the correst one is {question['answer']}")
    print(f"your total correct answer {correct}/{len(questions)}")


# Récupérer les questions de la catégorie choisie
questions = get_category_questions('qcm.json', category_name)

# Afficher les questions si elles ont été trouvées
if questions:
    print(f"Questions for the category '{category_name.capitalize()}':")
    getscore(questions)
else:
    print(f"The category '{category_name}' doesn't exist.")  # Si la catégorie n'existe pas, affiche un message d'erreur


