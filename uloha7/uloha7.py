from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np

f = import_data_column("uloha7.xlsx", "Sheet1", 10, 5, 17)
Au1 = import_data_column("uloha7.xlsx", "Sheet1", 10, 8, 17)
Au2 = import_data_column("uloha7.xlsx", "Sheet1", 10, 10, 17)
Au3 = import_data_column("uloha7.xlsx", "Sheet1", 10, 12, 17)

plt.rcParams['text.usetex'] = True
plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, Au1, marker = "x", markersize = 10, markeredgewidth=2)

plt.xscale("log")
plt.grid(True, which="both")
plt.ylabel(r"\textbf{A$_1$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

plt.figure(2, figsize=(11.69, 8.27))

plt.plot(f, Au2, marker = "x", markersize = 10, markeredgewidth=2)

plt.xscale("log")
plt.grid(True, which="both")
plt.ylabel(r"\textbf{A$_2$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")

plt.figure(3, figsize=(11.69, 8.27))

plt.plot(f, Au3, marker = "x", markersize = 10, markeredgewidth=2)

plt.xscale("log")
plt.grid(True, which="both")
plt.ylabel(r"\textbf{A$_3$ [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

plt.savefig("grafy/graf3.pdf", format="pdf", bbox_inches="tight")


U1 = import_data_column("uloha7.xlsx", "Sheet1", 31, 5, 5)
U21 = import_data_column("uloha7.xlsx", "Sheet1", 31, 6, 5)
U22 = import_data_column("uloha7.xlsx", "Sheet1", 31, 7, 5)
U23 = import_data_column("uloha7.xlsx", "Sheet1", 31, 8, 5)

plt.figure(4, figsize=(11.69, 8.27))
plt.plot(U1, U21, marker = "x", markersize = 10, markeredgewidth=2)
plt.grid(True, which="both")
plt.ylabel(r"\textbf{U$_{21}$ [mV]}", fontsize=16)
plt.xlabel(r"\textbf{U$_1$ [mV]}", fontsize=16)
plt.savefig("grafy/graf4.pdf", format="pdf", bbox_inches="tight")

plt.figure(5, figsize=(11.69, 8.27))
plt.plot(U1, U22, marker = "x", markersize = 10, markeredgewidth=2)
plt.grid(True, which="both")
plt.ylabel(r"\textbf{U$_{22}$ [mV]}", fontsize=16)
plt.xlabel(r"\textbf{U$_1$ [mV]}", fontsize=16)
plt.savefig("grafy/graf5.pdf", format="pdf", bbox_inches="tight")

plt.figure(6, figsize=(11.69, 8.27))
plt.plot(U1, U23, marker = "x", markersize = 10, markeredgewidth=2)
plt.grid(True, which="both")
plt.ylabel(r"\textbf{U$_{23}$ [mV]}", fontsize=16)
plt.xlabel(r"\textbf{U$_1$ [mV]}", fontsize=16)
plt.savefig("grafy/graf6.pdf", format="pdf", bbox_inches="tight")