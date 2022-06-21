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


# Setting up airflow configuration

1. ```bash 
   $ export AIRFLOW_HOME=${PWD}/airflow
   ```
2. ```bash 
   $ airflow db init
   ```
3. ```bash 
   $ Vim airflow.cfg 
   ```
   and inside that set 
   
   ```bash 
   $ enable_xcom_pickling = True  
   $ load_examples = False 
   ```
   
4. ```bash 
   $ airflow db reset
   ```
   
5. ```bash 
   $ airflow users create \
    --username admin \
    --firstname dsp \
    --lastname project \
    --role Admin \
    --email <any email>
    
    ```
    
    
 # Launch webserver
 
 1. Open another terminal
 
```bash 
   $ export AIRFLOW_HOME=${PWD}/airflow
   
  airflow webserver --port 8080  # http://localhost:8080
  
  ```
