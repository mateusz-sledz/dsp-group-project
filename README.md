# Starting application
1. Create a duplicate of the file `.env.sample` with the name `.env`.

2. Execute following command in the first terminal in folder 'backend'
```bash
$ uvicorn main:app --reload
```

3. Execute second command in the other terminal in folder 'frontend'
```bash
$ streamlit run page.py
```