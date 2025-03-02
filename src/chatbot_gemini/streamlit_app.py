import streamlit as st
from chatbot import ChatBot


def initialize_session_state():
    """セッション状態を初期化します"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBot()


def reset_conversation():
    """会話をリセットします"""
    st.session_state.messages = []
    st.session_state.chatbot = ChatBot()


def main():
    st.set_page_config(
        page_title="ばってん荒熊", page_icon="🐻", layout="centered"
    )

    # サイドバー
    with st.sidebar:
        st.markdown(
            """
        ### 使い方 📝
        1. メッセージを入力して会話を始めます
        2. 会話をリセットしたい時は下の「会話をリセット」ボタンを押してください
        3. 終了したいと時はブラウザの「×」で閉じてください
        """
        )
        st.markdown("---")

        if st.button("会話をリセット 🔄", use_container_width=True):
            reset_conversation()
            st.rerun()

    st.title("ばってん荒熊 🐻")
    st.write("ばってん荒熊は、あんたのパートナーばい  \nなんでっちゃ話しかけてはいよ！")
    st.caption("会話のリセットはサイドバーから")


    # セッション状態の初期化
    initialize_session_state()

    # カスタムCSS
    st.markdown(
        """
        <style>
        .user-avatar {
            background-color: #2E86C1;
            color: white;
            padding: 8px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .bot-avatar {
            background-color: #28B463;
            color: white;
            padding: 8px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
        }
        .user-message {
            background-color: #E3F2FD;
            color: #1A237E;
            font-weight: 500;
        }
        .bot-message {
            background-color: #F1F8E9;
            color: #1B5E20;
            font-weight: 500;
        }
        .message-content {
            flex-grow: 1;
            margin-top: 4px;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # チャット履歴の表示
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]

        if role == "user":
            with st.container():
                st.markdown(
                    f"""
                    <div class="chat-message user-message">
                        <span class="user-avatar">👤</span>
                        <div class="message-content">{content}</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
        else:
            with st.container():
                st.markdown(
                    f"""
                    <div class="chat-message bot-message">
                        <span class="bot-avatar">🐻</span>
                        <div class="message-content">{content}</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

    # 入力フォーム
    if prompt := st.chat_input("メッセージを入力してください"):
        # ユーザーメッセージを追加
        st.session_state.messages.append({"role": "user", "content": prompt})

        try:
            # ボットの応答を取得
            response = st.session_state.chatbot.send_message(prompt)
            # ボットの応答を追加
            st.session_state.messages.append({"role": "assistant", "content": response})

            # 画面を更新
            st.rerun()

        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")


if __name__ == "__main__":
    main()
