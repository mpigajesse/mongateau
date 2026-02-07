#!/bin/bash

echo "========================================"
echo "   MonGâteau - Backend Django"
echo "========================================"
echo ""

# Activer l'environnement virtuel
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo "Environnement virtuel activé!"
else
    echo "ERREUR: Environnement virtuel non trouvé!"
    echo "Créez-le avec: python3 -m venv venv"
    exit 1
fi

echo ""
echo "Démarrage du serveur Django..."
echo "Le backend sera accessible sur http://localhost:8000"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""

python manage.py runserver
