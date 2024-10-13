"""
:mod:`NRZ` module
:auteur: MENON Valentin
:date: 2024, October

Ce module contient les fonctions pour générer un signal NRZ à partir d'une chaîne de bits et calculer sa densité spectrale de puissance.

:function nrz: Génère un signal NRZ à partir d'une chaîne de bits.
:function nrz_spectral_density: Calcule la densité spectrale de puissance pour le signal NRZ.
:function plot_nrz: Trace le signal NRZ et sa densité spectrale de puissance.
"""

import numpy as np
import matplotlib.pyplot as plt

def nrz(bits):
    """
    Génère un signal NRZ à partir d'une chaîne de bits.

    :param bits: Liste de bits (0s et 1s) à coder.
    :return: Un tuple contenant le temps et le signal NRZ sous forme de tableau.

    **Exemple:**
    
    >>> nrz([0, 1, 0, 1])
    (array([0.  , 0.01, 0.02, ...]), array([-1,  1, -1, ...]))
    """
    signal = []
    for bit in bits:
        signal.append(1 if bit == 1 else -1)  # 1 en haute tension, 0 en basse
    samples_per_bit = 100
    signal_rep = np.repeat(signal, samples_per_bit)
    time = np.linspace(0, len(bits), len(signal_rep))
    return time, signal_rep

def nrz_spectral_density(f, Tb):
    """
    Calcule la densité spectrale de puissance pour le signal NRZ.

    :param f: Fréquences à évaluer.
    :param Tb: Durée d'un bit.
    :return: Valeurs de densité spectrale de puissance pour les fréquences données.

    **Exemple:**
    
    >>> f = np.linspace(0.01, 10, 100)
    >>> Tb = 1
    >>> nrz_spectral_density(f, Tb)
    """
    return (Tb**2) * (np.sinc(f * Tb))**2

def plot_nrz(bits):
    """
    Trace le signal NRZ et sa densité spectrale de puissance.

    :param bits: Liste de bits (0s et 1s) à coder.

    **Exemple:**
    
    >>> plot_nrz([0, 1, 0, 1])
    """
    Tb = 1  # Durée d'un bit
    n = len(bits)/4
    f = np.linspace(0.01, n, 1000)  # Fréquence pour la densité spectrale

    # Générer le signal NRZ
    time_signal, signal_rep = nrz(bits)

    # Tracer le signal NRZ
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time_signal, signal_rep, linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlim(-0.5, n)  # Ajuster les limites pour centrer sur les bits
    plt.xticks(np.arange(len(bits)), bits)  # Étiquettes correspondant à la chaîne de bits
    plt.title('Signal NRZ')
    plt.ylabel('Tension')
    plt.xlabel('Bits')
    plt.grid(True)

    # Calcul de la densité spectrale de puissance NRZ
    dsp = nrz_spectral_density(f, Tb)

    # Vérification des valeurs NaN ou Inf dans dsp
    if np.any(np.isnan(dsp)) or np.any(np.isinf(dsp)):
        print("Des valeurs NaN ou Inf ont été détectées dans le tableau de la densité spectrale.")

    # Tracer la densité spectrale de puissance
    plt.subplot(2, 1, 2)
    plt.plot(f, dsp, label="DSP du codage NRZ", color='b')
    plt.title('Densité Spectrale NRZ')
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
    plot_nrz(bits)
