from pathlib import Path
from matplotlib import animation as manimation, colors as mcolors, pyplot as plt
from matplotlib.axes import Axes
from typing import Any, Callable, Iterable
from matplotlib.lines import Line2D
from tqdm import tqdm
import numpy as np
import itertools

COLOR_TYPE = str | tuple[float, float, float]
PATH_LIKE = str | Path


def prepare_axes(
    *,
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
    *,
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
    *,
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


def plot_complex_function(
    *,
    function: Callable[[complex], complex],
    z_start: complex,
    z_end: complex,
    background_color: COLOR_TYPE,
    axis_color: COLOR_TYPE,
    plot_steps: int,
    fade_steps: int,
    line_base_color: COLOR_TYPE,
    min_opacity: float = 0.0,
    width: int,
    height: int,
    dpi: int = 100,
    out_path: PATH_LIKE | Iterable[PATH_LIKE] | None = None,
    show: bool = False,
) -> tuple[plt.Figure, Axes]:
    fig, ax = prepare_axes(
        background_color=background_color,
        axis_color=axis_color,
        grid=False,
        figsize=(width / dpi, height / dpi),
        dpi=dpi,
    )

    values = (
        function(z) for z in np.linspace(start=z_start, stop=z_end, num=plot_steps)
    )
    colors = make_faded_colors(
        base_color=line_base_color,
        fade_steps=fade_steps,
        min_opacity=min_opacity,
    )

    plot_complex(values=values, colors=colors, ax=ax)
    fig.tight_layout()

    if out_path is not None:
        out_paths = (out_path,) if isinstance(out_path, PATH_LIKE) else out_path
        for path in out_paths:
            fig.savefig(path, dpi=dpi)

    if show:
        plt.show()

    return fig, ax


def animate_complex_function(
    *,
    function: Callable[[complex], complex],
    z_start: complex,
    z_end: complex,
    background_color: COLOR_TYPE,
    axis_color: COLOR_TYPE,
    plot_steps: int,
    fade_steps: int,
    line_base_color: COLOR_TYPE,
    min_opacity: float = 0.0,
    width: int,
    height: int,
    dpi: int = 100,
    duration_s: float,
    fps: int = 24,
    out_path: PATH_LIKE,
):
    fig, ax = prepare_axes(
        background_color=background_color,
        axis_color=axis_color,
        grid=False,
        figsize=(width / dpi, height / dpi),
        dpi=dpi,
    )

    values = tuple(
        tqdm(
            iterable=(
                function(z)
                for z in np.linspace(start=z_start, stop=z_end, num=plot_steps)
            ),
            total=plot_steps,
            desc="Calculating function values",
        )
    )
    colors = tuple(
        make_faded_colors(
            base_color=line_base_color,
            fade_steps=fade_steps,
            min_opacity=min_opacity,
        )
    )
    num_frames = int(duration_s * fps)

    x_min, x_max = min(z.real for z in values), max(z.real for z in values)
    ax.set_xlim(float(x_min), float(x_max))
    y_min, y_max = min(z.imag for z in values), max(z.imag for z in values)
    ax.set_ylim(float(y_min), float(y_max))
    fig.tight_layout()

    writer = manimation.FFMpegWriter(fps=fps, codec="libx264", bitrate=35_000)
    with writer.saving(fig=fig, outfile=out_path, dpi=dpi):
        for i in tqdm(
            iterable=np.linspace(1, len(values) + 1, num_frames, dtype=int),
            total=num_frames,
            desc="Rendering frames",
        ):
            plot_complex(values=values[:i], colors=colors, ax=ax)
            writer.grab_frame()

    plt.close(fig)
