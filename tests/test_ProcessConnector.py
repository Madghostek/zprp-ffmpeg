from zprp_ffmpeg.FilterGraph import FilterGraph
from zprp_ffmpeg.ProcessConnector import ProcessConnector


# broken on windows
def test_ProcessConnector_empty_graph():
    fg = FilterGraph()
    ProcessConnector.run(fg)
