from vtkmodules.all import *

def main():
    planeSource = vtkPlaneSource()
    planeSource.SetOrigin(0.0, 0.0, 0.0)
    planeSource.SetPoint1(10.0, 0.0, 0.0)
    planeSource.SetPoint2(0.0, 10.0, 0.0)
    
    JPGReader = vtkJPEGReader()
    JPGReader.SetFileName("./images/lena.JPG") 
    JPGReader.Update()
    
    texture = vtkTexture()
    texture.SetInputConnection(JPGReader.GetOutputPort())
    
    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(planeSource.GetOutputPort())
    
    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    planeActor.SetTexture(texture)
    
    renderer = vtkRenderer()
    renderer.AddActor(planeActor)
    renderer.SetBackground(0.1, 0.2, 0.4)

    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
