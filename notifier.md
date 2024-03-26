# Notifier : service to send notifications to different channels 

# Overall architecture: 

![Notifier](<notifier.png>)

# Components:
   *    **Fastapi Server**: Server to accept the notification payload from the different services and then add that task to the redis queue.
   *    **Fastapi Background**: Celery worker to execute the tasks registered by the server.
   *    **Redis Queue**: Message bus for the server to register the task/event. Can be used as a storage for the tasks results of the worker.

# Steps:
   * Notifier's job is only to send the notification to the respective channel.
   * It doesn't care from which service it has arrived. It should be independent of it.

      1. Get the payload from different resource - Orders srvcs, Payment srvcs, Shipping srvcs.
      2. Generate the event payload.
      3. Add the event payload to redis.
      4. Background, celery worker picks up the event payload and sends the mail.

# How to send an email using python:

  * https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html
  * https://github.com/kootenpv/yagmail
  * https://realpython.com/python-send-email/
  * https://www.twilio.com/en-us/blog/how-to-send-emails-in-python-with-sendgrid
  * 


# Some random notes and references for understanding celery:

   * References links: 

      * Celery provides signals on which you can attach your listeners: https://docs.celeryproject.org/en/stable/userguide/signals.html
    
      * https://www.distributedpython.com/2018/10/26/celery-execution-pool/
    
      * https://medium.com/analytics-vidhya/python-celery-distributed-task-queue-demystified-for-beginners-to-professionals-part-1-b27030912fea
    
      * https://ayushshanker.com/posts/celery-in-production-bugfixes
    
      * Celery workers: https://docs.celeryq.dev/en/stable/userguide/workers.html
      
      * Celery worker pools: https://celery.school/celery-worker-pools

      * Celery queues:

         * https://stackoverflow.com/a/72572920/10283295

         * https://medium.com/@ffreitasalves/using-celery-with-multiple-queues-retries-and-scheduled-tasks-589fe9a4f9ba
   
      * Celery with KEDA: https://learnk8s.io/scaling-celery-rabbitmq-kubernetes
   
   * My related notes:

      * How celery makes sure each worker has a unique hostname when autoscaling is enabled:

         * `celery -A proj worker --loglevel=INFO --autoscale=10,2 -n worker%d@%h`

         * Each Celery worker process runs in its own OS process and has its own Python interpreter. When a new worker process is created, it is assigned a unique hostname based on the format you provide, which typically includes the machine's hostname or IP address. This hostname is used to uniquely identify the worker process in the Celery cluster.

         * Even if multiple Celery worker processes are running on the same machine, each process will have a unique hostname based on the machine's hostname and a random UUID. This ensures that each worker process has a unique name within the Celery cluster, even if they are running on the same machine.
      
      * A celery cluster can be composed of multiple workers, each of which can have multiple threads or processes for executing tasks concurrently.

      * A node, on the other hand, refers to a single worker process in the Celery cluster. Each node is identified by a unique name, which is usually composed of a hostname and a worker ID.
   
   * 
