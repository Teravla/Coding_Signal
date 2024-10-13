NRZI Coding Documentation
=========================

Cette documentation couvre les fonctions utilisées pour générer un signal codé NRZI (Non-Return-to-Zero Inverted) à partir d'une chaîne de bits et pour calculer et tracer la densité spectrale de puissance correspondante.

.. module:: nrzi
   :synopsis: Module pour le codage NRZI et la visualisation.

Fonctions
---------

.. function:: nrzi(bits)

   Génère un signal NRZI à partir d'une chaîne de bits.

   :param bits: Liste de bits (0s et 1s) à coder.
   :return: Un tuple contenant le temps et le signal NRZI sous forme de tableau.

   **Exemple:**

   >>> nrzi([0, 1, 0, 1])
   (array([0.  , 0.01, 0.02, ...]), array([ 1, -1, ...]))

.. function:: nrzi_spectral_density(f, Tb)

   Calcule la densité spectrale de puissance pour le signal NRZI.

   :param f: Fréquences à évaluer.
   :param Tb: Durée d'un bit.
   :return: Valeurs de densité spectrale de puissance pour les fréquences données.

   **Exemple:**

   >>> f = np.linspace(0.01, 10, 100)
   >>> Tb = 1
   >>> nrzi_spectral_density(f, Tb)

.. function:: plot_nrzi(bits)

   Trace le signal NRZI et sa densité spectrale de puissance.

   :param bits: Liste de bits (0s et 1s) à coder.

   **Exemple:**

   >>> plot_nrzi([0, 1, 0, 1])
