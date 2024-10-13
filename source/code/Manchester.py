"""
:mod:`Manchester` module
:auteur: MENON Valentin
:date: 2024, October

Ce module contient les fonctions pour générer un signal codé en Manchester à partir d'une chaîne de bits et calculer sa densité spectrale de puissance.

:function manchester: Génère un signal codé en Manchester à partir d'une chaîne de bits.
:function manchester_spectral_density: Calcule la densité spectrale de puissance pour le signal codé en Manchester.
:function plot_signals_manchester: Trace le signal codé en Manchester et sa densité spectrale de puissance.
"""

import numpy as np
import matplotlib.pyplot as plt

def manchester(bits):
    """
    Génère un signal codé en Manchester à partir d'une chaîne de bits.

    :param bits: Liste de bits (0s et 1s) à coder.
    :return: Dictionnaire avec les temps et les niveaux de tension pour le signal Manchester.
    
    **Exemple:**
    
    >>> manchester([0, 1, 0, 1])
    {0.0: 1, 0.5: 0, 1.0: 0, 1.5: 1, 2.0: 0, 2.5: 1}
    """
    manchester_dict = {}  # Dictionnaire pour stocker les niveaux de Manchester
    last_level = 1  # Niveau initial
    time = 0.0  # Temps initial

    for i, bit in enumerate(bits):
        if bit == 1:
            # Bit '1' : transition au milieu de la période de bit
            manchester_dict[time] = last_level  # Premier niveau du bit
            time += 0.5  # Avancer le temps pour la transition
            last_level = 0  # Transition vers 0
            manchester_dict[time] = last_level  # Deuxième niveau
            time += 0.5  # Avancer le temps à la fin du bit
            last_level = 1  # Remettre le niveau pour le prochain bit
        else:  # Bit '0'
            manchester_dict[time] = last_level  # Premier niveau du bit
            time += 0.5  # Avancer le temps pour la transition
            last_level = 1  # Transition vers 1
            manchester_dict[time] = last_level  # Deuxième niveau
            time += 0.5  # Avancer le temps à la fin du bit
            last_level = 0  # Remettre le niveau pour le prochain bit

    return manchester_dict

def manchester_spectral_density(f, Tb):
    """
    Calcule la densité spectrale de puissance pour le signal codé en Manchester.

    :param f: Fréquences à évaluer.
    :param Tb: Durée d'un bit.
    :return: Valeurs de densité spectrale de puissance pour les fréquences données.

    **Exemple:**

    >>> f = np.linspace(0.01, 10, 100)
    >>> Tb = 1
    >>> manchester_spectral_density(f, Tb)
    """
    return Tb * (((np.sin(np.pi * f * (Tb / 2)))**4) / ((np.pi * f * (Tb / 2))**2))

def plot_signals_manchester(bits):
    """
    Trace le signal codé en Manchester et sa densité spectrale de puissance.

    :param bits: Liste de bits (0s et 1s) à coder.

    **Exemple:**

    >>> plot_signals_manchester([0, 1, 0, 1])
    """
    Tb = 1  # Durée d'un bit
    n = len(bits) / 2  # Correction ici pour le nombre de bits
    f = np.linspace(0.01, n, 1000)  # Fréquence pour la densité spectrale

    # Générer le signal
    manchester_dict = manchester(bits)

    # Conversion du dictionnaire en deux listes pour le tracé
    time_signal = list(manchester_dict.keys())
    signal_rep = list(manchester_dict.values())

    # Tracer le signal
    plt.figure(figsize=(12, 6))

    # Tracer le signal Manchester
    plt.subplot(2, 1, 1)
    plt.step(time_signal, signal_rep, where='post', linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlim(-0.5, len(bits) - 0.5)  # Ajuster les limites pour centrer sur les bits
    plt.xticks(np.arange(len(bits)), bits)  # Étiquettes correspondant à la chaîne de bits
    plt.title('Signal Manchester')
    plt.ylabel('Tension')
    plt.xlabel('Bits')
    plt.grid(True)

    # Calcul de la densité spectrale de puissance
    dsp = manchester_spectral_density(f, Tb)

    # Vérification des valeurs NaN ou Inf dans dsp
    if np.any(np.isnan(dsp)) or np.any(np.isinf(dsp)):
        print("Des valeurs NaN ou Inf ont été détectées dans le tableau de la densité spectrale.")

    # Tracer la densité spectrale de puissance
    plt.subplot(2, 1, 2)
    plt.plot(f, dsp, label="DSP du codage Manchester", color='b')
    plt.title('Densité Spectrale Manchester')
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
    plot_signals_manchester(bits)
