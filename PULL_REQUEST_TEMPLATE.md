# Pull Request Senior - Task Architecture Brick

## Contexte
Objectif : démontrer une architecture senior opposable au « vibe coding » (code jetable généré sans typage strict, sans isolation de couches, sans tests).

Brique isolée :
- Service API FastAPI + Pydantic v2 (modèles étanches, Enums, validateurs)
- Couche service pure (TaskService) injectable
- Composant client React/TypeScript (TaskCard) avec types miroir et styles Tailwind

## Choix techniques
- **Pydantic ConfigDict(extra="forbid", strict=True)** : rejet de tout champ non déclaré, pas de coercion silencieuse.
- **Enums explicites** (Priority, TaskStatus) : pas de magic strings.
- **Séparation stricte** models / service / API : le service ne connaît pas FastAPI.
- **Updates immuables** via model_copy + exclude_unset.
- **Typage TypeScript miroir** côté client pour éviter les any.
- **Composant purement présentationnel** avec props typées et data-testid pour tests.

## Preuves d'exécution des tests
```bash
cd senior-task-api
PYTHONPATH=. pytest tests/ -v
```

Résultat :
```
============================= test session starts ==============================
platform linux -- Python 3.10.21, pytest-9.2.0
collected 8 items

tests/test_service.py::test_create_task PASSED                           [ 12%]
tests/test_service.py::test_title_stripped_and_validated PASSED          [ 25%]
tests/test_service.py::test_blank_title_rejected PASSED                  [ 37%]
tests/test_service.py::test_get_and_list PASSED                          [ 50%]
tests/test_service.py::test_update PASSED                                [ 62%]
tests/test_service.py::test_update_not_found PASSED                      [ 75%]
tests/test_service.py::test_delete PASSED                                [ 87%]
tests/test_service.py::test_list_by_status PASSED                        [100%]

============================== 8 passed in 2.82s ===============================
```

**100 % passed** — condition de commit respectée.

## Commit public
- SHA : `22e70279279a8b19cca3bd9ed24a867d7d97e400`
- URL : https://github.com/Kvnbbg/senior-task-architecture-demo/commit/22e70279279a8b19cca3bd9ed24a867d7d97e400
- Repo : https://github.com/Kvnbbg/senior-task-architecture-demo

## Prochaines étapes (hors scope de cette brique)
- Remplacement du store in-memory par repository PostgreSQL
- Tests d'intégration API (httpx + TestClient)
- Storybook + tests Jest pour le TaskCard
- CI GitHub Actions avec gate 100 % tests
