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

## Backend

バックエンドAPI開発環境の設定と使用方法。

### 技術スタック

- **フレームワーク**: FastAPI (Python 3.11)
- **データベース**: SQLite
- **サーバー**: Uvicorn
- **テスト**: pytest
- **コンテナ**: Docker + Docker Compose

### API仕様

#### エンドポイント一覧

- `GET /` - ルートエンドポイント（ヘルスチェック）
- `GET /health` - ヘルスチェック
- `GET /count` - 現在のカウント値を取得
- `POST /count` - カウント値を1増加

#### サンプルレスポンス

```json
// GET /count
{
  "count": 5
}

// POST /count
{
  "count": 6,
  "message": "カウントが増加しました"
}
```

### セットアップ

#### 初回セットアップ

```bash
# バックエンドサービスをビルド
docker compose build backend

# データベース初期化（自動実行）
docker compose up backend
```

#### 開発サーバーの起動

```bash
# バックエンドサーバー起動
docker compose up backend
```

起動後、以下のURLでアクセス可能：
- **API**: http://localhost:8000
- **API ドキュメント**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc

#### テストの実行

```bash
# 単体テスト実行
docker compose run --rm backend pytest

# テスト詳細表示
docker compose run --rm backend pytest -v

# カバレッジ付きテスト
docker compose run --rm backend pytest --cov=.
```

### 開発環境の特徴

- **ホットリロード**: コード変更時に自動でサーバーが再起動
- **自動API ドキュメント**: FastAPIによる自動生成
- **データ永続化**: SQLiteファイルがホストに保存
- **統合ログ**: 構造化されたログ出力
- **単体テスト**: pytest による包括的なテスト