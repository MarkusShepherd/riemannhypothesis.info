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
import numpy as np
from mpmath import zeta
from zeta_animation import make_faded_colors, plot_complex

jupyter_black.load()

# %%
critical_line = np.array(
    [complex(0.5, t) for t in np.linspace(start=0, stop=200, num=20_000)]
)
zetas = np.array([zeta(z) for z in critical_line])

# %%
colors = make_faded_colors(
    base_color="orange",
    fade_steps=300,
    min_opacity=0.2,
)
plot_complex(
    values=zetas[:5_000],
    colors=colors,
    background_color="black",
    axis_color="darkgrey",
)
