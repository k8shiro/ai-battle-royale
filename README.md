# AI Battle Royale

AI Battle Royaleプロジェクトです。

## Frontend

フロントエンド開発環境の設定と使用方法。

### 技術スタック

- **フレームワーク**: React (TypeScript)
- **ビルドツール**: Vite
- **スタイリング**: Tailwind CSS
- **リンター**: ESLint + Prettier
- **コンテナ**: Docker + Docker Compose

### セットアップ

#### 前提条件

- Docker
- Docker Compose

#### 初回セットアップ

1. リポジトリをクローン
```bash
git clone <repository-url>
cd ai-battle-royale
```

2. 初回起動（依存関係のインストール）
```bash
# Dockerコンテナ内で依存関係をインストール
docker-compose run --rm frontend npm install
```

#### 開発サーバーの起動

```bash
# 開発サーバーを起動
docker-compose up frontend
```

起動後、ブラウザで [http://localhost:5173](http://localhost:5173) にアクセスしてください。

#### リンターの実行

```bash
# ESLintでコードをチェック
docker-compose run --rm frontend npm run lint

# ESLintで自動修正
docker-compose run --rm frontend npm run lint:fix

# Prettierでフォーマット
docker-compose run --rm frontend npm run format
```

### 開発環境の特徴

- **ホットリロード**: ファイル変更時に自動で画面が更新されます
- **TypeScript**: 型安全性を確保
- **Tailwind CSS**: ユーティリティファーストなCSSフレームワーク
- **ESLint + Prettier**: コード品質と統一されたフォーマットを維持