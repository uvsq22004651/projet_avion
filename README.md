Ce code permet la simulation de passagers ce plaçant au sein d'un avion.
180 passagers reçoivent une place à laquelle ils doivent se rendre dans l'avion et un nombre de bagages compris entre 0 et 2.
Lorque le code est lancé, pas besoin d'utiliser le clavier ni la souris, les passagers vont à leur place d'eux mêmes.
Malheureusement seul un passager arrive à se rendre à son siège qui lui ait au préalable donné .
Nous avons créer l'interfarce graphique avec des légendes.
Ce que l'on a réussi à faire :
      - Une fonction qui créer le couloir et les sièges (sièges_couloir())
      - Une fonction qui attribue une coordonnée à tous les sièges (coordonnees_sièges())
      - Une fonction qui créer les sièges et le couloir dans une liste (tableau_2D())
      - Une fonction qui créer les 180 passagers dans une liste avec chacun un numéro, à qui on attribue un nombre de bagage(s) et une place dans l'avion (création_passagers_bagages_coords())
      - Une fonction qui créer les passagers sous forme de cercle (création_cercle_passagers())
      - Une fonction qui déplace le passager vers son siège (mouvement())
      -3 fonctions qui éxaminent l'ensemble de l'avion pour voir si des passagers sont l'un derrière l'autre ou l'un à côté de l'autre(voisins_couloir(), voisins_sièges_gauche(), voisins_sièges_droite())
      - Une fonction qui créer une légende de chaque couleur qui apparaît dans l'avion (legende()).
      
Le seul passager qui se place arrive à atteindre sa place si il est à droite du couloir, en revanche s'il est à gauche du couloir, il va au delà de sa place et sort du canvas.
