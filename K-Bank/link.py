import os
import glob

def process_link_file(filepath):
    """
    주어진 파일 경로의 텍스트 파일을 읽어 각 행 앞에 번호를 붙여 다시 저장합니다.

    Args:
        filepath (str): 처리할 텍스트 파일의 전체 경로.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        processed_lines = []
        for i, line in enumerate(lines):
            processed_lines.append(f"{i + 1}. {line.strip()}\n")

        with open(filepath, 'w', encoding='utf-8') as outfile:
            outfile.writelines(processed_lines)

        print(f"파일 '{filepath}'를 읽고 각 행에 번호를 추가하여 덮어썼습니다.")

    except FileNotFoundError:
        print(f"오류: 파일 '{filepath}'을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    current_folder_path = os.path.abspath('.')
    target_filename = None
    latest_modified_time = None

    # 현재 폴더의 'kbanknow_links_'로 시작하는 파일 찾기
    link_files = glob.glob(os.path.join(current_folder_path, "*.txt"))

    if link_files:
        # 가장 최근에 수정된 파일 찾기
        for file in link_files:
            modified_time = os.path.getmtime(file)
            if latest_modified_time is None or modified_time > latest_modified_time:
                latest_modified_time = modified_time
                target_filename = file

        if target_filename:
            print(f"가장 최근 링크 파일: {target_filename}")
            process_link_file(target_filename)
        else:
            print("처리할 링크 파일을 찾을 수 없습니다.")
    else:
        print("링크 파일('kbanknow_links_*.txt')을 찾을 수 없습니다.")