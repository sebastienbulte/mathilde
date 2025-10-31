import tkinter as tk
from tkinter import ttk

def calculer_cout():
    try:
        nb_credits = int(entry_credits.get())
        cout_unitaire = float(entry_prix_unitaire.get())
        total = nb_credits * cout_unitaire
        label_resultat.config(text=f"Coût total : {total:.2f} €")
    except ValueError:
        label_resultat.config(text="⚠️ Entrez des nombres valides.")

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice de coût d'outil")

# Prix unitaire (par défaut 10 €)
tk.Label(fenetre, text="Prix par crédit (€) :").grid(row=0, column=0, padx=10, pady=10)
entry_prix_unitaire = tk.Entry(fenetre)
entry_prix_unitaire.insert(0, "10")
entry_prix_unitaire.grid(row=0, column=1, padx=10, pady=10)

# Nombre de crédits
tk.Label(fenetre, text="Nombre de crédits :").grid(row=1, column=0, padx=10, pady=10)
entry_credits = tk.Entry(fenetre)
entry_credits.insert(0, "1")
entry_credits.grid(row=1, column=1, padx=10, pady=10)

# Bouton de calcul
btn_calculer = ttk.Button(fenetre, text="Calculer", command=calculer_cout)
btn_calculer.grid(row=2, column=0, columnspan=2, pady=10)

# Résultat
label_resultat = tk.Label(fenetre, text="Coût total : 0.00 €", font=("Arial", 12, "bold"))
label_resultat.grid(row=3, column=0, columnspan=2, pady=10)

fenetre.mainloop()
