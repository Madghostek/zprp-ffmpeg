import shlex
import subprocess

from .BaseConnector import BaseConnector
from .FilterGraph import Stream


class ProcessConnector(BaseConnector):

    # @TODO: this isn't ideal because attacker can sideload malicious executable...
    # Maybe warn user to set this in config for safety?
    ffmpeg_executable_path = "ffmpeg"

    def __init__(self, ffmpeg_process) -> None:
        self.ffmpeg_process: subprocess.Popen = ffmpeg_process
        super().__init__()

    @staticmethod
    def compile(graph: Stream) -> str:
        """
        Builds a command for ffmpeg from FilterGraph

        :param graph: the graph to compile
        :return: a string to pass as an argument to ffmpeg
        """
        # @TODO: implement this once FilterGraph is done
        return "-i input.mp4 -vf hflip -y output.mpt"

    @classmethod
    def run(cls, graph: Stream) -> "BaseConnector":
        """
        Builds a command from FilterGraph, starts ffmpeg process, and passes the command.

        :return: subprocess.Popen instance
        """

        command = ProcessConnector.compile(graph)
        ffmpeg_process = subprocess.Popen([ProcessConnector.ffmpeg_executable_path, *shlex.split(command)])  # noqa: S603
        return cls(ffmpeg_process)

    def communicate(self):
        return self.ffmpeg_process.communicate()
