# Aérokinator V2 — architecture évolutive

Application statique compatible GitHub Pages. Aucun serveur, framework ou compilation requis.

## Déploiement
Copier le contenu du dossier à la racine du dépôt GitHub Pages, puis publier la branche/dossier depuis **Settings → Pages**. L'application doit être servie en HTTPS pour que le service worker fonctionne.

## Architecture
- `index.html`, `style.css` : interface.
- `js/app.js` : navigation, encyclopédie, fiches, recherche d'images.
- `js/game.js` : sélection adaptative de questions par séparation des candidats.
- `js/data.js` : chargement des index et des fichiers JSON par catégorie.
- `data/index.json` : index léger chargé au démarrage pour la recherche et le jeu.
- `data/{category}.json` : fiches complètes chargées uniquement à l'ouverture d'une fiche.
- `data/manifest.json` : version, nombre de fiches et liste des fragments.
- `data/aircraft.schema.json` : schéma des fiches.
- `sw.js` : cache de l'application et des fragments déjà consultés.
- `scripts/import_csv.py` : import de nouveaux modèles depuis un CSV.

## Données de départ
La livraison contient 39 fiches reprises de la première version. Ce jeu de départ sert à valider l'architecture et le format ; il n'est pas exhaustif et plusieurs valeurs doivent être contrôlées. Les fiches portent `dataQuality: starter-unverified` pour éviter de les présenter comme des données certifiées.

## Modèle de données
Chaque appareil possède un `id` unique et un `familyId`. Les variantes partagent le `familyId` et renseignent `variantOf` avec l'identifiant du modèle parent. `status` distingue `flown`, `prototype-flown`, `project-only`, `cancelled` et `unknown`. Les catégories incluent civil, militaire, planeurs, hélicoptères, expérimental, amphibie et autre.

## Ajouter des appareils
Préparer un CSV avec au minimum : `id,name,manufacturer,category,type,status`. Colonnes facultatives : `country,role,era,firstFlight,variantOf,variant,propulsion,engineType,engineCount,maxSpeed,range,ceiling,crew,seats,keywords,sourceUrl`.

Puis exécuter :

```bash
python scripts/import_csv.py nouveaux-appareils.csv data
```

Faire une sauvegarde de `data/` avant de remplacer les fichiers. Vérifier les doublons d'identifiants, les liens de variantes et les sources avant publication.

## Chargement progressif et hors ligne
L'index compact est chargé au démarrage. Les fiches complètes sont réparties par catégorie. Le service worker met en cache l'interface et les fragments consultés. Les images distantes nécessitent une connexion et peuvent ne pas être disponibles hors ligne. Le cache hors ligne est progressif : il ne télécharge pas toute l'encyclopédie d'un coup.

## Images et droits
Les images sont recherchées à la demande via l'API Wikimedia Commons. La recherche automatique n'assure pas que chaque résultat représente exactement la variante recherchée. Chaque image doit être vérifiée et sa licence/auteur consultés sur la page Commons avant toute réutilisation. L'application ne copie ni n'héberge les photographies.
