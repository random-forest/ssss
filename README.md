### Install Qt
```pip install --user PySide2```
### Install n
```curl -L https://git.io/n-install | bash && n lts```
### Install yarn
```curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -```
```echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list```
### Build
```yarn && yarn compile```
### Run
```yarn start``` or ```yarn dev```
