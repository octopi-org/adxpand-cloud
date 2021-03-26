# Getting started with Django on Google Cloud Platform on App Engine Standard

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=appengine/standard_python38/django/README.md

This repository is an example of how to run a [Django](https://www.djangoproject.com/) 
app on Google App Engine Standard Environment. It uses the 
[Writing your first Django app](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) as the 
example app to deploy.


# Tutorial
See our [Running Django in the App Engine Standard Environment](https://cloud.google.com/python/django/appengine) tutorial for instructions for setting up and deploying this sample application.
Download the google cloud sdk and the google_cloud_prox.exe for your system to write changes from local to GCP

# Note to Developer:
0) Always activate cloud_sql_proxy.exe to write local changes into the remote GCP project
1) Remember to update your urls.py and settings.py to include any new data models and urls you have built in Django
2) Check that you are already in the environment 
3) For every new property, always start with python manage.py startproject new-property-name on the command line
3) After adding the new environment and making the necessary changes on urls and settings, don't forget to do python manage.py makemigrations, python manage.py makemigrations new-property-name and 
python manage.py migrate to complete bootstrapping
4) to check for changes, use python manage.py runserver 
5) to generate static changes, use python manage.py collectstatic 
5) finalise changes into GCP by doing gcloud app deploy

