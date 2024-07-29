.venv\Script\activate
pip install --upgrade pip
pip install -r requirements.txt
refelx init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate