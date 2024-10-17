from matplotlib import colors as mcolors, pyplot as plt
from matplotlib.axes import Axes
from typing import Iterable
from matplotlib.lines import Line2D
import numpy as np
import itertools


def make_faded_colors(
    base_color: str | tuple[float, float, float],
    fade_steps: int,
    min_opacity: float = 0.0,
) -> Iterable[tuple[float, float, float]]:
    base_color_rgb = np.array(mcolors.to_rgb(base_color))
    return (
        tuple(base_color_rgb * factor)
        for factor in np.linspace(min_opacity, 1, fade_steps)
    )


def _plot_line_segment(
    values: Iterable[complex],
    color: str | tuple[float, float, float],
    ax: Axes,
) -> list[Line2D]:
    values = tuple(values)
    return ax.plot([z.real for z in values], [z.imag for z in values], color=color)


def plot_complex(
    values: Iterable[complex],
    colors: Iterable[str | tuple[float, float, float]],
    ax: Axes | None = None,
    background_color: str | None = None,
    axis_color: str | None = None,
    figsize: tuple[int, int] | None = None,
) -> tuple[Axes, list[Line2D]]:
    if ax is None:
        _, ax = plt.subplots(figsize=figsize, facecolor=background_color)

    if background_color:
        ax.set_facecolor(background_color)

    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")

    if axis_color:
        ax.spines["bottom"].set_color(axis_color)
        ax.tick_params(axis="x", colors=axis_color)
        ax.spines["left"].set_color(axis_color)
        ax.tick_params(axis="y", colors=axis_color)

    values = tuple(values)
    colors = tuple(colors)

    non_faded_values = values[: -len(colors) + 1]
    faded_values = values[-len(colors) :]
    pairs = itertools.pairwise(faded_values)
    num_fades_pairs = len(faded_values) - 1

    artists = []

    if non_faded_values:
        artists.extend(_plot_line_segment(non_faded_values, colors[0], ax))

    for pair, color in zip(
        pairs,
        colors[-num_fades_pairs:],
    ):
        artists.extend(_plot_line_segment(pair, color, ax))

    return ax, artists
