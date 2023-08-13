#### Example Viewport Overlay ####
# An example for a Python-based viewport layer.

from ovito.vis import *

def example_render_function(args: PythonViewportOverlay.Arguments):
    
    # This demo code prints the current animation frame into the upper left corner of the viewport.
    text1 = f"Frame {args.frame}"
    args.painter.drawText(10, 10 + args.painter.fontMetrics().ascent(), text1)
    
    # Also print the current number of particles into the lower left corner of the viewport.
    pipeline = args.scene.selected_pipeline
    if pipeline:
        data = pipeline.compute(args.frame)
        num_particles = data.particles.count if data.particles else 0
        text2 = f"{num_particles} particles"
        args.painter.drawText(10, args.painter.window().height() - 10, text2)
