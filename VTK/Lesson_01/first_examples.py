# Imports
from vtkmodules.all import *

def main():
    # Criar o cone e definir suas propriedades
    coneSource = vtkConeSource()
    coneSource.SetHeight(2)  # Altura do cone
    coneSource.SetRadius(1)  # Raio do cone
    coneSource.SetResolution(50)  # Definir a resolução do cone

    # Mapper e Actor para o cone
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.SetPosition(-5 , 0, 0)  # Posicionar o cone à esquerda

    # Criar a esfera e definir suas propriedades
    sphereSource = vtkSphereSource()
    sphereSource.SetRadius(2)  # Raio da esfera
    sphereSource.SetThetaResolution(50)  # Resolução para theta
    sphereSource.SetPhiResolution(50)    # Resolução para phi

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.SetPosition(0, 0, 0)  # Posicionar a esfera no centro

    # Criar o cilindro e definir suas propriedades
    cylinderSource = vtkCylinderSource()
    cylinderSource.SetRadius(2)  # Raio do cilindro
    cylinderSource.SetHeight(3)  # Altura do cilindro
    cylinderSource.SetResolution(50)  # Definir a resolução do cilindro

    cylinderMapper = vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinderSource.GetOutputPort())

    cylinderActor = vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.SetPosition(5, 0, 0)  # Posicionar o cilindro à direita

    # Criar o Renderer e adicionar todos os atores
    ren = vtkRenderer()
    ren.AddActor(coneActor)  # Adicionar o cone
    ren.AddActor(sphereActor)  # Adicionar a esfera
    ren.AddActor(cylinderActor)  # Adicionar o cilindro
    ren.SetBackground(1.0, 1.0, 1.0)  # Definir o fundo como branco

    # Criar a janela de renderização
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('Cone, Esfera e Cilindro Lado a Lado')
    renWin.SetSize(900, 600)  # Definir o tamanho da janela para 900x600

    # Criar o interator de renderização
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Renderizar a cena
    renWin.Render()

    # Iniciar o interator para interação com a cena
    iren.Start()

if __name__ == '__main__':
    main()
