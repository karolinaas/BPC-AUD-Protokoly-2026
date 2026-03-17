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

####################################################################
# Modulová kmitočtová charakteristika
#####################################################################

f = import_data_column("uloha5.xlsx", "Sheet1", 4, 3, 15)
Au = import_data_column("uloha5.xlsx", "Sheet1", 4, 6, 15)

plt.rcParams['text.usetex'] = True
plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, Au, marker = "x", markersize = 10, markeredgewidth=2, label="Lineární korekce")

plt.xscale("log")
plt.grid(True, which="both")
plt.title(r"\textbf{Modulová kmitočtová charakteristika zesilovače Au=f(f)}", fontsize=18)
plt.ylabel(r"\textbf{Au [dB]}", fontsize=16)
plt.xlabel(r"\textbf{f [Hz]}", fontsize=16)

cutoff, _ = find_cutoff_frequency(f, Au)

plt.axvline(cutoff, linestyle="--")

plt.text(cutoff, 11, f"$f_h = {cutoff:.1f}$ Hz", color="tab:blue", horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = "tab:blue"))


plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")
	