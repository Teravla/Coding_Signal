bipolar Coding Documentation
================

Ce module fournit des fonctions pour générer et visualiser des signaux bipolaires ainsi que leur densité spectrale de puissance.

Fonctions
---------

.. function:: bipolar(bits)

    Génère un signal bipolaire à partir d'une chaîne de bits.

    :param bits: Liste de bits (0s et 1s) à coder.
    :return: Liste de niveaux de tension pour le signal bipolaire.

    **Exemple:**

    >>> bipolar([0, 1, 0, 1, 0])
    [0, 1, 0, -1, 0]

.. function:: bipolar_spectral_density(f, Tb)

    Calcule la densité spectrale de puissance pour le signal bipolaire.

    :param f: Fréquences à évaluer.
    :param Tb: Durée d'un bit.
    :return: Valeurs de densité spectrale de puissance pour les fréquences données.

    **Exemple:**

    >>> f = np.linspace(0.01, 10, 100)
    >>> Tb = 1
    >>> bipolar_spectral_density(f, Tb)

.. function:: plot_bipolar_signals(bits)

    Trace le signal bipolaire et sa densité spectrale de puissance.

    :param bits: Liste de bits (0s et 1s) à coder.
    
    **Exemple:**

    >>> plot_bipolar_signals([0, 1, 0, 1, 0])

Exemple d'utilisation
----------------------

Voici un exemple d'utilisation des fonctions du module :

.. code:: python

    import numpy as np
    from bipolar_signals import plot_bipolar_signals

    bits = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]  # Chaine de bits
    plot_bipolar_signals(bits)
