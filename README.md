# SecureFlow

Plateforme DevSecOps : pipeline CI/CD avec contrôles de sécurité automatisés et Security Gate.

## Démarrage rapide (Windows)

```
py -m venv .venv
.venv\Scripts\activate
pip install -r application\requirements-dev.txt
pytest application\tests -v
```

Lancer avec Docker :

```
docker compose up --build
```

Puis ouvrir http://127.0.0.1:5000/health

## Statut

Phase 1 : application et CI de base.
