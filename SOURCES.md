# Sources candidates et stratégie de constitution du catalogue

Il n'existe pas une source publique unique couvrant proprement tous les aéronefs historiques, prototypes, variantes, planeurs, hélicoptères et projets. La base devra être constituée par fusion contrôlée, avec provenance par fiche.

## Sources à étudier

1. **myControl.aero — types d'aéronefs** : documentation d'API publique, liste paginée de types, données annoncées sous licence CC BY 4.0. Utile pour les types courants et les champs techniques ; vérifier la couverture historique et les conditions d'attribution avant intégration. https://docs.mycontrol.aero/api/v10/public_data.html
2. **Aerospace Community** : catalogue communautaire accessible en JSON par API et pagination. Le site précise que les données ne sont pas garanties complètes ou exactes et que les contenus personnels des membres ne sont pas réutilisables sans consentement. Utiliser uniquement les champs du catalogue dont les conditions de réutilisation sont confirmées. https://aerospace-community.com/Data/Database
3. **OpenAirDocs** : agrégation de données FAA/NTSB et fiches de certification ; très utile pour enrichir certains modèles civils et leurs documents de certification, mais ce n'est pas un catalogue mondial historique exhaustif. La release annoncée est CC0, à l'exception des copies de documents de service. https://openairdocs.org/ et https://openairdocs.org/tcds
4. **ATDB / aerotransport.org** : annonce plusieurs milliers de types d'avions de transport et des sous-types, mais les conditions d'accès et de réutilisation doivent être vérifiées ; ne pas aspirer ou republier sans autorisation. https://atdb.aero/html/datasets.html
5. **Wikimedia Commons** : source d'images à interroger à la demande. Les licences varient fichier par fichier ; conserver le lien vers la page du fichier, l'auteur et la licence. https://www.mediawiki.org/wiki/API:Imageinfo

## Règles de qualité
- Ne pas mélanger un modèle/type avec une immatriculation d'appareil individuel.
- Conserver les variantes distinctes et leur relation parent/enfant.
- Marquer explicitement les projets n'ayant jamais volé.
- Conserver au moins une URL source par fiche lorsque disponible.
- Dédupliquer avec constructeur + désignation + variante, pas seulement le nom commercial.
- Ne jamais transformer une donnée manquante en zéro ou en valeur supposée.
- Vérifier les licences et conditions d'utilisation avant toute redistribution dans le dépôt GitHub.

## Références consultées
- myControl.aero Public Data API : https://docs.mycontrol.aero/api/v10/public_data.html
- Aerospace Community database/API : https://aerospace-community.com/Data/Database
- OpenAirDocs : https://openairdocs.org/
- ATDB datasets : https://atdb.aero/html/datasets.html
- Wikimedia API Imageinfo : https://www.mediawiki.org/wiki/API:Imageinfo
