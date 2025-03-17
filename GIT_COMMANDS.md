# 🚀 Git 常用指令 Cheat Sheet — LeetCode 練習專用

## 🟢 第一次設定 (只需設定一次)

```bash
git config --global user.name "你的GitHub帳號"
git config --global user.email "你的GitHub信箱"
```

## 🟠 把本地資料夾連接到 GitHub (第一次)

```bash
git init
git add .
git commit -m "Initial commit - Day01 added"
git remote add origin https://github.com/你的帳號/你的Repo.git
git branch -M main
git push -u origin main
```

## 🟡 每天更新 LeetCode 練習步驟

```bash
git add .
git commit -m "DayXX solved - 說明"
git push
```

## 🔄 其他常用指令

| 指令 | 功能 |
|-----|-----|
| git status | 查看目前有哪些檔案有改動 |
| git log | 查看歷史 commit 紀錄 |
| git diff | 查看改動內容 |
| git pull | 從 GitHub 把最新版本拉下來 |
| git clone [repo網址] | 複製別人的 repo 到本地 |
| git remote -v | 查看目前連結的 GitHub Repo |

## 📝 優化已存在內容怎麼做？

只要改完檔案，直接執行：

```bash
git add .
git commit -m "優化 Day01 內容"
git push
```

即可同步更新到 GitHub！
