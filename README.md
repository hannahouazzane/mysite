# My Readme

## Quickstart

1. install pipenv `pip3 install --user pipenv`
2. check where pip3 installs bin files and add it to $PATH
  1. find pipenv in bin folder
  2. edit PATH variable using bashrc/zshrc 
  3. add bin folder to start of PATH variable: e.g. `export PATH="${PATH}:/Users/<name>/Library/Python/3.9/bin"`
3. `pipenv install`
4. `pipenv run migrate`
5. `pipenv run dev`