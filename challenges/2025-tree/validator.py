import sys

def validate_tree(output_text):
    """
    簡單檢查 Output 是否像一棵樹
    1. 不可以是空的
    2. 必須包含常見的樹葉符號 (*, ^, #, @)。更新：考量到每個人對聖誕樹的創意不同，取消這個判段
    3. 形狀應該要是三角形? (太難判定，先略過)
    """
    if not output_text or not output_text.strip():
        return False, "Output is empty!"

if __name__ == "__main__":
    # 從 stdin 讀取 output
    content = sys.stdin.read()
    valid, message = validate_tree(content)
    
    if valid:
        print(f"PASS: {message}")
        sys.exit(0)
    else:
        print(f"FAIL: {message}")
        sys.exit(1)

