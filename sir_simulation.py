import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
 
# ──────────────────────────────────────────────
#  SIR MODEL SIMULATION
#  Virus Spread Simulation using SIR Model
# ──────────────────────────────────────────────
 
def run_simulation(beta, gamma, N, I0, vax_pct, days, label):
    """
    Run a single SIR simulation.
 
    Parameters:
        beta     : transmission rate
        gamma    : recovery rate
        N        : total population
        I0       : initial infected count
        vax_pct  : percentage vaccinated (0-100)
        days     : number of days to simulate
        label    : name for this scenario
    """
    S = N * (1 - vax_pct / 100) - I0
    I = float(I0)
    R = N * (vax_pct / 100)
 
    S_list, I_list, R_list = [], [], []
 
    for day in range(days):
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
 
        new_infected  = beta * S * I / N
        new_recovered = gamma * I
 
        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered
 
    peak_infected = max(I_list)
    peak_day      = I_list.index(peak_infected)
    total_affected = ((N - S_list[-1]) / N) * 100
    R0 = beta / gamma
 
    return {
        "label"         : label,
        "S"             : S_list,
        "I"             : I_list,
        "R"             : R_list,
        "peak_infected" : peak_infected,
        "peak_day"      : peak_day,
        "total_affected": total_affected,
        "R0"            : R0,
    }
 
 
def plot_single(result, days):
    """Plot S, I, R curves for a single scenario."""
    fig, ax = plt.subplots(figsize=(10, 5))
    t = range(days)
 
    ax.plot(t, result["S"], label="Susceptible", color="#378ADD", linewidth=2, linestyle="--")
    ax.plot(t, result["I"], label="Infected",    color="#D85A30", linewidth=2.5)
    ax.plot(t, result["R"], label="Recovered",   color="#639922", linewidth=2, linestyle=":")
 
    ax.axvline(result["peak_day"], color="#D85A30", linestyle="--", alpha=0.4, linewidth=1)
    ax.annotate(
        f"Peak: {int(result['peak_infected'])} on day {result['peak_day']}",
        xy=(result["peak_day"], result["peak_infected"]),
        xytext=(result["peak_day"] + days * 0.04, result["peak_infected"] * 0.92),
        fontsize=9, color="#D85A30",
        arrowprops=dict(arrowstyle="->", color="#D85A30", lw=1)
    )
 
    ax.set_xlabel("Days", fontsize=12)
    ax.set_ylabel("Population", fontsize=12)
    ax.set_title(f"SIR Model — {result['label']}  (R₀ = {result['R0']:.2f})", fontsize=14)
    ax.legend(fontsize=11)
    ax.set_xlim(0, days - 1)
    ax.set_ylim(0)
    ax.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig("sir_single.png", dpi=150)
    print("Saved: sir_single.png")
    plt.show()
 
 
def plot_comparison(results, days):
    """Plot infected curves for multiple scenarios side by side."""
    colors  = ["#888780", "#D85A30", "#378ADD", "#639922"]
    t = range(days)
 
    fig = plt.figure(figsize=(13, 7))
    gs  = gridspec.GridSpec(1, 2, width_ratios=[2, 1], figure=fig)
 
    # Left: line chart
    ax = fig.add_subplot(gs[0])
    for i, res in enumerate(results):
        ax.plot(t, res["I"], label=res["label"], color=colors[i], linewidth=2.5)
        ax.axvline(res["peak_day"], color=colors[i], linestyle="--", alpha=0.3, linewidth=1)
 
    ax.set_xlabel("Days", fontsize=12)
    ax.set_ylabel("Infected population", fontsize=12)
    ax.set_title("Comparison of virus spread strategies", fontsize=14)
    ax.legend(fontsize=11)
    ax.set_xlim(0, days - 1)
    ax.set_ylim(0)
    ax.grid(alpha=0.2)
 
    # Right: summary table
    ax2 = fig.add_subplot(gs[1])
    ax2.axis("off")
    col_labels = ["Scenario", "R₀", "Peak\ninfected", "Peak\nday", "Total\naffected"]
    table_data = [
        [
            res["label"],
            f"{res['R0']:.2f}",
            f"{int(res['peak_infected']):,}",
            str(res["peak_day"]),
            f"{res['total_affected']:.1f}%",
        ]
        for res in results
    ]
    tbl = ax2.table(
        cellText    = table_data,
        colLabels   = col_labels,
        cellLoc     = "center",
        loc         = "center",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1, 1.8)
 
    # Colour header row
    for j in range(len(col_labels)):
        tbl[(0, j)].set_facecolor("#D3D1C7")
        tbl[(0, j)].set_text_props(fontweight="bold")
 
    plt.tight_layout()
    plt.savefig("sir_comparison.png", dpi=150)
    print("Saved: sir_comparison.png")
    plt.show()
 
 
# ──────────────────────────────────────────────
#  SETTINGS  –  change these to run experiments
# ──────────────────────────────────────────────
 
N    = 1000   # total population
I0   = 1      # initial infected
days = 160    # simulation length in days
 
# ── SCENARIO DEFINITIONS ──────────────────────
scenarios = [
    # label           beta   gamma  vax%
    ("No control",    0.30,  0.10,  0   ),
    ("Masks (β×0.5)", 0.15,  0.10,  0   ),
    ("Distancing",    0.10,  0.10,  0   ),
    ("Vaccination 70%",0.30, 0.10,  70  ),
]
 
# ──────────────────────────────────────────────
#  RUN
# ──────────────────────────────────────────────
 
results = []
for label, beta, gamma, vax in scenarios:
    res = run_simulation(beta, gamma, N, I0, vax, days, label)
    results.append(res)
    print(f"[{label}]  R0={res['R0']:.2f}  "
          f"Peak={int(res['peak_infected'])} on day {res['peak_day']}  "
          f"Total affected={res['total_affected']:.1f}%")
 
# Plot baseline alone
plot_single(results[0], days)
 
# Plot all scenarios together
plot_comparison(results, days)