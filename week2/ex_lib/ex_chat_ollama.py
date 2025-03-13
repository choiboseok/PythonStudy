from tkinter import *
from tkinter import scrolledtext
import ollama
models = ollama.list()
model_nm = "mistral"
ollama.pull(model_nm)

messages = []
def send_messages(event=None):
    message = entry.get()
    if message :
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"\nYOU:{message}\n")
        chat_window.config(state=DISABLED)
        entry.delete(0, END)
        chat_window.yview(END) # 자동 스크롤
        # ollama에게 요청
        user_input = message
        messages.append({"role": "user", "content": message})
        # 응답 내용을 출력
        res_stream = ollama.chat(model=model_nm, messages=messages, stream=True)
        ai_all_response = ""
        for part in res_stream:
            text = part["message"]["content"]
            print(text, end="", flush=True)
            ai_all_response += text
        print()
        messages.append({"role": "assistant", "content": ai_all_response})
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"ollama AI:{ai_all_response}")
        chat_window.config(state=DISABLED)
        entry.delete(0, END)
        chat_window.yview(END)  # 자동 스크롤

app = Tk()
app.title("Chat UI")
app.geometry("400x500")
# 채팅 창
chat_window = scrolledtext.ScrolledText(app, wrap=WORD, state=DISABLED, height=20, width=50)
chat_window.pack(pady=10, padx=10, expand=True, fill=BOTH)

# 입력프레임
input_frame = Frame(app)
input_frame.pack(pady=10, padx=10, fill=X)

# input
entry = Entry(input_frame)
entry.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)

# btn
btn = Button(input_frame, text="Send", command=send_messages)
btn.pack(side=RIGHT, padx=5, pady=5)
app.mainloop()