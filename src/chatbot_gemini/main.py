from chatbot import ChatBot


def main():
    print("Geminiチャットボットを起動します...")
    print("終了するには 'quit' または 'exit' と入力してください。")

    chatbot = ChatBot()

    while True:
        user_input = input("\nあなた: ")

        if user_input.lower() in ["quit", "exit"]:
            print("チャットボットを終了します。")
            break

        try:
            response = chatbot.send_message(user_input)
            print(f"\nAI: {response}")
        except Exception as e:
            print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
