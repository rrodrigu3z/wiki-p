
![CI](https://github.com/rrodrigu3z/wiki-p/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/rrodrigu3z/wiki-p/branch/master/graph/badge.svg?token=1IKG6EXSCI)](https://codecov.io/gh/rrodrigu3z/wiki-p)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/rrodrigu3z/wiki-p.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/rrodrigu3z/wiki-p/context:python)

# Wiki-P: Wikipedia article paragraph extractor

A simple lambda function for extracting paragraphs from a Wikipedia article, or more specific, a wikipedia page title.

## Installation
This lammbda function is built using the [serverless framework](https://www.serverless.com/),
so you need to install it in order test and deploy this function. You can check the
[getting started](https://www.serverless.com/framework/docs/getting-started/) page for details.

Also, it's recommended to use a virtualenv.

```
git clone https://github.com/rrodrigu3z/wiki-p
cd wiki-p
pip install -r requirements.txt
```

## Deployment
In order to deploy the lambda function, make sure you have configured your AWS credentials.
Also, check `serverless.yml` for details about the deployment configuration. Then, simply run:

`serverless deploy`

## Run Locally

You can run the function locally using `serverless invoke local`, for example:

```
serverless invoke local --function paragraphs --data '{"title":"Artificial_intelligence"}'
```

## API

The function receives a Wikipedia page `title`:
```
{"title": "Artificial_intelligence"}
```

And responds with the following `body`:

```
[
  {"paragraph": "Cupidatat fugiat fugiat mollit nulla sunt labore sunt nisi consectetur cupidatat." },
  {"paragraph": "Tempor irure sint fugiat nisi. Elit ut do mollit et ullamco." },
  ...
]
```

## Run Tests
This repo uses `pytest`:

```
pip install pytest
pytest
```
