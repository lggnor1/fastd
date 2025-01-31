import tkinter as tk
from tkinter import ttk
import subprocess
import webbrowser

# 실행할 프로그램 경로 설정 (여기서 직접 추가/수정 가능)
PROGRAMS = {
    "Valorant": [
        ("Valorant", r"C:\Riot Games\Riot Client\RiotClientServices.exe"),
        ("Medal", r"C:\Users\호두 귀여미\AppData\Local\Medal\app-4.2535.0\Medal.exe"),
    ],
    "SMS": [
        ("Discord", r'"C:\Users\호두 귀여미\AppData\Local\Discord\Update.exe" --processStart Discord.exe'),
        ("KakaoTalk", r"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"),
    ],
    "Coding": [
        ("VS Code", r"C:\Users\호두 귀여미\AppData\Local\Programs\Microsoft VS Code\Code.exe"),
        ("GitHub", "https://github.com/"),  # 웹페이지 실행
        ("파일 탐색기", "explorer"),
    ],
}

# 프로그램 실행 함수
def run_programs(program_list):
    for name, path in program_list:
        if path.startswith("http"):  # 웹사이트인 경우
            webbrowser.open(path)
        else:
            subprocess.Popen(path, shell=True)

# 테이블 항목을 더블클릭하면 실행
def on_double_click(event):
    selected_item = tree.selection()
    if selected_item:
        category = tree.item(selected_item, "text")
        if category in PROGRAMS:
            run_programs(PROGRAMS[category])

# 마우스를 올렸을 때 실행 목록 표시
def on_hover(event):
    selected_item = tree.identify_row(event.y)
    if selected_item:
        category = tree.item(selected_item, "text")
        if category in PROGRAMS:
            tooltip_text = "\n".join([f"{name} ({path})" for name, path in PROGRAMS[category]])
            tooltip_label.config(text=tooltip_text)
        else:
            tooltip_label.config(text="")

# Tkinter GUI 생성
root = tk.Tk()
root.title("Speedrun")
root.geometry("400x300")

# 테이블 위젯
tree = ttk.Treeview(root)
tree["columns"] = ("Name")
tree.column("#0", width=150)
tree.heading("#0", text="Category")

# 테이블 항목 추가
for category in PROGRAMS.keys():
    tree.insert("", "end", text=category)

tree.pack(expand=True, fill="both")

# 툴팁 (마우스를 올리면 실행 목록 표시)
tooltip_label = tk.Label(root, text="", relief="solid", borderwidth=1, justify="left", anchor="w")
tooltip_label.pack(fill="x", padx=5, pady=5)

# 이벤트 바인딩
tree.bind("<Double-1>", on_double_click)  # 더블클릭 시 실행
tree.bind("<Motion>", on_hover)  # 마우스 오버 시 실행 목록 표시

root.mainloop()

#pyinstaller --onefile --icon="C:\Users\호두 귀여미\Documents\vsc\fast\icon.ico" --noconsole --uac-admin fast.py