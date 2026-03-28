# user.py
import key # key.so ကို import လုပ်တာပါ

if __name__ == "__main__":
    try:
        key.main_logic()
    except Exception as e:
        print(f"Error: {e}")
