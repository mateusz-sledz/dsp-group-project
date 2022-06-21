# Setting up postgreSQL database on docker
1. Start docker on your machine
2. Go to the docker folder and execute following commands
```bash 
$ docker build -t wine-postgres-db ./
$ docker run -d --name wine-postgresdb-container -p 5432:5432 wine-postgres-db
```
# Setting up airflow

```bash 
   $ export AIRFLOW_HOME=${PWD}/airflow
   ```
```bash 
   $ airflow db init
   ```
```bash 
   $ Vim airflow.cfg 
   ```
   and inside that file, change following variables
   
```bash 
   $ enable_xcom_pickling = True  
   $ load_examples = False 
   ```
   
```bash 
   $ airflow db reset
   ```
   
```bash 
   $ airflow users create \
    --username admin \
    --firstname dsp \
    --lastname project \
    --role Admin \
    --email <any email>
```
    
    
 # Launch scheduler and webserver
 
  1. Start airflow scheduler
 
```bash    
   $ airflow scheduler
  ```

 2. Open another terminal and start airflow webserver
 
```bash 
   $ export AIRFLOW_HOME=${PWD}/airflow
   
   $ airflow webserver       # http://localhost:8080
  ```

# Starting application

Execute following command in the first terminal in folder 'backend'


```bash
$ uvicorn main:app --reload
```

Execute second command in the other terminal in folder 'frontend'
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
