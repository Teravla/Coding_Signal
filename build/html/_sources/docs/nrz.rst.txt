NRZ Coding Documentation
========================

Cette documentation couvre les fonctions utilisées pour générer un signal codé NRZ (Non-Return-to-Zero) à partir d'une chaîne de bits et pour calculer et tracer la densité spectrale de puissance correspondante.

.. module:: nrz
   :synopsis: Module pour le codage NRZ et la visualisation.

Fonctions
---------

.. function:: nrz(bits)

   Génère un signal NRZ à partir d'une chaîne de bits.

   :param bits: Liste de bits (0s et 1s) à coder.
   :return: Un tuple contenant le temps et le signal NRZ sous forme de tableau.

   **Exemple:**

   >>> nrz([0, 1, 0, 1])
   (array([0.  , 0.01, 0.02, ...]), array([-1,  1, -1, ...]))

.. function:: nrz_spectral_density(f, Tb)

   Calcule la densité spectrale de puissance pour le signal NRZ.

   :param f: Fréquences à évaluer.
   :param Tb: Durée d'un bit.
   :return: Valeurs de densité spectrale de puissance pour les fréquences données.

   **Exemple:**

   >>> f = np.linspace(0.01, 10, 100)
   >>> Tb = 1
   >>> nrz_spectral_density(f, Tb)

.. function:: plot_nrz(bits)

   Trace le signal NRZ et sa densité spectrale de puissance.

   :param bits: Liste de bits (0s et 1s) à coder.

   **Exemple:**

   >>> plot_nrz([0, 1, 0, 1])
