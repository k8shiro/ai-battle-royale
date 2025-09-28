import sqlite3
from pathlib import Path
from logger import get_logger

# ロガーを取得
logger = get_logger(__name__)

# データベースファイルのパス
DB_PATH = Path("db/data/app.db")

def init_db():
    """データベースとテーブルを初期化"""
    # ディレクトリが存在しない場合は作成
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # データベースファイルが存在しない場合のみテーブルを作成
    db_exists = DB_PATH.exists()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if not db_exists:
        # テーブル作成
        cursor.execute("""
            CREATE TABLE counter (
                id INTEGER PRIMARY KEY,
                count INTEGER NOT NULL DEFAULT 0
            )
        """)

        # 初期値を挿入
        cursor.execute("INSERT INTO counter (id, count) VALUES (1, 0)")
        conn.commit()
        logger.info("データベースとテーブルが初期化されました")
    else:
        logger.info("既存のデータベースを使用します")

    conn.close()

def get_count() -> int:
    """現在のカウント値を取得"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT count FROM counter WHERE id = 1")
    result = cursor.fetchone()

    conn.close()

    count = result[0] if result else 0
    logger.debug(f"現在のカウント値: {count}")
    return count

def increment_count() -> int:
    """カウント値を1増加させて新しい値を返す"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("UPDATE counter SET count = count + 1 WHERE id = 1")
    cursor.execute("SELECT count FROM counter WHERE id = 1")
    new_count = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    logger.info(f"カウントが増加しました: {new_count}")
    return new_count