"""
:mod:`Miller` module
:auteur: MENON Valentin
:date: 2024, October

Ce module contient les fonctions pour générer un signal codé en Miller à partir d'une chaîne de bits et calculer sa densité spectrale de puissance.

:function miller: Génère un signal codé en Miller à partir d'une chaîne de bits.
:function miller_spectral_density: Calcule la densité spectrale de puissance pour le signal codé en Miller.
:function plot_signals: Trace le signal codé en Miller et sa densité spectrale de puissance.
"""

import numpy as np
import matplotlib.pyplot as plt

def miller(bits):
    """
    Génère un signal codé en Miller à partir d'une chaîne de bits.

    :param bits: Liste de bits (0s et 1s) à coder.
    :return: Dictionnaire avec les temps et les niveaux de tension pour le signal Miller.

    **Exemple:**
    
    >>> miller([0, 1, 0, 1])
    {0.0: 1, 0.5: -1, 1.0: -1, 1.5: 1, 2.0: 0, 2.5: 0}
    """
    miller_dict = {}  # Dictionnaire pour stocker les valeurs de Miller
    last_level = 1  # Niveau initial
    time = 0.0  # Temps initial

    for i, bit in enumerate(bits):
        if bit == 1:
            # Bit '1' : transition au milieu de la période de bit
            miller_dict[time] = last_level  # Premier niveau du bit
            time += 0.5  # Avancer le temps pour la transition
            last_level = -last_level  # Changer le niveau
            miller_dict[time] = last_level  # Deuxième niveau
            time += 0.5  # Avancer le temps à la fin du bit
        else:  # Bit '0'
            if i > 0 and bits[i - 1] == 1:
                # Si le bit précédent était '1', pas de transition
                miller_dict[time] = last_level  # Premier niveau du bit
                time += 0.5  # Avancer le temps pour le milieu
                # Pas de transition au milieu
                miller_dict[time] = last_level  # Deuxième niveau (pas de transition)
                time += 0.5  # Avancer le temps à la fin du bit
            else:
                # Si le bit précédent était aussi '0', on inverse la polarité
                last_level = -last_level
                miller_dict[time] = last_level  # Premier niveau du bit
                time += 0.5  # Avancer le temps pour le milieu
                # Pas de transition au milieu
                miller_dict[time] = last_level  # Deuxième niveau (pas de transition)
                time += 0.5  # Avancer le temps à la fin du bit

    return miller_dict

def miller_spectral_density(f, Tb):
    """
    Calcule la densité spectrale de puissance pour le signal codé en Miller.

    :param f: Fréquences à évaluer.
    :param Tb: Durée d'un bit.
    :return: Valeurs de densité spectrale de puissance pour les fréquences données.

    **Exemple:**
    
    >>> f = np.linspace(0.01, 10, 100)
    >>> Tb = 1
    >>> miller_spectral_density(f, Tb)
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        return Tb * (1 - np.cos(2 * np.pi * f * Tb)) * ((1 - np.cos(np.pi * f * Tb)) / ((np.pi * f * Tb)**2))

def plot_signals(bits):
    """
    Trace le signal codé en Miller et sa densité spectrale de puissance.

    :param bits: Liste de bits (0s et 1s) à coder.

    **Exemple:**
    
    >>> plot_signals([0, 1, 0, 1])
    """
    Tb = 1  # Durée d'un bit
    n = len(bits) / 2  # Correction ici pour le nombre de bits
    f = np.linspace(0.01, n, 1000)  # Fréquence pour la densité spectrale

    # Générer le signal
    miller_dict = miller(bits)

    # Conversion du dictionnaire en deux listes pour le tracé
    time_signal = list(miller_dict.keys())
    signal_rep = list(miller_dict.values())

    # Tracer le signal
    plt.figure(figsize=(12, 6))

    # Tracer le signal Miller
    plt.subplot(2, 1, 1)
    plt.step(time_signal, signal_rep, where='post', linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlim(-0.5, len(bits) - 0.5)  # Ajuster les limites pour centrer sur les bits
    plt.xticks(np.arange(len(bits)), bits)  # Étiquettes correspondant à la chaîne de bits
    plt.title('Signal Miller')
    plt.ylabel('Tension')
    plt.xlabel('Bits')
    plt.grid(True)

    # Calcul de la densité spectrale de puissance
    dsp = miller_spectral_density(f, Tb)

    # Vérification des valeurs NaN ou Inf dans dsp
    if np.any(np.isnan(dsp)) or np.any(np.isinf(dsp)):
        print("Des valeurs NaN ou Inf ont été détectées dans le tableau de la densité spectrale.")

    # Tracer la densité spectrale de puissance
    plt.subplot(2, 1, 2)
    plt.plot(f, dsp, label="DSP du codage Miller", color='b')
    plt.title('Densité Spectrale Miller')
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
    plot_signals(bits)
