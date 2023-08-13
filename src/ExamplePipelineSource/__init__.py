from ovito.data import DataCollection
from ovito.pipeline import PipelineSourceInterface
from traits.api import Range, observe
import math

class ExamplePipelineSource(PipelineSourceInterface):

    # Parameter controlling the animation length (value can be changed by the user):
    duration = Range(low=1, value=40)

    def compute_trajectory_length(self, **kwargs):
        return self.duration

    # This is needed to notify the pipeline system whenever the duration is changed by the user:
    @observe("duration")
    def anim_duration_changed(self, event):
        self.notify_trajectory_length_changed()

    def create(self, data: DataCollection, *, frame: int, **kwargs):
        size = 8.0 + math.cos(frame / self.duration * math.pi * 2)
        cell_matrix = [
            [size,0,0,-size/2],
            [0,size,0,-size/2],
            [0,0,size,-size/2]
        ]
        data.create_cell(cell_matrix, pbc=(False, False, False))
