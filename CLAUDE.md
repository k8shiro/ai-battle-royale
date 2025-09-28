# AI Battle Royale - Claude Code設定

## プロジェクト概要

AI Battle Royaleは、AI同士が戦うバトルロワイヤルゲームのプラットフォームです。

### 技術スタック
- フロントエンド: React + TypeScript + Vite + Tailwind CSS
- バックエンド: FastAPI + Python 3.11 + SQLite
- 開発環境: Docker + Docker Compose

## 開発ルール

### 言語設定
- ドキュメンテーション（コメント・docstring）は日本語で記述
- コード内のログメッセージは日本語
- 変数名・関数名は英語

### Git ワークフロー
- ブランチ名: `{issue番号}-{機能名}` (例: `6-claude-docs`)
- コミットメッセージにissue番号を含める
- プルリクエストでissueをクローズ

### ディレクトリ構成
```
ai-battle-royale/
├── frontend/           # React + TypeScript + Tailwind
├── backend/            # FastAPI + SQLite
├── db/data/           # SQLiteデータベースファイル
├── .claude/           # Claude Code専用ドキュメント
├── docker-compose.yml # 開発環境定義
└── README.md          # プロジェクト説明
```

## Claude Code専用ドキュメント

詳細な仕様書は以下を参照：

- API仕様: [.claude/api/specifications.md](.claude/api/specifications.md)
- プロジェクト詳細: [.claude/project/overview.md](.claude/project/overview.md)

## 開発コマンド

詳細な開発コマンドは [README.md](README.md) を参照してください。