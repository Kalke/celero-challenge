# api-celero-challenge
#### Henrique Kalke Challenge
#### This is an API built in Python using Django Rest Framework, the objective is create an CRUD to 
#### manage the Database. Here you can see how to run the application! Hope you enjoy :)

# Process Execution

## Docker

#### Running



## Docker 

#### Build

    sudo docker build . -t api_text_extractor

#### Run
    gtoken=`gcloud auth print-identity-token` && sudo docker run -it -p 9191:9191 -e MODE=dev -e TAG="0.0.0" -e PORT=9191 -e TOKEN=$gtoken -e VERSION_MODEL="1.0.0" api_text_extractor
