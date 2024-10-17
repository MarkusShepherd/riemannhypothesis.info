from matplotlib import colors as mcolors, pyplot as plt
from matplotlib.axes import Axes
from typing import Iterable
from matplotlib.lines import Line2D
import numpy as np
import itertools

COLOR_TYPE = str | tuple[float, float, float]


def make_faded_colors(
    base_color: COLOR_TYPE,
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
    color: COLOR_TYPE,
    ax: Axes,
) -> list[Line2D]:
    values = tuple(values)
    return ax.plot([z.real for z in values], [z.imag for z in values], color=color)


def plot_complex(
    values: Iterable[complex],
    colors: Iterable[COLOR_TYPE],
    ax: Axes | None = None,
    background_color: COLOR_TYPE | None = None,
    axis_color: COLOR_TYPE | None = None,
    figsize: tuple[int, int] | None = None,
) -> tuple[Axes, list[Line2D]]:
    background_color = mcolors.to_rgb(background_color) if background_color else None
    axis_color = mcolors.to_rgb(axis_color) if axis_color else None

    if ax is None:
        _, ax = plt.subplots(figsize=figsize, facecolor=background_color)

    if background_color:
        ax.set_facecolor(background_color)
        if axis_color:
            # Blend background color with axis color
            grid_color = tuple(
                (bc + ac) / 2 for bc, ac in zip(background_color, axis_color)
            )
            ax.grid(True, which="both", axis="both", color=grid_color)

    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    if axis_color:
        ax.spines["bottom"].set_color(axis_color)
        ax.tick_params(axis="x", colors=axis_color, direction="inout")
        ax.spines["left"].set_color(axis_color)
        ax.tick_params(axis="y", colors=axis_color, direction="inout")
        ax.plot(
            1,
            0,
            color=axis_color,
            marker=">",
            transform=ax.get_yaxis_transform(),
            clip_on=False,
        )
        ax.plot(
            0,
            1,
            color=axis_color,
            marker="^",
            transform=ax.get_xaxis_transform(),
            clip_on=False,
        )

    ax.set_aspect("equal")

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
