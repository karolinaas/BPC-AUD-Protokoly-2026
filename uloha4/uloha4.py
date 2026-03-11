from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np
import locale


def find_cutoff_frequency(freq, gain):
	"""Find max-3 dB crossing using linear interpolation between measured points."""
	threshold = max(gain) - 3

	for i in range(len(freq) - 1):
		y1, y2 = gain[i], gain[i + 1]
		if (y1 >= threshold and y2 <= threshold) or (y1 <= threshold and y2 >= threshold):
			if y2 == y1:
				return freq[i], threshold
			ratio = (threshold - y1) / (y2 - y1)
			cutoff = freq[i] + ratio * (freq[i + 1] - freq[i])
			return cutoff, threshold

	# Fallback when the threshold is not crossed exactly in measured range.
	nearest_idx = int(np.argmin(np.abs(np.array(gain) - threshold)))
	return freq[nearest_idx], threshold

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

line_80, = plt.plot(f2, Au2, marker = "x", markersize = 10, markeredgewidth=2, label=r"$f_m$ = 80\,Hz")
line_120, = plt.plot(f2, Au3, marker = "x", markersize = 10, markeredgewidth=2, label=r"$f_m$ = 120\,Hz")
line_160, = plt.plot(f2, Au4, marker = "x", markersize = 10, markeredgewidth=2, label=r"$f_m$ = 160\,Hz")

cutoff_80, _ = find_cutoff_frequency(f2, Au2)
cutoff_120, _ = find_cutoff_frequency(f2, Au3)
cutoff_160, _ = find_cutoff_frequency(f2, Au4)

plt.axvline(cutoff_80, linestyle = "--", color=line_80.get_color())
plt.axvline(cutoff_120, linestyle = "--", color=line_120.get_color())
plt.axvline(cutoff_160, linestyle = "--", color=line_160.get_color())
plt.text(cutoff_80, -70, f"$f_m = {cutoff_80:.1f}$ Hz", color = line_80.get_color(), horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = line_80.get_color()))
plt.text(cutoff_120, -70, f"$f_m = {cutoff_120:.1f}$ Hz", color = line_120.get_color(), horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = line_120.get_color()))
plt.text(cutoff_160, -65, f"$f_m = {cutoff_160:.1f}$ Hz", color = line_160.get_color(), horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = line_160.get_color()))

plt.axline([f2[0], Au2[0]], slope=63, linestyle="--", color="tab:gray")
plt.text(15, -47, "+63 dB/dek",rotation=45, color = "tab:gray", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))
plt.axline([f2[1], Au4[1]], slope=60, linestyle="--", color="tab:gray")
plt.text(23, -57, "+60 dB/dek",rotation=45, color = "tab:gray", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))

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

plt.xticks(np.arange(-6, 10, 3))
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

line_sw_80, = plt.plot(f3, Au7, marker = "x", markersize = 10, markeredgewidth=2, label=r"$f_m$ = 80\,Hz")
line_sw_120, = plt.plot(f3, Au8, marker = "x", markersize = 10, markeredgewidth=2, label=r"$f_m$ = 120\,Hz")
line_sw_160, = plt.plot(f3, Au9, marker = "x", markersize = 10, markeredgewidth=2, label=r"$f_m$ = 160\,Hz")

cutoff_sw_80, _ = find_cutoff_frequency(f3, Au7)
cutoff_sw_120, _ = find_cutoff_frequency(f3, Au8)
cutoff_sw_160, _ = find_cutoff_frequency(f3, Au9)

plt.axvline(cutoff_sw_80, linestyle = "--", color=line_sw_80.get_color())
plt.axvline(cutoff_sw_120, linestyle = "--", color=line_sw_120.get_color())
plt.axvline(cutoff_sw_160, linestyle = "--", color=line_sw_160.get_color())
plt.text(cutoff_sw_80, -35, f"$f_m = {cutoff_sw_80:.1f}$ Hz", color = line_sw_80.get_color(), horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = line_sw_80.get_color()))
plt.text(cutoff_sw_120, -33, f"$f_m = {cutoff_sw_120:.1f}$ Hz", color = line_sw_120.get_color(), horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = line_sw_120.get_color()))
plt.text(cutoff_sw_160, -31, f"$f_m = {cutoff_sw_160:.1f}$ Hz", color = line_sw_160.get_color(), horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = line_sw_160.get_color()))

plt.axline([f3[-1], Au7[-1]], slope=-58, linestyle="--", color="tab:gray")
plt.text(250, -30, "-58 dB/dek",rotation=-58, color = "tab:gray", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))
plt.axline([f3[-1], Au8[-1]], slope=-56, linestyle="--", color="tab:gray")
plt.text(250, -20, "-56 dB/dek",rotation=-56, color = "tab:gray", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))
plt.axline([f3[-1], Au9[-1]], slope=-54, linestyle="--", color="tab:gray")
plt.text(250, -11, "-54 dB/dek",rotation=-54, color = "tab:gray", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor ="tab:gray"))

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika - výstup subwoofer}", fontsize=18)
plt.ylabel(r"\textbf{Au [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

plt.savefig("grafy/graf4.pdf", format="pdf", bbox_inches="tight")