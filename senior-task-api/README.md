# Senior Task API

Isolated, strictly typed task management service demonstrating senior architecture.

## Stack
- Python 3.10+
- FastAPI + Pydantic v2 (strict models, extra=forbid)
- In-memory service layer (easily swappable for PostgreSQL repository)

## Design Principles
- Separation of concerns: models / service / API
- Immutable-style updates via model_copy
- Explicit Enums for Priority and Status
- Validators for business rules
- No "vibe" code: every field is typed, constrained, and tested

## Run
```bash
# from this directory
uvicorn main:app --reload
```

## Tests
```bash
pytest tests/ -v
```
