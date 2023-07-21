# Utilisez une image Nginx en tant que base pour le container
FROM nginx:alpine

# Copiez le contenu de votre répertoire de travail actuel (frontend_container)
# dans le répertoire racine de l'image Nginx
COPY . /usr/share/nginx/html

# Définissez l'image comme étant l'application par défaut pour Nginx
WORKDIR /usr/share/nginx/html

# Exposez le port 80 pour permettre aux requêtes d'atteindre l'application
EXPOSE 80

# Démarrez Nginx pour déployer votre application
CMD ["nginx", "-g", "daemon off;"]
