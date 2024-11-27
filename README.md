## Transactions challenge
This is a sample template for the proyect - Below is a brief explanation of the struct:

```bash
.
├── local-db                    <-- Files to run docker PSQL database in local docker container
├── stori-test                  <-- Source code for a lambda function
│   └── infra                   <-- Infrastucture variables
│   ├── adapters.go             <-- Lambda function code
│   └── usecase                 <-- This layer holds the business logic of our application
│   └── repository              <-- This layer is responsible for communicating with data sources, whether it is Database, another services, or external APIs
│   └── utils                   <-- Collection of small common functions, data and templates
├── Dockerfile                  <-- Dockerfile to generate local/deploy image 
├── go.mod.md                   <-- Lists the specific versions of the dependencies
├── go.sum.md                   <-- Maintains the checksum so when you run the project again it will not install all packages again
├── .gitignore                  <-- Ignore the files and directories which are unnecessary to project 
├── docker-compose.yam          <-- To run local PSQL database conatiner
├── Makefile                    <-- Executable file
└── template.yaml               <-- Specifies the infrastructure components, 
```

## Requirements

* [Docker installed](https://www.docker.com/community-edition)
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* AWS CLI already configured with Administrator permission (to deploy)
* You must have installed Python 3.12 to build the code (to deploy).


## Setup process

### Installing dependencies & building the target 

In this example we use the built-in `sam build` to build a docker image from a Dockerfile and then copy the source of your application inside the Docker image.  
Read more about [SAM Build here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-build.html) 

### Local development

**Invoking function locally through local API Gateway**

```bash
cd sam-pyhon

make run-db                # run the command in a terminal (run container with local PSQL database)
make test-local            # run in another terminal (Invoke lambda function locally)
```

**To test local running the function in local (change to your email)**

```bash
curl "http://localhost:3000/send_email" -d "{\"email\":\"ente011@gmail.com\"}"
```

**To run the aplication deployed in AWS run:**

```bash
curl -X POST https://rq83jjolo6.execute-api.us-west-1.amazonaws.com/Prod/send_email -d "{\"email\":\"ente011@gmail.com\"}"
```
