#!/usr/bin/env python3
"""seed_nav — file-tree sidebar for the vault repo.

A tall, narrow window holding nothing but the file tree, Obsidian-sidebar
style. Folders lazy-expand as drop-downs; double-clicking a file opens it
in the system's default application.

Launch:  python3 seed_nav.py [folder]
         no argument = the MESH_SEED_V2/ vault beside this app; repo root if absent
Refresh: F5 or Cmd-R rescans the tree.

Python 3 standard library only. No third-party dependencies.
"""

import os
import subprocess
import sys
import tkinter as tk
from tkinter import ttk

def system_open(path):
    """Open a file with the platform's native default application."""
    if sys.platform == "darwin":
        # a stock Mac has no app claiming .md — fall back to the default text editor
        if subprocess.call(["open", path]) != 0:
            subprocess.call(["open", "-t", path])
    elif os.name == "nt":
        os.startfile(path)  # noqa: B606 — windows native open
    else:
        subprocess.Popen(["xdg-open", path])


def list_entries(folder):
    """Folder contents: folders first, alphabetical, hidden files skipped."""
    try:
        names = [n for n in os.listdir(folder) if not n.startswith(".")]
    except OSError:
        return []
    names.sort(key=lambda n: (not os.path.isdir(os.path.join(folder, n)), n.lower()))
    return names


class SeedNav:
    def __init__(self, root_path):
        self.root_path = os.path.abspath(root_path)
        self.win = tk.Tk()
        self.win.title(os.path.basename(self.root_path) or self.root_path)
        self.win.geometry("320x900")
        self.win.minsize(220, 300)

        style = ttk.Style(self.win)
        style.configure("Treeview", rowheight=22)

        container = ttk.Frame(self.win)
        container.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(container, show="tree", selectmode="browse")
        ysb = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=ysb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        ysb.pack(side="right", fill="y")

        self.tree.bind("<Double-1>", self.on_double_click)
        self.win.bind("<F5>", self.refresh)
        self.win.bind("<Command-r>", self.refresh)

        self.build_root()

    # -- tree construction ---------------------------------------------------

    def build_root(self):
        # eager-load the entire tree once — clicks then do zero filesystem
        # work, expansion is pure UI
        for item in self.tree.get_children(""):
            self.tree.delete(item)
        self.build_branch("", self.root_path)

    def build_branch(self, parent, folder):
        for name in list_entries(folder):
            path = os.path.join(folder, name)
            node = self.tree.insert(parent, "end", text=" " + name, values=[path])
            if os.path.isdir(path):
                self.build_branch(node, path)

    # -- actions -------------------------------------------------------------

    def on_double_click(self, event):
        node = self.tree.identify_row(event.y)
        if not node:
            return
        values = self.tree.item(node, "values")
        if not values:
            return
        path = values[0]
        if os.path.isfile(path):
            system_open(path)
        # folders fall through to Treeview's native open/close toggle

    def refresh(self, _event=None):
        self.build_root()

    def run(self):
        self.win.mainloop()


def main():
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        # APPS/seed_nav/seed_nav.py -> repo root is two levels up;
        # prefer the seed vault so repo scaffolding stays out of the tree
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        seed = os.path.join(root, "MESH_SEED_V2")
        if os.path.isdir(seed):
            root = seed
    if not os.path.isdir(root):
        sys.exit(f"seed_nav: not a folder: {root}")
    SeedNav(root).run()


if __name__ == "__main__":
    main()
