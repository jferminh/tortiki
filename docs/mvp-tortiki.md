
***

# 🗓️ MVP Tortiki — Livraison 17/07/2026

**Principe directeur :** Le MVP n'est pas une application complète — c'est la **version minimale qui prouve la valeur** de Tortiki : un vendeur peut publier un plat, un client peut le trouver et commander. Tout le reste est post-MVP.

***

## Périmètre MVP — Matrice par Profil

### 👤 Profil Visiteur (non connecté)

| Fonctionnalité | Priorité MVP | Justification |
| :-- | :-- | :-- |
| Page d'accueil avec présentation | ✅ Must | Vitrine minimale |
| Inscription (email + mot de passe) | ✅ Must | Condition d'entrée |
| Connexion / Déconnexion | ✅ Must | Session utilisateur |
| Choix du rôle à l'inscription (Vendeur / Client) | ✅ Must | Différenciation des parcours |
| Page de recherche publique (lecture seule) | ✅ Must | Démonstration de valeur |
| Récupération de mot de passe | ❌ Post-MVP | Opérationnel mais non bloquant |
| Connexion sociale (Google/Facebook) | ❌ Post-MVP | Complexité disproportionnée |


***

### 🍳 Profil Vendeur

| Fonctionnalité | Priorité MVP | Justification |
| :-- | :-- | :-- |
| Création d'annonce (titre, desc, photo, prix, portions) | ✅ Must | Cœur de métier |
| Attribution d'une origine culinaire (liste fixe) | ✅ Must | USP du projet |
| Définition de 1 créneau de retrait (date, heure, adresse) | ✅ Must | Click \& Collect minimal |
| Mise à jour / suppression d'annonce | ✅ Must | CRUD basique |
| Vue de ses commandes reçues (liste simple) | ✅ Must | Gestion opérationnelle |
| Confirmation / Refus d'une commande | ✅ Must | Contrôle du vendeur |
| Upload de photo (1 photo par annonce) | ✅ Must | Attractivité de l'annonce |
| Dashboard CA / statistiques | ❌ Post-MVP | Reporting non critique v1 |
| Gestion de plusieurs créneaux par annonce | ❌ Post-MVP | 1 créneau suffit pour prouver le concept |
| Messagerie interne | ❌ Post-MVP | Email transactionnel suffisant |


***

### 🛒 Profil Client

| Fonctionnalité | Priorité MVP | Justification |
| :-- | :-- | :-- |
| Recherche de plats par ville / code postal | ✅ Must | Géolocalisation texte (Nominatim) |
| Filtrage par origine culinaire | ✅ Must | Différenciateur clé |
| Filtrage par régime alimentaire (végé, sans gluten) | ✅ Must | Sécurité alimentaire + RGAA |
| Affichage des allergènes sur chaque annonce | ✅ Must | Obligation légale EU |
| Fiche détail d'un plat | ✅ Must | Conversion visiteur → acheteur |
| Panier (1 vendeur à la fois en v1) | ✅ Must | Tunnel de commande simplifié |
| Email de confirmation de commande | ✅ Must | Preuve de transaction |
| Consultation de ses commandes passées | ✅ Must | Suivi client |
| Notation vendeur après livraison | ✅ Must | Confiance plateforme |
| Carte interactive (OpenStreetMap/Leaflet) | ❌ Post-MVP | Remplacé par recherche texte |
| Panier multi-vendeurs | ❌ Post-MVP | Complexité de gestion des créneaux |
| Notifications push | ❌ Post-MVP | Email suffisant pour v1 |
| Favoris / historique | ❌ Post-MVP | Confort, pas essentiel |


***

### 🔧 Profil Administrateur

| Fonctionnalité | Priorité MVP | Justification |
| :-- | :-- | :-- |
| CRUD des origines culinaires | ✅ Must | Référentiel évolutif |
| Liste des utilisateurs | ✅ Must | Contrôle minimal |
| Désactivation d'une annonce signalée | ✅ Must | Modération de base |
| Tableau de bord statistiques | ❌ Post-MVP | Nice-to-have |


***

## 📅 Planning Sprint (13 mai → 17 juillet 2026)

*9,3 semaines disponibles, découpées en 4 sprints de 2 semaines + 1 sprint de finalisation.*


| Sprint | Dates | Contenu | Livrable |
| :-- | :-- | :-- | :-- |
| **Phase 0 — Cadrage** | 13/05 → 24/05 | Setup environnement (FastAPI, MySQL, Docker), modèle BDD, Alembic migrations, JWT Auth, CI/CD GitHub Actions, maquettes Figma/wireframes | Dépôt Git propre, BDD initialisée, auth fonctionnelle |
| **Sprint 1 — Socle** | 25/05 → 07/06 | Inscription/Connexion/Profils, rôles Vendeur/Client, CRUD annonces, upload photo (S3/MinIO), référentiel origines culinaires | Vendeur peut créer et publier un plat |
| **Sprint 2 — Découverte** | 08/06 → 21/06 | Recherche par ville, filtres, fiche plat détail, allergènes, flux "Je suis intéressé(e)" + révélation coordonnées, emails notification | Parcours client complet jusqu'au contact vendeur |
| **Sprint 3 — Confiance & Admin** | 22/06 → 05/07 | Gestion des ContactRequest côté vendeur, notation post-retrait, panel admin | Transaction complète de bout en bout |
| **Sprint 4 — Qualité & Livraison** | 06/07 → 17/07 | Jeux de tests (Pytest), corrections bugs, conformité RGPD (mentions légales, cookies), accessibilité RGAA, déploiement prod (Railway/Render), documentation | Application déployée + dossier CDA finalisé |

> ⚠️ **Règle d'or :** Si une fonctionnalité n'est pas terminée au 05/07, elle passe en Post-MVP. La date de livraison est non négociable.

***

## 🎯 Definition of Done (DoD) du MVP

Une fonctionnalité est considérée **livrée** uniquement si :

- ✅ Code mergé sur la branche `main` via Pull Request
- ✅ Tests Pytest couvrant le cas nominal ET un cas d'erreur
- ✅ Endpoint documenté dans Swagger/OpenAPI (auto-généré par FastAPI)
- ✅ Données validées par Pydantic (pas d'injection possible)
- ✅ Responsive testé sur mobile (375px) et desktop (1280px)
- ✅ Accessible au clavier (tabindex, labels, focus visible)

***

## 🚦 Indicateurs de succès MVP

| Critère | Seuil d'acceptation |
| :-- | :-- |
| Parcours vendeur complet (inscription → annonce publiée) | < 5 minutes |
| Parcours client complet (recherche → paiement confirmé) | < 3 minutes |
| Temps de réponse API (recherche) | < 800 ms |
| Couverture de tests | ≥ 70% |
| Zéro vulnérabilité OWASP critique | 0 faille bloquante |
| Déploiement fonctionnel (URL publique HTTPS) | Accessible 24h/24 |


***

Ce MVP couvre **les 4 User Stories critiques** du référentiel CDA : création d'une entité métier (annonce), consultation avec filtres, transaction sécurisée, et notation. 

<div align="center">⁂</div>


