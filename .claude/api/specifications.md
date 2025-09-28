# API仕様書

## 概要

AI Battle Royale BackendのREST API仕様書です。

### ベースURL
- 開発環境: `http://localhost:8000`

### 認証
- 現在は認証なし
- 将来的にAPIキー認証を実装予定

## エンドポイント一覧

### 1. ルートエンドポイント

#### `GET /`
アプリケーションの基本情報を返すルートエンドポイント。

レスポンス:
```json
{
  "message": "AI Battle Royale Backend API",
  "status": "running"
}
```

ステータスコード:
- `200 OK`: 正常応答

---

### 2. ヘルスチェック

#### `GET /health`
アプリケーションの健康状態を確認するエンドポイント。

レスポンス:
```json
{
  "status": "healthy"
}
```

ステータスコード:
- `200 OK`: アプリケーションが正常に動作中

---

### 3. カウンター機能

#### `GET /count`
現在のカウント値を取得します。

レスポンス:
```json
{
  "count": 5
}
```

ステータスコード:
- `200 OK`: 正常応答

#### `POST /count`
カウント値を1増加させます。

レスポンス:
```json
{
  "count": 6,
  "message": "カウントが増加しました"
}
```

ステータスコード:
- `200 OK`: 正常応答

## データベース仕様

### カウンターテーブル (counter)
```sql
CREATE TABLE counter (
    id INTEGER PRIMARY KEY,
    count INTEGER NOT NULL DEFAULT 0
);
```

フィールド:
- `id`: プライマリキー（固定値: 1）
- `count`: カウント値

## エラーハンドリング

### エラーレスポンス形式
```json
{
  "detail": "エラーメッセージ"
}
```

### 一般的なエラーコード
- `404 Not Found`: 存在しないエンドポイント
- `500 Internal Server Error`: サーバー内部エラー

## ログ仕様

### ログレベル
- `INFO`: 一般的な処理情報
- `DEBUG`: デバッグ情報
- `ERROR`: エラー情報

### ログ形式
```
%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

## 自動生成ドキュメント

FastAPIによる自動生成ドキュメントが利用可能：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc