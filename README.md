### Install node version manager
```curl -L https://git.io/n-install | bash && n lts```
### Install yarn
```curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -```
```echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list```
### Build
```yarn && yarn prestart```
### Run
```yarn start:server | (sleep 5; yarn start:client)```
