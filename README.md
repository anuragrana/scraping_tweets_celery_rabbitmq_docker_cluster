### Scraping tweets quickly using celery, RabbitMQ and Docker cluster with Rotating proxy
-------------------------
Please go through the below article for better understanding:

https://www.pythoncircle.com/post/518/scraping-10000-tweets-in-60-seconds-using-celery-rabbitmq-and-docker-cluster-with-rotating-proxy/

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

-------------------------------------------

##### using host postgres from docker container
- for allowing connection from anywhere:

  in /etc/postgres/ postgres.conf file , update listen_addresses set it to '*' to listed from all IPs

- For authorizing any user from docker IPs, in pg_hba.conf file add line:

  `host    all             all             172.19.0.0/16            trust`

  172.19.0.0/16 is the range of docker container.

- restart the postgres: `sudo /etc/init.d/postgres restart`

- Host for DB config would be your local machine IP. Change in config file.


