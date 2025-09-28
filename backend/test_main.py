import pytest
import os
import tempfile
from pathlib import Path
from fastapi.testclient import TestClient
from unittest.mock import patch

from main import app
from database import init_db, get_count, increment_count

client = TestClient(app)

@pytest.fixture
def temp_db():
    """テスト用の一時データベースファイルを作成"""
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        with patch("database.DB_PATH", db_path):
            init_db()
            yield db_path

def test_root_endpoint():
    """ルートエンドポイントのテスト"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "AI Battle Royale Backend API"
    assert data["status"] == "running"

def test_health_check():
    """ヘルスチェックエンドポイントのテスト"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_get_count_initial(temp_db):
    """初期カウント値の取得テスト"""
    with patch("database.DB_PATH", temp_db):
        response = client.get("/count")
        assert response.status_code == 200
        data = response.json()
        assert data["count"] == 0

def test_increment_count(temp_db):
    """カウント増加のテスト"""
    with patch("database.DB_PATH", temp_db):
        # 初期値確認
        response = client.get("/count")
        assert response.json()["count"] == 0

        # カウント増加
        response = client.post("/count")
        assert response.status_code == 200
        data = response.json()
        assert data["count"] == 1
        assert "カウントが増加しました" in data["message"]

        # 増加後の値確認
        response = client.get("/count")
        assert response.json()["count"] == 1

def test_multiple_increments(temp_db):
    """複数回のカウント増加テスト"""
    with patch("database.DB_PATH", temp_db):
        # 5回増加
        for i in range(1, 6):
            response = client.post("/count")
            assert response.status_code == 200
            assert response.json()["count"] == i

        # 最終値確認
        response = client.get("/count")
        assert response.json()["count"] == 5

def test_database_functions(temp_db):
    """データベース関数の直接テスト"""
    with patch("database.DB_PATH", temp_db):
        # 初期値
        assert get_count() == 0

        # 1回増加
        new_count = increment_count()
        assert new_count == 1
        assert get_count() == 1

        # さらに増加
        new_count = increment_count()
        assert new_count == 2
        assert get_count() == 2