from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np

# GRAF 1 - Modulová kmitočtová charakteristika

f = import_data_column("uloha1.xlsx", "Sheet1", 33, 4, 18)
Au1 = import_data_column("uloha1.xlsx", "Sheet1", 33, 6, 18)
Au2 = import_data_column("uloha1.xlsx", "Sheet1", 33, 8, 18)
Au3 = import_data_column("uloha1.xlsx", "Sheet1", 33, 10, 18)
Au4 = import_data_column("uloha1.xlsx", "Sheet1", 33, 12, 18)

f_riaa_breaks = np.array([50.05, 500.5, 2122.0])
riaa_mid_gain_db = Au1[np.argmin(np.abs(np.array(f) - 1000))]

f_asymptote = np.logspace(np.log10(min(f)), np.log10(max(f)), 600)
riaa_asymptote = np.piecewise(
	f_asymptote,
	[
		f_asymptote < f_riaa_breaks[0],
		(f_asymptote >= f_riaa_breaks[0]) & (f_asymptote < f_riaa_breaks[1]),
		(f_asymptote >= f_riaa_breaks[1]) & (f_asymptote < f_riaa_breaks[2]),
		f_asymptote >= f_riaa_breaks[2],
	],
	[
		riaa_mid_gain_db + 20 * np.log10(f_riaa_breaks[1] / f_riaa_breaks[0]),
		lambda freq: riaa_mid_gain_db + 20 * np.log10(f_riaa_breaks[1] / freq),
		riaa_mid_gain_db,
		lambda freq: riaa_mid_gain_db - 20 * np.log10(freq / f_riaa_breaks[2]),
	],
)

plt.rcParams['text.usetex'] = True
plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, Au1, marker = "x", markersize = 10, markeredgewidth=2, label="RIAA")
plt.plot(f, Au2, marker = "x", markersize = 10, markeredgewidth=2, label="Fyziologická korekce")
plt.plot(f, Au3, marker = "x", markersize = 10, markeredgewidth=2, label="Zdůraznění řeči")
plt.plot(f, Au4, marker = "x", markersize = 10, markeredgewidth=2, label="Rock preset")
plt.plot(
	f_asymptote,
	riaa_asymptote,
	linestyle="--",
	linewidth=2,
	color="tab:gray",
	#label="RIAA asymptota",
)

for break_freq in f_riaa_breaks:
	plt.axvline(break_freq, linestyle = "--", color="tab:gray")

plt.text(50.05, -12, r"$f_1 = 50\,\mathrm{Hz}$", color = "black", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))
plt.text(500.5, -12, r"$f_2 = 500\,\mathrm{Hz}$", color = "black", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))
plt.text(2122.0, -12, r"$f_3 = 2.12\,\mathrm{kHz}$", color = "black", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika $A_U = f (U_2 / U_1)$}", fontsize=18)
plt.ylabel(r"\textbf{$\bf{A_U}$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{$\bf{f}$ [Hz]}", fontsize=16)

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

# GRAF 2 - Zkreslení

U1_DP = import_data_column("uloha1.xlsx", "Sheet1", 69, 5, 5)
U1_OZ = import_data_column("uloha1.xlsx", "Sheet1", 74, 5, 5)
THD_DP = import_data_column("uloha1.xlsx", "Sheet1", 69, 9, 5)
THD_OZ = import_data_column("uloha1.xlsx", "Sheet1", 74, 9, 5)

plt.figure(2, figsize=(11.69, 8.27))
plt.plot(U1_DP, THD_DP, marker = "x", markersize = 10, markeredgewidth=2, label="Diskretní Prvky")
plt.plot(U1_OZ, THD_OZ, marker = "x", markersize = 10, markeredgewidth=2, label="Operační Zesilovač")

plt.legend()
plt.grid(True)
plt.title(r"\textbf{Zkreslení $THD+N = f (U_1)$}", fontsize=18)
plt.ylabel(r"\textbf{THD+N [\%]}", fontsize=16)
plt.xlabel(r"\textbf{$\bf{U_1}$ [mV]}", fontsize=16)

plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")