# AI Battle Royale - プロジェクト概要

## プロジェクトの目的

AI Battle Royaleは、AI同士が戦うバトルロワイヤルゲームのプラットフォームです。参加者は独自のAIアルゴリズムを開発し、他のAIと競い合う環境を提供します。

## システムアーキテクチャ

### 全体構成
```
┌─────────────────┐    ┌─────────────────┐
│   Frontend      │◄──►│    Backend      │
│  React + TS     │    │   FastAPI       │
│  Tailwind CSS   │    │   Python 3.11   │
└─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │    Database     │
                       │     SQLite      │
                       └─────────────────┘
```

### 技術スタック詳細

#### フロントエンド
- React 18: UIライブラリ
- TypeScript: 型安全性の確保
- Vite: 高速ビルドツール
- Tailwind CSS: ユーティリティファーストCSS
- ESLint + Prettier: コード品質管理

#### バックエンド
- FastAPI: 現代的なPython Webフレームワーク
- Python 3.11: 最新の言語機能とパフォーマンス
- SQLite: 軽量データベース（開発・テスト用）
- Uvicorn: ASGIサーバー
- pytest: テストフレームワーク

#### インフラ
- Docker: コンテナ化
- Docker Compose: 開発環境オーケストレーション

## 現在の実装状況

### 完了している機能
- [x] フロントエンド開発環境（React + TypeScript + Tailwind）
- [x] バックエンド開発環境（FastAPI + SQLite）
- [x] Docker Compose による統合開発環境
- [x] カウンターAPI（基本的なCRUD操作の例）
- [x] 自動API ドキュメント生成
- [x] 単体テスト環境（pytest）
- [x] 構造化ログ出力

## 開発方針

### コード品質
- 型安全性の重視（TypeScript、Python型ヒント）
- 包括的なテストカバレッジ
- ESLint/Prettierによるコード統一
- 日本語でのドキュメンテーション

### 開発効率
- ホットリロード対応
- 自動API ドキュメント生成
- Docker Compose による簡単セットアップ
- 構造化ログによるデバッグ支援

### 拡張性
- マイクロサービス対応アーキテクチャ
- REST API設計
- 疎結合なコンポーネント設計
- スケーラブルなデータベース設計（将来）