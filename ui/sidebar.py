import customtkinter as ctk

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220)

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="🤖 KAPTEN AI",
            font=("Segoe UI", 20, "bold")
        )

        title.pack(pady=20)

        ctk.CTkButton(
            self,
            text="💬 Chat Baru"
        ).pack(fill="x", padx=15, pady=8)

        ctk.CTkButton(
            self,
            text="📜 History"
        ).pack(fill="x", padx=15, pady=8)

        ctk.CTkButton(
            self,
            text="⚙️ Pengaturan"
        ).pack(fill="x", padx=15, pady=8)