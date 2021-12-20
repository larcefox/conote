# Conote is console noting utility

## Install
1. Clone repo from git
> git clone https://github.com/larcefox/conote.github

2. Require "at"
> sudo apt install at

3. Add to youre .bashrc or similar
> alias note="path_to_main.py"

## Usage
- Save note to ~/.connote/conote.md
> note youre text here

- Save note to ~/.conote/conote.md and reminde in 10 minutes
> note youre text here -r 10

- Save command output
> note \`command\`

or

> command | note

- Save last console command
> note "!!"

- Save note in ~/.conote/any_file.md
> note youre text here -t any_file

- Multiline input
> cat << EOF | note

- Save curret file list
> note *

- If you want to write special simbols in note use "\" before simbol.
> note tmux kill-server \> kills all tmux session -t tmux

## Using tags and templates
- You can modify default templates in conote/templates folder.
- Default tags can be finde in conote/config/config.ini file.
