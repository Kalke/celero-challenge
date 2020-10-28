# api-celero-challenge
    Henrique Kalke Challenge
    This is an API built in Python using Django Rest Framework, the objective is create an CRUD to 
    manage the Database. Here you can see how to run the application! Hope you enjoy :)

# Process Execution

## Docker 

#### Build

    sudo docker-compose build

#### Running

    sudo docker-compose up

# REST API

Allowed methods GET, POST, PUT, DELETE
On the folder notebook you can find cells already configured to do the requests. 

#### Read All

`GET http://0.0.0.0:8000/api/challenge`

### Response

    "GET /api/challenge HTTP/1.1" 200 1501

    [
    {
        "unique_id": 1234567,
        "id": 1,
        "name": "Henrique Kalke",
        "sex": "M",
        "age": 20,
        "height": 182.0,
        "weight": 98.0,
        "team": "Brazil",
        "noc": "BRA",
        "games": "2012 Summer",
        "year": 2012,
        "season": "Summer",
        "city": "London",
        "sport": "Basketball",
        "event": "Basketball Men's Basketball",
        "medal": "Silver"
    },
    {
        "unique_id": 1,
        "id": 1,
        "name": "Henrique Kalke",
        "sex": "M",
        "age": 20,
        "height": 182.0,
        "weight": 98.0,
        "team": "Brazil",
        "noc": "BRA",
        "games": "2012 Summer",
        "year": 2012,
        "season": "Summer",
        "city": "London",
        "sport": "Basketball",
        "event": "Basketball Men's Basketball",
        "medal": "Silver"
    },
    .
    .
    .
]

#### Create an Athlete Event
    You must pass an unique id

`POST http://0.0.0.0:8000/api/challenge`

### Payload

    { 
    "unique_id":13,
    "id": 1,
    "name": "Henrique Kalke",
    "sex": "M",
    "age": 20,
    "height": 182,
    "weight": 98,
    "team": "Brazil",
    "noc": "BRA",
    "games": "2012 Summer",
    "year": 2012,
    "season" : "Summer",
    "city": "London",
    "sport": "Basketball",
    "event": "Basketball Men's Basketball",
    "medal": "Silver"
    }

#### Response

    "POST /api/challenge HTTP/1.1" 201 298

    {
    "unique_id": 13,
    "id": 1,
    "name": "Henrique Kalke",
    "sex": "M",
    "age": 20,
    "height": 182.0,
    "weight": 98.0,
    "team": "Brazil",
    "noc": "BRA",
    "games": "2012 Summer",
    "year": 2012,
    "season": "Summer",
    "city": "London",
    "sport": "Basketball",
    "event": "Basketball Men's Basketball",
    "medal": "Silver"
    }

#### Delete all

`DELETE http://0.0.0.0:8000/api/challenge`

### Response

    "DELETE /api/challenge HTTP/1.1" 204 59

    {
    "message": "13 Athlete Events were deleted from database!"
    }   

#### Retrieve information using unique id

`GET http://0.0.0.0:8000/api/challenge/0`

### Response

    "GET /api/challenge/2 HTTP/1.1" 200 295

    {
    "unique_id": 0,
    "id": 1,
    "name": "Henrique Kalke",
    "sex": "M",
    "age": 20,
    "height": 182.0,
    "weight": 98.0,
    "team": "Brazil",
    "noc": "BRA",
    "games": "2012 Summer",
    "year": 2012,
    "season": "Summer",
    "city": "London",
    "sport": "Basketball",
    "event": "Basketball Men's Basketball",
    "medal": "Silver"
    }

#### Update information using unique id

`PUT http://0.0.0.0:8000/api/challenge/0`

### Payload

    {
    "unique_id": 0,
    "id": 1,
    "name": "Henrique Teixeira Kalke",
    "sex": "M",
    "age": 20,
    "height": 182,
    "weight": 98,
    "team": "Brazil",
    "noc": "BRA",
    "games": "2012 Summer",
    "year": 2012,
    "season" : "Summer",
    "city": "London",
    "sport": "Basketball",
    "event": "Basketball Men's Basketball",
    "medal": "Silver"
    }

### Response

    "PUT /api/challenge/0 HTTP/1.1" 200 307

    {
    "unique_id": 13,
    "id": 1,
    "name": "Henrique Teixeira Kalke",
    "sex": "M",
    "age": 20,
    "height": 182.0,
    "weight": 98.0,
    "team": "Brazil",
    "noc": "BRA",
    "games": "2012 Summer",
    "year": 2012,
    "season": "Summer",
    "city": "London",
    "sport": "Basketball",
    "event": "Basketball Men's Basketball",
    "medal": "Silver"
    }

#### Delete information using unique id

`DELETE http://0.0.0.0:8000/api/challenge/0`

### Response

    "DELETE /api/challenge/15 HTTP/1.1" 204 69

    {
    "message": "The specified Athletic Event was deleted successfully."
    }

