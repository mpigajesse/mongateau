@echo off
echo ========================================
echo    MonGateau - Backend Django
echo ========================================
echo.

REM Activer l'environnement virtuel
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Environnement virtuel active!
) else (
    echo ERREUR: Environnement virtuel non trouve!
    echo Creez-le avec: python -m venv venv
    pause
    exit
)

echo.
echo Demarrage du serveur Django...
echo Le backend sera accessible sur http://localhost:8000
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

python manage.py runserver

pause
