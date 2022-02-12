# SLAMBURK
...
# TL;DR

<a href="https://www.slamburk.cz">www.slamburk.cz</a>


## Prerequirements

Docker

COPY settings.env.dist file and rename it to settings.env

requirements.txt with the following content:
<code>
django==4.0
requests==2.27.1
psycopg2-binary==2.9.3
django-cors-headers==3.8.0
django-environ==0.8.1
</code>


## How to run
# with pipenv
<code>#stay in root</code>
<code>pipenv update</code>
<code>pipenv shell</code>
<code>cd slamburk</code>
<code>python3 manage.py runserver</code>


# with docker
<code>cd slamburk</code>
<code>docker build -t slam .</code>
<code>docker run -it --rm -p 8000:8000 slam</code>
