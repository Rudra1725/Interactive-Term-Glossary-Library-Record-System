import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Book:
    def __init__(self, book_id, title, author, year):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__is_available = True

    def get_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__is_available

    def toggle_status(self):
        self.__is_available = not self.__is_available

    def get_details(self):
        status = "Available" if self.__is_available else "Issued"
        return f"[{self.__book_id}] '{self.__title}' by {self.__author} ({self.__year}) - Status: {status}"


class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, year):
        if book_id in self.books:
            return False
        self.books[book_id] = Book(book_id, title, author, year)
        return True

    def get_book(self, book_id):
        return self.books.get(book_id)

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

    def get_all_books(self):
        return [book.get_details() for book in self.books.values()]


class GlossaryManager:
    def __init__(self):
        self.terms = {
            "Polymorphism": "Ability of different classes to respond to the same method call in their own way.",
            "Encapsulation": "Bundling data and methods into a single unit while restricting direct outside access.",
            "Inheritance": "Mechanism where a new class derives properties and behaviors from an existing class.",
            "Recursion": "A programming technique where a function calls itself to solve smaller subproblems.",
        }

    def add_term(self, term, definition):
        normalized = term.strip().title()
        if normalized in self.terms:
            return False
        self.terms[normalized] = definition.strip()
        return True

    def search_term(self, term):
        normalized = term.strip().title()
        return self.terms.get(normalized)

    def delete_term(self, term):
        normalized = term.strip().title()
        if normalized in self.terms:
            del self.terms[normalized]
            return True
        return False

    def get_all(self):
        return sorted(self.terms.items(), key=lambda item: item[0])


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Interactive Term Glossary & Library System")
        self.geometry("900, 620")
        self.minsize(820, 560)

        self.glossary_mgr = GlossaryManager()
        self.library_mgr = LibraryManager()

        self.library_mgr.add_book("B101", "Clean Code", "Robert C. Martin", "2008")
        self.library_mgr.add_book("B102", "Design Patterns", "Erich Gamma", "1994")
        self.library_mgr.add_book("B103", "Fluent Python", "Luciano Ramalho", "2015")

        self.tabview = ctk.CTkTabview(self, corner_radius=12)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)

        self.tab_glossary = self.tabview.add("Term Glossary")
        self.tab_library = self.tabview.add("Library Records")

        self.build_glossary_tab()
        self.build_library_tab()

    def build_glossary_tab(self):
        container = ctk.CTkFrame(self.tab_glossary, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        left_panel = ctk.CTkFrame(container, width=320, corner_radius=10)
        left_panel.pack(side="left", fill="y", padx=(0, 10), pady=0)
        left_panel.pack_propagate(False)

        ctk.CTkLabel(left_panel, text="Glossary Controls", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(15, 12))

        self.glossary_term_entry = ctk.CTkEntry(left_panel, placeholder_text="Term (e.g. Encapsulation)")
        self.glossary_term_entry.pack(fill="x", padx=15, pady=6)

        self.glossary_def_entry = ctk.CTkTextbox(left_panel, height=110)
        self.glossary_def_entry.pack(fill="x", padx=15, pady=6)
        self.glossary_def_entry.insert("1.0", "Enter definition here...")
        self.glossary_def_entry.bind("<FocusIn>", self._clear_placeholder_def)

        btn_add = ctk.CTkButton(left_panel, text="Add Term", command=self.handle_add_glossary_term)
        btn_add.pack(fill="x", padx=15, pady=(10, 5))

        btn_search = ctk.CTkButton(left_panel, text="Search Term", fg_color="#3B82F6", hover_color="#2563EB", command=self.handle_search_glossary_term)
        btn_search.pack(fill="x", padx=15, pady=5)

        btn_delete = ctk.CTkButton(left_panel, text="Delete Term", fg_color="#EF4444", hover_color="#DC2626", command=self.handle_delete_glossary_term)
        btn_delete.pack(fill="x", padx=15, pady=5)

        btn_refresh = ctk.CTkButton(left_panel, text="Show All Terms", fg_color="transparent", border_width=1, command=self.refresh_glossary_display)
        btn_refresh.pack(fill="x", padx=15, pady=(15, 10))

        right_panel = ctk.CTkFrame(container, corner_radius=10)
        right_panel.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(right_panel, text="Glossary Database", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=15, pady=(15, 10))

        self.glossary_display = ctk.CTkTextbox(right_panel, font=ctk.CTkFont(family="Consolas", size=13))
        self.glossary_display.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.refresh_glossary_display()

    def _clear_placeholder_def(self, event):
        current_text = self.glossary_def_entry.get("1.0", "end-1c").strip()
        if current_text == "Enter definition here...":
            self.glossary_def_entry.delete("1.0", "end")

    def handle_add_glossary_term(self):
        term = self.glossary_term_entry.get().strip()
        defn = self.glossary_def_entry.get("1.0", "end-1c").strip()

        if not term or not defn or defn == "Enter definition here...":
            messagebox.showwarning("Input Error", "Please provide both a valid term and its definition.")
            return

        if self.glossary_mgr.add_term(term, defn):
            messagebox.showinfo("Success", f"Term '{term}' added successfully.")
            self.glossary_term_entry.delete(0, "end")
            self.glossary_def_entry.delete("1.0", "end")
            self.refresh_glossary_display()
        else:
            messagebox.showerror("Duplicate", f"The term '{term}' already exists.")

    def handle_search_glossary_term(self):
        term = self.glossary_term_entry.get().strip()
        if not term:
            messagebox.showwarning("Input Missing", "Enter a term to search.")
            return

        result = self.glossary_mgr.search_term(term)
        self.glossary_display.configure(state="normal")
        self.glossary_display.delete("1.0", "end")

        if result:
            self.glossary_display.insert("end", f"SEARCH RESULT:\n\nTerm: {term.title()}\n\nDefinition:\n{result}\n")
        else:
            self.glossary_display.insert("end", f"No entry found for '{term}'.\n")
        self.glossary_display.configure(state="disabled")

    def handle_delete_glossary_term(self):
        term = self.glossary_term_entry.get().strip()
        if not term:
            messagebox.showwarning("Input Missing", "Enter a term to delete.")
            return

        if self.glossary_mgr.delete_term(term):
            messagebox.showinfo("Deleted", f"'{term}' was removed from the glossary.")
            self.glossary_term_entry.delete(0, "end")
            self.refresh_glossary_display()
        else:
            messagebox.showerror("Not Found", f"Could not find term '{term}'.")

    def refresh_glossary_display(self):
        self.glossary_display.configure(state="normal")
        self.glossary_display.delete("1.0", "end")

        all_items = self.glossary_mgr.get_all()
        if not all_items:
            self.glossary_display.insert("end", "Glossary is currently empty.")
        else:
            for idx, (term, defn) in enumerate(all_items, 1):
                self.glossary_display.insert("end", f"{idx}. {term}\n   -> {defn}\n\n")

        self.glossary_display.configure(state="disabled")

    def build_library_tab(self):
        container = ctk.CTkFrame(self.tab_library, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        left_panel = ctk.CTkFrame(container, width=320, corner_radius=10)
        left_panel.pack(side="left", fill="y", padx=(0, 10), pady=0)
        left_panel.pack_propagate(False)

        ctk.CTkLabel(left_panel, text="Book Management", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(15, 12))

        self.book_id_entry = ctk.CTkEntry(left_panel, placeholder_text="Book ID (e.g. B104)")
        self.book_id_entry.pack(fill="x", padx=15, pady=4)

        self.book_title_entry = ctk.CTkEntry(left_panel, placeholder_text="Title")
        self.book_title_entry.pack(fill="x", padx=15, pady=4)

        self.book_author_entry = ctk.CTkEntry(left_panel, placeholder_text="Author")
        self.book_author_entry.pack(fill="x", padx=15, pady=4)

        self.book_year_entry = ctk.CTkEntry(left_panel, placeholder_text="Publication Year")
        self.book_year_entry.pack(fill="x", padx=15, pady=4)

        btn_add_book = ctk.CTkButton(left_panel, text="Add New Book", command=self.handle_add_book)
        btn_add_book.pack(fill="x", padx=15, pady=(10, 4))

        btn_search_book = ctk.CTkButton(left_panel, text="Find by ID", fg_color="#3B82F6", hover_color="#2563EB", command=self.handle_search_book)
        btn_search_book.pack(fill="x", padx=15, pady=4)

        btn_toggle_book = ctk.CTkButton(left_panel, text="Toggle Issue/Return", fg_color="#F59E0B", hover_color="#D97706", command=self.handle_toggle_book_status)
        btn_toggle_book.pack(fill="x", padx=15, pady=4)

        btn_delete_book = ctk.CTkButton(left_panel, text="Remove Book", fg_color="#EF4444", hover_color="#DC2626", command=self.handle_delete_book)
        btn_delete_book.pack(fill="x", padx=15, pady=4)

        btn_refresh_lib = ctk.CTkButton(left_panel, text="Show All Records", fg_color="transparent", border_width=1, command=self.refresh_library_display)
        btn_refresh_lib.pack(fill="x", padx=15, pady=(12, 10))

        right_panel = ctk.CTkFrame(container, corner_radius=10)
        right_panel.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(right_panel, text="Library Catalog", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=15, pady=(15, 10))

        self.library_display = ctk.CTkTextbox(right_panel, font=ctk.CTkFont(family="Consolas", size=13))
        self.library_display.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.refresh_library_display()

    def handle_add_book(self):
        b_id = self.book_id_entry.get().strip().upper()
        title = self.book_title_entry.get().strip()
        author = self.book_author_entry.get().strip()
        year = self.book_year_entry.get().strip()

        if not (b_id and title and author and year):
            messagebox.showwarning("Incomplete Fields", "Please fill in all book fields.")
            return

        if self.library_mgr.add_book(b_id, title, author, year):
            messagebox.showinfo("Success", f"Book '{title}' registered.")
            self.book_id_entry.delete(0, "end")
            self.book_title_entry.delete(0, "end")
            self.book_author_entry.delete(0, "end")
            self.book_year_entry.delete(0, "end")
            self.refresh_library_display()
        else:
            messagebox.showerror("Conflict", f"A book with ID '{b_id}' already exists.")

    def handle_search_book(self):
        b_id = self.book_id_entry.get().strip().upper()
        if not b_id:
            messagebox.showwarning("Missing ID", "Enter a Book ID in the field to search.")
            return

        book = self.library_mgr.get_book(b_id)
        self.library_display.configure(state="normal")
        self.library_display.delete("1.0", "end")

        if book:
            self.library_display.insert("end", f"BOOK FOUND:\n\n{book.get_details()}\n")
        else:
            self.library_display.insert("end", f"No book found with ID: {b_id}\n")

        self.library_display.configure(state="disabled")

    def handle_toggle_book_status(self):
        b_id = self.book_id_entry.get().strip().upper()
        if not b_id:
            messagebox.showwarning("Missing ID", "Enter the Book ID to change status.")
            return

        book = self.library_mgr.get_book(b_id)
        if book:
            book.toggle_status()
            new_status = "Available" if book.is_available() else "Issued"
            messagebox.showinfo("Status Updated", f"Book {b_id} is now marked as: {new_status}")
            self.refresh_library_display()
        else:
            messagebox.showerror("Error", f"No record found for ID '{b_id}'.")

    def handle_delete_book(self):
        b_id = self.book_id_entry.get().strip().upper()
        if not b_id:
            messagebox.showwarning("Missing ID", "Enter the Book ID to delete.")
            return

        if self.library_mgr.remove_book(b_id):
            messagebox.showinfo("Removed", f"Book {b_id} deleted from catalog.")
            self.book_id_entry.delete(0, "end")
            self.refresh_library_display()
        else:
            messagebox.showerror("Error", f"No record exists with ID '{b_id}'.")

    def refresh_library_display(self):
        self.library_display.configure(state="normal")
        self.library_display.delete("1.0", "end")

        records = self.library_mgr.get_all_books()
        if not records:
            self.library_display.insert("end", "Catalog has no registered records.")
        else:
            for idx, rec in enumerate(records, 1):
                self.library_display.insert("end", f"{idx}. {rec}\n\n")

        self.library_display.configure(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()