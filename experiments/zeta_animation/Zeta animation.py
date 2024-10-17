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
from zeta_animation import make_faded_colors, plot_complex

jupyter_black.load()

# %%
critical_line = np.array(
    [complex(0.5, t) for t in np.linspace(start=0, stop=200, num=20_000)]
)
zetas = np.array([zeta(z) for z in critical_line])
colors = tuple(
    make_faded_colors(
        base_color="orange",
        fade_steps=1000,
        min_opacity=0.2,
    )
)

# %%
ax, lines = plot_complex(
    values=zetas[:5_000],
    colors=colors,
    background_color="black",
    axis_color="darkgrey",
)
plt.show()

# %%
fig, ax = plt.subplots(facecolor="black")
steps = len(zetas)
artists = (
    plot_complex(
        values=zetas[:i],
        colors=colors,
        background_color="black",
        axis_color="darkgrey",
        ax=ax,
    )[1]
    for i in trange(1, steps + 1, 8)
)
ani = animation.ArtistAnimation(
    fig=fig,
    artists=tuple(artists),
    interval=40,
    blit=True,
    repeat=False,
)
ani.save("movie.mp4", dpi=300)
