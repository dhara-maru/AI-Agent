from functions.write_file import write_file

def test():
    print("--- Test 1: Existing File ---")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("\n--- Test 2: New Subdirectory ---")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("\n--- Test 3: Security Breach (Should Error) ---")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    test()