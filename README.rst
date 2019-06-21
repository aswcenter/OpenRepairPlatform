Atelier Soudé
=============

OpenRepairPlatform is a Django based application designed to organize collaborative repair structures, features provides organization managment, event publishing, community members managment, repair tracking and sharing.

The plateform is created by Atelier Soudé, an organization which repair everyday's people electric and electronic objects in Lyon, France.


Dépendances :
-------------

- postgresql

---------------------------------

Lancer le projet en développement :
-----------------------------------

Par défault, en développement, l'application tente de se connecter à la BDD
"ateliersoude" en local en utilisant le compte de l'utilisateur courant, sans mot de passe

.. code-block:: bash

    createdb ateliersoude
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

Si vous préférez, vous pouvez également lancer le projet en développement en utilisant docker:

.. code-block:: bash

    sudo docker build -f deployment/django/Dockerfile -t ateliersoude .
    sudo docker run -it --rm -p 8000:8000 ateliersoude

Vous pouvez ensuite accéder au site à l'addresse http://127.0.0.1:8000/ l'utilisateur admin étant: admin@example.com passwd: adminpass

Des recettes docker-compose sont disponibles, avec une intégration de postgres comme service et nginx avec SSL

environnement de production :

.. code-block:: bash
  docker-compose -f deployment/docker-compose.yml -f deployment/docker-compose.prod.yml up --build

environnement de développement :

.. code-block:: bash

  docker-compose -f deployment/docker-compose.yml -f deployment/docker-compose.dev.yml up --build

Lancer la création de la base de données postgres (une fois le docker-compose en fonction):

.. code-block:: bash

  docker exec -ti deployment_postgres_1 createdb -U ateliersoude ateliersoude
