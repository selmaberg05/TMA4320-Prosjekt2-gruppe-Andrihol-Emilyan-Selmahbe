# Git-intructions for babes

## Add files
```bash 
git add <file_name> #forbokstav+inrykksknapp
```
```bash
#to add all files
git add .
```

## Commit staged files
```bash
git commit -m '<describing text>'
```

## Push commit
```bash
git push
```

## Fetch latest update
```bash
git fetch
```

## Git pull
```bash
git pull
```

## Create branch
```bash
git checkout -b '<branch_name>'
```

## Switch to branch
```bash
git checkout <name_of_branch>
```


## Git merge
```bash
git merge <branch_name> #du må være i den du vil merge inn i. F.eks main. branch_name er den andre
```

# Before use 

## Create venv with name env
```bash
python3 -m venv env
```

## Activate venv type
```bash
source env/bin/activate 
```

## Install requirements from requirements.txt type:
```bash
pip install -r requirements.txt
```

# If change in requirements
```bash
pip freeze > requirements.txt #freezer nåværende requirements inn i egen fil
```


