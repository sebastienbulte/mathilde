import streamlit as st

st.set_page_config(page_title="Calculatrice de coût d'outil", page_icon="💰", layout="centered")

st.title("💰 Calculatrice de coût d’un outil")

# Prix par crédit (par défaut 10 €)
prix_par_credit = st.number_input("Prix par crédit (€)", min_value=0.0, value=10.0, step=0.5)

# Nombre de crédits
nb_credits = st.number_input("Nombre de crédits", min_value=1, value=1, step=1)

# Calcul du coût total
cout_total = nb_credits * prix_par_credit

# Affichage
st.markdown("---")
st.subheader("🧮 Résultat")
st.metric(label="Coût total", value=f"{cout_total:.2f} €")

st.markdown(f"➡️ {int(nb_credits)} crédit(s) × {prix_par_credit:.2f} € = **{cout_total:.2f} €**")
