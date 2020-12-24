# AutoFocusAssist

[Click here for English README](README.md)

DiscordでGoLiveを開始したときに、Windows10の「集中モード」をオンにします。

DiscordBotを利用してGoLiveの開始・終了を検出しているため、Botが参加していないGuildで行われるGoLiveは検出できません。

## Requirements

- Windows 10 (April 2018 Updateを適用済みであること)
- Python 3.6 以上

### Using Library / Project

- [ionescu007/wnfun](https://github.com/ionescu007/wnfun)
- [discord.py](https://github.com/Rapptz/discord.py)

## Installation

1. プロジェクトをクローンします: `git clone --recursive https://github.com/book000/AutoFocusAssist`
2. `config.json`を`config.sample.json`からコピーし、トークンとユーザーIDを書き込みます。
3. スタートアップ(`shell:startup`)に`startBackground.vbs`のショートカットを配置し、起動時に動作するようにします。

## Reference list

- [Toggling Focus Assist mode in Win 10 Programmatically](https://stackoverflow.com/questions/55477041/toggling-focus-assist-mode-in-win-10-programmatically)

## Disclaimer

このプロジェクトを使用したことによって引き起こされた問題に関して開発者は一切の責任を負いません。

## License

このプロジェクトのライセンスは[MIT License](LICENSE)です。
