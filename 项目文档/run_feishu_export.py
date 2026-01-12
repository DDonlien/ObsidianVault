import platform
import subprocess
import os
import sys

## 自建应用信息
## 1. AppID: cli_a8d89e76c8bc1013
## 2. AppSecret: zW4piXiliJhQgMTSz9n3Ofd32g81VKuG
## 知识库ID
## 1. 跃入迷城: 7355379709528293404
## 2. 迷宫球: 7436770975573639170

def main():
    # Detect the current operating system
    system = platform.system()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Determine the executable name based on the OS
    if system == "Windows":
        executable = "feishu-doc-export.exe"
    elif system == "Darwin":  # macOS
        executable = "feishu-doc-export"
    else:
        # Default for Linux or other Unix-like systems
        executable = "feishu-doc-export"

    executable_path = os.path.join(current_dir, executable)

    # Check if the executable exists
    if not os.path.exists(executable_path):
        print(f"Error: Executable not found at {executable_path}")
        sys.exit(1)

    # Ensure the file has execute permissions on Unix-like systems
    if system != "Windows":
        try:
            st = os.stat(executable_path)
            # Add execute permission for user, group, and others
            os.chmod(executable_path, st.st_mode | 0o111)
        except Exception as e:
            print(f"Warning: Could not make file executable: {e}")

    print(f"Detected system: {system}")
    print(f"Launching: {executable_path}")
    
    try:
        # Run the executable, passing any arguments provided to this script
        subprocess.run([executable_path] + sys.argv[1:], check=True)
    except subprocess.CalledProcessError as e:
        # The called process returned a non-zero exit code
        sys.exit(e.returncode)
    except Exception as e:
        print(f"An error occurred while trying to run the executable: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
