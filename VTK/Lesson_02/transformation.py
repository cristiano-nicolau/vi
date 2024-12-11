from vtkmodules.all import *

def create_textured_plane(rotation, translation, texture_image):
    plane = vtkPlaneSource()
    plane.SetOrigin(0.0, 0.0, 0.0)
    plane.SetPoint1(1.0, 0.0, 0.0)
    plane.SetPoint2(0.0, 1.0, 0.0)

    transform = vtkTransform()
    transform.RotateX(rotation[0])
    transform.RotateY(rotation[1])
    transform.RotateZ(rotation[2])
    transform.Translate(translation)

    transform_filter = vtkTransformPolyDataFilter()
    transform_filter.SetTransform(transform)
    transform_filter.SetInputConnection(plane.GetOutputPort())

    reader = vtkJPEGReader()
    reader.SetFileName(texture_image)
    texture = vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(transform_filter.GetOutputPort())
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetTexture(texture)

    return actor

def main():
    renderer = vtkRenderer()
    render_window = vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(render_window)

    rotations = [
        (0, 0, 0),
        (0, 0, 0),
        (0, 90, 0),
        (0, -90, 0),
        (90, 0, 0),
        (-90, 0, 0)
    ]
    translations = [
        (0, 0, 0.5),
        (0, 0, -0.5),
        (-0.5, 0, 1),
        (-0.5, 0, 0),
        (0, -0.5, -1),
        (0, -0.5, 0)
    ]

    textures = ["./images/Im1.jpg", "./images/Im6.jpg","./images/Im2.jpg", "./images/Im3.jpg", "./images/Im4.jpg", "./images/Im5.jpg"]

    for rotation, translation, texture in zip(rotations, translations, textures):
        actor = create_textured_plane(rotation, translation, texture)
        renderer.AddActor(actor)

    renderer.SetBackground(0.1, 0.2, 0.4)
    render_window.SetSize(800, 800)
    render_window.Render()

    camera = renderer.GetActiveCamera()
    camera.SetPosition(5, 5, 5)
    camera.SetFocalPoint(0, 0, 0)

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
