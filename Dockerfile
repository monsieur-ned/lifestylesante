FROM python:3.9

# Copier l'application dans le répertoire de travail
COPY . /app

WORKDIR /app

# Installer les dépendances système requises pour dlib
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


# Copier et rendre exécutable le script entrypoint.sh
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

# Démarrer l'application
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
