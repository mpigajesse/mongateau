# Démo publique de MonGâteau (gratuite, Render)

Un seul **Web Service** Render (Python) sert l'API Django **et** une vitrine de démonstration sur
`/` : le frontend React du projet n'est pas versionné dans ce dépôt.

- `DEMO_PUBLIQUE=1` active la vitrine (`/`, `/commande/`) et retire l'administration Django.
- Base **SQLite éphémère** : à chaque réveil du service gratuit, `migrate` puis
  `seed_demo_public` recréent le catalogue (5 gâteaux), 10 commandes et 2 demandes sur mesure
  **fictives**, avec leurs tickets. Le profil et les réglages boutique sont aussi fictifs.
- La démo n'a pas de comptes : le projet n'a pas d'authentification (voir « Limites »).

| Champ Render | Valeur |
|---|---|
| Root Directory | `backend` |
| Build Command | `pip install -r requirements.txt && python manage.py collectstatic --noinput` |
| Start Command | `python manage.py migrate --noinput && python manage.py seed_demo_public && gunicorn mongateau.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 60` |
| Variables | `PYTHON_VERSION=3.12.7`, `DEBUG=False`, `DEMO_PUBLIQUE=1`, `DATABASE_URL=sqlite:///demo.sqlite3`, `SECRET_KEY` (générée), `ALLOWED_HOSTS` / `CSRF_TRUSTED_ORIGINS` avec le domaine personnalisé |

## Limites (à corriger avant toute mise en production)

Les routes `/api/admin/*` et la liste `/api/orders/` sont en `AllowAny` (« TODO: add auth » dans le
code) : n'importe qui peut lister, modifier ou supprimer les commandes. Sans conséquence en démo
(données fictives, remises à zéro), mais bloquant pour un vrai déploiement.
