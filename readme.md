# Lab 5: Products CRUD



## Introduction

This lab build on the previous one where you created a To Do list with an add item function. Next you will complete the **CRUD** (create, read, update, delete) functions.

![crud](assets/todos_complete.png)

### Getting started

**Start by cloning this repository and opening in VS Code.**

1. Configure the Python Virtual Environment

   `python -m venv venv --prompt="lab6"`

2. Activate the Virtual Environment

   `venv\Scripts\activate`

3. Install dependencies

   `pip install fastapi uvicorn jinja2 python-multipart httpx`

4. Setup the `.env` file, e.g. based on `.env.example`

5. To run the application

   `uvicorn app.main:app --reload --port=5000`



