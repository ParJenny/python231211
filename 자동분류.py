import os
import shutil

def classify_files(source_folder, images_folder, data_folder, docs_folder):
    # 확인할 파일 확장자들
    image_extensions = ['.jpg', '.jpeg']
    data_extensions = ['.csv', '.xlsx']
    pdf_extensions = ['.pdf']

    # 폴더가 없으면 생성
    for folder in [images_folder, data_folder, docs_folder]:
        folder_path = os.path.join(source_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # 폴더 내 파일 분류
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_name)

            if file_extension.lower() in image_extensions:
                destination_folder = os.path.join(source_folder, images_folder)
            elif file_extension.lower() in data_extensions:
                destination_folder = os.path.join(source_folder, data_folder)
            elif file_extension.lower() in pdf_extensions:
                destination_folder = os.path.join(source_folder, docs_folder)
            else:
                # 다른 확장자를 가진 파일은 무시
                continue

            destination_path = os.path.join(destination_folder, file_name)

            # 파일을 목적지로 이동
            shutil.move(file_path, destination_path)
            print(f"Moved {file_name} to {destination_folder}")

if __name__ == "__main__":
    source_folder = 'C:/Users/Student/Downloads'
    images_folder = 'images'
    data_folder = 'data'
    docs_folder = 'docs'

    classify_files(source_folder, images_folder, data_folder, docs_folder)
