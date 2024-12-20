# test_web_scraping_by_python
自己学習のために作成したPython、seleniumuによるWebスクレイピングアプリです（秘匿情報は配慮して公開しております）。

## URL

サンプルのスプレッドシート：https://docs.google.com/spreadsheets/d/1sIsZ_p2TX8NDjCeEsz0YY3Q0WeWnOeQgvKQKUZHIrng/edit?gid=1634617248#gid=1634617248


## 簡単な説明

このツールはPythonとSeleniumを用いて開発されたWebスクレイピングツールです。任意のサイトのHTML要素からスプレッドシートに効率よくデータを収集できます。

**_デモ_**

<img src="https://github.com/user-attachments/assets/3bfa96c2-8578-412b-9bb2-29c2ed499c92" width="800">

## 機能

自動的なデータ収集: あらかじめ設定したサイトから様々なデータがコマンド実行だけで収集できます。

Googleアカウント認証を使ったデータ収集: 既存のプロファイルを読み込むことによりOAuth認証済みでログイン済みしか得られないサイトのデータでも収集可能です。

## 使用技術

**バックエンド** 

- Python:3.11.1
- Selenium
- Poetry

**開発環境** 

- 開発PC: Windows 10 Home
- コードエディタ: VScode
- リンター＆フォーマッター: Ruff, Black

## その他

本アプリはあくまで自己学習のために作成したものです。もし業務利用で作成する場合、WEBサイトの利用規約を確認しましょう。

「ロボットによる...○○を禁止」や「スクレイピングを禁止」 のようなことが書いている場合があるので、その規約に準拠するようにしましょう。
