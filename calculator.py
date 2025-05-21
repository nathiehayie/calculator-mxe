import tkinter as tk
import numpy as np
import re

class SciCalc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Scientific Calculator')
        self.geometry('480x700')
        self.resizable(False, False)
        self.configure(bg='#181c20')
        self.bastawidget()

    def bastawidget(self):
        title = tk.Label(self, text='Scientific Calculator', font=('Segoe UI', 22, 'bold'), bg='#181c20', fg='#fff')
        title.pack(pady=(18, 0))
        entry_frame = tk.Frame(self, bg='#181c20')
        entry_frame.pack(pady=(10, 18), padx=18, fill='x')
        self.entry = tk.Entry(entry_frame, font=('Segoe UI', 26), bg='#23272e', fg='#fff', bd=0, justify='right', insertbackground='#fff', relief='flat', highlightthickness=2, highlightcolor='#3a3f47', highlightbackground='#23272e')
        self.entry.pack(fill='x', ipady=18, padx=6, pady=4)
        self.entry.focus_set()
        btns = [
            ['(', ')', 'n√x','E', '%', '1/x', '!'],
            ['√', 'mod','log','|x|','∛', 'x²', 'C'],
            ['rad', 'deg','exp','7', '8', '9', '÷'],
            ['cos', 'tan', 'cot', '4', '5', '6', '×'],
            ['csc', 'sin⁻¹','cos⁻¹','1', '2', '3', '−'],
            ['cot⁻¹','sec⁻¹','csc⁻¹','0', '.', '±', '+'],
            ['e', 'π', 'tan⁻¹', 'sec', 'sin', 'ln','='],
        ]
        btn_frame = tk.Frame(self, bg='#181c20')
        btn_frame.pack(padx=12, fill='both', expand=True)
        color_num = '#23272e'
        color_op = '#2d8cff'
        color_func = '#23272e'
        color_eq = '#ff9500'
        color_hover = '#31363e'
        color_active = '#1a1d22'
        for r, row in enumerate(btns):
            for c, char in enumerate(row):
                if char == '':
                    continue
                if char in '0123456789.':
                    bg = color_num
                    fg = '#fff'
                elif char in ['+', '−', '×', '÷', '=', '^',]:
                    bg = color_op if char != '=' else color_eq
                    fg = '#fff'
                elif char in ['C', '⌫']:
                    bg = '#ff4d4d'
                    fg = '#fff'
                elif char in ['(', ')']:
                    bg = '#23272e'
                    fg = '#b0b6be'
                else:
                    bg = color_func
                    fg = '#b0b6be'
                btn = tk.Button(
                    btn_frame, text=char, font=('Segoe UI', 17, 'bold'),
                    bg=bg, fg=fg, bd=0, relief='flat',
                    activebackground=color_active, activeforeground='#ff9500',
                    cursor='hand2',
                    highlightthickness=0,
                    command=lambda ch=char: self._on_btn(ch)
                )
                btn.grid(row=r, column=c, sticky='nsew', padx=2, pady=2, ipadx=2, ipady=8)
                btn.bind('<Enter>', lambda e, b=btn: b.config(bg=color_hover))
                btn.bind('<Leave>', lambda e, b=btn, bg=bg: b.config(bg=bg))
        for i in range(7):
            btn_frame.grid_columnconfigure(i, weight=1, uniform='col')
        for i in range(len(btns)):
            btn_frame.grid_rowconfigure(i, weight=1, uniform='row')

    def _on_btn(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '⌫':
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])
        elif char == '=':
            self._calculate()
        elif char in ['π', 'e', 'E']:
            self.entry.insert(tk.END, char)
        elif char == 'x²':
            self.entry.insert(tk.END, '²')
        elif char == '√':
            self.entry.insert(tk.END, '√(')
        elif char == '∛':
            self.entry.insert(tk.END, '∛(')
        elif char == 'n√x':
            self.entry.insert(tk.END, 'n√(')
        elif char == '1/x':
            self.entry.insert(tk.END, '1/(')
        elif char == '|x|':
            self.entry.insert(tk.END, 'abs(')
        elif char == 'mod':
            self.entry.insert(tk.END, ' mod ')
        elif char == '!':
            self.entry.insert(tk.END, '!')
        elif char == '^':
            self.entry.insert(tk.END, '^')
        elif char == 'log':
            self.entry.insert(tk.END, 'log(')
        elif char == 'ln':
            self.entry.insert(tk.END, 'ln(')
        elif char == 'exp':
            self.entry.insert(tk.END, 'exp(')
        elif char in ['sin', 'cos', 'tan', 'cot', 'sec', 'csc']:
            self.entry.insert(tk.END, f'{char}(')
        elif char in ['sin⁻¹']:
            self.entry.insert(tk.END, 'sin⁻¹(')
        elif char in ['cos⁻¹']:
            self.entry.insert(tk.END, 'cos⁻¹(')
        elif char in ['tan⁻¹']:
            self.entry.insert(tk.END, 'tan⁻¹(')
        elif char in ['cot⁻¹']:
            self.entry.insert(tk.END, 'cot⁻¹(')
        elif char in ['sec⁻¹']:
            self.entry.insert(tk.END, 'sec⁻¹(')
        elif char in ['csc⁻¹']:
            self.entry.insert(tk.END, 'csc⁻¹(')
        elif char == 'deg':
            self.entry.insert(tk.END, 'deg(')
        elif char == 'rad':
            self.entry.insert(tk.END, 'rad(')
        elif char == '±':
            current = self.entry.get()
            if current:
                if current.startswith('-'):
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, current[1:])
                else:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, '-' + current)
        elif char == '×':
            self.entry.insert(tk.END, '×')
        elif char == '÷':
            self.entry.insert(tk.END, '÷')
        elif char == '−':
            self.entry.insert(tk.END, '−')
        else:
            self.entry.insert(tk.END, char)

    def _translate_expr(self, expr):
        expr = expr.replace('π', 'np.pi')
        expr = expr.replace('e', 'np.e')
        expr = expr.replace('×', '*')
        expr = expr.replace('÷', '/')
        expr = expr.replace('−', '-')
        expr = expr.replace('^', '**')
        expr = expr.replace('E', 'e')
        for n, sup in zip(range(2,10), ['²','³','⁴','⁵','⁶','⁷','⁸','⁹']):
            expr = re.sub(r'(\d+|\))'+sup, r'(\1**'+str(n)+')', expr)
        expr = re.sub(r'(\d+)√\(([^)]+)\)', r'(\2**(1/\1))', expr)
        expr = re.sub(r'√\(', 'np.sqrt(', expr)
        expr = re.sub(r'∛\(', 'np.cbrt(', expr)
        expr = re.sub(r'y√\(', '(', expr)
        expr = re.sub(r'abs\(', 'np.abs(', expr)
        expr = re.sub(r'\|([^|]+)\|', r'np.abs(\1)', expr)
        expr = re.sub(r'log\(', 'np.log10(', expr)
        expr = re.sub(r'ln\(', 'np.log(', expr)
        expr = re.sub(r'exp\(', 'np.exp(', expr)
        expr = re.sub(r'sin\(', 'np.sin(np.radians(', expr)
        expr = re.sub(r'cos\(', 'np.cos(np.radians(', expr)
        expr = re.sub(r'tan\(', 'np.tan(np.radians(', expr)
        expr = re.sub(r'cot\(', '1/np.tan(np.radians(', expr)
        expr = re.sub(r'sec\(', '1/np.cos(np.radians(', expr)
        expr = re.sub(r'csc\(', '1/np.sin(np.radians(', expr)
        expr = re.sub(r'sin⁻¹\(', 'np.degrees(np.arcsin(', expr)
        expr = re.sub(r'cos⁻¹\(', 'np.degrees(np.arccos(', expr)
        expr = re.sub(r'tan⁻¹\(', 'np.degrees(np.arctan(', expr)
        expr = re.sub(r'cot⁻¹\(', 'np.degrees(np.arccot(', expr)
        expr = re.sub(r'sec⁻¹\(', 'np.degrees(np.arccos(1/(', expr)
        expr = re.sub(r'csc⁻¹\(', 'np.degrees(np.arcsin(1/(', expr)
        expr = re.sub(r'deg\(([^)]+)\)', r'np.degrees(\1)', expr)
        expr = re.sub(r'rad\(([^)]+)\)', r'np.radians(\1)', expr)
        expr = re.sub(r'(\d+)%', r'(\1/100)', expr)
        expr = re.sub(r'(\d+)\s*mod\s*(\d+)', r'(\1%\2)', expr)
        expr = re.sub(r'(\d+)!', r'np.math.factorial(\1)', expr)
        expr = re.sub(r'1/\(([^)]+)\)', r'(1/(\1))', expr)
        return expr

    def _calculate(self):
        expr = self.entry.get()
        try:
            expr = self._translate_expr(expr)
            np.arccot = lambda x: np.arctan(1/x)
            result = eval(expr, {'np': np, '__builtins__': {}})
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, 'Syntax Error')

if __name__ == '__main__':
    SciCalc().mainloop() 