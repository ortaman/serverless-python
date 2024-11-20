
## Installation
- Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository1) 
- Install [docker descktop](https://docs.docker.com/desktop/install/ubuntu/)

## Transactions challenge
This is a sample template for the project - Below is a brief explanation of the struct:

```bash
app
├── local-db                    <-- Files to run docker PSQL database in local docker container
├── src                         <-- Source code for a lambda function
│   └── infra                   <-- Infrastucture variables
│   ├── adapters                <-- Lambda function code
│   └── usecase                 <-- This layer holds the business logic of our application
│   └── repository              <-- This layer is responsible for communicating with data sources, whether it is Database, another services, or external APIs
│   └── utils                   <-- Collection of small common functions, data and templates
├── Dockerfile                  <-- Dockerfile to generate local/deploy image 
├── .gitignore                  <-- Ignore the files and directories which are unnecessary to project 
├── docker-compose.yml          <-- To run local PSQL database conatiner
├── Makefile                    <-- Defines set of tasks to be executed
```

## Set up and run the project:
- Clone the repository to your local machine:
```bash
git clone https://github.com/ortaman/serverless-python.git
```

- Go to app folder and run:
```bash
docker compose up
```

- Open a new terminal and run the next command with the email to send the information:
```bash
curl "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"body": "{\"email\":\"username@domain.com\"}"}'
```