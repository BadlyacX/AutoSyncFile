import os
import shutil
import time

source_dir = r"D:\stable-diffusion\stable-diffusion-webui\outputs"
dest_dir = r"E:\stable-diffusion\stable-diffusion-webui\outputs"

def sync_directories(source, destination):
    for root, dirs, files in os.walk(source):
        relative_path = os.path.relpath(root, source)
        dest_path = os.path.join(destination, relative_path)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)


        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)

            if not os.path.exists(dest_file) or os.path.getmtime(source_file) > os.path.getmtime(dest_file):
                shutil.copy2(source_file, dest_file)

        for file in os.listdir(dest_path):
            dest_file = os.path.join(dest_path, file)
            source_file = os.path.join(root, file)
            if not os.path.exists(source_file):
                os.remove(dest_file)

    for root, dirs, files in os.walk(destination):
        relative_path = os.path.relpath(root, destination)
        source_path = os.path.join(source, relative_path)
        for directory in dirs:
            dest_subdir = os.path.join(root, directory)
            source_subdir = os.path.join(source_path, directory)
            if not os.path.exists(source_subdir):
                shutil.rmtree(dest_subdir)

def main():
    print("開始同步...")
    while True:
        try:
            sync_directories(source_dir, dest_dir)
            print("同步完成。")
        except Exception as e:
            print(f"同步時出現錯誤: {e}")

        time.sleep(10)

if __name__ == "__main__":
    main()
