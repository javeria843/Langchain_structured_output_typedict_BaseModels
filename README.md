# TypedDict vs Pydantic BaseModel

This repo demonstrates the difference between Python's `TypedDict` and Pydantic's `BaseModel` for defining structured data.

## 🔹 TypedDict
- Lightweight
- No runtime validation
- Good for internal type hints

## 🔹 BaseModel (Pydantic)
- Validates data at runtime
- Converts types automatically
- Useful for APIs, user input, and external data

## 🧪 Code Examples
- `typedict_example.py`: Defines a review schema using `TypedDict`
- `basemodel_example.py`: Defines the same schema using `BaseModel`

## 📦 Requirements
To run `basemodel_example.py`, install Pydantic:
```bash
pip install pydantic

---

## 🧑‍💻 Steps to Push to GitHub

### 1. **Create Local Folder**
```bash
mkdir typedict-vs-basemodel
cd typedict-vs-basemodel
