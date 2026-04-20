from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np

f = import_data_column("uloha8.xlsx", "Sheet1", 7, 5, 31)
Au = import_data_column("uloha8.xlsx", "Sheet1", 7, 7, 31)
u1 = import_data_column("uloha8.xlsx", "Sheet1", 52, 5, 9)
u2L = import_data_column("uloha8.xlsx", "Sheet1", 52, 6, 9)
u2R = import_data_column("uloha8.xlsx", "Sheet1", 52, 7, 9)
THD = import_data_column("uloha8.xlsx", "Sheet1", 73, 6, 6)

# GRAF 1 - Modulová kmitočtová charakteristika

plt.rcParams['text.usetex'] = True
plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, Au, marker = "x", markersize = 10, markeredgewidth=2)

plt.xscale("log")
plt.grid(True, which="both")
plt.ylabel(r"\textbf{$\bf{A_U}$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{$\bf{f}$ [Hz]}", fontsize=16)
plt.title(r"\textbf{Modulová kmitočtová charakteristika zesilovače $\bf{A_{U}=f(U_2 / U_1)}$}", fontsize=18)

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

# GRAF 2 - Linearita D/A převodníku

plt.figure(2, figsize=(11.69, 8.27))

plt.plot(u1, u2L, marker = "x", markersize = 10, markeredgewidth=2, label="Levý kanál")
plt.plot(u1, u2R, marker = "x", markersize = 10, markeredgewidth=2, label="Pravý kanál")
plt.grid(True, which="both")
plt.ylabel(r"$\bf{U_2\ [dB]}$", fontsize=16)
plt.xlabel(r"$\bf{U_1\ [dB]}$", fontsize=16)
plt.title(r"\textbf{Linearita D/A převodníku $\bf{U_2=f(U_1)}$}", fontsize=18)
plt.legend()

plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")

# GRAF 3 - Závislost THD na vstupním napětí

plt.figure(3, figsize=(11.69, 8.27))

plt.plot(u1[:len(THD)], THD, marker = "x", markersize = 10, markeredgewidth=2)
plt.grid(True, which="both")
plt.ylabel(r"$\bf{THD\ [}$\textbf{\%}$\bf{]}$", fontsize=16)
plt.xlabel(r"$\bf{U_1\ [dB]}$", fontsize=16)
plt.title(r"\textbf{Závislost THD na vstupním napětí $\bf{THD=f(U_1)}$}", fontsize=18)
plt.gca().invert_xaxis() # Otočit osu x, aby vyšší napětí bylo vlevo

plt.savefig("grafy/graf3.pdf", format="pdf", bbox_inches="tight")
