from matplotlib import colors as mcolors, pyplot as plt
from matplotlib.axes import Axes
from typing import Any, Iterable
from matplotlib.lines import Line2D
import numpy as np
import itertools

COLOR_TYPE = str | tuple[float, float, float]


def prepare_axes(
    background_color: COLOR_TYPE | None = None,
    axis_color: COLOR_TYPE | None = None,
    grid: bool = False,
    **fig_kw: Any,
) -> tuple[plt.Figure, Axes]:
    background_color = background_color or fig_kw.get("facecolor")
    background_color = mcolors.to_rgb(background_color) if background_color else None
    axis_color = mcolors.to_rgb(axis_color) if axis_color else None

    fig_kw["facecolor"] = background_color
    fig, ax = plt.subplots(**fig_kw)

    if background_color:
        ax.set_facecolor(background_color)

    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    if axis_color:
        ax.spines["bottom"].set_color(axis_color)
        ax.plot(
            1,
            0,
            color=axis_color,
            marker=">",
            transform=ax.get_yaxis_transform(),
            clip_on=False,
        )
        ax.spines["left"].set_color(axis_color)
        ax.plot(
            0,
            1,
            color=axis_color,
            marker="^",
            transform=ax.get_xaxis_transform(),
            clip_on=False,
        )
        ax.tick_params(
            axis="both",
            bottom=False,
            top=False,
            left=False,
            right=False,
            labelbottom=False,
            labeltop=False,
            labelleft=False,
            labelright=False,
        )

    if grid:
        grid_color = (
            tuple((bc + ac) / 2 for bc, ac in zip(background_color, axis_color))
            if background_color and axis_color
            else None
        )
        ax.grid(True, which="major", axis="both", color=grid_color)

    ax.set_aspect("equal")

    return fig, ax


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
) -> list[Line2D]:
    if ax is None:
        _, ax = prepare_axes()

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

    return artists
