create a virtual environment

```bash
conda create -n winequa python=3.7 -y
```

activate the environment

```bash
conda activate winequa
```

install the requirements.txt

```bash
pip install -r requirements.txt
```

```bash
git init 
dvc init
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git config --global user.name "Your name"
git config --global user.email "Your email-id"
```

```bash
git commit -m "first commit"
```

another way of git add and commit

```bash
git add . && git commit -m "first commit"
```