# 📚 Interactive Term Glossary & Library Record System

A modern desktop record management application built with Python and CustomTkinter, designed to organize, search, and manage programming definitions alongside an encapsulated library book catalog.

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-1f6aa5)](https://github.com/TomSchimansky/CustomTkinter)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 💡 Overview

Managing reference documentation and physical asset logs typically requires structured data storage and intuitive operational interfaces:
- Combines dictionary-based key-value storage and object-oriented records into a unified dual-tab desktop interface[cite: 1].
- Implements strict data encapsulation with private class attributes and controlled getter/mutator methods[cite: 1].
- Provides full CRUD (Create, Read, Update, Delete) workflows for programming terminology and physical book records[cite: 1].
- Delivers real-time catalog filtering, status toggling, and input validation guards with native system dialog alerts[cite: 1].

---

## 🛠️ Built With

- **Python 3.12** – Core object-oriented architecture, dictionary manipulation, and data logic[cite: 1].
- **CustomTkinter** – Responsive dark-mode tabbed interface and styled widgets.
- **Tkinter (`messagebox`)** – System modal notifications for validations and operation alerts.

---

## ⚙️ Core Architecture & Concept Pipeline

| Component | Architecture Pattern | Key Logic Applied | Primary Objective |
| :--- | :--- | :--- | :--- |
| **Term Glossary** | Key-Value Hash Map (`dict`)[cite: 1] | Normalized title-casing, $O(1)$ search lookups, dictionary key-value iteration[cite: 1] | Instant definition lookup, addition, and alphabetical sorting[cite: 1] |
| **Book Record** | Encapsulated Class (`Book`)[cite: 1] | Private fields (`__book_id`, `__title`, `__author`, `__is_available`), instance methods[cite: 1] | Secure state isolation and controlled status toggling[cite: 1] |
| **Catalog Manager** | Object Registry (`LibraryManager`)[cite: 1] | Unique ID validation, dictionary object indexing, deletion safeguards[cite: 1] | Centralized inventory management and issue tracking[cite: 1] |
| **Presentation Layer** | Tabbed GUI (`CTkTabview`) | Monospace text formatting, real-time buffer updates, modal alerts | Visual record feed and intuitive data manipulation |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher installed
* `customtkinter` package

### Setup & Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/interactive-glossary-library.git](https://github.com/your-username/interactive-glossary-library.git)
   cd interactive-glossary-library
---

