# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account DONE
2. Select a unique tenant domain DONE
3. Create a new, single page web application DONE
4. Create a new API DONE
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions: DONE
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for: DONE
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`


https://dev-r2v8kom9.auth0.com/authorize?
  audience=coffeeShop&
  response_type=token&
  client_id=JQzfDDyl9mbkxw0p73d8fwXxlK5xQSwV&
  redirect_uri=http://localhost:8100


  JWT Barista: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1rUkJOelF6UlRrelJFRXpOREUyTlRFd056QXpNREUzUlVSQlFUYzJSRGcyTmtZM1FUUXhOQSJ9.eyJpc3MiOiJodHRwczovL2Rldi1yMnY4a29tOS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxZTBhZWFkYThmZmEwMDNkMjA2OGJjIiwiYXVkIjoiY29mZmVlU2hvcCIsImlhdCI6MTU5NTgwNDQ0MCwiZXhwIjoxNTk1ODExNjQwLCJhenAiOiJKUXpmRER5bDltYmt4dzBwNzNkOGZ3WHhsSzV4UVN3ViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOltdfQ.yhJEzji_2Wq99-LhPRnq7XjTsWACgU3z5ItmM1H8Aaq3ZkmJYpyOW7zCTae-gAVkgaiV6Z8cXRGF7vpItH4GGw-kePvYvMC6LxCOqco8mHVSQY-OznErTQk5rxbYLjRyirD6zSCZ6uOkTMHpTF2Xa5NBkYYtEwsZ9kz6zXpnNqGXaPE4qQ4ZQqEKmuhBuqYeC526xS3VpgL9YT29Y-SVVsZSZ7QT1lGMWIOZOebzDWiAEO_0R0xekbiyk2aQBMAImzUHk7ShZnmjgIIzTSOcZi8tlwcnItz30VSxypab6Z8FiNWWyuPSVK15hcjdfurV-cZKOKn_UqPTpE_JH2HsAg
  
  JWT Manager: 

  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1rUkJOelF6UlRrelJFRXpOREUyTlRFd056QXpNREUzUlVSQlFUYzJSRGcyTmtZM1FUUXhOQSJ9.eyJpc3MiOiJodHRwczovL2Rldi1yMnY4a29tOS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTMxOTc2NDk2MzE2NDYxNTQ0MzAiLCJhdWQiOlsiY29mZmVlU2hvcCIsImh0dHBzOi8vZGV2LXIydjhrb205LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTU4MDQ2NzYsImV4cCI6MTU5NTgxMTg3NiwiYXpwIjoiSlF6ZkREeWw5bWJreHcwcDczZDhmd1h4bEs1eFFTd1YiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.vQL8BJVUMjUWWOeCCHD5i3mo61qI19SarJn8gcCorXYf-mYe5qHuXUdEYBFr5SnnvTkruLWwxAgfZYEJWXwAD1hJL3GpoBc0n6s4gtMpc6i4iLb3cgM-UsLjgKz4Xs4BV3VZsQAomy8u8Y27Rl4z1oDNU6aWbUPi3Bq23YhZpulhd0oEGJMVHLQ8TZlz_eNYXd2tf_CIhnTBcWpNUSs8mTXoCtLLLluCb0vefi3ERfowxhBoYxqWfFw8SnmCDiABC8b-qmVK5bY8b2z6vtAihjEBQ9u0XiiCuT4ns7DCoAplRVdcZGfiji7yl19wusqPPu8xE1AkXvzOTB9XZ2Aong