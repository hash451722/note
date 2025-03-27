# FFmpeg note

作成日： March 27th, 2025  
更新日： -

---
## 目次
[Windowsへのインストール](#Windowsへのインストール)  
[FFmpegのPreset設定](#FFmpegのPreset設定)  
[リンク](#リンク)  

---
## Windowsへのインストール

wingetを使ったインストール方法は、ターミナルで次のPowerShellを実行。
```PowerShell
winget install ffmpeg
```

インストールの確認
```PowerShell
ffmpeg -version
```

インストールされたFFmpegのバージョン情報が表示されれば、インストールは成功。

アップデート
```PowerShell
winget upgrade ffmpeg
```

アンインストール
```PowerShell
winget uninstall ffmpeg
```


## FFmpegのPreset設定

### Presetとは

プリセットは、エンコード速度と圧縮率を提供するオプションのコレクション。
速度の速い順で利用可能なプリセットは次のとおり。

```
- ultrafast
- superfast
- veryfast
- faster
- fast
- medium（default preset）
- slow
- slower
- veryslow
- placebo（ignore this as it is not useful ）
```



## リンク

[FFmpeg official](https://www.ffmpeg.org/)