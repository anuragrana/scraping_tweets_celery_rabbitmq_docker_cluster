### Boilerplate code for celery rabbitmq docker cluster

-------------------------

##### Version

- Docker-compose : `docker-compose version 1.8.0, build unknown`
- Docker : `Docker version 17.12.0-ce, build c97c6d6`
-----------------------


##### How to run

- Run command `sudo docker-compose up`

- Above command will start 1 container for each worker and rabbit

- Now go inside one worker container and run `python -m celery_main.task_submitter`

- this will start pushing tasks in rabitmq and workers
---------------------


##### Speedup the process

- To run 5 workers and 1 rabbitmq:

  `sudo docker-compose up --scale worker=5`

- Do not increase concurrency to too much in dockerfile as machine might not be able to handle it

  `ENTRYPOINT celery -A test_celery worker --concurrency=10 --loglevel=info`


