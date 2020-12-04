import tkinter as tk


class Find(tk.Toplevel):
    """Find whole or partial words within a text widget"""

    def __init__(self, master, text_widget):
        super().__init__(master)
        self.text = text_widget
        self.title('Find')
        self.transient(master)
        self.resizable(False, False)
        self.wm_attributes('-topmost', 'true', '-toolwindow', 'true')
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.focus_set()

        # create widgets
        lbl = tk.Label(self, text='Find what:')
        self.text_find = tk.Entry(self, width=30, font='-size 10')
        self.btn_next = tk.Button(
            self, text='Find Next', width=10, command=self.ask_find_match)
        self.whole_word_var = tk.IntVar()
        self.whole_word_var.set(0)
        check_btn = tk.Checkbutton(
            self,
            text='Match whole word only',
            variable=self.whole_word_var, anchor=tk.W, command=self.change_match_type)

        # add widgets to window
        lbl.grid(row=0, column=0, padx=(15, 2), pady=15)
        self.text_find.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=15)
        self.btn_next.grid(row=0, column=2, sticky=tk.EW,
                           padx=(5, 15), pady=15)
        self.text_find.focus_set()
        check_btn.grid(row=1, column=0, padx=15, pady=(
            5, 15), columnspan=2, sticky=tk.EW)

        # other variables
        self.chars = 0
        self.term = None
        self.start = '1.0'

        # configure text widget tags
        self.text.tag_configure(
            'found', foreground='black', background='silver')
        self.text.tag_configure(
            'found.focus', foreground='white', background='SystemHighlight')

        # add additional bindings
        self.bind("<Return>", self.ask_find_match)

    def cancel(self):
        """Cancel the request and return control to main window"""
        end = self.start
        start = self.start + f'-{self.chars}c'
        self.text.tag_delete('found', 1.0, tk.END)
        self.text.tag_delete('found.focus', 1.0, tk.END)
        self.text.tag_add(tk.SEL, start, end)
        self.text.mark_set(tk.INSERT, start)
        self.text.focus_set()
        self.destroy()

    def change_match_type(self):
        """Reset found tags when match type is changed"""
        self.term = None
        self.chars = None
        self.text.tag_remove('found', '1.0', tk.END)
        self.text.tag_remove('found.focus', '1.0', tk.END)

    def ask_find_match(self, event=None):
        """Check for new searches, and route traffic by search types"""
        term = self.text_find.get()
        if term == '':
            return
        if self.term != term:
            self.term = term
            self.chars = len(term)
            self.text.tag_remove('found', '1.0', tk.END)
            self.route_match()
        self.highlight_next_match()

    def route_match(self):
        """Direct to whole or partial match"""
        if self.whole_word_var.get():
            self.whole_word_matches()
        else:
            self.partial_word_matches()

    def whole_word_matches(self):
        """Locate and tag all whole word matches"""
        start = '1.0'
        while True:
            start = self.text.search(self.term, start, stopindex=tk.END)
            if not start:
                break
            end = start + ' wordend'
            # whole word includes a space before
            found = self.text.get(start + '-1c', end)
            if found == ' ' + self.term:
                self.text.tag_add('found', start, end)
            start = end

    def partial_word_matches(self):
        """Locate and tag all partial word matches"""
        start = '1.0'
        while True:
            start = self.text.search(self.term, start, stopindex=tk.END)
            if not start:
                break
            end = start + f'+{self.chars}c'
            self.text.tag_add('found', start, end)
            start = end

    def highlight_next_match(self):
        """Highlight the next matching word"""
        self.text.tag_remove('found.focus', '1.0',
                             tk.END)  # remove existing tag
        try:
            start, end = self.text.tag_nextrange('found', self.start, tk.END)
            self.text.tag_add('found.focus', start, end)
            self.text.mark_set(tk.INSERT, start)
            self.text.see(start)
            self.start = end
        except ValueError:
            if self.start != '1.0':
                self.start = '1.0'
                self.text.see('1.0')
                self.highlight_next_match()
