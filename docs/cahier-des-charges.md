
# 📄 Cahier des Charges Complet — Application "Tortiki"

**Version :** 2.0 | **Date :** 13 mai 2026 | **Auteur :** [Votre nom] | **Statut :** En cours de validation

***

## 1. Contexte \& Objectifs

### 1.1 Présentation du projet

**Tortiki** est une marketplace P2P (Peer-to-Peer) spécialisée dans la vente de plats cuisinés maison entre particuliers. La plateforme met en avant la diversité culturelle gastronomique en permettant à des cuisiniers amateurs de valoriser leurs recettes traditionnelles auprès d'une clientèle locale cherchant des repas authentiques.

### 1.2 Problème résolu

Les plateformes de livraison existantes (UberEats, Deliveroo) ne permettent pas à des particuliers de vendre leurs plats. Il n'existe pas de marketplace dédiée au "fait maison culturel" avec géolocalisation et Click \& Collect en France.

### 1.3 Objectifs SMART

| Objectif | Indicateur (KPI) | Cible à 6 mois |
| :-- | :-- | :-- |
| Acquisition vendeurs | Nb de profils vendeurs actifs | 50 vendeurs |
| Acquisition acheteurs | Nb de comptes clients actifs | 200 acheteurs |
| Confiance plateforme | Note moyenne des transactions | ≥ 4,2 / 5 |
| Performance technique | Temps de réponse API (p95) | < 500 ms |
| Disponibilité | Uptime mensuel | ≥ 99,5% |


***

## 2. Parties Prenantes \& Personas

### 2.1 Parties prenantes

| Acteur | Rôle | Responsabilité |
| :-- | :-- | :-- |
| Porteur de projet | Maîtrise d'ouvrage (MOA) | Valide les fonctionnalités et livrables |
| Développeur (CDA) | Maîtrise d'œuvre (MOE) | Conçoit et développe l'application |
| Utilisateurs pilotes | Testeurs beta | Valident les parcours UX |
| Jury CDA | Évaluateur | Évalue la conformité au référentiel |

### 2.2 Personas utilisateurs

**Persona 1 — La Cuisinière Entrepreneuriale**
> *Sofia, 38 ans, d'origine ukrainienne, habite Nancy. Elle cuisine des bortschs et varenyky pour sa famille. Elle cherche un revenu complémentaire et un moyen de partager sa culture.*

**Persona 2 — Le Curieux Gourmand**
> *Théo, 26 ans, étudiant. Lassé des fast-foods, il cherche des repas faits maison, variés et abordables. Il commande via smartphone et récupère son repas en sortant du travail.*

***

## 3. Périmètre Fonctionnel

### 3.1 User Stories avec critères d'acceptation

Les User Stories suivent le format **BDD (Behavior-Driven Development)** : *Étant donné / Quand / Alors*.

**Module : Gestion des comptes**

> **US-01** — En tant que visiteur, je veux m'inscrire afin d'accéder à la plateforme.
> - ✅ Le formulaire accepte email + mot de passe (min. 12 caractères, 1 maj, 1 chiffre, 1 spécial)
> - ✅ Un email de confirmation est envoyé dans les 60 secondes
> - ✅ Le compte est inactif tant que l'email n'est pas confirmé

> **US-02** — En tant qu'utilisateur, je veux choisir mon rôle (Vendeur ou Client) afin d'accéder aux fonctionnalités adaptées.
> - ✅ Le choix du rôle est modifiable depuis le profil
> - ✅ Un utilisateur peut cumuler les deux rôles

**Module : Côté Vendeur**

> **US-03** — En tant que vendeur, je veux créer une annonce de plat afin de proposer ma cuisine à la vente.
> - ✅ Champs obligatoires : titre, description (max 500 car.), photo (JPEG/PNG, max 5 Mo), prix, nb portions, origines culinaires (1 à 5)
> - ✅ L'annonce passe en statut "en attente" si le stock atteint 0
<!-- > - ✅ Le vendeur définit 1 à 7 créneaux de retrait hebdomadaires (date, heure, lieu) -->

> **US-04** — En tant que vendeur, je veux gérer mon tableau de bord afin de suivre mes commandes et revenus.
> - ✅ Affichage des commandes (en attente, confirmées, retirées, annulées)
> - ✅ Chiffre d'affaires cumulé visible par semaine/mois

> **US-05** — En tant que vendeur, je veux gérer mes demandes de contact afin de confirmer ou refuser les intéressés.
> - ✅ Liste des ContactRequest avec statuts (en attente / confirmé / refusé)
> - ✅ Le vendeur peut marquer une demande comme "confirmée" (le client reçoit un email)
> - ✅ Le vendeur peut masquer son numéro de téléphone (affichage email uniquement)

**Module : Côté Client**

> **US-06** — En tant que client, je veux rechercher des plats par localisation afin de trouver des vendeurs proches de moi.
> - ✅ Intégration OpenStreetMap / Nominatim (API gratuite, RGPD-friendly)
> - ✅ Rayon de recherche paramétrable (1 km à 50 km)
> - ✅ Résultats affichés sur carte et en liste

> **US-07** — En tant que client, je veux filtrer les plats par origine culinaire et régime alimentaire afin d'explorer de nouvelles cuisines.
> - ✅ Filtres combinables : origine culturelle + végétarien/vegan/sans gluten/sans lactose
> - ✅ Affichage des allergènes déclarés (liste réglementaire EU des 14 allergènes majeurs)

> **US-08** — En tant que client, je veux signaler mon intérêt pour un plat afin d'obtenir les coordonnées du vendeur et finaliser l'achat directement.
> - ✅ Le bouton "Je suis intéressé(e)" n'est visible qu'aux utilisateurs connectés
> - ✅ Une ContactRequest est créée en base (statut : pending)
> - ✅ Le vendeur reçoit un email de notification automatique
> - ✅ Le téléphone et l'email du vendeur sont affichés uniquement après confirmation de l'intérêt
> - ✅ Le client ne peut pas envoyer deux demandes pour la même annonce (idempotence)
> - ✅ Un bandeau légal indique que le paiement s'effectue en espèces/virement lors du retrait

**Module : Confiance \& Administration**

> **US-09** — En tant que client, je veux noter un vendeur après ma commande afin d'aider la communauté.
> - ✅ Note de 1 à 5 étoiles + commentaire libre (après statut "retiré" uniquement)
> - ✅ Signalement d'avis abusif disponible

> **US-10** — En tant qu'administrateur, je veux gérer le référentiel des types de cuisines afin de maintenir le catalogue culturel.
> - ✅ Interface CRUD des origines culinaires via panel d'administration
> - ✅ Modération des annonces signalées

### 3.2 Matrice de priorité MoSCoW

| Priorité | Fonctionnalités |
| :-- | :-- |
| **Must Have** | Inscription/connexion, annonces, recherche géo, panier, système de contact direct (téléphone/email révélé post-intention), allergènes |
| **Should Have** | Tableau de bord vendeur, filtres avancés, notation, emails transactionnels |
| **Could Have** | Notifications push, messagerie interne, favoris, partage réseaux sociaux |
| **Won't Have (v1)** | Livraison à domicile, abonnement premium, app mobile native |


***

## 4. Exigences Non-Fonctionnelles

Ces exigences sont mesurables et testables  :

- **Performance :** Temps de réponse < 500 ms (p95) pour les endpoints de recherche sous 100 utilisateurs simultanés
- **Disponibilité :** Uptime ≥ 99,5% par mois, fenêtre de maintenance planifiée la nuit (02h-04h)
- **Scalabilité :** Architecture stateless permettant le scaling horizontal; ajout de cuisines sans déploiement
- **Sécurité :** OWASP Top 10 2025 couvert, authentification JWT (access token 15 min, refresh 7 jours)
- **Accessibilité :** Conformité RGAA 4.1 niveau AA
- **Conformité RGPD :** Consentement granulaire, droit à l'effacement, export des données, durée de conservation définie
- **Maintenabilité :** Couverture de tests ≥ 80%, code commenté en français, README complet

***

## 5. Architecture Technique

### 5.1 Stack technologique

| Couche | Technologie | Justification |
| :-- | :-- | :-- |
| Backend API | Python / FastAPI | Performances async, typage fort (Pydantic), documentation OpenAPI auto-générée |
| Base de données | PostgreSQL 16 | Robustesse ACID, JSON natif, exigence tuteur |
| ORM | SQLAlchemy 2.x + Alembic | Migrations versionnées, agnostique au SGBD |
| Authentification | JWT + bcrypt | Standard industriel, stateless |
| Géolocalisation | OpenStreetMap / Nominatim | Gratuit, RGPD-friendly, sans clé API payante |
| Stockage fichiers | MinIO (local dev) | Découplage des médias du serveur applicatif |
| Frontend | HTML5 / Jinja2 + HTMX | Rendu serveur léger, progressive enhancement |
| Tests | Pytest + HTTPX | Tests unitaires et d'intégration |
| CI/CD | GitHub Actions | Automatisation lint, tests, déploiement |
| Déploiement | Docker + Render/Railway | Conteneurisation reproductible |

### 5.2 Architecture applicative

```
┌─────────────────────────────────────────────┐
│              Client (Navigateur)            │
└──────────────────────┬──────────────────────┘
                       │ HTTPS
┌──────────────────────▼──────────────────────┐
│         FastAPI Application Layer           │
│  ┌────────────┐  ┌──────────────────────┐   │
│  │  Routers   │  │  Middlewares         │   │
│  │ (Controllers)│ │ (Auth, CORS, Rate   │   │
│  └─────┬──────┘  │  Limiting, Logging)  │   │
│        │         └──────────────────────┘   │
│  ┌─────▼──────────────────────────────────┐ │
│  │      Services Layer (Business Logic)   │ │
│  └─────┬──────────────────────────────────┘ │
│  ┌─────▼──────────────────────────────────┐ │
│  │   Repository Layer (Data Access)       │ │
│  │          SQLAlchemy ORM                │ │
│  └─────┬──────────────────────────────────┘ │
└────────│────────────────────────────────────┘
         │
┌────────▼────────┐    ┌──────────┐
│  PostgreSQL DB  │    │ S3/MinIO │
└─────────────────┘    └──────────┘
```


***

## 6. Sécurité \& Conformité

### 6.1 Mesures OWASP Top 10 (2025)

| Risque OWASP | Mesure appliquée |
| :-- | :-- |
| A01 - Broken Access Control | RBAC strict par rôle (admin, seller, buyer), vérification à chaque endpoint |
| A02 - Cryptographic Failures | HTTPS obligatoire, bcrypt pour les mots de passe (cost=12), chiffrement données sensibles en base |
| A03 - Injection | ORM SQLAlchemy (requêtes paramétrées), validation Pydantic sur toutes les entrées |
| A07 - Auth Failures | Rate limiting login (5 tentatives / 15 min), JWT à courte durée de vie |
| A09 - Logging Failures | Journalisation structurée (JSON logs), sans données personnelles dans les logs |

### 6.2 RGPD — Données collectées

| Donnée | Finalité | Durée de conservation | Base légale |
| :-- | :-- | :-- | :-- |
| Email, nom, prénom | Identification, communications | 3 ans après dernière activité | Contrat |
| Adresse de retrait | Géolocalisation de l'annonce | Durée de l'annonce + 1 an | Contrat |
| Téléphone/email vendeur | Contact pour finaliser la transaction |  | Contrat |
| Avis et notations | Confiance communautaire | 5 ans | Intérêt légitime |

> Clause CGU à ajouter : "Le vendeur consent à ce que ses coordonnées de contact soient communiquées aux utilisateurs ayant exprimé un intérêt pour son annonce. Ce consentement peut être retiré à tout moment depuis les paramètres du profil."

***

## 7. Planning \& Méthodologie

Le projet suit une approche **Agile Scrum**


 Sprint | Dates | Contenu | Livrable |
| :-- | :-- | :-- | :-- |
| **Phase 0 — Cadrage** | 13/05 → 24/05 | Setup environnement (FastAPI, MySQL, Docker), modèle BDD, Alembic migrations, JWT Auth, CI/CD GitHub Actions, maquettes Figma/wireframes | Dépôt Git propre, BDD initialisée, auth fonctionnelle |
| **Sprint 1 — Socle** | 25/05 → 07/06 | Inscription/Connexion/Profils, rôles Vendeur/Client, CRUD annonces, upload photo (S3/MinIO), référentiel origines culinaires | Vendeur peut créer et publier un plat |
| **Sprint 2 — Découverte** | 08/06 → 21/06 | Recherche par ville, filtres, fiche plat détail, allergènes, flux "Je suis intéressé(e)" + révélation coordonnées, emails notification | Parcours client complet jusqu'au contact vendeur |
| **Sprint 3 — Confiance & Admin** | 22/06 → 05/07 | Gestion des ContactRequest côté vendeur, notation post-retrait, panel admin | Transaction complète de bout en bout |
| **Sprint 4 — Qualité & Livraison** | 06/07 → 17/07 | Jeux de tests (Pytest), corrections bugs, conformité RGPD (mentions légales, cookies), accessibilité RGAA, déploiement prod (Railway/Render), documentation | Application déployée + dossier CDA finalisé |

> ⚠️ Une marge de 15 à 20% est à prévoir sur chaque estimation.

***

## 8. Gestion des Risques

| Risque | Probabilité | Impact | Mitigation |
| :-- | :-- | :-- | :-- |
| Problèmes de géolocalisation (qualité OSM) | Faible | Moyen | Tester sur plusieurs villes, prévoir fallback adresse manuelle |
| Non-conformité RGPD | Faible | Fort | Audit RGPD en Phase 0 |
| Sous-estimation des délais | Forte | Moyen | Marge de 20% intégrée au planning |
| Sécurité alimentaire (responsabilité légale) | Moyenne | Fort | Mentions légales obligatoires, CGU claires, clause de non-responsabilité |


***

## 9. Livrables \& Critères d'Acceptation

| Livrable | Critère de validation | Responsable |
| :-- | :-- | :-- |
| Dossier de projet CDA | Couvre les 8 sections du référentiel | MOA + Jury |
| Code source (Git) | Commits atomiques, branches feature/main/dev, README | MOE |
| Scripts SQL | Migration Alembic fonctionnelle, données de test | MOE |
| Jeux d'essais | 15 scénarios de test couvrant les US Must Have | MOE |
| Application déployée | URL publique accessible, HTTPS, temps de réponse < 500ms | MOE |
| Documentation API | OpenAPI/Swagger auto-générée par FastAPI | MOE |


***

## 10. Glossaire

| Terme | Définition |
| :-- | :-- |
| **P2P** | Pair-à-pair : échange direct entre particuliers sans intermédiaire stockiste |
| **Click \& Collect** | Mode de retrait : le client commande en ligne et retire physiquement chez le vendeur |
| **BLL** | Business Logic Layer : couche de traitement des règles métier |
| **DAL** | Data Access Layer : couche d'accès à la base de données |
| **RGPD** | Règlement Général sur la Protection des Données (UE 2016/679) |
| **RGAA** | Référentiel Général d'Amélioration de l'Accessibilité (version 4.1) |
| **JWT** | JSON Web Token : standard d'authentification sans état |
| **PCI-DSS** | Standard de sécurité des données de l'industrie des cartes de paiement |


***