
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
 
  1. Start airflow webserver
 
 ```bash 

$ airflow webserver       # http://localhost:8080
  ```
 2. Open another terminal and start airflow scheduler 
   
```bash 
$ export AIRFLOW_HOME=${PWD}/airflow
$ airflow scheduler
```

# Setting up mlflow
1. To run mlflow server, run the following command:
```bash
$ mlflow server --backend-store-uri postgresql://${db_username}:${db_password}@127.0.0.1:5432/winedb \
  --default-artifact-root ${PWD}/mlruns
```
# Set up and start the application

1. Create a duplicate of the file `.env.sample` with the name `.env` and the correct data of your environment configuration.
2. Execute following command in the first terminal in folder 'backend'
```bash
$ uvicorn main:app --reload
```
3. Execute second command in the other terminal in folder 'frontend'
```bash
$ streamlit run page.py
```
