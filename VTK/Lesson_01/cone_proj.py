from vtkmodules.all import *


def esferas_creater(renderer, color, position):
    """
    Cria as esferas e o foco de luz
    """
    light = vtkLight()
    light.SetColor(color)
    light.SetPosition(position)
    light.SetLightTypeToSceneLight()
    renderer.AddLight(light)


    sphere_source = vtkSphereSource()
    sphere_source.SetRadius(0.5)

    sphere_mapper = vtkPolyDataMapper()
    sphere_mapper.SetInputConnection(sphere_source.GetOutputPort())

    sphere_actor = vtkActor()
    sphere_actor.SetMapper(sphere_mapper)
    sphere_actor.SetPosition(position)
    sphere_actor.GetProperty().SetColor(color)
    sphere_actor.GetProperty().LightingOff()  # este comando serv para desligar a iluminacao da esfera, para que ela nao seja afetada pela luz das outras esferas todas

    renderer.AddActor(sphere_actor)


def main():
    colors = vtkNamedColors()

    renderer = vtkRenderer()
    renderer.SetBackground(colors.GetColor3d("Black"))


    esferas_creater(renderer, colors.GetColor3d("Blue"), [5, 0, 0])     
    esferas_creater(renderer, colors.GetColor3d("Yellow"), [0, 0, 5])  
    esferas_creater(renderer, colors.GetColor3d("Red"), [-5, 0, 0])    
    esferas_creater(renderer, colors.GetColor3d("Green"), [0, 0, -5])   
    
    #cone_source = vtkConeSource() 
    cone_source = vtkCylinderSource()
    cone_source.SetRadius(1.0)
    cone_source.SetHeight(2.0)
    cone_source.SetResolution(50)



    cone_mapper = vtkPolyDataMapper()
    cone_mapper.SetInputConnection(cone_source.GetOutputPort())

    cone_actor = vtkActor()
    cone_actor.SetMapper(cone_mapper)
    cone_actor.SetPosition(0, 0, 0) 

    renderer.AddActor(cone_actor)

    render_window = vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(800, 800)
    render_window.SetWindowName("Lighting with Spheres and Cone")

    render_window.Render()
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)
    interactor.Initialize()
    interactor.Start()
    


if __name__ == '__main__':
    main()
