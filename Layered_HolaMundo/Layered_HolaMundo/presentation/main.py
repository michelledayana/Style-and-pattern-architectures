from application.hello_service import get_hello_message

def main():
    message = get_hello_message()
    print(message)

if __name__ == "__main__":
    main()
