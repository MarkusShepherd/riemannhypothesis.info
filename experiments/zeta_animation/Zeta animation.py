# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import jupyter_black
import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from mpmath import zeta

jupyter_black.load()

# %%
zs = np.array([complex(0.5, t) for t in np.linspace(start=0, stop=50, num=10_000)])
ys = np.array([zeta(z) for z in zs])

# %%
coordxs = np.array([y.real for y in ys])
coordys = np.array([y.imag for y in ys])

# %%
plt.figure(facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")
ax.spines["left"].set_position("zero")
ax.spines["left"].set_color("darkgrey")
ax.tick_params(axis="x", colors="darkgrey")
ax.spines["bottom"].set_position("zero")
ax.spines["bottom"].set_color("darkgrey")
ax.tick_params(axis="y", colors="darkgrey")
plt.plot(coordxs, coordys, color=matplotlib.colors.to_rgba("orange", alpha=0.1))
