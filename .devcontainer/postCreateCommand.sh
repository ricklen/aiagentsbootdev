# uv install dependencies
uv sync
git config --global --add safe.directory /workspaces/*
git config core.autocrlf true
git config user.name $GIT_NAME
git config user.email $GIT_EMAIL
git config credential.useHttpPath true



#######
# Config ZSH
#######
# powerline fonts for zsh theme
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd .. && rm -rf fonts
sudo cp -av ~/.local/share/fonts/* /usr/share/fonts/

# oh-my-zsh plugins
zsh -c 'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k'
cp .devcontainer/dotfiles/.zshrc ~
cp .devcontainer/dotfiles/.p10k.zsh ~