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
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika $A_U = f (U_2 / U_1)$}", fontsize=18)
plt.ylabel(r"\textbf{$A_U$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{$f$ [Hz]}", fontsize=16)

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

#####################################################################
# Měření harmonického zkreslení zesilovače
#####################################################################

p2 = import_data_column("uloha3.xlsx", "Sheet1", 62, 5, 5)
k2 = import_data_column("uloha3.xlsx", "Sheet1", 62, 6, 20)
k3 = import_data_column("uloha3.xlsx", "Sheet1", 62, 7, 20)
thdn = import_data_column("uloha3.xlsx", "Sheet1", 62, 8, 20)

plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, Au, marker = "x", markersize = 10, markeredgewidth=2, label="Lineární korekce")
