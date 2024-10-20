from pathlib import Path
from matplotlib import animation as manimation, colors as mcolors, pyplot as plt
from matplotlib.axes import Axes
from typing import Any, Callable, Iterable
from matplotlib.lines import Line2D
from tqdm import tqdm
import numpy as np
import itertools

COLOR_TYPE = str | tuple[float, float, float] | tuple[float, float, float, float]
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
    **plot_kw: Any,
) -> list[Line2D]:
    values = tuple(values)
    return ax.plot(
        [z.real for z in values],
        [z.imag for z in values],
        color=color,
        **plot_kw,
    )


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


def _pad_tuple(tuple_: tuple, length: int) -> tuple:
    if length <= 0:
        return ()
    if length <= len(tuple_):
        return tuple_[-length:]
    return (tuple_[0],) * (length - len(tuple_)) + tuple_


def _animate_complex_function_infinite_visiblity(
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
) -> None:
    fig, ax = prepare_axes(
        background_color=background_color,
        axis_color=axis_color,
        grid=False,
        figsize=(width / dpi, height / dpi),
        dpi=dpi,
    )
    fig.tight_layout()

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

    lines = [
        _plot_line_segment(
            values=pair,
            color=(0, 0, 0, 0),
            ax=ax,
        )[0]
        for pair in itertools.pairwise(tqdm(values, desc="Plotting lines"))
    ]

    def update(
        frame: int,
        lines: list[Line2D] = lines,
        fade_colors: tuple[tuple[float, float, float], ...] = colors,
    ) -> list[Line2D]:
        lines_to_update = lines[:frame]
        colors_to_update = _pad_tuple(fade_colors, len(lines_to_update))
        for line, color in zip(lines_to_update, colors_to_update):
            line.set_color(color)
        return lines_to_update

    animation = manimation.FuncAnimation(
        fig=fig,
        func=update,
        init_func=lambda: lines,
        frames=np.linspace(1, len(values) + 1, num_frames, dtype=int),
        interval=1_000 / fps,
        blit=True,
    )
    writer = manimation.FFMpegWriter(fps=fps, codec="libx264", bitrate=35_000)
    with tqdm(total=num_frames, desc="Rendering frames") as pbar:
        animation.save(
            out_path,
            writer=writer,
            dpi=dpi,
            progress_callback=lambda *_: pbar.update(1),
        )

    plt.close(fig)


def _animate_complex_function_limited_visibility(
    *,
    function: Callable[[complex], complex],
    z_start: complex,
    z_end: complex,
    background_color: COLOR_TYPE,
    axis_color: COLOR_TYPE,
    plot_steps: int,
    fade_steps: int,
    visible_steps: int,
    line_base_color: COLOR_TYPE,
    min_opacity: float = 0.0,
    width: int,
    height: int,
    dpi: int = 100,
    duration_s: float,
    fps: int = 24,
    out_path: PATH_LIKE,
) -> None:
    fig, ax = prepare_axes(
        background_color=background_color,
        axis_color=axis_color,
        grid=False,
        figsize=(width / dpi, height / dpi),
        dpi=dpi,
    )
    fig.tight_layout()

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
    x_min, x_max = min(z.real for z in values), max(z.real for z in values)
    ax.set_xlim(float(x_min - 0.5), float(x_max + 0.5))
    y_min, y_max = min(z.imag for z in values), max(z.imag for z in values)
    ax.set_ylim(float(y_min - 0.5), float(y_max + 0.5))

    colors = _pad_tuple(
        tuple(
            make_faded_colors(
                base_color=line_base_color,
                fade_steps=fade_steps,
                min_opacity=min_opacity,
            )
        ),
        visible_steps,
    )
    num_frames = int(duration_s * fps)

    lines = [
        _plot_line_segment(
            values=(0 + 0j, 0 + 0j),
            color=color,
            ax=ax,
            visible=False,
        )[0]
        for color in colors
    ]

    def update(
        frame: int,
        lines: list[Line2D] = lines,
        values: tuple[complex, ...] = values,
    ) -> list[Line2D]:
        values_to_update = values[max(0, frame - len(lines) - 1) : frame]
        pairs_to_update = tuple(itertools.pairwise(values_to_update))
        lines_to_update = lines[-len(pairs_to_update) :]
        for line, pair in zip(lines_to_update, pairs_to_update):
            line.set_data([z.real for z in pair], [z.imag for z in pair])
            line.set_visible(True)
        return lines_to_update

    animation = manimation.FuncAnimation(
        fig=fig,
        func=update,
        init_func=lambda: lines,
        frames=np.linspace(1, len(values) + 1, num_frames, dtype=int),
        interval=1_000 / fps,
        blit=True,
    )

    writer = manimation.FFMpegWriter(
        fps=fps,
        codec="libx264",
        bitrate=35_000,
    )

    with tqdm(total=num_frames, desc="Rendering frames") as pbar:
        animation.save(
            out_path,
            writer=writer,
            dpi=dpi,
            progress_callback=lambda *_: pbar.update(1),
        )

    plt.close(fig)


def animate_complex_function(
    *,
    function: Callable[[complex], complex],
    z_start: complex,
    z_end: complex,
    background_color: COLOR_TYPE,
    axis_color: COLOR_TYPE,
    plot_steps: int,
    fade_steps: int,
    visible_steps: int | None = None,
    line_base_color: COLOR_TYPE,
    min_opacity: float = 0.0,
    width: int,
    height: int,
    dpi: int = 100,
    duration_s: float,
    fps: int = 24,
    out_path: PATH_LIKE,
) -> None:
    if visible_steps:
        _animate_complex_function_limited_visibility(
            function=function,
            z_start=z_start,
            z_end=z_end,
            background_color=background_color,
            axis_color=axis_color,
            plot_steps=plot_steps,
            fade_steps=fade_steps,
            visible_steps=visible_steps,
            line_base_color=line_base_color,
            min_opacity=min_opacity,
            width=width,
            height=height,
            dpi=dpi,
            duration_s=duration_s,
            fps=fps,
            out_path=out_path,
        )
    else:
        _animate_complex_function_infinite_visiblity(
            function=function,
            z_start=z_start,
            z_end=z_end,
            background_color=background_color,
            axis_color=axis_color,
            plot_steps=plot_steps,
            fade_steps=fade_steps,
            line_base_color=line_base_color,
            min_opacity=min_opacity,
            width=width,
            height=height,
            dpi=dpi,
            duration_s=duration_s,
            fps=fps,
            out_path=out_path,
        )
