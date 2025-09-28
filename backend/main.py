from fastapi import FastAPI
from database import init_db, get_count, increment_count
from logger import setup_logger, get_logger

# ログ設定を初期化
setup_logger()
logger = get_logger(__name__)

app = FastAPI(
    title="AI Battle Royale Backend",
    description="バックエンドAPIサービス",
    version="1.0.0"
)

# アプリケーション起動時にデータベースを初期化
@app.on_event("startup")
async def startup_event():
    logger.info("アプリケーションを起動中...")
    init_db()
    logger.info("アプリケーションの起動が完了しました")

@app.get("/")
async def root():
    """ルートエンドポイント - ヘルスチェック用"""
    return {"message": "AI Battle Royale Backend API", "status": "running"}

@app.get("/count")
async def get_current_count():
    """現在のカウント値を取得"""
    logger.info("カウント値の取得リクエスト")
    count = get_count()
    return {"count": count}

@app.post("/count")
async def increment_current_count():
    """カウント値を1増加させる"""
    logger.info("カウント値の増加リクエスト")
    new_count = increment_count()
    return {"count": new_count, "message": "カウントが増加しました"}

@app.get("/health")
async def health_check():
    """ヘルスチェック用エンドポイント"""
    return {"status": "healthy"}