This is student result prediction application

Create virtual envirment : python -m venv myenv

ACTIVATE VENV: source myenv/Scripts/activate

CONDA env: source C:/Users/Malith/anaconda3/Scripts/activate condamyenv

Create Requirment File: pip freeze > requirements.txt

requirement.text install: pip install -r requirements.txt

RUN SERVER: uvicorn index:app --reload

Test Api: http://localhost:8000/docs

kadawatha location : 8.311352,80.403651
Anuradhapura: 8.311352,80.403651
app psw: axsrbizmfuepylid

Mongodb Detaisl

password: oWfBHWmnl77NQYao

username: admin

How to deploy App in Gcloud
git clone
cd project-name
virtualenv env
source env/bin/activate
pip install -r requirements.txt
run app - gunicorn -w 4 -k uvicorn.workers.UvicornWorker index:app
