# Install Qt
pip install --user PySide2

# Install node version manager
curl -L https://git.io/n-install | bash

n lts

# Install yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt-get update && sudo apt-get install yarn

# Build
yarn && yarn prestart

# Run
yarn start:server | (sleep 3; yarn start:client)
