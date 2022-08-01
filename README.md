# books-database-api
REST APIS with flask

A brief guide to get this running
Set up a vitual environment 
```python -m venv env ```  

Activate the environment(windows)  
```.\env\Scripts\activate.bat```

Install the required dependencies by running  

```pip install -r requirements.txt```  

Set up a database (postgres). follow this tutorial to set up a postgres container   
https://dev.to/shree_j/how-to-install-and-run-psql-using-docker-41j2

In the api/__init__.py file, set app.config["SQLALCHEMY_DATABASE_URI"] to the correct database connection url

Create and populate the database by running   

```python insert_data.py ```

confirm that the database has indeed been created and populated with data, and run
```flask run```


