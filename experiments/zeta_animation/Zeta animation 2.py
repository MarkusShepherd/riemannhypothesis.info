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
from matplotlib import animation, pyplot as plt
from mpmath import zeta
from tqdm import trange
from zeta_animation import make_faded_colors, plot_complex, prepare_axes

jupyter_black.load()

# %%
critical_line = np.array(
    [complex(0.5, t) for t in np.linspace(start=0, stop=200, num=20_000)]
)
zetas = np.array([zeta(z) for z in critical_line])
colors = tuple(
    make_faded_colors(
        base_color="orange",
        fade_steps=2000,
        min_opacity=0.1,
    )
)

# %%
fig, ax = prepare_axes(
    background_color="black",
    axis_color="darkgrey",
    grid=False,
    figsize=(38.4, 21.6),
    dpi=100,
)
steps = len(zetas)
artists = (
    plot_complex(values=zetas[:i], colors=colors, ax=ax)
    for i in trange(1, steps + 1, 8)
)
ani = animation.ArtistAnimation(
    fig=fig,
    artists=tuple(artists),
    interval=40,
    blit=True,
    repeat=False,
)
ani.save("zeta.mp4")
