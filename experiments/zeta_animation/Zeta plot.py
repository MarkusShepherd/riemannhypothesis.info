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
from mpmath import zeta
from zeta_animation import plot_complex_function

jupyter_black.load()

# %%
_, _ = plot_complex_function(
    function=zeta,
    z_start=0.5,
    z_end=0.5 + 50j,
    background_color="black",
    axis_color="darkgrey",
    plot_steps=5_000,
    fade_steps=2_000,
    line_base_color="orange",
    min_opacity=0.2,
    width=3840,
    height=2160,
    dpi=100,
    out_path=("zeta_50.png", "zeta_50.svg"),
    show=True,
)
