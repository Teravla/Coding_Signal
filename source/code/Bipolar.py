"""
:mod:`Bipolar` module
:auteur: MENON Valentin
:date: 2024, October

Ce module contient les fonctions pour générer un signal bipolaire à partir d'une chaîne de bits et calculer sa densité spectrale de puissance.

:function bipolar: Génère un signal bipolaire à partir d'une chaîne de bits.
:function bipolar_spectral_density: Calcule la densité spectrale de puissance pour le signal bipolaire.
:function plot_bipolar_signals: Trace le signal bipolaire et sa densité spectrale de puissance.
"""


import numpy as np
import matplotlib.pyplot as plt

def bipolar(bits):
    """
    Génère un signal bipolaire à partir d'une chaîne de bits.

    :param bits: Liste de bits (0s et 1s) à coder.
    :return: Liste de niveaux de tension pour le signal bipolaire.

    **Exemple:**

    >>> bipolar([0, 1, 0, 1, 0])
    [0, 1, 0, -1, 0]
    """
    bipolar_code = []
    last_one = 1
    for bit in bits:
        if bit == 1:
            bipolar_code.append(last_one)
            last_one = -last_one
        else:
            bipolar_code.append(0)
    return bipolar_code

def bipolar_spectral_density(f, Tb):
    """
    Calcule la densité spectrale de puissance pour le signal bipolaire.

    :param f: Fréquences à évaluer.
    :param Tb: Durée d'un bit.
    :return: Valeurs de densité spectrale de puissance pour les fréquences données.

    **Exemple:**

    >>> f = np.linspace(0.01, 10, 100)
    >>> Tb = 1
    >>> bipolar_spectral_density(f, Tb)
    """
    return (Tb * np.sin(np.pi * f * Tb)**2) * ((np.sin(f * Tb * np.pi)) / (np.pi * f * Tb))**2

def plot_bipolar_signals(bits):
    """
    Trace le signal bipolaire et sa densité spectrale de puissance.

    :param bits: Liste de bits (0s et 1s) à coder.

    **Exemple:**

    >>> plot_bipolar_signals([0, 1, 0, 1, 0])
    """
    Tb = 1  # Durée d'un bit
    n = len(bits) / 2  # Correction ici pour le nombre de bits
    f = np.linspace(0.01, n, 1000)  # Fréquence pour la densité spectrale

    # Générer le signal
    bipolar_signal = bipolar(bits)

    # Tracer le signal
    plt.figure(figsize=(12, 6))

    # Tracer le signal bipolaire
    plt.subplot(2, 1, 1)
    plt.step(range(len(bipolar_signal)), bipolar_signal, where='post', linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlim(-0.5, len(bits) - 0.5)  # Ajuster les limites pour centrer sur les bits
    plt.xticks(np.arange(len(bits)), bits)  # Étiquettes correspondant à la chaîne de bits
    plt.title('Signal Bipolaire')
    plt.ylabel('Tension')
    plt.xlabel('Bits')
    plt.grid(True)

    # Calcul de la densité spectrale de puissance
    dsp = bipolar_spectral_density(f, Tb)

    # Vérification des valeurs NaN ou Inf dans dsp
    if np.any(np.isnan(dsp)) or np.any(np.isinf(dsp)):
        print("Des valeurs NaN ou Inf ont été détectées dans le tableau de la densité spectrale.")

    # Tracer la densité spectrale de puissance
    plt.subplot(2, 1, 2)
    plt.plot(f, dsp, label="DSP du codage Bipolaire", color='b')
    plt.title('Densité Spectrale Bipolaire')
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Densité Spectrale de Puissance")
    plt.grid(True)
    plt.xlim(0, n)  # Limiter l'axe x pour la plage spécifiée
    plt.ylim(0, np.max(dsp) * 1.1)  # Ajuster l'axe y pour montrer toute la courbe

    # Définir les ticks sur l'axe des x
    plt.xticks(np.arange(0, n + 1, 1/(2 * Tb)))

    plt.tight_layout()
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    bits = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]  # Chaine de bits
    plot_bipolar_signals(bits)
