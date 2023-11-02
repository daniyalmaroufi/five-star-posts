# five-star-posts
A simple Django Rest Framework application

## API

To use the API, user must first login to their account using Django Auth.

### Posts

Shows the list of posts ordered by id descending with the title of each post, the number of users rated that post and its rating. If the logged in user has rated a post before, their rating would be shown.

`GET /api/posts`

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "ok": true,
    "posts": [
        {
            "title": "Post Three",
            "scores_count": 0,
            "score": 0.0
        },
        {
            "title": "Second Post",
            "scores_count": 1,
            "score": 4.0
        },
        {
            "title": "Post 1",
            "scores_count": 2,
            "score": 4
        }
    ]
}
```

#### Exceptions

Happens when there are no posts in the database.

```json
HTTP 404 Not Found
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "ok": false,
    "detail": "No posts exist"
}
```

### Score

A logged in user rates a post by calling this method. if the user has never rated the post before, a new rating would be submitted and otherwise their previous rating would get updated.

`POST /api/score`

data: `{"post":1,"score":5}`

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "ok": true,
    "detail": "set"
}
```

#### Exceptions

Happens when the requested post does not exists or the rating is not between 0 and 5.

```json
HTTP 403 Forbidden
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "ok": false
}```

## Create venv

Clone the repository and create a virtual environment:

```bash
python -m venv venv
```

## Activate venv

Activate the virtual environment by running:

```bash
source venv/bin/activate
```

## Install Requirements

Install the python packages on the `venv` using this command:

```bash
pip install -r requirements.txt
```

## Django

### Run server

You can run the development server by:

```bash
python manage.py runserver
```

### Migrate

to migrate the models to the database use:

```bash
python manage.py migrate
```

### Create Super User

```bash 
python manage.py createsuperuser
```

## Developer

[Daniyal Maroufi](https://github.com/daniyalmaroufi/)
