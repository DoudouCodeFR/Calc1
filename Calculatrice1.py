def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : Division par zéro impossible."
    return a / b

def calculatrice():
    print("Bienvenue dans la calculatrice !")
    
    while True:
        try:
            # Demande des nombres à l'utilisateur
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
            
            # Demande de l'opération
            operation = input("Choisissez une opération (+, -, *, /) : ")
            
            # Calcul en fonction de l'opération choisie
            if operation == "+":
                result = addition(num1, num2)
            elif operation == "-":
                result = soustraction(num1, num2)
            elif operation == "*":
                result = multiplication(num1, num2)
            elif operation == "/":
                result = division(num1, num2)
            else:
                print("Opération invalide. Veuillez choisir parmi (+, -, *, /).")
                continue
            
            # Affichage du résultat
            print(f"Résultat : {num1} {operation} {num2} = {result}")
        
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            continue

        # Demander si l'utilisateur veut continuer
        choix = input("Voulez-vous faire une autre opération ? (oui/non) : ").lower()
        if choix != "oui":
            print("Merci d'avoir utilisé la calculatrice !")
            break

# Lancer la calculatrice
calculatrice()
