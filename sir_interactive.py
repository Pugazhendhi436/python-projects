import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.gridspec as gridspec
 
# ──────────────────────────────────────────────
#  INTERACTIVE SIR SIMULATION — Tkinter version
# ──────────────────────────────────────────────
 
def run_simulation(beta, gamma, N, I0, vax_pct, days):
    S = N * (1 - vax_pct / 100) - I0
    I = float(I0)
    R = N * (vax_pct / 100)
    S_list, I_list, R_list = [], [], []
 
    for _ in range(days):
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
        new_infected  = beta * S * I / N
        new_recovered = gamma * I
        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered
 
    return S_list, I_list, R_list
 
 
def update(event=None):
    # Read slider values
    beta    = beta_slider.get()
    gamma   = gamma_slider.get()
    N       = int(pop_slider.get())
    I0      = int(infected_slider.get())
    vax     = vax_slider.get()
    days    = int(days_slider.get())
 
    S_list, I_list, R_list = run_simulation(beta, gamma, N, I0, vax, days)
 
    peak    = max(I_list)
    peakday = I_list.index(peak)
    total   = ((N - S_list[-1]) / N) * 100
    R0      = beta / gamma
 
    # Update labels
    beta_val.config(text=f"{beta:.2f}")
    gamma_val.config(text=f"{gamma:.2f}")
    pop_val.config(text=f"{N:,}")
    infected_val.config(text=str(I0))
    vax_val.config(text=f"{vax:.0f}%")
    days_val.config(text=str(days))
 
    r0_val.config(text=f"{R0:.2f}")
    r0_color = "#27a84a" if R0 < 1 else "#e08c1a" if R0 < 2 else "#cc3b1a"
    r0_val.config(fg=r0_color)
 
    peak_val.config(text=f"{int(peak):,}")
    peakday_val.config(text=f"Day {peakday}")
    total_val.config(text=f"{total:.1f}%")
 
    # Redraw chart
    t = list(range(days))
    ax.clear()
    ax.plot(t, S_list, label="Susceptible", color="#378ADD", linewidth=2, linestyle="--")
    ax.plot(t, I_list, label="Infected",    color="#D85A30", linewidth=2.5)
    ax.plot(t, R_list, label="Recovered",   color="#639922", linewidth=2, linestyle=":")
    ax.axvline(peakday, color="#D85A30", linestyle="--", alpha=0.35, linewidth=1)
    ax.annotate(
        f"Peak day {peakday}",
        xy=(peakday, peak),
        xytext=(peakday + days * 0.03, peak * 0.88),
        fontsize=8, color="#D85A30",
        arrowprops=dict(arrowstyle="->", color="#D85A30", lw=0.8)
    )
    ax.set_xlabel("Days")
    ax.set_ylabel("Population")
    ax.set_title(f"SIR Virus Spread Simulation  (R₀ = {R0:.2f})", fontsize=12)
    ax.legend(fontsize=9)
    ax.set_xlim(0, days - 1)
    ax.set_ylim(0)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    canvas.draw()
 
 
def load_scenario(beta, gamma, vax):
    beta_slider.set(beta)
    gamma_slider.set(gamma)
    vax_slider.set(vax)
    update()
 
 
# ── WINDOW SETUP ──────────────────────────────
root = tk.Tk()
root.title("🦠 SIR Virus Spread Simulator")
root.geometry("1050x680")
root.configure(bg="#f5f5f0")
 
FONT       = ("Segoe UI", 10)
FONT_BOLD  = ("Segoe UI", 10, "bold")
FONT_SMALL = ("Segoe UI", 9)
BG         = "#f5f5f0"
CARD_BG    = "#eceae3"
 
# ── LEFT PANEL ────────────────────────────────
left = tk.Frame(root, bg=BG, width=280)
left.pack(side=tk.LEFT, fill=tk.Y, padx=12, pady=12)
left.pack_propagate(False)
 
tk.Label(left, text="⚙️  Parameters", font=FONT_BOLD, bg=BG).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0,8))
 
def make_slider(parent, row, label, from_, to, resolution, default):
    tk.Label(parent, text=label, font=FONT_SMALL, bg=BG, anchor="w").grid(row=row, column=0, sticky="w", pady=3)
    slider = tk.Scale(parent, from_=from_, to=to, resolution=resolution,
                      orient=tk.HORIZONTAL, length=160, bg=BG,
                      highlightthickness=0, command=update, showvalue=False)
    slider.set(default)
    slider.grid(row=row, column=1, padx=6)
    val_label = tk.Label(parent, text=str(default), font=FONT_SMALL, bg=BG, width=6, anchor="w")
    val_label.grid(row=row, column=2, sticky="w")
    return slider, val_label
 
beta_slider,    beta_val    = make_slider(left, 1, "Transmission β",  0.01, 0.80, 0.01, 0.30)
gamma_slider,   gamma_val   = make_slider(left, 2, "Recovery γ",      0.01, 0.50, 0.01, 0.10)
pop_slider,     pop_val     = make_slider(left, 3, "Population (N)",  100,  5000, 100,  1000)
infected_slider,infected_val= make_slider(left, 4, "Initial infected", 1,   50,   1,    1)
vax_slider,     vax_val     = make_slider(left, 5, "Vaccinated %",    0,    90,   1,    0)
days_slider,    days_val    = make_slider(left, 6, "Days",            30,   365,  5,    160)
 
# ── SCENARIO BUTTONS ──────────────────────────
tk.Label(left, text="📋  Quick Scenarios", font=FONT_BOLD, bg=BG).grid(row=7, column=0, columnspan=3, sticky="w", pady=(16,6))
 
scenarios = [
    ("No Control",      0.30, 0.10, 0),
    ("😷 Masks",        0.15, 0.10, 0),
    ("🏠 Distancing",   0.10, 0.10, 0),
    ("💉 Vaccination",  0.30, 0.10, 70),
]
for i, (name, b, g, v) in enumerate(scenarios):
    tk.Button(left, text=name, font=FONT_SMALL, bg=CARD_BG, relief="flat",
              cursor="hand2", padx=8, pady=4,
              command=lambda b=b, g=g, v=v: load_scenario(b, g, v)
              ).grid(row=8+i, column=0, columnspan=3, sticky="ew", pady=2)
 
# ── STATS CARDS ───────────────────────────────
tk.Label(left, text="📊  Stats", font=FONT_BOLD, bg=BG).grid(row=13, column=0, columnspan=3, sticky="w", pady=(16,6))
 
def stat_card(parent, row, label, color="#222"):
    tk.Label(parent, text=label, font=FONT_SMALL, bg=CARD_BG, fg="#666").grid(row=row, column=0, sticky="w", padx=8, pady=(4,0))
    val = tk.Label(parent, text="—", font=("Segoe UI", 13, "bold"), bg=CARD_BG, fg=color)
    val.grid(row=row+1, column=0, columnspan=3, sticky="w", padx=8, pady=(0,6))
    return val
 
card_frame = tk.Frame(left, bg=CARD_BG, bd=0, relief="flat")
card_frame.grid(row=14, column=0, columnspan=3, sticky="ew", pady=2)
 
tk.Label(card_frame, text="R₀  (β ÷ γ)", font=FONT_SMALL, bg=CARD_BG, fg="#666").grid(row=0, column=0, sticky="w", padx=8, pady=(6,0))
r0_val = tk.Label(card_frame, text="3.00", font=("Segoe UI", 14, "bold"), bg=CARD_BG, fg="#D85A30")
r0_val.grid(row=1, column=0, sticky="w", padx=8, pady=(0,4))
 
tk.Label(card_frame, text="Peak infected", font=FONT_SMALL, bg=CARD_BG, fg="#666").grid(row=2, column=0, sticky="w", padx=8)
peak_val = tk.Label(card_frame, text="—", font=("Segoe UI", 13, "bold"), bg=CARD_BG, fg="#D85A30")
peak_val.grid(row=3, column=0, sticky="w", padx=8, pady=(0,4))
 
tk.Label(card_frame, text="Peak day", font=FONT_SMALL, bg=CARD_BG, fg="#666").grid(row=4, column=0, sticky="w", padx=8)
peakday_val = tk.Label(card_frame, text="—", font=("Segoe UI", 13, "bold"), bg=CARD_BG)
peakday_val.grid(row=5, column=0, sticky="w", padx=8, pady=(0,4))
 
tk.Label(card_frame, text="Total affected", font=FONT_SMALL, bg=CARD_BG, fg="#666").grid(row=6, column=0, sticky="w", padx=8)
total_val = tk.Label(card_frame, text="—", font=("Segoe UI", 13, "bold"), bg=CARD_BG, fg="#639922")
total_val.grid(row=7, column=0, sticky="w", padx=8, pady=(0,8))
 
# ── CHART (right side) ────────────────────────
right = tk.Frame(root, bg=BG)
right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(0,12), pady=12)
 
fig, ax = plt.subplots(figsize=(7, 5))
fig.patch.set_facecolor("#f5f5f0")
ax.set_facecolor("#fafaf7")
 
canvas = FigureCanvasTkAgg(fig, master=right)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
 
# ── FIRST DRAW ────────────────────────────────
update()
root.mainloop()