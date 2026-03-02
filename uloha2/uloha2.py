from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np
import locale

#####################################################################
# Modulová kmitočtová charakteristika měřených korekcí zesilovače
#####################################################################

f = import_data_column("uloha2.xlsx", "Sheet1", 6, 3, 18)
Au1 = import_data_column("uloha2.xlsx", "Sheet1", 6, 5, 18)
Au2 = import_data_column("uloha2.xlsx", "Sheet1", 6, 7, 18)
Au3 = import_data_column("uloha2.xlsx", "Sheet1", 6, 9, 18)

plt.rcParams['text.usetex'] = True
plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, Au1, marker = "x", markersize = 10, markeredgewidth=2, label="Lineární korekce")
plt.plot(f, Au2, marker = "x", markersize = 10, markeredgewidth=2, label="Korekce H+ a V+")
plt.plot(f, Au3, marker = "x", markersize = 10, markeredgewidth=2, label="Korekce H- a V-")

#plt.axhline(3)

plt.axvline(380, linestyle = "--", color="tab:orange", ymax=0.645)
plt.axvline(2600, linestyle = "--", color="tab:orange", ymax=0.645)
plt.text(380, -20, "$f_d = 380$ Hz", color = "tab:orange", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:orange"))
plt.text(2600, -20, "$f_h = 2600$ Hz", color = "tab:orange", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:orange"))

#plt.axhline(-3)

plt.axvline(380, linestyle = "--", color="tab:green", ymax=0.49)
plt.axvline(2450, linestyle = "--", color="tab:green", ymax=0.49)
plt.text(380, -18, "$f_d = 380$ Hz", color = "tab:green", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:green"))
plt.text(2450, -18, "$f_h = 2450$ Hz", color = "tab:green", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:green"))

plt.axline([f[-8], Au3[-8]], slope=-14.5, linestyle="--", color="tab:gray")
plt.axline([f[4], Au2[4]], slope=-17, linestyle="--", color="tab:gray")
plt.text(200, 7.5, "-17 dB/dek",rotation=-49, color = "tab:gray", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))
plt.text(5000, -7.6, "-14.5 dB/dek",rotation=-45, color = "tab:gray", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika $A_U = f (U_2 / U_1)$}", fontsize=18)
plt.ylabel(r"\textbf{$A_U$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{$f$ [Hz]}", fontsize=16)

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

###############################################################
# Modulová kmitočtová charakteristika regulací hlasitosti
###############################################################


f2 = import_data_column("uloha2.xlsx", "Sheet1", 51, 3, 18)
Au4 = import_data_column("uloha2.xlsx", "Sheet1", 51, 5, 18)
Au5 = import_data_column("uloha2.xlsx", "Sheet1", 51, 7, 18)

plt.figure(2, figsize=(11.69, 8.27))

plt.plot(f2, Au4, marker = "x", markersize = 10, markeredgewidth=2, label="Lineární regulace")
plt.plot(f2, Au5, marker = "x", markersize = 10, markeredgewidth=2, label="Loudness")

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika $A_U = f (U_2 / U_1)$}", fontsize=18)
plt.ylabel(r"\textbf{$A_U$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{$f$ [Hz]}", fontsize=16)


plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")
