from vtkmodules.all import *

def main():
    sphereSource1 = vtkSphereSource()
    sphereSource2 = vtkSphereSource()

    sphereMapper1 = vtkPolyDataMapper()
    sphereMapper1.SetInputConnection(sphereSource1.GetOutputPort())
    
    sphereMapper2 = vtkPolyDataMapper()
    sphereMapper2.SetInputConnection(sphereSource2.GetOutputPort())

    sphereActor1 = vtkActor()
    sphereActor1.SetMapper(sphereMapper1)

    sphereActor2 = vtkActor()
    sphereActor2.SetMapper(sphereMapper2)

    ren1 = vtkRenderer()
    ren1.AddActor(sphereActor1)
    ren1.SetViewport(0.0, 0.0, 0.5, 1.0)
    ren1.SetBackground(0.1, 0.2, 0.4)

    ren2 = vtkRenderer()
    ren2.AddActor(sphereActor2)
    ren2.SetViewport(0.5, 0.0, 1.0, 1.0)
    ren2.SetBackground(0.2, 0.3, 0.4)

    ren2.GetActiveCamera().Azimuth(90)

    ren1.GetActiveCamera().SetPosition(0, 0, 5)
    ren1.GetActiveCamera().SetFocalPoint(0, 0, 0)

    ren2.GetActiveCamera().SetPosition(0, 0, 5)
    ren2.GetActiveCamera().SetFocalPoint(0, 0, 0)

    sphereActor1.GetProperty().SetInterpolationToFlat()
    sphereActor2.GetProperty().SetInterpolationToGouraud()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.AddRenderer(ren2)
    renWin.SetSize(600, 300)
    renWin.SetWindowName('Spheres')

    for i in range(0, 360):
        renWin.Render()
        ren1.GetActiveCamera().Azimuth(1)
        ren2.GetActiveCamera().Azimuth(1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    style = vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)

    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
