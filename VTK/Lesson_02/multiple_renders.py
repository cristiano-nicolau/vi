from vtkmodules.all import *

def main():
    coneSource = vtkConeSource()
    coneSource.SetResolution(50)
    
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetViewport(0.0, 0.0, 0.5, 1.0)
    ren1.SetBackground(0.1, 0.2, 0.4)

    ren2 = vtkRenderer()
    ren2.AddActor(coneActor)
    ren2.SetViewport(0.5, 0.0, 1.0, 1.0)
    ren2.SetBackground(0.2, 0.3, 0.4)

    ren1.GetActiveCamera().SetPosition(0, 0, 5)
    ren2.GetActiveCamera().SetPosition(0, 0, 5)
    ren2.GetActiveCamera().Azimuth(90)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.AddRenderer(ren2)
    renWin.SetSize(600, 300)
    renWin.SetWindowName('Cone')

    for i in range(0, 360):
        renWin.Render()
        ren1.GetActiveCamera().Azimuth(1)
        ren2.GetActiveCamera().Azimuth(1)

if __name__ == '__main__':
    main()
