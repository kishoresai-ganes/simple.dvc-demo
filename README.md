create a virtual environment

'''bash
conda create -n winequa python=3.7 -y'''

activate the environment

'''bash
conda activate winequa'''

install the requirements.txt

'''bash
pip install -r requirements.txt'''

git init 

dvc init

dvc add data_given/winequality.csv

git add .

git config --global user.name "kishore sai"

git config --global user.email "kishoresai.ganes@tigeranalytics.com"

git commit -m "first commit"