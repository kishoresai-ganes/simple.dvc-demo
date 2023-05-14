create a virtual environment

'''conda create -n winequa python=3.7 -y'''

activate the environment

'''conda activate winequa'''

install the requirements.txt

'''pip install -r requirements.txt'''

git init 

dvc init

dvc add data_given/winequality.csv

git add .

git config --global user.name "kishore sai"

git config --global user.email "kishoresai.ganes@tigeranalytics.com"

git commit -m "first commit"