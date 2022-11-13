# Project #4: Continuous Delivery of FastAPI Movie_List_API Severlessly on AWS

[![Python application test with Github Actions](https://github.com/nogibjj/Project4_FastAPI_YZ/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/nogibjj/Project4_FastAPI_YZ/actions/workflows/main.yml)

## Overview

In this project, I built a web app using FastAPI to create a movie list. It will load movies from a json file, including each movie's title, poster, rating, released year and genre. This web app has four functions: 1. List all the movies; 2. Pick a random movie for the user; 3. Return a movie by its index; 4. Return a movie by its title. After testing it in Codespaces, I packed all the dependencies and stored in AWS S3. Finally in AWS, I deployed the web app using Lambda function, API Gateway, CodePipeline and Elastic Beanstalk.

Here is the flow chart and demo video: 

![image](https://user-images.githubusercontent.com/110933007/201536067-50c35ad0-5a1e-42e4-afea-ac9696abcc30.png)


## Methodology

### GitHub Codespaces
Code for building this web app is in **main.py**. The movie title, poster, genre, rating and released year come from **movies.json**. 
To start the server locally, type the following command in terminal:
```
uvicorn main:app --reload
```
FastApi provides a console interface to look at all our apis on the server. Type "*/docs#*" after the root path.

### GitHub repo <-> AWS S3
Pack all the dependencies for building this web app into a zip file, and uploaed the zip file to AWS S3 bucket. 
```
pip install -t lib -r requirements.txt
(cd lib; zip ../lambda_function.zip -r .)
zip lambda_function.zip -u main.py
zip lambda_function.zip -u movies.json
```

### Lambda Function
Create a lambda function, upload the code source from Amazon S3 location which holds the zip file. 

**NOTE:** Change the lambda handler name to be the same as our *file_name.handler_name*. This is because the Lambda function handler is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method.

Create several tests to make sure it is working.


### Deploy the web app

1. In Lambda function - Configuration - Function URL, create a function URL, and Lambda will automatically generate a unique URL endpoint.

2. In Amazon API Gateway: Create API - REST API - Build - Choose Lambda Function as the integration point.

3. Using Elastic Beanstalk and CodePipeline: First create a new application in Elastic Beanstalk choosing python as the platform, then create a CodePipeline choosing your GitHub repo as source provider (need password to allow permissions) and the Elastic Beanstalk that just created as deploy provider. 


## Way to use

1. Lambda Configure Function URL:
```
https://3aiwdvlj5kasnschcz6rwj45nu0jgfnx.lambda-url.us-east-1.on.aws/
https://3aiwdvlj5kasnschcz6rwj45nu0jgfnx.lambda-url.us-east-1.on.aws/list-movies
https://3aiwdvlj5kasnschcz6rwj45nu0jgfnx.lambda-url.us-east-1.on.aws/random-movie
https://3aiwdvlj5kasnschcz6rwj45nu0jgfnx.lambda-url.us-east-1.on.aws/movies_by_index/{index_number}
https://3aiwdvlj5kasnschcz6rwj45nu0jgfnx.lambda-url.us-east-1.on.aws/get-movie_by_title/{movie_title}
```

2. API Gateway URL:
```
https://cljn6rt1n1.execute-api.us-east-1.amazonaws.com/dev/
https://cljn6rt1n1.execute-api.us-east-1.amazonaws.com/dev/list-movies
https://cljn6rt1n1.execute-api.us-east-1.amazonaws.com/dev/random-movie
https://cljn6rt1n1.execute-api.us-east-1.amazonaws.com/dev/movies_by_index/{index_number}
https://cljn6rt1n1.execute-api.us-east-1.amazonaws.com/dev/get-movie_by_title/{movie_title}
```

3. CodePipeline:
```
http://fastapimovielist-env.eba-du53t6i7.us-east-1.elasticbeanstalk.com/
http://fastapimovielist-env.eba-du53t6i7.us-east-1.elasticbeanstalk.com/list-movies
http://fastapimovielist-env.eba-du53t6i7.us-east-1.elasticbeanstalk.com/random-movie
http://fastapimovielist-env.eba-du53t6i7.us-east-1.elasticbeanstalk.com/movies_by_index/{index_number}
http://fastapimovielist-env.eba-du53t6i7.us-east-1.elasticbeanstalk.com/get-movie_by_title/{movie_title}
```