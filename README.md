### THIS PROJECT WAS DONE WITH PYTHON 3.10.13

## Run it:


- Create a virtual environment (this is done only once): 

        python -m venv venv

- Activate venv on linux:

      source venv/bin/activate

- Install dependencies:

      pip install -r requirements.txt

- Run server

      uvicorn main:app

To access the swagger docs with all available endpoints, access 127.0.0.1:8000/docs in your browser

To create a new database with some products, city and state on it, 
first of all uncomment line 46 in main.py file:

    # reset_database()

after you uncommented it, run the file:

    python main.py

it should reset the database and run the server

<br>

##### Thanks for taking a look at my project!