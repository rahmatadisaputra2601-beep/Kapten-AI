import customtkinter as ctk

class ChatArea(ctk.CTkTextbox):

    def __init__(self, master):
        super().__init__(
            master,
            font=("Consolas", 15)
        )

        self.insert(
            "end",
            "🤖 Halo Kapten 👋\n\n"
        )

    def add_user(self, text):
        self.insert(
            "end",
            f"\n🧑 Kamu:\n{text}\n\n"
        )
        self.see("end")

    def add_ai(self, text):
        self.insert(
            "end",
            f"🤖 KAPTEN AI:\n{text}\n\n"
        )
        self.see("end")