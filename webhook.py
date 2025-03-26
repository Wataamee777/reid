import sys
import requests

def send_webhook(webhook_url, count):
    message = {
        "content": "@everyone 荒らしたね？殺します。"
    }
    success_count = 0  # 成功回数を記録する変数

    for i in range(count):
        response = requests.post(webhook_url, json=message)
        if response.status_code == 204:
            success_count += 1
            print(f"Message {i + 1} sent successfully!")
        else:
            print(f"Failed to send message {i + 1}. Status code: {response.status_code}, Response: {response.text}")
    
    # 最終結果を出力
    print(f"送信成功! ({success_count}回送信しました)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python webhook.py {webhook_url} <number_of_times>")
        sys.exit(1)

    webhook_url = sys.argv[1]
    try:
        count = int(sys.argv[2])
        if count <= 0:
            raise ValueError
    except ValueError:
        print("The number of times must be a positive integer.")
        sys.exit(1)

    send_webhook(webhook_url, count)
