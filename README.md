# Wine quality prediction app

## Description

We are targeting vineyards 🍷, which are doing chemical analysis of wine on a regular
basis (acidity, citric acid, residual sugar, etc). Thanks to our system, they will be able
to assess the quality of currently produced wine without any expert knowledge,
therefore saving resources and time.

## Dataset description
We will be using an open source dataset found on kaggle which contains the red
variants of **Portuguese 🇵🇹 “Vinho Verde” wine**. This dataset consists of 11 features
which are based on physicochemical tests of a wine, and **a target variable ranging
from 0 to 10, 0** meaning lowest quality wine, and 10 meaning highest quality wine.

After doing a review of the variables, we think that all the 11 features seem relevant
for our purpose. And after doing a preliminary charge and analysis of the dataset,
they seem to have some range of influence in the result. These are the physicochemical features:

- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol

## System architecture
![alt text](architecture.png)

# Setup
## Setting up PostgreSQL database on Docker

🚨 _Important note: Install Postgres using `brew install postgres`, then `pip install -r requirements.txt` for users in
Apple Silicon devices._

1. Start docker on your machine
2. Go to the docker folder and execute following commands

```bash 
$ docker build -t wine-postgres-db ./
$ docker run -d --name wine-postgresdb-container -p 5432:5432 wine-postgres-db
```

## Setting up airflow

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

## Launch scheduler and webserver

1. Start airflow webserver

 ```bash 

$ airflow webserver       # http://localhost:8080
  ```

2. Open another terminal and start airflow scheduler

```bash 
$ export AIRFLOW_HOME=${PWD}/airflow
$ airflow scheduler
```

## Setting up mlflow

1. To run mlflow server, run the following command:

```bash
$ mlflow server --backend-store-uri postgresql://${db_username}:${db_password}@127.0.0.1:5432/winedb \
  --default-artifact-root ${PWD}/mlruns
```

## Set up and start the application

1. Create a duplicate of the file `.env.sample` with the name `.env` and the correct data of your environment
   configuration.
2. Execute following command in the first terminal in folder 'backend'

```bash
$ uvicorn main:app --reload
```

3. Execute second command in the other terminal in folder 'frontend'

```bash
$ streamlit run page.py
```
