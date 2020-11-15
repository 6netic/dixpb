First of all, this project refers to project8 where all the main code is imported from.
So if you want to install it locally, please go and have a look at that project.

The aim of this project is to prepare the code for deployment on IAAS platform.
This website is developped in Python 3.7.6 using Django framework v.3.1.

At the begining, we have 529 products from 41 categories.
Every Sunday at 3:30 some products will be added randomly.
This is done thanks to a cron task.

As we're working in continuous integration I chose TravisCI to automate the checking processes while changes are made on the second branch.
You can visit it on : https://travis-ci.com/github/6netic/dixpb

To make it work correctly, you'll need to install a web server as Nginx to transfer requests from public address to private one on your hosting provider.
As it's a Django app, you'll also need a Python HTTP server to deal with requests as Gunicorn.

To be sure this website will always stay online, I installed and configured Supervisor.

For monitoring performances, logs and error handling I used Sentry.

You can see the website working on : http://206.189.19.209





