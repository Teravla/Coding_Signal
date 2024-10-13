Manchester Coding Documentation
==============================

.. module:: manchester
   :synopsis: Implémentation du codage Manchester et de sa densité spectrale.

Introduction
============

Ce module fournit des fonctions pour générer un signal codé en Manchester et pour calculer sa densité spectrale de puissance.

Fonctions
=========

.. function:: manchester(bits)

   Génère un signal codé en Manchester à partir d'une chaîne de bits.

   :param bits: Liste de bits (0s et 1s) à coder.
   :return: Dictionnaire avec les temps et les niveaux de tension pour le signal Manchester.

   **Exemple:**

   >>> manchester([0, 1, 0, 1])
   {0.0: 1, 0.5: 0, 1.0: 0, 1.5: 1, 2.0: 0, 2.5: 1}

.. function:: manchester_spectral_density(f, Tb)

   Calcule la densité spectrale de puissance pour le signal codé en Manchester.

   :param f: Fréquences à évaluer.
   :param Tb: Durée d'un bit.
   :return: Valeurs de densité spectrale de puissance pour les fréquences données.

   **Exemple:**

   >>> f = np.linspace(0.01, 10, 100)
   >>> Tb = 1
   >>> manchester_spectral_density(f, Tb)

.. function:: plot_signals_manchester(bits)

   Trace le signal codé en Manchester et sa densité spectrale de puissance.

   :param bits: Liste de bits (0s et 1s) à coder.

   **Exemple:**

   >>> plot_signals_manchester([0, 1, 0, 1])

Exemple d'utilisation
=====================

Voici un exemple d'utilisation des fonctions fournies dans le module:

.. code-block:: python

   import numpy as np

   # Exemple de chaîne de bits
   bits = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]  
   plot_signals_manchester(bits)
