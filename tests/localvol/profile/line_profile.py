# Description: This file is used to profile the code using line_profiler

from line_profiler import LineProfiler
from finmc.utils.mc import antithetic_normal
from finmc.models.localvol import LVMC
from tests.localvol.examples.option import run_model  # noqa: F401

if __name__ == "__main__":
    # Create a LineProfiler object, specifying the methods to be profiled by line
    lprofiler = LineProfiler(LVMC.step, antithetic_normal)
    # Wrap the entry function with the LineProfiler object, then run it.
    lp_wrapper = lprofiler(run_model)
    lp_wrapper()
    # Print the profiling results in milliseconds
    lprofiler.print_stats(output_unit=1e-03)
