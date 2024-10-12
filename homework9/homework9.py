import re

def processEmail(email):
    pattern = r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'

    if not re.match(pattern, email):
        print("Некорректный формат email. Должно начинаться с буквы, содержать в себе знак - @")
        return None

    username, domain = email.split('@')
    return username, domain


def main():
    email = input("Введите ваш email: ")

    result = processEmail(email)
    if result:
        username, domain = result
        print(f"Username: {username}")
        print(f"Domain: {domain}")

if __name__ == "__main__":
    main()