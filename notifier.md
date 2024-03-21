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

