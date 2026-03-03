from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np
import locale

#####################################################################
# Modulová kmitočtová charakteristika zesilovače
#####################################################################

f = import_data_column("uloha3.xlsx", "Sheet1", 6, 4, 20)
Au = import_data_column("uloha3.xlsx", "Sheet1", 6, 6, 20)

plt.rcParams['text.usetex'] = True
plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, Au, marker = "x", markersize = 10, markeredgewidth=2, label="Lineární korekce")

plt.xscale("log")
plt.axhline(max(Au) - 3, linestyle = "--", color="tab:orange")
plt.axvline(10, linestyle = "--", color="tab:orange")
plt.axvline(52500, linestyle = "--", color="tab:orange")
plt.text(10, -15, "$f_d = 10$ Hz", color = "tab:orange", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:orange"))
plt.text(52500, -15, "$f_h = 52500$ Hz", color = "tab:orange", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:orange"))
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika zesilovače}", fontsize=18)
plt.ylabel(r"\textbf{$A_U$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{$f$ [Hz]}", fontsize=16)

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

#####################################################################
# Měření harmonického zkreslení zesilovače
#####################################################################

p2 = import_data_column("uloha3.xlsx", "Sheet1", 62, 5, 20)
k2 = import_data_column("uloha3.xlsx", "Sheet1", 62, 6, 20)
k3 = import_data_column("uloha3.xlsx", "Sheet1", 62, 7, 20)
thdn = import_data_column("uloha3.xlsx", "Sheet1", 62, 8, 20)

plt.figure(2, figsize=(11.69, 8.27))

plt.plot(p2, k2, marker = "x", markersize = 10, markeredgewidth=2, label="$k_2$")
plt.plot(p2, k3, marker = "x", markersize = 10, markeredgewidth=2, label="$k_3$")
plt.plot(p2, thdn, marker = "x", markersize = 10, markeredgewidth=2, label="$THD+N$")

plt.legend()
plt.grid(True, which="both")
plt.title(r"\textbf{Měření harmonického zkreslení zesilovače}", fontsize=18)
plt.ylabel(r"\textbf{$THD+N, k_2, k_3$ [\%]}", fontsize=16)
plt.xlabel(r"\textbf{$P_2$ [W]}", fontsize=16)


plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")