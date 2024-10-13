import tkinter as tk
from tkinter import messagebox
from Bipolar import plot_bipolar_signals
from Manchester import plot_signals_manchester
from Miller import plot_signals
from NRZ import plot_nrz
from NRZi import plot_nrzi

def generate_signal(coding_type, bit_string):
    try:
        bits = [int(bit) for bit in bit_string]  # Convertir la chaîne en liste de bits
    except ValueError:
        messagebox.showerror("Erreur", "La chaîne de bits doit contenir uniquement des 0 et des 1.")
        return

    if coding_type == "Bipolar":
        plot_bipolar_signals(bits)
    elif coding_type == "Manchester":
        plot_signals_manchester(bits)
    elif coding_type == "Miller":
        plot_signals(bits)
    elif coding_type == "NRZ":
        plot_nrz(bits)
    elif coding_type == "NRZi":
        plot_nrzi(bits)
    else:
        messagebox.showerror("Erreur", "Codage non supporté.")

def on_submit():
    coding_type = var.get()
    bit_string = bit_entry.get()
    
    if coding_type and bit_string:
        if all(bit in '01' for bit in bit_string):  # Vérifier que la chaîne contient seulement des 0 et des 1
            generate_signal(coding_type, bit_string)
        else:
            messagebox.showwarning("Avertissement", "La chaîne doit contenir uniquement des 0 et des 1.")
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner un type de codage et entrer une chaîne de bits.")

def center_window(root, width=400, height=350):
    # Dimensions de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcul des coordonnées x et y pour centrer la fenêtre
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Positionner la fenêtre au centre
    root.geometry(f'{width}x{height}+{x}+{y}')

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Sélection du Codage")

# Centrer la fenêtre
center_window(root)

# Label d'instruction
label = tk.Label(root, text="Sélectionnez le type de codage pour générer le signal :")
label.pack(pady=10)

# Boutons radio pour les types de codage, avec "Bipolar" sélectionné par défaut
var = tk.StringVar(value="Bipolar")  # "Bipolar" est sélectionné par défaut

codings = [("Bipolar", "Bipolar"), 
           ("Manchester", "Manchester"), 
           ("Miller", "Miller"), 
           ("NRZ", "NRZ"), 
           ("NRZi", "NRZi")]

for text, value in codings:
    tk.Radiobutton(root, text=text, variable=var, value=value).pack(anchor=tk.W)

# Champ d'entrée pour la chaîne de bits
bit_label = tk.Label(root, text="Entrez une chaîne de bits (ex : 0101011) :")
bit_label.pack(pady=10)

bit_entry = tk.Entry(root)
bit_entry.pack(pady=5)

# Bouton pour soumettre la sélection
submit_button = tk.Button(root, text="Générer le signal", command=on_submit)
submit_button.pack(pady=20)

# Lancement de la boucle principale
root.mainloop()
