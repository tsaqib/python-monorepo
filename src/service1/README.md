# Service 1

## How to run locally (live reload only works this way)

```bash
cd /src/service1
virtualenv .
source bin/activate
pip install -r requirements.txt
cd /src
uvicorn service1.main:app --reload
```

## How to run locally using docker-compose

Go to `/src` and execute the following:

```bash
docker-compose -f service1/docker-compose.dev.yml up --build
docker-compose -f service1/docker-compose.dev.yml down

# To remove pip packages (purge site-packages cache)
docker-compose -f service1/docker-compose.dev.yml down --rmi=local --remove-orphans -v
```

## How to build for deployment

Go to `/src` and execute the following:

```bash
docker-compose -f service1/docker-compose.prod.yml up --build
docker-compose -f service1/docker-compose.prod.yml down

# To remove pip packages (purge site-packages cache)
docker-compose -f service1/docker-compose.yml down --rmi=local --remove-orphans -v
```

## Unit tests

First, create a `virtualenv` for the respective project directory or centrally at `/` and then execute the following:

```bash
cd /src
python -m unittest discover -p "*_test.py" # All tests in the repo
python -m unittest discover -p "*_test.py" -s service1 # Project specific
```

## Find code coverage

Go to `/src` and execute the following:

```bash
coverage run -m unittest discover -p "*_test.py" -s service1
coverage report
```

## Consistent code formatting

Go to `/src` and execute the following:

```bash
black common/ service1/ --exclude "/(bin|lib)/"
```

## Find dead code

Go to `/src` and execute the following:

```bash
vulture service1/ --ignore-decorators "@router.*"
```

## Find package vulnerability

Go to `/src` and execute the following:

```bash
safety check
```

## Find unsecure coding practice

Go to `/src` and execute the following:

```bash
bandit -r service1/ common/
```

## Perform statical analysis

Go to `/src` and execute the following:

```bash
mypy service1/main.py
```

## Calculate cyclomatic complexity and maintenance index

```bash
radon cc -as service1/ common/
radon mi -s service1/ common/
```