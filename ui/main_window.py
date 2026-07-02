import threading
import customtkinter as ctk

from ui.theme import WINDOW_WIDTH, WINDOW_HEIGHT
from ui.sidebar import Sidebar
from ui.chat import ChatArea
from core.ai import ask


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🤖 KAPTEN AI")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        # Area kanan
        right = ctk.CTkFrame(self)
        right.pack(side="right", fill="both", expand=True)

        # Chat
        self.chat = ChatArea(right)
        self.chat.pack(fill="both", expand=True, padx=10, pady=10)

        # Panel bawah
        bottom = ctk.CTkFrame(right)
        bottom.pack(fill="x", padx=10, pady=10)

        self.entry = ctk.CTkEntry(
            bottom,
            placeholder_text="Ketik pesan..."
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry.bind("<Return>", self.send)

        self.send_button = ctk.CTkButton(
            bottom,
            text="➤ Kirim",
            width=100,
            command=self.send
        )
        self.send_button.pack(side="right")

    def send(self, event=None):
        pesan = self.entry.get().strip()

        if not pesan:
            return

        self.chat.add_user(pesan)
        self.entry.delete(0, "end")

        threading.Thread(
            target=self.reply,
            args=(pesan,),
            daemon=True
        ).start()

    def reply(self, pesan):
        try:
            jawaban = ask(pesan)
        except Exception as e:
            jawaban = f"❌ Error:\n{e}"

        self.after(0, lambda: self.chat.add_ai(jawaban))