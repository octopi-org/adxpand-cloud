# The amplifyIo API Project 

> a proud BuildIT.Io project

# **Contents**

* [Top](#the-amplifyio-api-project)
	* [Overview](#overview)
		* [Technologies and Documentation](#all-the-tech)
		* [What you need to know](#using-git-for-ides)
	* [Setting Up](#getting-started)
	* [Making Changes](#making-changes)
	* [Some stuff to care about](#note-to-developer)

## Overview

**amplifyIo**:copyright: is a digital infrastructure that enables clients to visualize data from Search Engine Marketing(SEM) campaigns at a microscopic level, marrying the business logic of clients together with the data from sales campaigns to help companies align their campaign objectives and methodology with their SEM campaigns. 

This project is a private project and further information regarding the specific business logic of **amplifyIo:copyright:** can only be obtained by request to the maintainer of this **GitHub**:copyright: repository.

### All the Tech

Click on the links to read more about the technologies in the respective repositories!

#### Languages Used
1. [Python 3.9 or greater](https://www.python.org/downloads/release/python-390/)
2. [MySQL 8.0](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/)

#### Frameworks
1. [django](https://www.djangoproject.com/) + [django REST Framework](https://www.django-rest-framework.org/)

#### Libraries
1. [pandas](https://pandas.pydata.org/)
2. [Google Ads API Python Client Library](https://github.com/googleads/google-ads-python/)

#### Subsidiary Technologies 
1. [Google Ads API](https://developers.google.com/google-ads/api/docs/start)
2. [Google Cloud Platform](https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=japac-SG-all-en-dr-bkws-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_498697927861-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP%20~%20General_cloud%20-%20platform-KWID_43700020290823408-kwd-297423147525&userloc_9062542-network_g&utm_term=KW_cloud%20google%20platform&gclid=Cj0KCQjwmIuDBhDXARIsAFITC_5lqqFuB4b4MKNYfuit5KON90y88vwl8t6tQyFvPUbKDJWL4Xk2cGkaAobgEALw_wcB&gclsrc=aw.ds)
	* [App Engine](https://cloud.google.com/appengine/?utm_source=google&utm_medium=cpc&utm_campaign=japac-SG-all-en-dr-bkws-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_505050348941-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Compute%20~%20App%20Engine_app%20engine-google%20cloud-KWID_43700008276145764-kwd-79074736158&userloc_9062542-network_g&utm_term=KW_google%20cloud%20app%20engine&gclid=Cj0KCQjwmIuDBhDXARIsAFITC_5UZ11f7uiEulTaKp6Gd6-PSq06kK7l7MvDADClSdcYMlo7pshxFYQaAi3gEALw_wcB&gclsrc=aw.ds)
	* [CloudSQL](https://cloud.google.com/sql/?utm_source=google&utm_medium=cpc&utm_campaign=japac-SG-all-en-dr-bkwsrmkt-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_505012083112-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Databases%20~%20Cloud%20SQL_cloud%20storage-google%20cloud%20sql-KWID_43700054967487601-kwd-28489936691&userloc_9062542-network_g&utm_term=KW_google%20cloud%20sql&gclid=Cj0KCQjwmIuDBhDXARIsAFITC_7waWh5yIuH4ViOG_XcNETBeUcbPgYRfkGsHctJHfj11h_TI9p7v5caArh0EALw_wcB&gclsrc=aw.ds)
	* [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)

### Some "Pre-Requisites" Before We Begin...

> For an in-depth walk-through for setting up an entire project on GCP, it is best to refer back to the Google Cloud Platform (GCP) docs to see how a Django project is set up on GCP and how to configure a GCP project yourself (alternatively, create your own project!). 

This [tutorial](https://cloud.google.com/python/django/appengine) will walk you through on how to configure your own GCP Project with django.
> ***DISCLAIMER AND REITERATION: This GitHub is not meant to teach you how to set up on GCP.** Do note that knowledge on how Django is set up on GCP is **NOT REQUIRED** as the set up has already been taken care of during the configuration of this repository.*

This [tutorial](https://github.com/buildit-Io/README#github-for-the-new-dev) will walk you through on how to start working on this project with GIT

This [tutorial](https://github.com/buildit-Io/README#using-git-for-ides) will walk you through on how to use an IDE together with GIT

Alternatively, head over to BuildIT.Io's [introduction page](https://github.com/buildit-Io/README) for all the things a new developer needs to know.

## Getting Started
1. Clone this repository into a desired folder
2. Create a virtual environment using your IDE (we recommend strictly following the procedure of your IDE rather than using the in built command line and running `virtualenv new-env` to create the virtual environment). Place the location of your environment at the same level where the .gitignore file is. You may also be prompted to use a requirements.txt file to download all necessary packages. This can be found in the \amplifyIo directory.
3. Test if your virtual environment has been created successfully by running
	
	For Mac/Linux:
	
	```
	new-env/bin/activate
	```
	
	For Windows:
	```
	new-env\Scripts\activate
	```
   Always remember to be running from the **correct** directory where your `new-env` is. if successful you should see something similar to below:
   
   	```
	(new-env) MyComputer\User-19982: $
	```
5. [Download Google Cloud SDK](https://cloud.google.com/sdk/?utm_source=google&utm_medium=cpc&utm_campaign=japac-SG-all-en-dr-bkws-all-pkws-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_396364030216-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Developer%20Tools%20~%20Cloud%20SDK_cloud%20sdk-general%20-%20Products-KWID_43700049545049408-kwd-76317487932&userloc_9062507-network_g&utm_term=KW_google%20cloud%20sdk&gclid=CjwKCAjwu5CDBhB9EiwA0w6sLflBzTZ-QAQVpTciNqK96RHXg_lbyDyN1NhX4FDUx7aEhUOO7djQTRoCkToQAvD_BwE&gclsrc=aw.ds)
6. [Download Cloud SQL Proxy](https://cloud.google.com/python/django/appengine#installingthecloudsqlproxy) (we recommend placing this file in the same location as where the Google CLoud SDK Program is kept, although it should not matter since Cloud SQL Proxy can technically run from any directory in the command line)
7. Open and run the Google Cloud SDK.
8. Next, we need to connect to the Google Cloud Server to even begin making edits.
	For Window Users:
	
	```
	cloud_sql_proxy.exe -instances"amplifyio-308412:asia-southeast1:amplify-io"=tcp:3306
	```
	
	For Mac/Linux Users:
	
	```
	.\cloud_sql_proxy -instances"amplifyio-308412:asia-southeast1:amplify-io"=tcp:3306
	```
 	
	At times you may try to connect and result in the following error:
	
	```
	Can't connect to MySQL server on '127.0.0.1' (3306)
	```
	
	This is completely normal if you already downloaded MySQL or equivalent technologies in your computer as 3306 is usually the main port for servers to listen for calls on. In such cases, just check [which ports are open on your computer](https://smallbusiness.chron.com/identify-ports-use-computer-55829.html) and substitute 3306 with an available port provided by the computer. **Keep this running throughout the development process**.
7. Now, we need to install all the dependencies into the virtual environement you created in 2 if this has not been done. On the terminal, actiavte your environement and run the following command:
	
	```
	pip install -r requirements.txt
	```
8. Once all this is done, we can then run django normally. Navigate to the folder with the `manage.py` file and start a local web server.
	```
	python manage.py runserver
	``` 
	Then, in your browser, proceed to 
	```
	http://localhost:8000
	```
9. Add an account to use the django admin console (signing in and viewing the databases from the built-in admin page on django)
	
	```
	python manage.py createsuperuser
	```
	Follow the prompts, then restart your local web server again.
	
You can now make changes to your django project. Here are some [reminders](#note-to-developers) when making changes visible on the local web server.

## Making Changes
With django, you need to enter a few standard commands everytime changes are made. This is done by 
	
	```
	python manage.py makemigrations
	python manage.py makemigrations amplifyIoAPI-or-any-other-project
	python manage.py migrate
	```

## Note to Developer:
0) Always activate cloud_sql_proxy.exe to write local changes into the remote GCP project
1) Stop your local webserver with `Ctrl-C` if you intend to use manage.py to run other functions like `createsuperuser`.
2) Remember to update your urls.py and settings.py to include any new data models and urls you have built in Django
3) Check that you are already in the environment 
4) For every new property, always start with python manage.py startproject new-property-name on the command line
5) After adding the new environment and making the necessary changes on urls and settings, don't forget to do python manage.py makemigrations, python manage.py makemigrations new-property-name and 
python manage.py migrate to complete bootstrapping
4) to check for changes, use python manage.py runserver 
5) to generate static changes, use python manage.py collectstatic 
5) finalise changes into GCP by doing gcloud app deploy

