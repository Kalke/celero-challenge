# api-celero-challenge

# Process Execution
## Local

#### Environment
    conda create -n api-celero-challenge python=3.8
    source activate api-celero-challenge
    pip install -r requirements.txt

#### Make migrations 

    python manage.py makemigrations

## Docker 

#### Build

    sudo docker build . -t 

#### Run

