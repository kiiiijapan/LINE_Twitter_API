# LINE_Twitter_API
Pythonを使用してTwitterで「いいね」した最新ツイートを日次でLineに送ります。

Tweepy、LINE Notify、GitHub Actionsを使用します。

コードでは以下のような流れで進んでいきます。
1. Twiiter APIを使用して、「いいね」した最新のツイートを取得
2. LINE Notify APIを使用して、①で取得したツイートをLINEに通知する
3. GitHub Actionsを使用して、日次で最新ツイートをLineに送る

