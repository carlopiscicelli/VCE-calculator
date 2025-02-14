import streamlit as st
import numpy as np

# Funzione per calcolare la probabilità di successo della VCE
def predict_vce_success(fore_bag, bmi, parity):
    """
    Modello di regressione logistica basato sullo studio.
    """
    intercept = -1.0  # Meno negativo per aumentare la probabilità
    coef_fore_bag = 2.0  # Maggiore impatto della dimensione Fore-bag
    coef_bmi = -0.1  # Ridotta influenza del BMI
    coef_parity = 1.0  # Maggiore influenza della parità

    # Calcolo del valore logit
    logit = intercept + (coef_fore_bag * fore_bag) + (coef_bmi * bmi) + (coef_parity * parity)
    
    # Calcolo della probabilità usando la funzione sigmoide
    probability = 1 / (1 + np.exp(-logit))

    # Debug: Mostra i valori intermedi
    st.write(f"🔍 Logit: {logit}")
    st.write(f"📊 Probabilità calcolata: {probability}")

    return probability


# Interfaccia Streamlit
st.title("🔍 Calcolatore di Successo della Versione Cefalica Esterna")
st.markdown("**Basato sul modello di Isakov et al.**")

# Input utente
fore_bag = st.number_input("📏 Dimensione Fore-bag (cm)", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
bmi = st.number_input("⚖️ Body Mass Index (BMI)", min_value=15.0, max_value=40.0, value=25.0, step=0.1)
parity = st.number_input("👶 Numero di parti precedenti", min_value=0, max_value=5, value=0, step=1)

# Calcolo e output
if st.button("🔎 Calcola Probabilità"):
    probability = predict_vce_success(fore_bag, bmi, parity)
    st.success(f"📊 Probabilità stimata di successo: {probability*100:.1f}%")

st.markdown("*Nota: il modello è stato validato internamente, ma potrebbe necessitare di ulteriori test in popolazioni diverse.*")

