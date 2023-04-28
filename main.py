import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

win = tk.Tk()
win.title("Cardiocycle model")
win.geometry("920x600+300+50")
win.resizable(False, False)

param_static = {"P": [0.14, 0.025, 0.026, 0.273],
         "Q": [-0.15, 0.003, 0.008, 0.392],
         "R": [1.453, 0.0091, 0.01, 0.4446],
         "S": [-0.34, 0.0115, 0.0417, 0.498],
         "ST": [0.03, 0.1, 0.024, 0.555],
         "T": [0.45, 0.026, 0.044, 0.734]}

param_changeble = {"P": [0.14, 0.025, 0.026, 0.273],
         "Q": [-0.15, 0.003, 0.008, 0.392],
         "R": [1.453, 0.0091, 0.01, 0.4446],
         "S": [-0.34, 0.0115, 0.0417, 0.498],
         "ST": [0.03, 0.1, 0.024, 0.555],
         "T": [0.45, 0.026, 0.044, 0.734]}

def del_frames():
    try:
        P_frame.destroy()
    except:
        print('no such frame')
    try:
        Q_frame.destroy()
    except:
        print('no such frame')
    try:
        R_frame.destroy()
    except:
        print('no such frame')
    try:
        S_frame.destroy()
    except:
        print('no such frame')
    try:
        ST_frame.destroy()
    except:
        print('no such frame')
    try:
        T_frame.destroy()
    except:
        print('no such frame')


fig, ax = plt.subplots()


def main(params, hr):
    Fs = hr * 1000
    t0 = 60 * 1000 / Fs

    def find_t(a):
        t1 = params[a][3] - 3 * params[a][1]
        t2 = params[a][3] + 3 * params[a][2]
        return t1, t2

    def find_b(a, t):
        if t <= params[a][3]:
            return params[a][1]
        else:
            return params[a][2]

    def Gauss(a, time):
        return params[a][0] * np.exp(-((time - params[a][3]) ** 2) / ((2 * find_b(a, time) ** 2)))

    global t
    t = np.arange(0, t0, 0.001)
    global x
    x = []

    for i in t:
        if (find_t('P')[0] <= i < find_t('P')[1]):
            x.append(Gauss("P", i))
        elif (i >= find_t("Q")[0] and i < find_t("Q")[1]):
            x.append(Gauss("Q", i))
        elif (i >= find_t("R")[0] and i < find_t("R")[1]):
            x.append(Gauss("R", i))
        elif (i >= find_t("S")[0] and i < find_t("S")[1]):
            x.append(Gauss("S", i))
        elif (i >= find_t("ST")[0] and i < find_t("ST")[1]):
            x.append(Gauss("ST", i))
        elif (i >= find_t("T")[0] and i < find_t("T")[1]):
            x.append(Gauss("T", i))
        else:
            x.append(0)
    def plot():
        ax.clear()
        ax.plot(t, x, color = "#444444", linewidth =1)
        ax.grid(True, linewidth=0.9, color="#c8e6e9")
        ax.set_xlabel("c", loc='right')
        ax.set_ylabel("мВ", loc='top', rotation=0, labelpad=0.1)
        fig.patch.set_facecolor('#F0F0E2')
        canvas.draw()

    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.get_tk_widget().place(x=240, y=1, width=640, height=500)
    plot()

def get_amp_P(val):
    param_changeble["P"][0] = float(val)
    main(param_changeble, int(hr.get()))

def get_b1_P(val):
    param_changeble["P"][1] = float(val)
    main(param_changeble, int(hr.get()))

def get_b2_P(val):
    param_changeble["P"][2] = float(val)
    main(param_changeble, int(hr.get()))

def get_t_P(val):
    param_changeble["P"][3] = float(val)
    main(param_changeble, int(hr.get()))

def get_amp_Q(val):
    param_changeble["Q"][0] = float(val)
    main(param_changeble, int(hr.get()))

def get_b1_Q(val):
    param_changeble["Q"][1] = float(val)
    main(param_changeble, int(hr.get()))

def get_b2_Q(val):
    param_changeble["Q"][2] = float(val)
    main(param_changeble, int(hr.get()))

def get_t_Q(val):
    param_changeble["Q"][3] = float(val)
    main(param_changeble, int(hr.get()))

def get_amp_R(val):
    param_changeble["R"][0] = float(val)
    main(param_changeble, int(hr.get()))

def get_b1_R(val):
    param_changeble["R"][1] = float(val)
    main(param_changeble, int(hr.get()))

def get_b2_R(val):
    param_changeble["R"][2] = float(val)
    main(param_changeble, int(hr.get()))

def get_t_R(val):
    param_changeble["R"][3] = float(val)
    main(param_changeble, int(hr.get()))

def get_amp_S(val):
    param_changeble["S"][0] = float(val)
    main(param_changeble, int(hr.get()))

def get_b1_S(val):
    param_changeble["S"][1] = float(val)
    main(param_changeble, int(hr.get()))

def get_b2_S(val):
    param_changeble["S"][2] = float(val)
    main(param_changeble, int(hr.get()))

def get_t_S(val):
    param_changeble["S"][3] = float(val)
    main(param_changeble, int(hr.get()))

def get_amp_ST(val):
    param_changeble["ST"][0] = float(val)
    main(param_changeble, int(hr.get()))

def get_b1_ST(val):
    param_changeble["ST"][1] = float(val)
    main(param_changeble, int(hr.get()))

def get_b2_ST(val):
    param_changeble["ST"][2] = float(val)
    main(param_changeble, int(hr.get()))

def get_t_ST(val):
    param_changeble["ST"][3] = float(val)
    main(param_changeble, int(hr.get()))

def get_amp_T(val):
    param_changeble["T"][0] = float(val)
    main(param_changeble, int(hr.get()))

def get_b1_T(val):
    param_changeble["T"][1] = float(val)
    main(param_changeble, int(hr.get()))

def get_b2_T(val):
    param_changeble["T"][2] = float(val)
    main(param_changeble, int(hr.get()))

def get_t_T(val):
    param_changeble["T"][3] = float(val)
    main(param_changeble, int(hr.get()))

def labels(text, x, y):
    tk.Label(main_frame, text=text,
             bg="white",
             font=("Arial", 12),
             width=11,
             height=1,
             # cursor="sizing",
             relief=tk.RAISED).place(x=x, y=y)

def scale_amp(frame, x, y, func):
    tk.Scale(frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=-1,
             to=1.7,
             width=5,
             takefocus=0,
             # variable=a,
             command=func,
             activebackground="white",
             bd=1.3,
             resolution=0.01).place(x=x, y=y)

def scale_t(frame, x, y, func):
    tk.Scale(frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=0,
             to=0.9,
             width=5,
             takefocus=0,
             # variable=a,
             command=func,
             activebackground="white",
             bd=1.3,
             resolution=0.001).place(x=x, y=y)

def scales(frame, x, y, func):
    tk.Scale(frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=-0.1,
             to=0.1,
             width=5,
             takefocus=0,
             # variable=a,
             command=func,
             activebackground="white",
             bd=1.3,
             resolution=0.001).place(x=x, y=y)

hr = tk.StringVar()
def entry(frame):
    tk.Entry(frame,
             bg='#d4eeee',
             fg='#444444',
             justify='center',
             width=5,
             takefocus=0,
             textvariable=hr).place(x=18, y=329)

def P_page():
    del_frames()
    global P_frame
    P_frame = tk.Frame(main_frame, bg="#F0F0E2")
    P_frame.pack(side='left')

    labels("Amplitude", 15, 15)
    labels("Width (b1)", 15, 87)
    labels("Width (b2)", 15, 159)
    labels("Time", 15, 231)
    labels("Heart rate", 15, 303)

    scale_amp(P_frame, 15, 42, get_amp_P)
    scales(P_frame, 15, 114, get_b1_P)
    scales(P_frame, 15, 186, get_b2_P)
    scale_t(P_frame, 15, 258, get_t_P)

    entry(P_frame)

    P_frame.pack_propagate(False)
    P_frame.configure(width=230, height=800)

def Q_page():
    del_frames()
    global Q_frame
    Q_frame = tk.Frame(main_frame, bg="#F0F0E2")
    Q_frame.pack(side='left')

    labels("Amplitude", 70, 15)
    labels("Width (b1)", 70, 87)
    labels("Width (b2)", 70, 159)
    labels("Time", 70, 231)
    labels("Heart rate", 70, 303)

    scale_amp(Q_frame, 15, 42, get_amp_Q)
    tk.Scale(Q_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=-0.01,
             to=0.05,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_b1_Q,
             activebackground="white",
             bd=1.3,
             resolution=0.001).place(x=15, y=114)
    tk.Scale(Q_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=-0.005,
             to=0.01,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_b2_Q,
             activebackground="white",
             bd=1.3,
             resolution=0.001).place(x=15, y=186)
    tk.Scale(Q_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=0.3,
             to=0.5,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_t_Q,
             activebackground="white",
             bd=1.3,
             resolution=0.001).place(x=15, y=258)

    entry(Q_frame)

    Q_frame.pack_propagate(False)
    Q_frame.configure(width=230, height=800)

def R_page():
    del_frames()
    global R_frame
    R_frame = tk.Frame(main_frame, bg="#F0F0E2")
    R_frame.pack(side='left')

    labels("Amplitude", 70, 15)
    labels("Width (b1)", 70, 87)
    labels("Width (b2)", 70, 159)
    labels("Time", 70, 231)
    labels("Heart rate", 70, 303)

    scale_amp(R_frame, 15, 42, get_amp_R)
    tk.Scale(R_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=-0.004,
             to=0.01,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_b1_R,
             activebackground="white",
             bd=1.3,
             resolution=0.0001).place(x=15, y=114)
    tk.Scale(R_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=0,
             to=0.01,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_b2_R,
             activebackground="white",
             bd=1.3,
             resolution=0.0001).place(x=15, y=186)
    tk.Scale(R_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=0.46,
             to=0.4,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_t_R,
             activebackground="white",
             bd=1.3,
             resolution=0.0001).place(x=15, y=258)

    entry(R_frame)

    R_frame.pack_propagate(False)
    R_frame.configure(width=230, height=800)

def S_page():
    del_frames()
    global S_frame
    S_frame = tk.Frame(main_frame, bg="#F0F0E2")
    S_frame.pack(side='left')

    labels("Amplitude", 15, 15)
    labels("Width (b1)", 15, 87)
    labels("Width (b2)", 15, 159)
    labels("Time", 15, 231)
    labels("Heart rate", 15, 303)

    scale_amp(S_frame, 15, 42, get_amp_S)
    tk.Scale(S_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=-0.007,
             to=0.038,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_b1_S,
             activebackground="white",
             bd=1.3,
             resolution=0.0001).place(x=15, y=114)
    tk.Scale(S_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=0.003,
             to=0.1,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_b2_S,
             activebackground="white",
             bd=1.3,
             resolution=0.0001).place(x=15, y=186)
    scale_t(S_frame, 15, 258, get_t_S)

    entry(S_frame)

    S_frame.pack_propagate(False)
    S_frame.configure(width=230, height=800)

def ST_page():
    del_frames()
    global ST_frame
    ST_frame = tk.Frame(main_frame, bg="#F0F0E2")
    ST_frame.pack(side='left')

    labels("Amplitude", 15, 15)
    labels("Width (b1)", 15, 87)
    labels("Width (b2)", 15, 159)
    labels("Time", 15, 231)
    labels("Heart rate", 15, 303)

    scale_amp(ST_frame, 15, 42, get_amp_ST)
    scales(ST_frame, 15, 114, get_b1_ST)
    scales(ST_frame, 15, 186, get_b2_ST)
    tk.Scale(ST_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=0.4,
             to=0.65,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_t_ST,
             activebackground="white",
             bd=1.3,
             resolution=0.001).place(x=15, y=258)

    entry(ST_frame)

    ST_frame.pack_propagate(False)
    ST_frame.configure(width=230, height=800)

def T_page():
    del_frames()
    global T_frame
    T_frame = tk.Frame(main_frame, bg="#F0F0E2")
    T_frame.pack(side='left')

    labels("Amplitude", 15, 15)
    labels("Width (b1)", 15, 87)
    labels("Width (b2)", 15, 159)
    labels("Time", 15, 231)
    labels("Heart rate", 15, 303)

    scale_amp(T_frame, 15, 42, get_amp_T)
    scales(T_frame, 15, 114, get_b1_T)
    scales(T_frame, 15, 186, get_b2_T)
    tk.Scale(T_frame,
             orient="horizontal",
             bg="#d4eeee",
             troughcolor='grey',
             length=200,
             relief="groove",
             from_=0.6,
             to=0.9,
             width=5,
             takefocus=0,
             # variable=a,
             command=get_t_T,
             activebackground="white",
             bd=1.3,
             resolution=0.001).place(x=15, y=258)

    entry(T_frame)

    T_frame.pack_propagate(False)
    T_frame.configure(width=230, height=800)

def hide_indicators():
    P_indicate.config(bg="#c8e6e9")
    Q_indicate.config(bg="#c8e6e9")
    R_indicate.config(bg="#c8e6e9")
    S_indicate.config(bg="#c8e6e9")
    ST_indicate.config(bg="#c8e6e9")
    T_indicate.config(bg="#c8e6e9")

def indicate(lb, page):
    hide_indicators()
    lb.config(bg = "#518281")
    page()
zub_choise_frame = tk.Frame(win, bg = "#c8e6e9")


P_button = tk.Button(zub_choise_frame, text="P", font=('bold', 14), bd=1, fg="#518281", command=lambda: indicate(P_indicate, P_page))
P_button.place(x=10, y=7)
P_indicate = tk.Label(zub_choise_frame, text="", bg="#c8e6e9")
P_indicate.place(x=2, y=5, height=30)

Q_button = tk.Button(zub_choise_frame, text="Q", font=('bold', 14), bd=1, fg="#518281", width=1, command=lambda: indicate(Q_indicate, Q_page))
Q_button.place(x=10, y=47)
Q_indicate = tk.Label(zub_choise_frame, text="", bg="#c8e6e9")
Q_indicate.place(x=2, y=45, height=30)

R_button = tk.Button(zub_choise_frame, text="R", font=('bold', 14), bd=1, fg="#518281", command=lambda: indicate(R_indicate, R_page))
R_button.place(x=10, y=87)
R_indicate = tk.Label(zub_choise_frame, text="", bg="#c8e6e9")
R_indicate.place(x=2, y=85, height=30)

S_button = tk.Button(zub_choise_frame, text="S", font=('bold', 14), bd=1, fg="#518281", command=lambda: indicate(S_indicate, S_page))
S_button.place(x=10, y=127)
S_indicate = tk.Label(zub_choise_frame, text="", bg="#c8e6e9")
S_indicate.place(x=2, y=125, height=30)

ST_button = tk.Button(zub_choise_frame, text="ST", font=('bold', 14), bd=1, fg="#518281", width=1, command=lambda: indicate(ST_indicate, ST_page))
ST_button.place(x=10, y=167)
ST_indicate = tk.Label(zub_choise_frame, text="", bg="#c8e6e9")
ST_indicate.place(x=2, y=165, height=30)

T_button = tk.Button(zub_choise_frame, text="T", font=('bold', 14), bd=1, fg="#518281", command=lambda: indicate(T_indicate, T_page))
T_button.place(x=10, y=207)
T_indicate = tk.Label(zub_choise_frame, text="", bg="#c8e6e9")
T_indicate.place(x=2, y=205, height=30)



zub_choise_frame.pack(side=tk.LEFT)
zub_choise_frame.pack_propagate(False)
zub_choise_frame.configure(width = 60, height = 800)


main_frame = tk.Frame(win, highlightbackground='grey', highlightthickness=1)

def reset():
    main(param_static, int(hr.get()))

T_button = tk.Button(main_frame, text="Reset", font=('bold', 16), bd=1, fg="#518281", command=reset)
T_button.place(x=743, y=540)


def generate():
    win_2 = tk.Tk()
    win_2.title("Noise generation")
    win_2.geometry("1000x450+300+100")
    win_2.resizable(False, False)

    figu, axe = plt.subplots()

    menu_frame = tk.Frame(win_2, bg="#c8e6e9")
    menu_frame.pack(side=tk.BOTTOM)
    menu_frame.pack_propagate(False)
    menu_frame.configure(width=1000, height=75)

    # def get_cycle_num(val):
    #     cycle_num = val
    #     return cycle_num

    cycle_num = tk.StringVar(win_2)
    cycle_num.set('8')

    def get_cycle():
        global Cycle
        Cycle = int(cycle_number.get())
        try:
            main_2(param_changeble, int(hr.get()), Cycle, alter)
        except:
            main_2(param_changeble, int(hr.get()), Cycle, 0)


    cycle_number = tk.Spinbox(menu_frame,
                            bg='#F1F2EA',
                            fg='#444444',
                            justify='center',
                            width=5,
                            from_=2,
                            to = 30,
                            increment=1,
                            textvariable=cycle_num,
                            command=get_cycle)
    cycle_number.place(x=65, y=29)


    def main_2(params, hr, cycle, alt):
        Fs = hr * 1000
        t0 = 60 * 1000 / Fs

        def find_t(a):
            t1 = params[a][3] - 3 * params[a][1]
            t2 = params[a][3] + 3 * params[a][2]
            return t1, t2

        def find_b(a, t):
            if t <= params[a][3]:
                return params[a][1]
            else:
                return params[a][2]

        def Gauss(a, time):
            return params[a][0] * np.exp(-((time - params[a][3]) ** 2) / ((2 * find_b(a, time) ** 2)))

        def Gauss_T(a, time):
            return params[a][0] * (1 + (alt / params[a][0])) * np.exp(
                -((time - params[a][3]) ** 2) / ((2 * find_b(a, time) ** 2)))

        def x_arr(change):
            x = []
            for i in t:
                if (find_t('P')[0] <= i < find_t('P')[1]):
                    x.append(Gauss("P", i))
                elif (i >= find_t("Q")[0] and i < find_t("Q")[1]):
                    x.append(Gauss("Q", i))
                elif (i >= find_t("R")[0] and i < find_t("R")[1]):
                    x.append(Gauss("R", i))
                elif (i >= find_t("S")[0] and i < find_t("S")[1]):
                    x.append(Gauss("S", i))
                elif (i >= find_t("ST")[0] and i < find_t("ST")[1]):
                    x.append(Gauss("ST", i))
                elif (i >= find_t("T")[0] and i < find_t("T")[1]):
                    if change == 0:
                        x.append(Gauss("T", i))
                    if change == 1:
                        x.append(Gauss_T("T", i))
                else:
                    x.append(0)
            return x

        t = np.arange(0, t0, 0.001)

        global all_arrs
        all_arrs = []

        for i in range(0, cycle):
            if i % 2 == 0:
                all_arrs += x_arr(0)
            else:
                all_arrs += x_arr(1)

        t_generate = np.arange(0, t0*(cycle), 0.001)

        def generate_plot():
            axe.clear()
            axe.plot(t_generate, all_arrs, color="#444444", linewidth=1)
            axe.set_ylim([-0.6, 1.9])
            axe.grid(True, linewidth=0.9, color="#c8e6e9")
            axe.set_xlabel("c", loc='right')
            axe.set_ylabel("мВ", loc='top', rotation=0, labelpad=0.1)
            figu.patch.set_facecolor('#F0F0E2')
            canvas.draw()

        canvas = FigureCanvasTkAgg(figu, master=win_2)
        canvas.get_tk_widget().place(x=-50, y=-5, width=1100, height=380)
        generate_plot()


    def get_alt(val):
        global alter
        alter = float(val)
        main_2(param_changeble, int(hr.get()), Cycle, alter)

    tk.Label(menu_frame, text="Alternation level, mV",
             bg="#c8e6e9",
             font=("Arial", 13),
             width=20,
             height=1,
             bd=0,
             # cursor="sizing",
             relief=tk.RAISED).place(x=220, y=8)
    tk.Label(menu_frame, text="Noise level",
             bg="#c8e6e9",
             font=("Arial", 13),
             width=20,
             height=1,
             bd=0,
             # cursor="sizing",
             relief=tk.RAISED).place(x=750, y=8)
    tk.Label(menu_frame,
             text="Number of cycles",
             bg="#c8e6e9",
             font=("Arial", 13),
             width=20,
             height=1,
             bd=0,
             # cursor="sizing",
             relief=tk.RAISED).place(x=20, y=8)

    tk.Scale(menu_frame,
             orient="horizontal",
             bg="#c8e6e9",
             troughcolor='#645D5D',
             length=200,
             relief="groove",
             from_=-3,
             to=3,
             width=6,
             takefocus=0,
             activebackground="#c8e6e9",
             bd=0,
             command=get_alt,
             resolution=0.01).place(x=200, y=25)

    tk.Scale(menu_frame,
             orient="horizontal",
             bg="#c8e6e9",
             troughcolor='#645D5D',
             length=200,
             relief="groove",
             from_=-5,
             to=5,
             width=6,
             takefocus=0,
             activebackground="#c8e6e9",
             bd=0,
             resolution=0.1).place(x=730, y=25)



    main_2(param_changeble, 60, 8, 0)

    win_2.mainloop()


Generate_button = tk.Button(main_frame, text="Generate", font=('bold', 16), bd=1, fg="#518281", command=generate)
Generate_button.place(x=625, y=540)

main(param_static, 60)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=600, width=970, bg="#F0F0E2")

win.mainloop()