from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np
import locale

#####################################################################
# Modulová kmitočtová charakteristika - výstup linear
#####################################################################

f1 = import_data_column("uloha4.xlsx", "Sheet1", 7, 5, 17)
Au1 = import_data_column("uloha4.xlsx", "Sheet1", 7, 7, 17)

plt.rcParams['text.usetex'] = True
plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f1, Au1, marker = "x", markersize = 10, markeredgewidth=2, label="Lineární korekce")

plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika - výstup linear}", fontsize=18)
plt.ylabel(r"\textbf{Au [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

#####################################################################
# Modulová kmitočtová charakteristika - výstup korekce
#####################################################################

f2 = import_data_column("uloha4.xlsx", "Sheet1", 29, 5, 11)
Au2 = import_data_column("uloha4.xlsx", "Sheet1", 29, 7, 11)
Au3 = import_data_column("uloha4.xlsx", "Sheet1", 29, 9, 11)
Au4 = import_data_column("uloha4.xlsx", "Sheet1", 29, 11, 11)

plt.figure(2, figsize=(11.69, 8.27))

plt.plot(f2, Au2, marker = "x", markersize = 10, markeredgewidth=2, label="80Hz")
plt.plot(f2, Au3, marker = "x", markersize = 10, markeredgewidth=2, label="120Hz")
plt.plot(f2, Au4, marker = "x", markersize = 10, markeredgewidth=2, label="160Hz")

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika - výstup korekce}", fontsize=18)
plt.ylabel(r"\textbf{Au [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")

#####################################################################
# Závislost zesílení subwooferu na nastavení
#####################################################################

Au5 = import_data_column("uloha4.xlsx", "Sheet1", 44, 5, 6)
Au6 = import_data_column("uloha4.xlsx", "Sheet1", 44, 7, 6)

plt.figure(3, figsize=(11.69, 8.27))

plt.plot(Au5, Au6, marker = "x", markersize = 10, markeredgewidth=2, label="Závislost zesílení")

plt.grid(True, which="both")
plt.title(r"\textbf{Závislost zesílení subwooferu na nastavení}", fontsize=18)
plt.ylabel(r"\textbf{Au [dB] - změřeno}", fontsize=16)
plt.xlabel(r"\textbf{Au [dB] - nastaveno}", fontsize=16)

plt.savefig("grafy/graf3.pdf", format="pdf", bbox_inches="tight")

#####################################################################
# Modulová kmitočtová charakteristika - výstup subwoofer
#####################################################################

f3 = import_data_column("uloha4.xlsx", "Sheet1", 60, 5, 10)
Au7 = import_data_column("uloha4.xlsx", "Sheet1", 60, 7, 10)
Au8 = import_data_column("uloha4.xlsx", "Sheet1", 60, 9, 10)
Au9 = import_data_column("uloha4.xlsx", "Sheet1", 60, 11, 10)

plt.figure(4, figsize=(11.69, 8.27))

plt.plot(f3, Au7, marker = "x", markersize = 10, markeredgewidth=2, label="80Hz")
plt.plot(f3, Au8, marker = "x", markersize = 10, markeredgewidth=2, label="120Hz")
plt.plot(f3, Au9, marker = "x", markersize = 10, markeredgewidth=2, label="160Hz")

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika - výstup subwoofer}", fontsize=18)
plt.ylabel(r"\textbf{Au [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

plt.savefig("grafy/graf4.pdf", format="pdf", bbox_inches="tight")