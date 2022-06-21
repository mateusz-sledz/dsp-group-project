
# Setting up PostgreSQL database on Docker
🚨 _Important note: Install Postgres using `brew install postgres`, then `pip install -r requirements.txt` for users in Apple Silicon devices._
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

# Set up and start the application

1. Create a duplicate of the file `.env.sample` with the name `.env`
2. Execute following command in the first terminal in folder 'backend'
```bash
$ uvicorn main:app --reload
```
3. Execute second command in the other terminal in folder 'frontend'
```bash
$ streamlit run page.py
```