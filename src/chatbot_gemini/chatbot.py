import os
from typing import List
import google.generativeai as genai
from dotenv import load_dotenv


class ChatBot:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

        # 熊本弁キャラクターの設定
        kumamoto_prompt = """
あなたは熊本県出身の熊本人です。以下の特徴を持っています：
- こてこての熊本弁を使って会話します
- 熊本弁の特徴（～たい、～ばい、～なっせ、～ごたる、など）を積極的に使います
- 熊本の方言や文化に詳しく、時々熊本の話題を出します
- フレンドリーで親しみやすい性格です
- 語尾には「ばい」「たい」「なっせ」などをよく使います
- 「～です・ます」調は使わず、くだけた熊本弁で話します

例：
- 「こんにちは」→「やっほー！元気かい？」
- 「ありがとう」→「サンキュー！助かったばい！」
- 「さようなら」→「また来なっせ！待っとるけん！」

間違い例：
- ✕「行こなっせ」→ 〇「行こばいた」
- ✕「行こうなっせ」→ 〇「行きなっせ」

このキャラクター設定を守って会話してください。
"""
        self.chat = self.model.start_chat(
            history=[
                {"role": "user", "parts": [kumamoto_prompt]},
            ]
        )

    def send_message(self, message: str) -> str:
        """
        メッセージを送信し、応答を取得します。

        Args:
            message (str): ユーザーからのメッセージ

        Returns:
            str: AIからの応答
        """
        response = self.chat.send_message(message)
        return response.text

    def get_chat_history(self) -> List[dict]:
        """
        チャット履歴を取得します。

        Returns:
            List[dict]: チャット履歴
        """
        return self.chat.history
