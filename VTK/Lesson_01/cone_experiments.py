###############################################################################
#       						Cone.py
###############################################################################

# This example creates a polygonal model of a Cone e visualize the results in a
# VTK render window.
# The program creates the cone, rotates it 360º and closes
# The pipeline  source -> mapper -> actor -> renderer  is typical 
# and can be found in most VTK programs

# Imports

# Import all VTK modules
from vtkmodules.all import *

# Import only needed modules
# import vtkmodules.vtkInteractionStyle
# import vtkmodules.vtkRenderingOpenGL2
# from vtkmodules.vtkFiltersSources import vtkConeSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )

def main():

    # We Create an instance of vtkConeSource and set some of its
    # properties. The instance of vtkConeSource "cone" is part of a
    # visualization pipeline (it is a source process object); it produces data
    # (output type is vtkPolyData) which other filters may process.
    
    coneSource = vtkConeSource()
    
    # We create an instance of vtkPolyDataMapper to map the polygonal data
    # into graphics primitives. We connect the output of the cone source 
    # to the input of this mapper.
  
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection( coneSource.GetOutputPort() )

    # We create an actor to represent the cone. The actor orchestrates rendering
    # of the mapper's graphics primitives. An actor also refers to properties
    # via a vtkProperty instance, and includes an internal transformation
    # matrix. We set this actor's mapper to be coneMapper which we created
    # above.
  
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    # TODO: Add to Report
    coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)

    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()
    ren.AddActor( coneActor )


    # TODO: Add to Report
    cam1 = vtkCamera()
    cam1.SetPosition(10,0,0)
    cam1.SetViewUp(0,1,0)
    ren.SetActiveCamera(cam1)

    # TODO: Add to Report
    cam1 = ren.GetActiveCamera()
    light = vtkLight()
    light.SetColor(1,0,0)
    light.SetFocalPoint(cam1.GetFocalPoint())
    light.SetPosition(cam1.GetPosition())
    ren.AddLight(light)

    
    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetWindowName('Cone')


    # TODO: Add to Report
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

    


if __name__ == '__main__':
    main()