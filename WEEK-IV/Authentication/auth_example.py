import hashlib

users = {}


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_user(username: str, password: str) -> str:
    if username in users:
        return "User already exists."
    users[username] = hash_password(password)
    return f"User {username} registered successfully."


def login_user(username: str, password: str) -> str:
    if username not in users:
        return "User not found."
    if users[username] == hash_password(password):
        return f"Welcome back, {username}!"
    return "Invalid password."


if __name__ == "__main__":
    print(register_user("alice", "secret123"))
    print(login_user("alice", "secret123"))
    print(login_user("alice", "wrongpassword"))
