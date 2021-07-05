from tkinter import (
    Canvas,
    Frame,
    IntVar,
    Menu,
    Toplevel,
    Tk,
    NW,
    Menubutton,
    Checkbutton,
    StringVar,
)
import tkinter.ttk as ttk
from tkinter.constants import CENTER, DISABLED, END, INSERT, NORMAL
from tkinter.font import Font
from os import startfile
from winregistry import WinRegistry
from dattAMsh import (
    lang_code,
    DISPLAY_DATA,
    display_lang_lists,
    bhAShAH,
    AJAY,
    bhAShAH_img,
)
from mouse import get_position
from threading import Thread
from copy import deepcopy
from PIL import Image, ImageTk

ver = 1.0
lengths = [[], []]
for x in range(0, len(lang_code[2])):
    lengths[1].append(x)
for x in range(0, len(display_lang_lists)):
    lengths[0].append(x)


def start_file(f):
    def s():
        startfile(f)

    a = Thread(target=s)
    a.daemon = True
    a.start()


def get_registry(name):
    reg = WinRegistry()
    path = r"HKCU\SOFTWARE\lekhika"
    try:
        a = int(reg.read_value(path, name)["data"])
        err = False
        if name in ("app_status", "sa_mode", "sg_st", "window_start") and a not in (
            0,
            1,
        ):
            err = True
        elif name == "language" and (a not in lengths[0]):
            err = True
        elif name == "typ_lang" and (a not in lengths[1]):
            err = True
        if err:
            raise FileNotFoundError
        return a
    except:
        store_registry(0 if name != "sg_st" else 1, name)
        return get_registry(name)


def store_registry(value, name):
    reg = WinRegistry()
    path = r"HKCU\SOFTWARE\lekhika"
    if "lekhika" not in reg.read_key(r"HKCU\SOFTWARE")["keys"]:
        reg.create_key(path)
    reg.write_value(path, name, str(value).encode("ascii"), "REG_BINARY")


def alert(msg, color, AkAra=19, geo=None, lapse=0, wait=False, bg=None):
    def s(msg, color, lapse, geo, AkAra, bgi):
        master = Tk()
        master.wm_overrideredirect(True)
        a = Frame(master, highlightbackground="brown", highlightthickness=3)
        style = ttk.Style(master)
        if bgi != None:
            style.configure(
                "A.TLabel",
                font=("Nirmala UI", AkAra, "bold"),
                foreground=color,
                background=bgi,
            )
        else:
            style.configure(
                "A.TLabel", font=("Nirmala UI", AkAra, "bold"), foreground=color
            )
        sd = ttk.Label(a, text=msg, style="A.TLabel", justify=CENTER)
        sd.pack()
        a.pack()
        master.title("")
        if geo == None:
            master.geometry("+20+10")
        else:
            master.eval("tk::PlaceWindow . center")
        master.attributes("-topmost", True)
        master.update()
        master.after(650 + lapse, master.destroy)
        master.mainloop()

    lapse += 650
    if wait:
        s(msg, color, lapse, geo, AkAra, bg)
        return
    a = Thread(target=s, args=(msg, color, lapse, geo, AkAra, bg))
    a.daemon = True
    a.start()


class ToolTip:
    def __init__(self, name, root, widget, text, x, y, lang):
        self.widget = widget
        self.name = name + ".TLabel"
        self.x = x
        self.root = root
        self.y = y
        if x == -1:
            self.x = 25
        if y == -1:
            self.y = 20
        if lang == "English":
            size = 9
        else:
            size = 10
        self.win = Toplevel(self.root)
        self.win.wm_withdraw()
        self.style = ttk.Style(self.win)
        self.style.configure(
            self.name,
            font=("Nirmala UI", size),
            foreground="#ffffe1",
            background="#000023",
        )
        self.text = StringVar(self.win, text)
        label = ttk.Label(
            self.win,
            textvariable=self.text,
            justify="left",
            relief="solid",
            borderwidth=1.7,
            style=self.name,
        )
        label.pack(ipadx=1)
        self.win.wm_overrideredirect(True)
        self.chalita_sthiti = False
        widget.bind("<Enter>", self.enter)
        widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x += self.widget.winfo_rootx() + self.x
        y += self.widget.winfo_rooty() + self.y
        self.win.wm_geometry("+%d+%d" % (x, y))

        def show():
            if self.chalita_sthiti:
                self.win.wm_deiconify()

        self.win.after(200, show)
        self.chalita_sthiti = True

    def close(self, event=None):
        if self.chalita_sthiti:
            self.win.wm_withdraw()
            self.chalita_sthiti = False

    def update_lekha(self, lekha, lang=None):
        self.text.set(lekha)
        if lang != None:
            if lang == "English":
                size = 9
            else:
                size = 10
            self.style.configure(self.name, font=("Nirmala UI", size))


class pradarshanam:
    def __init__(self, m):
        self.main_object = m

    def prArambh(self):
        self.root = Tk()
        return self

    def init(self):
        main_obj = self.main_object
        self.ex = False
        self.centred = False
        self.style = ttk.Style(self.root)
        self.advanced_window_data_preperation = False
        self.root.wm_withdraw()
        self.__objs = {}
        self.img_window_status = False
        sdf = get_registry("language")
        self.language = StringVar(self.root, display_lang_lists[sdf])
        self.l_data = DISPLAY_DATA[self.language.get()]
        self.display_values = {}
        self.root.bind("<Control-q>", lambda s: self.open_img())
        for x in self.l_data["values"]:
            self.display_values[x] = StringVar(self.root, self.l_data["values"][x])
        b = lang_code[1][self.main_object.lang_mode]
        self.karyAsthiti = self.main_object.ks
        a = self.main_object.sa_lang
        self.typing_lang = StringVar(self.root, value=b)
        self.sanskrit_mode = IntVar(self.root, value=a)
        self.ajay_texts = [StringVar(self.root), StringVar(self.root)]
        t = "ajay➠" + AJAY[lang_code[0][self.typing_lang.get()]]
        self.ajay_texts[0].set(t[:-1])
        self.ajay_texts[1].set(t)
        self.option_values = {
            "startup": IntVar(self.root, value=main_obj.window_start_status),
            "app": IntVar(self.root, main_obj.ks),
            "typing": StringVar(self.root, value=b),
            "sg": IntVar(self.root, self.main_object.sg_status),
        }
        self.root.resizable(False, False)
        self.root.iconbitmap(r"resources\Icon.ico")
        self.root.title(self.l_data["app_title"])
        self.__top_frame()
        self.__input_frame()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.hide(True))
        self.kAryaM.configure(image=self.image[self.karyAsthiti])
        self.sg_button.configure(image=self.image1[int(main_obj.sg_status)])
        about_img = ImageTk.PhotoImage(Image.open(r"resources\img\about.png"))
        convert_img = ImageTk.PhotoImage(Image.open(r"resources\img\convert.png"))
        self.m.menu.entryconfigure(2, image=self.image[0], selectimage=self.image[1])
        self.m.menu.entryconfigure(3, image=self.image1[0], selectimage=self.image1[1])
        self.m.menu.entryconfigure(4, image=self.image1[0], selectimage=self.image1[1])
        self.m.menu.entryconfigure(8, image=about_img)
        self.m.menu.entryconfigure(7, image=convert_img)
        fh = ImageTk.PhotoImage(Image.open(r"resources\img\menu.png"))
        add = ImageTk.PhotoImage(Image.open(r"resources\img\add.png"))
        self.__objs["add_lang"].configure(image=add)
        self.m.configure(image=fh)
        i = ImageTk.PhotoImage(
            master=self.root, image=Image.open(r"resources\img\usage.png")
        )
        self.usage_btn.configure(image=i)
        lang_img = ImageTk.PhotoImage(Image.open(r"resources\img\lang.png"))
        dfg = ttk.Label(self.top_frame, image=lang_img)
        self.__objs["app_lang_img"] = dfg
        dfg.grid(row=0, column=3, sticky=NW)
        if main_obj.window_start_status == 0:
            self.root.wm_deiconify()
            self.root.eval("tk::PlaceWindow . center")
            self.centred = True
            self.root.attributes("-topmost", True)
            self.root.after(600, lambda: self.root.attributes("-topmost", False))
        else:
            main_obj.give_startup_msg()
        self.root.update()
        main_obj.tk_status = True
        self.root.after(1000, self.__titles)
        self.root.mainloop()

    def __titles(self):
        self.__dynamic_titles = {
            "main": self.karyAsthiti,
            "sahayika": int(self.main_object.sg_status),
        }
        self.__title_properties = {
            "usage": (-33, 24),
            "app_lang_img": (-20, 26),
            "app_lang_option": (-30, 25),
            "typ_lang": (-20, 28),
            "background": (-40, 28),
            "menu": (35, 9),
            "main": (4, 32),
            "sahayika": (-10, 23),
            "add_lang": (-28, 22),
        }
        self.title_ref = {}
        for x in self.__objs:
            d = self.__title_properties[x]
            name = x
            if x in self.__dynamic_titles:
                n = self.__dynamic_titles[x]
                name = x + str(n)
            self.title_ref[x] = ToolTip(
                x,
                self.root,
                self.__objs[x],
                self.l_data["title"][name],
                d[0],
                d[1],
                self.language.get(),
            )

    def __top_frame(self):
        self.top_frame = Frame(self.root)
        self.style.configure(
            "B.TMenubutton",
            font=("Nirmala UI", 8, "bold"),
            foreground="purple",
            background="white",
        )
        self.usage_btn = ttk.Label(self.top_frame, compound="left")
        self.__objs["usage"] = self.usage_btn
        self.usage_btn.bind("<Button-1>", lambda s: self.open_img())
        self.usage_btn.grid(row=0, column=2, sticky=NW, padx=(18, 0))
        ad = list(deepcopy(display_lang_lists))[::-1]
        ad.append("")
        ad = ad[::-1]
        frame1 = Frame(
            self.top_frame, highlightbackground="black", highlightthickness=1
        )
        bhASA = ttk.OptionMenu(
            frame1,
            self.language,
            *ad,
            style="B.TMenubutton",
            command=self.update_lang_data,
        )
        bhASA.grid(row=0, column=0, stick=NW)
        frame1.grid(row=0, column=4, stick=NW, padx=(0, 25), pady=(1.5, 0))
        self.__objs["app_lang_option"] = frame1
        bhASA["menu"].config(font=("Nirmala UI", (8), "bold"), fg="red")
        self.style.configure(
            "A.TButton",
            font=("Nirmala UI", 9, "bold"),
            foreground="red",
            background="black",
        )
        bac = ttk.Button(
            self.top_frame,
            style="A.TButton",
            compound="left",
            textvariable=self.display_values["background_run"],
            command=self.hide,
        )
        bac.grid(row=0, column=6, sticky="ne", padx=(0, 19.5))
        self.__objs["background"] = bac
        self.top_frame.grid(row=0, sticky=NW)
        self.__menu_kAraH()

    def __menu_kAraH(self):
        self.m = Menubutton(self.top_frame)
        self.m.menu = Menu(self.m, tearoff=False)
        self.__objs["menu"] = self.m
        self.m["menu"] = self.m.menu
        self.menu_values = self.l_data["menu_values"]
        self.m.menu.add_command(
            label=self.menu_values["default"],
            foreground="#3a2e2e",
            activeforeground="yellow",
            font=Font(family="Nirmala UI", weight="bold", size=13),
        )
        nested = Menu(self.m.menu, tearoff=False)
        for x in bhAShAH[::-1]:
            nested.add_radiobutton(
                label=x,
                value=x,
                variable=self.option_values["typing"],
                font=Font(family="Nirmala UI", weight="bold", size=9),
                foreground="#8b0000",
                activeforeground="yellow",
                command=lambda: store_registry(
                    lang_code[2].index(
                        lang_code[0][self.option_values["typing"].get()]
                    ),
                    "typ_lang",
                ),
            )
        self.m.menu.add_cascade(
            label=self.menu_values["typing_lang"],
            menu=nested,
            font=Font(family="Nirmala UI", weight="bold", size=10),
            activeforeground="yellow",
            foreground="purple",
            background="#e8f5bf",
        )
        self.m.menu.add_checkbutton(
            variable=self.option_values["app"],
            indicatoron=False,
            background="#e8f5bf",
            foreground="green",
            command=lambda: store_registry(
                self.option_values["app"].get(), "app_status"
            ),
        )
        self.m.menu.add_checkbutton(
            label=self.menu_values["sahayika"],
            compound="left",
            variable=self.option_values["sg"],
            indicatoron=False,
            font=Font(family="Nirmala UI", weight="bold", size=9),
            activeforeground="yellow",
            background="#e8f5bf",
            foreground="blue",
            command=lambda: store_registry(self.option_values["sg"].get(), "sg_st"),
        )
        self.m.menu.add_checkbutton(
            label=self.menu_values["startup"],
            variable=self.option_values["startup"],
            onvalue=0,
            activeforeground="yellow",
            offvalue=1,
            background="#e8f5bf",
            compound="left",
            font=Font(family="Nirmala UI", weight="bold", size=9),
            foreground="brown",
            indicatoron=False,
            command=lambda: store_registry(
                self.option_values["startup"].get(), "window_start"
            ),
        )
        self.m.menu.add_separator()
        self.m.menu.add_separator()
        self.m.menu.add_command(
            label=self.menu_values["normal_version"],
            command=lambda: start_file("samanya.exe"),
            foreground="purple",
            compound="left",
            background="white",
            activeforeground="yellow",
            font=Font(family="Nirmala UI", weight="bold", size=10),
        )
        self.m.menu.add_command(
            label=self.menu_values["about"],
            command=lambda: self.__about_window(),
            compound="left",
            background="#fdfdd6",
            foreground="green",
            activeforeground="yellow",
            font=Font(family="Nirmala UI", weight="bold", size=10),
        )
        self.m.menu.add_command(
            label=self.menu_values["extra"],
            command=lambda: start_file(r"resources\Additional Information.pdf"),
            background="#fdfdd6",
            foreground="red",
            activeforeground="white",
            font=Font(family="Nirmala UI", weight="bold", size=10),
        )
        self.m.grid(row=0, column=0, sticky="n")

    def __input_frame(self):
        command_frame = Frame(self.root)
        self.image = (
            ImageTk.PhotoImage(Image.open(r"resources\img\off.png")),
            ImageTk.PhotoImage(Image.open(r"resources\img\on.png")),
        )
        self.kAryaM = ttk.Label(command_frame)
        self.kAryaM.grid(row=0, column=0, sticky=NW, padx=(0, 25))
        self.kAryaM.bind(
            "<Button-1>", lambda x: self.main_object.change(True, False, True)
        )
        self.__objs["main"] = self.kAryaM
        self.style.configure(
            "SA.TRadiobutton", font=("Nirmala UI", 9, "bold"), background="lightblue"
        )
        self.fr_ajay = Frame(command_frame)
        saoff = ttk.Radiobutton(
            self.fr_ajay,
            textvariable=self.ajay_texts[0],
            value=0,
            style="SA.TRadiobutton",
            variable=self.sanskrit_mode,
            command=self.update_sans_mode,
        )
        saoff.grid(row=0, column=0, sticky=NW)
        saon = ttk.Radiobutton(
            self.fr_ajay,
            textvariable=self.ajay_texts[1],
            value=1,
            style="SA.TRadiobutton",
            variable=self.sanskrit_mode,
            command=self.update_sans_mode,
        )
        saon.grid(row=0, column=1, sticky=NW)
        if self.main_object.lang_mode not in ("Urdu", "Romanized", "Kashmiri"):
            self.fr_ajay.grid(row=0, column=2, sticky="nw", pady=(1.8, 0))
        command_frame.grid(row=2, column=0, sticky=NW)
        frame = ttk.Frame(self.root)
        self.style.configure(
            "TYP.TLabel", font=("Nirmala UI", 12, "bold"), foreground="brown"
        )
        ttk.Label(
            frame,
            style="TYP.TLabel",
            textvariable=self.display_values["typing_lang_main"],
        ).grid(row=0, column=0, sticky=NW)
        frame1 = Frame(frame, highlightbackground="black", highlightthickness=1)
        self.style.configure(
            "A.TMenubutton",
            font=("Nirmala UI", 10, "bold"),
            foreground="green",
            background="white",
        )
        asd = deepcopy(bhAShAH)
        asd.append("")
        asd = asd[::-1]
        sd = ttk.OptionMenu(
            frame1,
            self.typing_lang,
            *asd,
            style="A.TMenubutton",
            command=lambda s: self.main_object.update_typ_lang(
                self.typing_lang.get(), True
            ),
        )
        sd.grid(row=0, column=1, stick=NW)
        frame1.grid(row=0, column=1, stick=NW, padx=1)
        self.__objs["typ_lang"] = frame1
        sd["menu"].config(font=("Nirmala UI", 10, "bold"), fg="red", bg="#faf9ae")
        add = ttk.Label(frame)
        add.grid(row=0, column=2, sticky=NW, pady=4, padx=(3.3, 6.4))
        self.__objs["add_lang"] = add
        self.image1 = (
            ImageTk.PhotoImage(Image.open(r"resources\img\off1.png")),
            ImageTk.PhotoImage(Image.open(r"resources\img\on1.png")),
        )
        self.sg_button = ttk.Label(frame)
        self.sg_button.grid(row=0, column=4, sticky=NW, pady=2.5)
        self.sg_button.bind(
            "<Button-1>", lambda x: self.main_object.exec_taskbar_commands("sg", False)
        )
        self.__objs["sahayika"] = self.sg_button
        self.style.configure(
            "sah.TLabel", font=("Nirmala UI", 11, "bold"), foreground="blue"
        )
        hl = ttk.Label(
            frame, textvariable=self.display_values["sahayika"], style="sah.TLabel"
        )
        hl.grid(row=0, column=5, sticky=NW)

        def sg_label_click():
            self.style.configure("sah.TLabel", foreground="black")
            self.root.after(
                300, lambda: self.style.configure("sah.TLabel", foreground="blue")
            )
            self.main_object.exec_taskbar_commands("sg", False)

        hl.bind("<Button-1>", lambda x: sg_label_click())
        frame.grid(row=3, column=0, sticky=NW)
        self.style.configure(
            "ins.TLabel", font=("Nirmala UI", 10, "bold"), foreground="purple"
        )
        ttk.Label(
            self.root,
            style="ins.TLabel",
            textvariable=self.display_values["instructions"],
        ).grid(row=4, column=0, sticky=NW)

    def update_sans_mode(self, mannual=0, v=0):
        if mannual == 1:  # from lang change
            self.sanskrit_mode.set(v)
            self.main_object.sa_lang = v
        else:
            self.main_object.sa_lang = self.sanskrit_mode.get()
        self.main_object.msg.add("update_sa")
        self.main_object.value_change[1] = True

    def __about_window(self):
        about = Toplevel(self.root)
        about.title(self.l_data["about_title"])
        about.geometry("+140+70")
        about.wm_withdraw()
        about.resizable(False, False)
        about.iconbitmap(r"resources\Icon.ico")
        self.style.configure(
            "about.TLabel", font=("Nirmala UI", 11, "bold"), foreground="brown"
        )
        self.style.configure(
            "email.TLabel", font=("Nirmala UI", 10, "bold"), foreground="green"
        )
        ttk.Label(
            about,
            textvariable=self.display_values["app_description"],
            style="about.TLabel",
            justify=CENTER,
        ).pack()
        ttk.Label(
            about, text="Email :- shubhamanandgupta@outlook.com", style="email.TLabel"
        ).pack()
        self.display_values["version"].set(
            self.display_values["version"].get().format(ver)
        )
        self.style.configure(
            "ver.TLabel", font=("Nirmala UI", 11, "bold"), foreground="red"
        )
        ttk.Label(
            about, textvariable=self.display_values["version"], style="ver.TLabel"
        ).pack()
        self.style.configure(
            "bh.TLabel", font=("Nirmala UI", 11, "bold"), foreground="blue"
        )
        f = ttk.Frame(about)
        ttk.Label(f, text="भारते रचितः", style="bh.TLabel").grid(
            row=0, column=0, padx=(0, 10)
        )
        git = ttk.Label(f)
        git.grid(row=0, column=2)
        f.pack()
        fh = ImageTk.PhotoImage(Image.open(r"resources\img\github.png"))
        git.configure(image=fh)
        git.bind("<Button-1>", lambda s: start_file(r"resources\srota.url"))

        def pratyAdesham():
            r = Toplevel(about)
            r.title(self.l_data["licence_title"])
            r.geometry("+200+50")
            r.wm_withdraw()
            r.resizable(False, False)
            r.iconbitmap(r"resources\Icon.ico")
            lpo = (
                "MIT License\n"
                "\n"
                "Copyright (c) 2021 Lipi Lekhika (shubhamanandgupta@outlook.com)\n"
                "\n"
                "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
                'of this software and associated documentation files (the "Software"), to deal\n'
                "in the Software without restriction, including without limitation the rights\n"
                "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
                "copies of the Software, and to permit persons to whom the Software is\n"
                "furnished to do so, subject to the following conditions:\n"
                "\n"
                "The above copyright notice and this permission notice shall be included in all\n"
                "copies or substantial portions of the Software.\n"
                "\n"
                'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
                "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
                "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
                "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
                "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
                "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
                "SOFTWARE."
            )
            self.style.configure(
                "LIC.TLabel", font=("Consolas", 12, "bold"), foreground="green"
            )
            ttk.Label(r, text=lpo, style="LIC.TLabel").pack()
            r.wm_deiconify()
            r.mainloop()

        self.style.configure(
            "LIC.TButton", font=("Nirmala Ui", 10, "bold"), foreground="black"
        )
        ttk.Button(
            about,
            textvariable=self.display_values["licence"],
            command=pratyAdesham,
            style="LIC.TButton",
        ).pack()
        about.wm_deiconify()
        about.mainloop()

    def update_img_win(self):
        self.img_window_status = False
        self.img_win.destroy()

    def open_img(self):
        self.img_on_top_status = False

        def change_img_top():
            self.img_on_top_status = not self.img_on_top_status
            self.img_win.attributes("-topmost", self.img_on_top_status)

        if self.img_window_status:
            self.img_win.wm_deiconify()
            return
        self.img_win = Toplevel(self.root)
        self.img_win.wm_withdraw()
        self.img_win.title("परिवर्तनसूच्यः")
        self.img_win.geometry("+{0}+0".format(int(self.root.winfo_screenwidth() - 600)))
        self.img_win.protocol("WM_DELETE_WINDOW", self.update_img_win)
        self.img_win.iconbitmap(r"resources\Icon.ico")
        image_collection = {}
        for v in bhAShAH_img:
            try:
                a = lang_code[0][v]
                if a in ["Sanskrit", "Nepali", "Konkani", "Marathi"]:
                    a = "Hindi"
                if a == "Kashmiri":
                    a = "Urdu"
                image_collection[v] = ImageTk.PhotoImage(
                    Image.open("resources\\img\\lang\\" + a + ".png")
                )
            except:
                pass
        try:
            image_collection["Vedic"] = ImageTk.PhotoImage(
                Image.open("resources\\img\\lang\\Vedic.png")
            )
        except:
            pass
        fr = ttk.Frame(self.img_win)
        lang = StringVar(self.img_win, value=self.typing_lang.get())
        self.style.configure(
            "B.TMenubutton",
            font=("Nirmala UI", 10, "bold"),
            background="white",
            foreground="green",
        )
        im = deepcopy(bhAShAH_img)[::-1]
        im.append("")
        im = im[::-1]
        frame1 = Frame(fr, highlightbackground="brown", highlightthickness=1)
        bhASAd = ttk.OptionMenu(
            frame1,
            lang,
            *im,
            style="B.TMenubutton",
            command=lambda _: sUchI.configure(image=image_collection[lang.get()]),
        )
        bhASAd.grid(row=0, column=0, stick=NW)
        frame1.grid(row=0, column=0, stick=NW)
        bhASAd["menu"].config(font=("Nirmala UI", (10), "bold"), fg="red", bg="#faf9ae")
        ck_btn = IntVar(self.img_win, 0)
        Checkbutton(
            fr,
            variable=ck_btn,
            offvalue=0,
            onvalue=1,
            textvariable=self.display_values["pin_top"],
            command=change_img_top,
            fg="purple",
            font=("Nirmala UI", 10, "bold"),
        ).grid(row=0, column=1, sticky=NW)
        fr.grid(row=0, column=0, sticky=NW)
        self.img_win.resizable(False, False)
        self.img_window_status = True
        self.style.configure(
            "SUC.TLabel", font=("Nirmala UI", 12, "bold"), foreground="green"
        )
        ttk.Label(
            self.img_win,
            textvariable=self.display_values["sUchI_msg"],
            style="SUC.TLabel",
            justify=CENTER,
        ).grid(row=1, column=0, sticky="n")
        self.style.configure("kl.TLabel", padding=5)
        sUchI = ttk.Label(
            self.img_win, image=image_collection[lang.get()], style="kl.TLabel"
        )
        sUchI.grid(row=2, column=0, sticky=NW)
        self.style.configure(
            "N.TLabel", font=("Nirmala UI", 9, "bold"), foreground="brown"
        )
        ttk.Label(
            self.img_win, textvariable=self.display_values["nirdesh"], style="N.TLabel"
        ).grid(row=3, column=0, sticky=NW)
        self.img_win.wm_deiconify()
        self.img_win.attributes("-topmost", True)
        self.img_win.after(2300, lambda: self.img_win.attributes("-topmost", False))
        self.root.after(20, lambda: self.img_win.mainloop())

    def hide(self, event=None):
        self.root.wm_withdraw()
        if self.main_object.tk_status:
            if event == True:
                self.main_object.sandesh.add("close")
                self.main_object.value_change[0] = True
            else:
                alert(
                    self.l_data["hide2"],
                    color="purple",
                    lapse=1800,
                    geo=True,
                    AkAra=13,
                )

    def display(self, t):
        if t == "show":
            self.root.wm_deiconify()
            if not self.centred:
                self.root.after(20, lambda: self.root.eval("tk::PlaceWindow . center"))
                self.centred = True
            self.root.attributes("-topmost", True)
            self.root.after(1300, lambda: self.root.attributes("-topmost", False))

    def update_lang_data(self, event):
        def set_text():
            for x in self.l_data["values"]:
                self.display_values[x].set(self.l_data["values"][x])
            self.root.title(self.l_data["app_title"])
            self.main_object.sg.set_extra_values()
            self.menu_values = self.l_data["menu_values"]
            loc = (
                "default",
                "typing_lang",
                None,
                "sahayika",
                "startup",
                None,
                None,
                "normal_version",
                "about",
                "extra",
            )
            for x in range(len(loc)):
                if loc[x] == None:
                    continue
                self.m.menu.entryconfigure(x, label=self.menu_values[loc[x]])
                self.m.update()

        self.ex = True
        a = display_lang_lists.index(self.language.get())
        self.l_data = DISPLAY_DATA[self.language.get()]
        store_registry(a, "language")
        set_text()
        for x in self.__title_properties:
            if x in self.__dynamic_titles:
                n = self.__dynamic_titles[x]
                self.title_ref[x].update_lekha(
                    self.l_data["title"][x + str(n)], self.language.get()
                )
                continue
            self.title_ref[x].update_lekha(self.l_data["title"][x], self.language.get())
        self.display_values["version"].set(
            self.display_values["version"].get().format(ver)
        )
        self.root.update()
        self.main_object.sandesh.add("app_lang")
        self.main_object.value_change[0] = True


class sahAyikA:
    def __init__(self, m):
        th = Thread(target=self.__start)
        th.daemon = True
        th.start()
        self.c = 0
        self.d = 0
        self.main = m
        self.closed = True

    def __start(self):
        self.root = Tk()
        self.extra = [StringVar(self.root), StringVar(self.root)]
        self.set_extra_values()
        self.root.wm_withdraw()
        self.root.configure(bg="#faf9ae")
        self.root.attributes("-topmost", True)
        self.key = [StringVar(self.root), StringVar(self.root)]
        self.next = []
        self.varna = []
        self.reset_capital_status = False
        for x in range(0, 60):
            self.next.append(StringVar(self.root, value=""))
            self.varna.append(StringVar(self.root, value=""))
        self.root.wm_overrideredirect(True)
        self.root.update()
        f = Frame(self.root, bg="#faf9ae")
        f.grid(row=0, column=0, sticky=NW)
        style = ttk.Style(self.root)
        f2 = Frame(f, bg="#faf9ae")
        can = Canvas(f2, width=24, height=43, bg="#faf9ae")
        can.pack()
        img = ImageTk.PhotoImage(
            image=Image.open(r"resources\img\main.png"), master=can
        )
        can.create_image(3, 24, anchor=NW, image=img)
        f2.grid(row=0, column=0, sticky=NW)
        self.frame = Frame(f, bg="#faf9ae")
        style.configure(
            "A.TLabel",
            font=("Nirmala UI", 18, "bold"),
            foreground="brown",
            background="#faf9ae",
        )
        style.configure(
            "B.TLabel",
            font=("Nirmala UI", 13, "bold"),
            foreground="red",
            background="#faf9ae",
        )
        style.configure(
            "C.TLabel",
            font=("Nirmala UI", 15, "bold"),
            foreground="black",
            background="#faf9ae",
        )
        style.configure(
            "D.TLabel",
            font=("Nirmala UI", 15, "bold"),
            foreground="green",
            background="#faf9ae",
        )
        frm = Frame(self.frame, bg="#faf9ae")
        ttk.Label(frm, textvariable=self.key[0], style="A.TLabel", justify=CENTER).grid(
            row=0, column=0, sticky="n"
        )
        ttk.Label(frm, textvariable=self.key[1], style="B.TLabel", justify=CENTER).grid(
            row=1, column=0, sticky="n"
        )
        frm.grid(row=0, column=0, sticky=NW, padx=(0, 8))
        self.f = []
        for x in range(0, 60):
            self.f.append(None)
        for x in range(0, 13):
            self.f[x] = Frame(self.frame, bg="#faf9ae")
            ttk.Label(
                self.f[x], textvariable=self.next[x], style="C.TLabel", justify=CENTER
            ).pack()
            ttk.Label(
                self.f[x], textvariable=self.varna[x], style="D.TLabel", justify=CENTER
            ).pack()
            self.f[x].grid(row=0, column=x + 1, sticky=NW)
        self.f_count = 12
        self.pUrvavarNa = [("", "", -1), ""]
        self.frame.grid(row=0, column=1, sticky=NW)
        f1 = Frame(self.root, bg="#faf9ae")
        style.configure(
            "Z1.TLabel",
            font=("Nirmala UI", 9, "bold"),
            foreground="purple",
            background="#faf9ae",
        )
        ttk.Label(f1, textvariable=self.extra[0], style="Z1.TLabel").grid(
            row=0, column=0, sticky=NW
        )
        style.configure(
            "Z2.TLabel", font=("Nirmala UI", 8), foreground="blue", background="#faf9ae"
        )
        ttk.Label(f1, textvariable=self.extra[1], style="Z2.TLabel").grid(
            row=1, column=0, sticky=NW
        )
        f1.grid(row=1, column=0, sticky=NW)
        self.root.mainloop()

    def hide(self, s=False):
        if s:
            if not self.closed:
                self.__reset()
                self.closed = True
            return
        if self.c == 1 and not self.closed:
            self.__reset()
            self.closed = True
        self.c -= 1

    def __reset(self):
        self.root.wm_withdraw()
        if self.f_count > 12:
            for x in range(13, self.f_count + 1):
                self.f[x].grid_forget()
            self.f_count = 12
        for x in range(0, 13):
            self.next[x].set("")
            self.varna[x].set("")

    def show(self, v):
        self.reset_capital_status = False

        def reset_capital(k):
            self.d -= 1
            if not self.reset_capital_status:
                return
            if self.d == 0:
                x = k[0]
                while x < k[1]:
                    self.varna[x].set("")
                    self.next[x].set("")
                    x += 1
                self.main.msg.add("clear_sg")
                self.main.value_change[1] = True

        if self.f_count > 12:
            for x in range(13, self.f_count + 1):
                self.f[x].grid_forget()
            self.f_count = 12
        next = v["key"][1]
        key = v["key"][0]
        matra = v["mAtrA"]
        extra_cap = v["special_cap"]
        if extra_cap[0]:
            self.pUrvavarNa = (
                [
                    self.main.akSharAH[self.main.lang_mode][extra_cap[1][0]][
                        extra_cap[1][0]
                    ][0],
                    "",
                    extra_cap[1][1],
                ],
                extra_cap[1][0],
            )
        s = get_position()
        self.root.geometry("+{0}+{1}".format(s[0] + 5, s[1] + 25))
        halant = ("", False)
        if self.main.lang_mode not in ("Urdu", "Romanized"):
            halant = (
                self.main.akSharAH[self.main.lang_mode]["q"]["qq"][0],
                self.main.sa_lang == 1,
            )
        a = {}
        b = self.main.akSharAH[self.main.lang_mode][key[0]]
        count = 0
        for x in next:
            if key + x in b:
                a[x] = b[key + x]
                for y in b[key + x][-2]:
                    if key + x + y in b:
                        a[x + y] = b[key + x + y]
                        count += 1
                count += 1
        c = 0
        cap_count = [0, 0]  # to store of capitals to be cleared
        if "cap" in v:
            cap_count[0] = count
            b1 = self.main.akSharAH[self.main.lang_mode][key.upper()]
            a[key + key] = b1[key.upper()]
            next = a[key + key][-2]
            tmp = key.upper()
            for x in next:
                if tmp + x in b1:
                    a[key + key + x] = b1[tmp + x]
                    for y in b1[tmp + x][-2]:
                        if tmp + x + y in b1:
                            a[key + key + x + y] = b1[tmp + x + y]
                            count += 1
                    count += 1
            cap_count[1] = count + 1
        if (self.pUrvavarNa[0][-1] in [1, 3] or matra) and b[key][-1] == 0:
            k12 = self.pUrvavarNa[0][0] + b[key][1]
            if self.pUrvavarNa[0][-1] == 3 and key != "a":
                k12 = k12[:-2] + k12[-1] + k12[-2]
            elif self.pUrvavarNa[0][-1] == 3 and key == "a":
                k12 = k12[:-1] + k12[-1]
            self.key[0].set(self.pUrvavarNa[1] + key)
            self.key[1].set(k12)
        else:
            self.key[0].set(key)
            l12 = b[key][0] + (halant[0] if b[key][-1] in [1, 3] else "")
            if b[key][-1] == 3:
                l12 = l12[:-2] + l12[-1] + l12[-2]
            self.key[1].set(l12)
        for x in a:
            self.next[c].set(x)
            k = a[x][0]
            if a[x][-1] == 0 and self.pUrvavarNa[0][-1] in [1, 3]:
                k = a[x][1]
            if a[x][-1] in [1, 3] and halant[1]:
                k += halant[0]
                if a[x][-1] == 3:
                    k = k[:-2] + k[-1] + k[-2]
            if (self.pUrvavarNa[0][-1] in [1, 3] or matra) and a[x][-1] == 0:
                k = self.pUrvavarNa[0][0] + k
                if self.pUrvavarNa[0][-1] == 3:
                    k = k[:-2] + k[-1] + k[-2]
            self.varna[c].set(k)
            c += 1
        if len(a) - 1 > self.f_count + 1:
            for x in range(self.f_count + 1, len(a)):
                self.f[x] = Frame(self.frame, bg="#faf9ae")
                ttk.Label(
                    self.f[x],
                    textvariable=self.next[x],
                    style="C.TLabel",
                    justify=CENTER,
                ).pack()
                ttk.Label(
                    self.f[x],
                    textvariable=self.varna[x],
                    style="D.TLabel",
                    justify=CENTER,
                ).pack()
                self.f[x].grid(row=0, column=x + 1, sticky=NW)
            self.f_count = len(a) - 1
        for x in range(c, 13):
            self.next[x].set("")
            self.varna[x].set("")
        self.c += 1
        if not matra:
            self.pUrvavarNa = (b[key], key)
        if self.closed:
            self.closed = False
            self.root.wm_deiconify()
        if "cap" in v:
            self.d += 1
            self.reset_capital_status = True
            self.frame.after(4000, lambda: reset_capital(cap_count))
        self.root.after(15000, self.hide)

    def set_extra_values(self):
        l_data = DISPLAY_DATA[display_lang_lists[get_registry("language")]]
        self.extra[0].set(l_data["sahAyikA_msg"]["first_sahayika"])
        self.extra[1].set(l_data["sahAyikA_msg"]["second_sahayika"])
