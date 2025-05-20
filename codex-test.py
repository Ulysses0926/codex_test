def hello():
    return "Hello from CodeX!"

def test_hello():
    assert hello() == "Hello from CodeX!"
    print("✅ All tests passed.")

if __name__ == "__main__":
    test_hello()
