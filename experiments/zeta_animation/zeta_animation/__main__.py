import argparse
import logging
from pathlib import Path
import sys
from mpmath import zeta
from zeta_animation import animate_complex_function

LOGGER = logging.getLogger(__name__)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Animate a complex function")
    parser.add_argument(
        "--function",
        type=str,
        default="zeta",
        help="The name of the function to animate",
    )
    parser.add_argument(
        "--z-start",
        "-s",
        type=complex,
        default=0.5 + 0j,
        help="The start of the complex plane",
    )
    parser.add_argument(
        "--z-end",
        "-e",
        type=complex,
        default=0.5 + 100j,
        help="The end of the complex plane",
    )
    parser.add_argument(
        "--background-color",
        "-b",
        type=str,
        default="black",
        help="The background color of the plot",
    )
    parser.add_argument(
        "--axis-color",
        "-a",
        type=str,
        default="darkgrey",
        help="The color of the axes",
    )
    parser.add_argument(
        "--plot-steps",
        type=int,
        default=10_000,
        help="The number of steps to plot",
    )
    parser.add_argument(
        "--fade-steps",
        type=int,
        default=2_000,
        help="The number of steps to fade the lines",
    )
    parser.add_argument(
        "--visible-steps",
        type=int,
        help="The number of steps to keep the lines visible (default: all)",
    )
    parser.add_argument(
        "--base-color",
        "-c",
        type=str,
        default="orange",
        help="The base color of the lines",
    )
    parser.add_argument(
        "--min-opacity",
        "-o",
        type=float,
        default=0.2,
        help="The minimum opacity of the lines",
    )
    parser.add_argument(
        "--width",
        "-x",
        type=int,
        default=960,
        help="The width of the plot in pixels",
    )
    parser.add_argument(
        "--height",
        "-y",
        type=int,
        default=540,
        help="The height of the plot in pixels",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=100,
        help="The DPI of the plot",
    )
    parser.add_argument(
        "--duration",
        "-d",
        type=float,
        default=100,
        help="The duration of the animation in seconds",
    )
    parser.add_argument(
        "--fps",
        "-f",
        type=int,
        default=24,
        help="The frames per second of the animation",
    )
    parser.add_argument(
        "--out-path",
        type=str,
        help="The path to save the animation",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the output file if it exists",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        help="Enable verbose logging (use -vv for more verbosity)",
    )

    return parser.parse_args()


def main():
    args = _parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )

    if args.function == "zeta":
        function = zeta
    else:
        # TODO: Add more functions
        raise ValueError(f"Unknown function: {args.function}")

    out_path = Path(args.out_path or f"{args.function}_animation.mp4").resolve()

    LOGGER.info(
        "Plotting function %s from %g%+gi to %g%+gi",
        args.function,
        args.z_start.real,
        args.z_start.imag,
        args.z_end.real,
        args.z_end.imag,
    )
    LOGGER.info("Output file: %s", out_path)

    if out_path.exists():
        if args.overwrite:
            LOGGER.info("Overwriting existing file: <%s>", out_path)
        else:
            raise FileExistsError(f"File already exists: {out_path}")

    animate_complex_function(
        function=function,
        z_start=args.z_start,
        z_end=args.z_end,
        background_color=args.background_color,
        axis_color=args.axis_color,
        plot_steps=args.plot_steps,
        fade_steps=args.fade_steps,
        visible_steps=args.visible_steps,
        line_base_color=args.base_color,
        min_opacity=args.min_opacity,
        width=args.width,
        height=args.height,
        dpi=args.dpi,
        duration_s=args.duration,
        fps=args.fps,
        out_path=out_path,
    )


if __name__ == "__main__":
    main()
