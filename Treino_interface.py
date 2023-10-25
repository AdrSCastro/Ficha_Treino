from PySimpleGUI import PySimpleGUI as sg
import random
from reportlab.pdfgen import canvas
from pathlib import Path

# Definir estilos para o documento
titulo_estilo = ('Helvetica-Bold', 16)
cabecalho_estilo = ('Helvetica-Bold', 12)
texto_estilo = ('Helvetica', 9.4)

# Lista de exercícios
treino_biceps = ['Rosca direta c/ barra - 4 x 8-10 repetições', 'Rosca direta c/ halteres - 3 x 10-12 repetições', 'Rosca martelo c/ halteres - 4 x 8-10 repetições', 'Rosca concentrada - 3 x 10-12 repetições',
                 'Rosca scott c/ barra - 4 x 8-10 repetições', 'Rosca scott c/ halteres - 3 x 10-12 repetições', 'Rosca 21 - 4 x 8-10 repetições', 'Rosca inversa c/ barra - 3 x 10-12 repetições',
                 'Rosca inversa c/ halteres - 4 x 8-10 repetições', 'Rosca spider - 3 x 10-12 repetições', 'Rosca concentrada alternada - 4 x 8-10 repetições', 'Rosca martelo alternada - 3 x 10-12 repetições',
                 'Rosca simultânea c/ halteres - 4 x 8-10 repetições', 'Rosca alternada c/ halteres - 3 x 10-12 repetições', 'Rosca cross over - 4 x 8-10 repetições', 'Rosca 21 invertida - 3 x 10-12 repetições',
                 'Rosca scott máquina - 4 x 8-10 repetições', 'Rosca martelo máquina - 3 x 10-12 repetições', 'Rosca direta polia baixa - 4 x 8-10 repetições', 'Rosca alternada polia baixa - 3 x 10-12 repetições',
                 'Rosca concentrada polia baixa - 4 x 8-10 repetições', 'Rosca direta polia alta - 3 x 10-12 repetições', 'Rosca inversa polia alta - 4 x 8-10 repetições', 'Rosca concentrada polia alta - 3 x 10-12 repetições',
                 'Rosca scott c/ pegada ampla - 4 x 8-10 repetições', 'Rosca martelo c/ pegada neutra - 3 x 10-12 repetições', 'Rosca simultânea no cross over - 4 x 8-10 repetições', 'Rosca concentrada no cross over - 3 x 10-12 repetições',
                 'Rosca 21 polia alta - 4 x 8-10 repetições', 'Rosca spider polia alta - 3 x 10-12 repetições'
                 ]
treino_costas = ['Barra fixa - 4 x 8-10 repetições', 'Levantamento terra - 3 x 8-10 repetições', 'Remada curvada c/ barra - 4 x 10-12 repetições', 'Puxada frente - 3 x 10-12 repetições', 'Remada cavalinho - 4 x 8-10 repetições',
                 'Puxada alta - 3 x 10-12 repetições', 'Remada unilateral c/ halteres - 4 x 10-12 repetições', 'Remada baixa - 3 x 10-12 repetições', 'Puxada no pulley - 4 x 8-10 repetições', 'Remada máquina - 3 x 10-12 repetições',
                 'Remada aberta - 4 x 8-10 repetições', 'Remada T - 3 x 10-12 repetições', 'Puxada inversa - 4 x 8-10 repetições', 'Remada polia baixa - 3 x 10-12 repetições', 'Remada polia alta - 4 x 8-10 repetições',
                 'Remada c/ barra T - 3 x 10-12 repetições', 'Puxada triangular - 4 x 8-10 repetições', 'Remada máquina unilateral - 3 x 10-12 repetições', 'Puxada polia alta c/ pegada aberta - 4 x 8-10 repetições',
                 'Puxada polia alta c/ pegada fechada - 3 x 10-12 repetições', 'Puxada  cross over - 4 x 8-10 repetições', 'Puxada unilateral  cross over - 3 x 10-12 repetições', 'Puxada c/ corda - 4 x 8-10 repetições',
                 'Remada c/ halteres - 3 x 10-12 repetições', 'Puxada  cross over c/ pegada invertida - 4 x 8-10 repetições', 'Remada curvada unilateral - 3 x 10-12 repetições', 'Puxada máquina c/ pegada aberta - 4 x 8-10 repetições',
                 'Puxada máquina c/ pegada fechada - 3 x 10-12 repetições', 'Remada polia c/ pegada aberta - 4 x 8-10 repetições', 'Puxada polia c/ pegada fechada - 3 x 10-12 repetições'
                 ]
treino_triceps = ['Barra paralela - 4 x 8-10 repetições', 'Supino fechado - 3 x 10-12 repetições', 'Tríceps testa c/ barra - 4 x 8-10 repetições', 'Tríceps testa c/ halteres - 3 x 10-12 repetições', 'Tríceps francês - 4 x 8-10 repetições',
                  'Tríceps corda  pulley - 3 x 10-12 repetições', 'Tríceps pulley corda - 4 x 8-10 repetições', 'Tríceps mergulho entre bancos - 3 x 10-12 repetições', 'Tríceps coice c/ halter - 4 x 8-10 repetições', 'Tríceps coice polia - 3 x 10-12 repetições',
                  'Tríceps corda polia alta - 4 x 8-10 repetições', 'Tríceps testa c/ halteres inclinado - 3 x 10-12 repetições', 'Tríceps corda invertido  pulley - 4 x 8-10 repetições', 'Tríceps testa máquina - 3 x 10-12 repetições', 'Tríceps polia alta - 4 x 8-10 repetições',
                  'Tríceps banco - 3 x 10-12 repetições', 'Tríceps testa unilateral c/ halter - 4 x 8-10 repetições', 'Tríceps testa polia baixa - 3 x 10-12 repetições', 'Tríceps francês c/ barra - 4 x 8-10 repetições', 'Tríceps polia c/ corda - 3 x 10-12 repetições',
                  'Tríceps corda c/ pegada invertida - 4 x 8-10 repetições', 'Tríceps testa  cross over - 3 x 10-12 repetições', 'Tríceps testa c/ barra reta - 4 x 8-10 repetições', 'Tríceps corda  cross over - 3 x 10-12 repetições', 'Tríceps coice polia baixa - 4 x 8-10 repetições',
                  'Tríceps banco unilateral - 3 x 10-12 repetições', 'Tríceps corda polia baixa - 4 x 8-10 repetições', 'Tríceps testa polia alta - 3 x 10-12 repetições', 'Tríceps corda  cross over c/ pegada invertida - 4 x 8-10 repetições', 'Tríceps corda polia alta - 3 x 10-12 repetições'
                  ]
treino_peitos = ['Supino reto - 4 x 8-10 repetições', 'Supino inclinado - 3 x 10-12 repetições', 'Supino declinado - 4 x 8-10 repetições', 'Flexão de braço - 3 x 10-12 repetições', 'Crossover - 4 x 8-10 repetições', 'Supino com halteres - 3 x 10-12 repetições', 'Peck deck - 4 x 8-10 repetições',
                 'Pullover com halter - 3 x 10-12 repetições', 'Abertura com halteres - 4 x 8-10 repetições', 'Supino fechado - 3 x 10-12 repetições', 'Flexão de braço inclinada - 4 x 8-10 repetições', 'Crossover polia - 3 x 10-12 repetições', 'Flexão de braço declinada - 4 x 8-10 repetições',
                 'Abertura máquina - 3 x 10-12 repetições', 'Flexão de braço com pegada diamante - 4 x 8-10 repetições', 'Pullover máquina - 3 x 10-12 repetições', 'Dips - 4 x 8-10 repetições', 'Flexão de braço máquina - 3 x 10-12 repetições', 'Crossover inverso - 4 x 8-10 repetições',
                 'Flexão de braço com apoio - 3 x 10-12 repetições', 'Flexão de braço bola - 4 x 8-10 repetições', 'Flexão de braço com expansão - 3 x 10-12 repetições', 'Flexão de braço com banda elástica - 4 x 8-10 repetições', 'Flexão de braço máquina Hammer - 3 x 10-12 repetições',
                 'Supino inclinado com halteres - 4 x 8-10 repetições', 'Flexão de braço barra fixa - 3 x 10-12 repetições', 'Mergulho entre bancos - 4 x 8-10 repetições', 'Flexão de braço máquina Smith - 3 x 10-12 repetições', 'Supino declinado com halteres - 4 x 8-10 repetições',
                 'Flexão de braço com peso - 3 x 10-12 repetições'
                 ]
treino_pernas = ['Agachamento livre - 4 x 8-10 repetições', 'Leg press - 3 x 10-12 repetições', 'Afundo - 4 x 8-10 repetições', 'Cadeira extensora - 3 x 10-12 repetições', 'Cadeira flexora - 4 x 8-10 repetições', 'Stiff - 3 x 10-12 repetições', 'Mesa flexora - 4 x 8-10 repetições',
                 'Agachamento hack - 3 x 10-12 repetições', 'Panturrilha  leg press - 4 x 8-10 repetições', 'Elevação de panturrilha com halteres - 3 x 10-12 repetições', 'Cadeira adutora - 4 x 8-10 repetições', 'Cadeira abdutora - 3 x 10-12 repetições', 'Avanço - 4 x 8-10 repetições',
                 'Caminhada lateral com elástico - 3 x 10-12 repetições', 'Agachamento sumô - 4 x 8-10 repetições', 'Cadeira extensora unilateral - 3 x 10-12 repetições', 'Agachamento búlgaro - 4 x 8-10 repetições', 'Flexão plantar em pé - 3 x 10-12 repetições', 'Flexão plantar sentado - 4 x 8-10 repetições',
                 'Agachamento com salto - 3 x 10-12 repetições', 'Agachamento máquina Smith - 4 x 8-10 repetições', 'Prensa 45° - 3 x 10-12 repetições', 'Mesa extensora - 4 x 8-10 repetições', 'Mesa flexora unilateral - 3 x 10-12 repetições', 'Cadeira extensora drop set - 4 x 8-10 repetições',
                 'Agachamento isométrico - 3 x 10-12 repetições', 'Panturrilha  leg press drop set - 4 x 8-10 repetições', 'Elevação de panturrilha  smith - 3 x 10-12 repetições', 'Elevação de panturrilha  hack - 4 x 8-10 repetições', 'Elevação de panturrilha  leg press unilateral - 3 x 10-12 repetições'
                 ]
treino_ombros = ['Desenvolvimento c/ barra - 4 x 8-10 repetições', 'Elevação lateral c/ halteres - 3 x 12-15 repetições', 'Desenvolvimento c/ halteres - 4 x 8-10 repetições', 'Elevação frontal c/ barra - 3 x 10-12 repetições',
                 'Elevação lateral inclinada - 3 x 12-15 repetições', 'Desenvolvimento Arnold - 4 x 8-10 repetições', 'Elevação frontal c/ halteres - 3 x 10-12 repetições', 'Desenvolvimento máquina Smith - 4 x 8-10 repetições',
                 'Elevação lateral máquina - 3 x 12-15 repetições', 'Elevação frontal máquina - 3 x 10-12 repetições', 'Desenvolvimento c/ polia alta - 4 x 8-10 repetições', 'Elevação lateral c/ polia baixa - 3 x 12-15 repetições',
                 'Elevação frontal c/ polia baixa - 3 x 10-12 repetições', 'Desenvolvimento c/ corda polia - 4 x 8-10 repetições', 'Elevação lateral c/ cabo - 3 x 12-15 repetições', 'Elevação frontal c/ cabo - 3 x 10-12 repetições',
                 'Desenvolvimento c/ kettlebell - 4 x 8-10 repetições', 'Elevação lateral c/ kettlebell - 3 x 12-15 repetições', 'Elevação frontal c/ kettlebell - 3 x 10-12 repetições', 'Desenvolvimento c/ halteres posição neutra - 4 x 8-10 repetições',
                 'Elevação lateral c/ halteres posição neutra - 3 x 12-15 repetições', 'Elevação frontal c/ halteres posição neutra - 3 x 10-12 repetições', 'Elevação lateral c/ barra - 3 x 12-15 repetições', 'Elevação frontal alternada c/ halteres - 3 x 10-12 repetições',
                 'Elevação frontal c/ barra sentado - 3 x 10-12 repetições', 'Elevação lateral c/ halteres sentado - 3 x 12-15 repetições'
                 ]


# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Clique no botão para gerar sua ficha de treino')],
    [sg.Button('Gerar', size=(33,1))]
]

# Janela
janela = sg.Window('Gerador de treino', layout)

# Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Gerar':
        # Criar o documento PDF
        desktop = Path.home()
        cnv = canvas.Canvas(str(desktop)+'\Downloads\Treino.pdf')
        cnv.setTitle('FICHA DE TREINO')

        # Funções de treino
        def peito_triceps():
            peito = random.sample(treino_peitos, 4)
            triceps = random.sample(treino_triceps, 4)

            cnv.setFont(*cabecalho_estilo)
            cnv.drawString(20, cnv._pagesize[1] - 90, 'Peito')
            cnv.setFont(*texto_estilo)
            y = cnv._pagesize[1] - 110
            for exercicio in peito:
                cnv.drawString(20, y, exercicio)
                y -= 20

            cnv.setFont(*cabecalho_estilo)
            cnv.drawString(310, cnv._pagesize[1] - 90, 'Triceps')
            cnv.setFont(*texto_estilo)
            y = cnv._pagesize[1] - 110
            for exercicio in triceps:
                cnv.drawString(310, y, exercicio)
                y -= 20


        def perna_ombro():
            pernas = random.sample(treino_pernas, 4)
            ombro = random.sample(treino_ombros, 3)

            cnv.setFont(*cabecalho_estilo)
            cnv.drawString(20, cnv._pagesize[1] - 240, 'Pernas')
            cnv.setFont(*texto_estilo)
            y = cnv._pagesize[1] - 260
            for exercicio in pernas:
                cnv.drawString(20, y, exercicio)
                y -= 20

            cnv.setFont(*cabecalho_estilo)
            cnv.drawString( 310, cnv._pagesize[1] - 240, 'Ombro')
            cnv.setFont(*texto_estilo)
            y = cnv._pagesize[1] - 260
            for exercicio in ombro:
                cnv.drawString( 310, y, exercicio)
                y -= 20


        def costa_biceps():
            costas = random.sample(treino_costas, 4)
            biceps = random.sample(treino_biceps, 4)

            cnv.setFont(*cabecalho_estilo)
            cnv.drawString(20, cnv._pagesize[1] - 390, 'Costas')
            cnv.setFont(*texto_estilo)
            y = cnv._pagesize[1] - 410
            for exercicio in costas:
                cnv.drawString(20, y, exercicio)
                y -= 20

            cnv.setFont(*cabecalho_estilo)
            cnv.drawString( 310, cnv._pagesize[1] - 390, 'Biceps')
            cnv.setFont(*texto_estilo)
            y = cnv._pagesize[1] - 410
            for exercicio in biceps:
                cnv.drawString( 310, y, exercicio)
                y -= 20


        # Gera tabela de dias de treino
        def gera_tabela():
            cnv.drawString(50, 300, 'Tabela de Treino')

            cnv.drawString(50, 270, 'Segunda          Terça            Quarta           Quinta             Sexta')
            cnv.drawString(50, 260,
                           '-----------------------------------------------------------------------------------------')
            cnv.drawString(50, 250,
                           '     A                    B                     C                   A                    B')
            cnv.drawString(50, 240,
                           '-----------------------------------------------------------------------------------------')
            cnv.drawString(50, 230,
                           '     C                    B                     A                   C                    B')
            cnv.drawString(50, 220,
                           '-----------------------------------------------------------------------------------------')
            cnv.drawString(50, 210,
                           '     A                    B                     C                   A                    B')
            cnv.drawString(50, 200,
                           '-----------------------------------------------------------------------------------------')
            cnv.drawString(50, 190,
                           '     C                    B                     A                   C                    B')
            cnv.drawString(50, 180,
                           '-----------------------------------------------------------------------------------------')

        # função de alerta
        def alerta():
            alerta = [

                [sg.Text('Ficha de treino gerada em c:/Downloads', text_color='green',size=(33,4),auto_size_text=False)],
            ]

            # Janela alerta
            janela_alerta = sg.Window('Gerado com Sucesso!', alerta)
            while True:
                janela_alerta.read()
                break


        # Escrever no PDF
        cnv.setFont(*titulo_estilo)
        cnv.drawString(230, 800, 'FICHA DE TREINO')
        cnv.setFont(*cabecalho_estilo)
        cnv.drawString(20, cnv._pagesize[1] - 70, 'TREINO A')
        peito_triceps()
        cnv.setFont(*cabecalho_estilo)
        cnv.drawString(20, cnv._pagesize[1] - 220, 'TREINO B')
        perna_ombro()
        cnv.setFont(*cabecalho_estilo)
        cnv.drawString(20, cnv._pagesize[1] - 370, 'TREINO C')
        costa_biceps()
        cnv.setFont(*cabecalho_estilo)
        gera_tabela()
        cnv.save()
        alerta()
        break
