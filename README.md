# Gilded_Rose_Nico_Joan
TU 03/03/2023 - groupe Nicolas et Joan


Smells identifiés:

    test_gilded_rose:
        Tests non maintenus: 
            - "fixme" à remplacer par "foo" pour rendre le test passant
            - AssertEquals à remplacer par AssertEqual pour suivre la version de python
        Tests à ajouter:
            - test sell_in
            - test qualité
            - test sell_in et qualité post update item normaux
            - test qualité brie post update
            - test sell_in et qualité Sulfuras post update
            - test qualité backstage pass à moins de 10, 5 et 0 jours post update
            
    gilded_rose:
        - if imbriqués
        - magic strings
        - magic numbers
        - complexité cognitive élevée sur certaines formules
        - O de SOLID non respecté (pas fermé a la modification)
        - D de SOLID non respecté (GildedRose dépend de Item)
        
        
Priorisation des modifications/ajouts/refactos:

    - Ajout des tests manquants et correction du test existant
    - Gestion des magic strings et numbers
    - Correction des formules à complexité cognitive élevée
    - Eclatement des if imbriqués
    - Recheck du code pour vérifier qu'il n'y ait pas d'autres smells à modifiers
    - Respect de SOLID
