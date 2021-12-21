# Conote is console noting utility

## Install
1. Clone repo from git
> git clone https://github.com/larcefox/conote.github

2. Require "at"
> sudo apt install at

3. Add to youre .bashrc or similar
> alias note="path_to_main.py"

4. Install librarys
>   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

5. For using google calendar required registred app in 
Google cloud console with Oauth authentication and
permission to create secondary calendars.
You mast activate calendar api.
Download Oauth credentials to conote/credentials folder.


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

- Save note to google calendar
> note your text here -c

- If you want to write special simbols in note use "\" before simbol.
> note tmux kill-server \> kills all tmux session -t tmux


## Using tags and templates
- You can modify default templates in conote/templates folder.
- Default tags can be fonde in conote/config/config.ini file.
