# AutoFocusAssist

[日本語のREADMEはこちらから](README-ja.md)

Turn on Windows 10 "Focus Assist" when you start GoLive on Discord.

Since we are using DiscordBot to detect the start and end of GoLive, we cannot detect GoLive that takes place in a Guild that the Bot is not a part of.

## Requirements

- Windows 10 (Applied the April 2018 Update)
- Python 3.6 and above

### Using Library / Project

- [ionescu007/wnfun](https://github.com/ionescu007/wnfun)
- [discord.py](https://github.com/Rapptz/discord.py)

## Installation

1. Clone the project: `git clone --recursive https://github.com/book000/AutoFocusAssist`
2. Copy `config.json` from `config.sample.json` and write the token and user ID.
3. Place a shortcut for `startBackground.vbs` in startup (`shell:startup`) so that it works at startup.

## Reference list

- [Toggling Focus Assist mode in Win 10 Programmatically](https://stackoverflow.com/questions/55477041/toggling-focus-assist-mode-in-win-10-programmatically)

## Disclaimer

The author is not responsible for any problems caused by the user using this project.

## License

The license for this project is [MIT License](LICENSE).
