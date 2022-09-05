
import csv

import time

import datetime



def trivia(jugar):
    
    #Lee los archivos

    csvfile = open('pregunta.csv')
    data = list(csv.DictReader(csvfile))
    csvfile.close()

    jug_01 = input('Ingrese su nombre: ').capitalize()
    jug_02 = input('Ingrese su nombre: ').capitalize()
        
    #puntaje de los jugadores

    puntaje_n1 = 0
    puntaje_n2 = 0

    pregunta = 1
    respuesta = 4
   
    n_preg = 1

    #Itera cada una de las preguntas

    for preg in data: 

        print('\t\tPregunta numero {}'.format(n_preg))
        print()
        print(preg['Preguntas'])
        print()
        print('1)', preg['1'])
        print('2)', preg['2'])
        print('3)', preg['3'])
        print('4)', preg['4'])
        print()

        n_preg+=1

        rta1= (input('⦿  {} Ingresa el numero de la opcion correcta: '.format(jug_01)))
    
        while rta1 !='1' and rta1 !='2' and rta1 !='3' and rta1 !='4':
            rta1= (input('⦿  {} Esa opcion no existe, elige entre las mencionadas anteriormente: '.format(jug_01)))  

        rta2= (input('⦿  {} Ingresa el numero de la opcion correcta: '.format(jug_02)))
        
        while rta2 !='1' and rta2 !='2' and rta2 !='3' and rta2 !='4':
            rta2= (input('⦿  {} Esa opcion no existe, elige entre las mencionadas anteriormente: '.format(jug_01))) 
         
        
        print()

        rta = preg['Correcta']
        print('La respuesta correcta es la opcion {}'.format(rta))
        print()
        if rta1 == rta:
            puntaje_n1+=10
        print('⦿  {} acumula {} puntos'.format(jug_01,puntaje_n1))
        print()
        if rta2 == rta:
            puntaje_n2+=10
        print('⦿  {} acumula {} puntos'.format(jug_02,puntaje_n2))
        print()
        time.sleep(3)

    rta_correcta_j1 = int(puntaje_n1/10)
    rta_correcta_j2 = int(puntaje_n2/10)

    #Consulta el ganador

    if puntaje_n1 > puntaje_n2: 
        print('El Campeon es: {} con {} puntos y {} respuestas correctas'.format(jug_01,puntaje_n1,rta_correcta_j1))
        print()
        print()

        print('''███████╗███████╗██╗     ██╗ ██████╗██╗████████╗ █████╗  ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗
██╔════╝██╔════╝██║     ██║██╔════╝██║╚══██╔══╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝
█████╗  █████╗  ██║     ██║██║     ██║   ██║   ███████║██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗
██╔══╝  ██╔══╝  ██║     ██║██║     ██║   ██║   ██╔══██║██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║
██║     ███████╗███████╗██║╚██████╗██║   ██║   ██║  ██║╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║
╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝''')
    elif puntaje_n2 > puntaje_n1:
        print('El Campeon es: {} con {} puntos y {} respuestas correctas'.format(jug_02,puntaje_n2,rta_correcta_j2))
        print()
        print()

        print(''' ███████╗███████╗██╗     ██╗ ██████╗██╗████████╗ █████╗  ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗
██╔════╝██╔════╝██║     ██║██╔════╝██║╚══██╔══╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝
█████╗  █████╗  ██║     ██║██║     ██║   ██║   ███████║██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗
██╔══╝  ██╔══╝  ██║     ██║██║     ██║   ██║   ██╔══██║██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║
██║     ███████╗███████╗██║╚██████╗██║   ██║   ██║  ██║╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║
╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝''')
    else: 
        print('Ambos empataron con {} puntos' .format(puntaje_n1))
        print()
        print()
        print('''███████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███████╗███╗   ██╗██████╗ ███████╗███╗   ██╗████████╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝
███████╗██║   ██║██████╔╝██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   █████╗  
╚════██║██║   ██║██╔══██╗██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  
███████║╚██████╔╝██║  ██║██║     ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║ ╚████║   ██║   ███████╗
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝''')


    #Crea un csv con el ganador
        
    fecha = datetime.date.today()

    if puntaje_n1 > puntaje_n2:
        Puntos = [(jug_01),(puntaje_n1),(fecha)]
    
    elif puntaje_n2 > puntaje_n1:
        Puntos = [(jug_02),(puntaje_n2),(fecha)]
    else:
        Puntos = None
    if Puntos != None:
        try:
            csvfile = open('Historico_Ganadores.csv')
        except:    
            csvfile = open('Historico_Ganadores.csv','w', newline='')

            header = ['Jugador','Puntaje','Fecha']
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()

            
        csvfile = open('Historico_Ganadores.csv','a', newline='')

        header = ['Jugador','Puntaje','Fecha']
        writer = csv.DictWriter(csvfile, fieldnames=header)

        fila = {'Jugador':Puntos[0],'Puntaje':Puntos[1],'Fecha':Puntos[2]}

        writer.writerow(fila)


        csvfile.close()


if __name__ == '__main__':




    
    print('═════════════════════════════════════════════════════════════════════════════════')
    print('**                                                                             **')
    print('**                               BIENVENIDOS                                   **')
    print('**                                    A                                        **')
    print('**                               PYTHONTADOS                                   **')
    print('**                          (una trivia de Python)                             **')
    print('**                                                                             **')
    print('═════════════════════════════════════════════════════════════════════════════════')
    print()
    print ('El juego consta de una trivia de 10 preguntas en donde 2 jugadores compentiran \npara saber quien sabe mas sobre Python inicial')
    print()

    jugar = (input('Desean jugar: \n1 SI.\n2 NO. \nIngrese la opcion correcta: '))

     #bucle para verificar que el valor ingresado sea el correcto

    while jugar !='1' and jugar !='2':
        jugar = (input('Opcion erronea.\nIngrese 1 para jugar o 2 para terminar: '))

    if jugar =='1':
             trivia(jugar)   
            
    else: print('Que lastima, Adios.')

