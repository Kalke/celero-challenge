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

    sudo docker build . -t api_text_extractor

#### Run
    gtoken=`gcloud auth print-identity-token` && sudo docker run -it -p 9191:9191 -e MODE=dev -e TAG="0.0.0" -e PORT=9191 -e TOKEN=$gtoken -e VERSION_MODEL="1.0.0" api_text_extractor
