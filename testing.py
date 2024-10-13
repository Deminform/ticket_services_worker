from src.service.rmq.producer import send_notification


if __name__ == '__main__':
    send_notification(email="test@example.com", message="new notification")
