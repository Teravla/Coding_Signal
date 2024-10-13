Miller Coding Documentation
===========================

Cette documentation couvre les fonctions utilisées pour générer un signal codé en Miller à partir d'une chaîne de bits et pour calculer et tracer la densité spectrale de puissance correspondante.

.. module:: miller
   :synopsis: Module pour le codage Miller et la visualisation.

Fonctions
---------

.. function:: miller(bits)

   Génère un signal codé en Miller à partir d'une chaîne de bits.

   :param bits: Liste de bits (0s et 1s) à coder.
   :return: Dictionnaire avec les temps et les niveaux de tension pour le signal Miller.

   **Exemple:**

   >>> miller([0, 1, 0, 1])
   {0.0: 1, 0.5: -1, 1.0: -1, 1.5: 1, 2.0: 0, 2.5: 0}

.. function:: miller_spectral_density(f, Tb)

   Calcule la densité spectrale de puissance pour le signal codé en Miller.

   :param f: Fréquences à évaluer.
   :param Tb: Durée d'un bit.
   :return: Valeurs de densité spectrale de puissance pour les fréquences données.

   **Exemple:**

   >>> f = np.linspace(0.01, 10, 100)
   >>> Tb = 1
   >>> miller_spectral_density(f, Tb)

.. function:: plot_signals(bits)

   Trace le signal codé en Miller et sa densité spectrale de puissance.

   :param bits: Liste de bits (0s et 1s) à coder.

   **Exemple:**

   >>> plot_signals([0, 1, 0, 1])
