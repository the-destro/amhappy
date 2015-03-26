amhappy
=======

amhappy is all about making QA, dev, and designers lives happier by making
it easier to spin up sandboxes of web applications. THIS IS Proof Of Concept
quality code!

-----------
Terminology
-----------
* Container: A packaged "machine" as defined by a Dockerfile
* Application: A group of Containers, defined in a fig.yml or a docker-compose.yml, that allow a system to operate. For example Mysql+Apache/PHP(dependencies)+Code containers is an Application
* Happinstance: It is a "Happy Instance" of an application with a specific configuration. Things like port, specific branch and VHOST are all part of a Happinstance's configuration.
* Happstore: Our repository of configured applications on Git.(WIP, currently a directory)


--------------------
General Architecture
--------------------

amhappy is a REST-ish webserver written in Pyramid using Cornice on the backend with an AngularJS based web UI.

Setup instructions
##################
(WIP)
To achieve this magical land of happiness, some initial setup is required.

1. Install Docker
2. Install CouchDB(either standalone or via an image)
3. Pull and run the jwilder/nginx-proxy image for vhost routing support
4. Pull a fig repository
5. Make adjustments to this application's development.ini to point at your fig repository checkout.
6. Start it up!

Usage
#####

The use case flow should be pretty straightforward

---------
Dashboard
---------

The main page is the dashboard. It allows you to see Happinstances that have been created, their statuses and links
to the detail page. Also there will be a link to the virtualhost, if applicable.

------
Create
------

The create page has a dropdown of all of the applications in the Happstore. When one selected it loads the .yaml file
for it and turns it to JSON and displays it for the user. It also looks for Environment keys and puts them below the
config along with a form to customize them. Once all selections, plus the Happinstance name, are filled out click
submit to create the Happinstance. The app will then take you back to the dashboard.
