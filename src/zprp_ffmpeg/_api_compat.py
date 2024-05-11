"""compatibility layer to match the kkroening library.
@TODO: better docstrings"""

from typing import Tuple

from zprp_ffmpeg.BaseConnector import BaseConnector

from .FilterGraph import SinkFilter
from .FilterGraph import SourceFilter
from .FilterGraph import Stream
from .generated_filters import extension_method
from .ProcessConnector import ProcessConnector


# this one is unique, creates the Stream object
@extension_method
def input(filename: str):
    source = SourceFilter(filename)
    return Stream().append(source)


@extension_method
def output(stream: Stream, filename: str):
    sink = SinkFilter(filename)
    stream.append(sink)
    return stream


# this api always uses process
@extension_method
def run(stream: Stream, extra_options: str) -> Tuple[str, str]:
    """Returns (stdout,stderr) tuple"""
    return ProcessConnector.run(stream, extra_options).communicate()


# this api always uses process
@extension_method
def run_async(stream: Stream) -> BaseConnector:
    """Returns handle to a process. Can raise an exception if script tries to terminate before ffmpeg is done."""
    return ProcessConnector.run(stream)
