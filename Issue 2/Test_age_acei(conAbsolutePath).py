import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, entropy

# === Caricamento file ===
# Carica i due file MIMIC reali
df_age = pd.read_csv("/Users/grazianicoletti/Desktop/Dottorato ING-INF/Asclepyus/Task/Demo 19 maggio/Issue 2/mimiciv_3_1_derived_export_age_data.csv")
df_acei = pd.read_csv("/Users/grazianicoletti/Desktop/Dottorato ING-INF/Asclepyus/Task/Demo 19 maggio/Issue 2/mimiciv_3_1_derived_export_acei_data.csv")

# === Estraggo solo un campione ridotto per ogni campo (conceptual) ===
# Estrae solo 10 valori casuali da ciascun campo
age_sample = df_age['age'].dropna().sample(10, random_state=1)
acei_sample = df_acei['acei'].dropna().sample(10, random_state=1)

# === Calcolo alcune statistiche di base per 'age' ===
# Calcola: count, unique, mean, median, std_dev, min, max, skewness, kurtosis
print("\n===== SAMPLE AGE VALUES =====")
print(age_sample.tolist())

print("\n===== BASIC STATISTICS AGE =====")
print(f"Count: {len(age_sample)}")
print(f"Unique: {age_sample.nunique()}")
print(f"Mean: {age_sample.mean():.2f}")
print(f"Median: {age_sample.median():.2f}")
print(f"Std Dev: {age_sample.std():.2f}")
print(f"Min: {age_sample.min()}")
print(f"Max: {age_sample.max()}")
print(f"Skewness: {skew(age_sample):.4f}")
print(f"Kurtosis: {kurtosis(age_sample):.4f}")

# === Calcolo alcune statistiche di base per 'acei' ===
# Calcola: count, unique, moda, frequenze nel sample, entropia
print("\n===== SAMPLE ACEI VALUES =====")
print(acei_sample.tolist())

print("\n===== BASIC STATISTICS ACEI =====")
print(f"Count: {len(acei_sample)}")
print(f"Unique: {acei_sample.nunique()}")
mode_acei = acei_sample.mode().iloc[0]
print(f"Mode: {mode_acei}")
print(f"Mode Frequency: {(acei_sample == mode_acei).sum()}")

# Frequenze di tutte le categorie nel sample
category_counts = acei_sample.value_counts()
print(f"Category Frequencies:\n{category_counts.to_dict()}")

# Entropia (solo a livello concettuale sul sample)
probs = category_counts / category_counts.sum()
print(f"Entropy (sample level): {round(entropy(probs, base=2), 4)}")

# Output:
# Stampa tutto in modo leggibile direttamente nel terminale



