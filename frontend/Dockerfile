# Node.js 20 Alpine イメージを使用
FROM node:20-alpine

# 作業ディレクトリを設定
WORKDIR /app

# パッケージマネージャーの最新化
RUN npm install -g npm@latest

# package.jsonとpackage-lock.jsonをコピー（依存関係の効率的なキャッシュのため）
COPY package*.json ./

# 依存関係をインストール
RUN npm install

# ポート5173を公開
EXPOSE 5173

# デフォルトの開発サーバー起動コマンド
CMD ["npm", "run", "dev"]