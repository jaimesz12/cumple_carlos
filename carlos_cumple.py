import streamlit as st
from PIL import Image
import base64

# Configuración app web
st.set_page_config(
    layout="wide",
    page_icon=':birthday:',
    page_title="26 - Carlos",
    initial_sidebar_state='expanded'
)

# Añadir espacios streamlit
def space(num_lines=1):
    for _ in range(num_lines):
        st.write("")


# Sidebar con imágenes
with st.sidebar:
    imagen_borat = """
    <center><img src="https://i.ibb.co/GWfYmtp/boratt.png"
    style="float:none; width:250px;height:600px; "><center>
    """
    space(3)
    st.markdown(imagen_borat, unsafe_allow_html=True)


st.markdown("<center><font face='Adobe Garamond Premier Pro' size='8' >🥳🤩🎂🎉 ¡FELICIDADES CARLITOS! 🥳🤩🎂🎉</font><br /></center>",
            unsafe_allow_html=True)
st.markdown("<center><font face='WildWest' size='6' >Te quiero mucho  ❤️</font><br /></center>",
            unsafe_allow_html=True)
space(1)

st.markdown("""
<center><font face='WildWest' size='4' >Deberás responder a los siguientes tests para poder descubrir
lo que se esconde al final. ¡Mucha suerte!</font><br /></center>""", unsafe_allow_html=True)

space(1)

st.markdown("""
<center><font face='WildWest' size='4' >Ah... y ¡cuidado con meter la pata!</font><br /></center>""", unsafe_allow_html=True)

space(1)

c1, c2, c3 = st.columns([2.7, 2.5, 3])

with c1:
    pass

with c2:
    # Imagen meter la pata
    meter_la_pata = Image.open('Fotos/meter_la_pata_codif.jpg')
    st.image(meter_la_pata, width=400)

    st.markdown("""
    <center><font face='WildWest' size='4' >¿Estás listo? ¡COMENCEMOS! 📋🖋⬇️</font><br /></center>""", unsafe_allow_html=True)

with c3:
    pass

space(3)


st.markdown("""
        <center><font face='WildWest' size='4' >El test se divide en distintas categorías, las cuales agrupan preguntas del mismo tipo o época. Instrucciones para que puedas rellenar las preguntas de manera óptima:
        </font><br /><center>""", unsafe_allow_html=True)

space(1)


st.markdown("""
        <center><font face='WildWest' size='4' >1. En las preguntas donde tienes que introducir frases o palabras, introduce todo en <strong>minúsculas</strong> para evitar fallos de codificación y pulsa enter para enviar la respuesta.
        </font><br /><center>""", unsafe_allow_html=True)

st.markdown("""
        <center><font face='WildWest' size='4' >2. Como consejo, cuando termines una categoría, contrae la cajita de preguntas para que puedas ver todo lo demás mejor (es opcional).
        </font><br /><center>""", unsafe_allow_html=True)

st.markdown("""
        <center><font face='WildWest' size='4' >3. En las preguntas de tipo test, de forma predeterminada la elección estará en <strong>"Elige"</strong>. ¡Pulsas la opción que creas y ya!
        </font><br /><center>""", unsafe_allow_html=True)

st.markdown("""
        <center><font face='WildWest' size='4' >4. Sólo puedes avanzar si aciertas la pregunta anterior. Sale un <strong>CORRECTO</strong> cuando le das a enter o eliges la respuesta.
        </font><br /><center>""", unsafe_allow_html=True)        

st.markdown("""
        <center><font face='WildWest' size='4' >5. Cuando tengas que calcular ecuaciones trigonométricas es mejor que... (tranquilo que no hay 🤣​🤣​)
        </font><br /><center>""", unsafe_allow_html=True)

space(2)
st.markdown("""
        <center><font face='WildWest' size='4' >Según las respuestas que aciertes tendrás más o menos premios, así que <strong>¡SUERTE!</strong>
        </font><br /><center>""", unsafe_allow_html=True)




space(2)

# Momentos especiales

st.markdown(
        """
            <style>
            .streamlit-expanderHeader {
                font-family:Helvetica;
                font-size: large;
                color:;
                text-align: center;
            }
            </style>
            """,
        unsafe_allow_html=True,
    )

momentos = st.expander("1. Momentos/detalles especiales en nuestras vidas:")
momentos.write(' ')
momentos.markdown("""
            <center><font face='WildWest' size='4' color= >1.1 ¿Cómo se titula la siguiente canción?</font><br /><center>""", unsafe_allow_html=True)

momentos.markdown("""
            <center><font face='WildWest' size='2' color= >*Poner el nombre completo en minúsculas (3 palabras)</font><br /><center>""", unsafe_allow_html=True)

momentos.write(' ')

 # Tunak tunak
c1, c2, c3 = momentos.columns(3)

with c1:
    pass

with c2:
    tunak = open('Audios/Daler Mehndi - Tunak Tunak Tun Video.ogg', 'rb')

    c2.audio(tunak, format='audio/ogg')

    # Respuesta
    respuesta1_1 = st.text_input('1.1. Respuesta:')

    if respuesta1_1:

        if respuesta1_1 == 'tunak tunak tun':
            st.success("""¡Correcto! Puedes continuar.""")

            tunak = Image.open('Fotos/ktunak.jpg')
            st.image(tunak)

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
momentos.write(' ')


# Película más risas

momentos.markdown("""
            <center><font face='WildWest' size='4' color= >1.2 ¿Cuál es la película con la que más nos hemos reído?</font><br /><center>""", unsafe_allow_html=True)

momentos.write(' ')

c1, c2, c3 = momentos.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta1_2 = st.text_input('1.2. Respuesta:')

    if respuesta1_2:

        if respuesta1_2 == 'borat':
            st.success("""¡Correcto! Puedes continuar.""")

            borat = Image.open('Fotos/kborat.jpg')
            st.image(borat)

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
momentos.write(' ')


# Conciertos

momentos.markdown("""
            <center><font face='WildWest' size='4' color= >1.3 ¿A qué conciertos fuimos en Rivas?</font><br /><center>""", unsafe_allow_html=True)

momentos.write(' ')

c1, c2, c3 = momentos.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta1_3 = st.radio('1.3. Respuesta:', ('¡Elige!','Musicland y Boafest' ,'EnVivo y Boafest', 'Rock in Rio y EnVivo'))

    if respuesta1_3:

        if respuesta1_3 == 'EnVivo y Boafest':
            st.success("""¡Correcto! Puedes continuar.""")

            st.write(' ')
            imagen_concierto = Image.open('boafest.jpg')
            st.image(imagen_concierto)
        
        elif respuesta1_3 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
momentos.write(' ')

# Fiestas

momentos.markdown("""
            <center><font face='WildWest' size='4' color= >1.4 ¿Qué me diste cuando me emborraché la primera vez en las fiestas de Aluche?</font><br /><center>""", unsafe_allow_html=True)

momentos.write(' ')

c1, c2, c3 = momentos.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta1_4 = st.radio('1.4. Respuesta:', ('¡Elige!','Kebab' ,'Jaggermeister', 'Café'))

    if respuesta1_4:

        if respuesta1_4 == 'Café':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
            aluche = Image.open('Fotos/kaluche.jpg')
            st.image(aluche)
        
        elif respuesta1_4 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
momentos.write(' ')

# Primera comida

momentos.markdown("""
            <center><font face='WildWest' size='4' color= >1.5 ¿Cuál fue la primera comida que nos preparaste en tu casa cuando éramos pequeños?</font><br /><center>""", unsafe_allow_html=True)

momentos.write(' ')

c1, c2, c3 = momentos.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta1_5 = st.radio('1.5. Respuesta:', ('¡Elige!','Arroz blanco' ,'Spaghettis carbonara', 'Pizza'))

    if respuesta1_5:

        if respuesta1_5 == 'Spaghettis carbonara':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta1_5 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
momentos.write(' ')

# Sierra compañía

momentos.markdown("""
            <center><font face='WildWest' size='4' color= >1.6 ¿Con quién fuimos a Guadarrama un día que nevaba? </font><br /><center>""", unsafe_allow_html=True)

momentos.write(' ')

c1, c2, c3 = momentos.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta1_6 = st.radio('1.6. Respuesta:', ('¡Elige!','Marta' ,'María Cantón', 'Mario Georgiev'))

    if respuesta1_6:

        if respuesta1_6 == 'María Cantón':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
            imagen_canton = Image.open('Fotos/IMG_3439.JPG')
            st.image(imagen_canton)

            imagen_nosotr = Image.open('Fotos/IMG_3436.JPG')
            st.image(imagen_nosotr)
        
        elif respuesta1_6 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
momentos.write(' ')


# Jaraíz cem alemán

momentos.markdown("""
            <center><font face='WildWest' size='4' color= >1.7 ¿De quién era la cara que pusimos en la cruz del cementerio militar alemán de Cuacos de Yuste? </font><br /><center>""", unsafe_allow_html=True)

momentos.write(' ')

c1, c2, c3 = momentos.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta1_7 = st.radio('1.7. Respuesta:', ('¡Elige!','Dani' ,'Miguel Ángel', 'Andrés'))

    if respuesta1_7:

        if respuesta1_7 == 'Andrés':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
            imagen_cem = Image.open('Fotos/ITLQ0594.JPG')
            st.image(imagen_cem)
        
        elif respuesta1_7 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
momentos.write(' ')
    
## Siguiente expander
# Instituto
instituto = st.expander("2. Cosas de críos. Momentos en el instituto:")
instituto.write(' ')
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.1 ¿Cuál o cuáles de estas frases son de las más repetidas por Giuseppe?</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')

 # Giu

c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_1= st.radio('2.1. Respuesta:', ('¡Elige!','Y digo: ¡eeeeeeeeh etilla! / ¡Métete el dedo, loco!' ,'Bobotron', 'Enséñame la cosita'))

    if respuesta2_1:

        if respuesta2_1 == 'Y digo: ¡eeeeeeeeh etilla! / ¡Métete el dedo, loco!':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta2_1 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')


# Mote de Einar
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.2 ¿Cuál era el mote de Einar?</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')
c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_2= st.radio('2.2. Respuesta:', ('¡Elige!','Pichón' ,'Mafias', 'Jabalí'))

    if respuesta2_2:

        if respuesta2_2 == 'Jabalí':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta2_2 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")


instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')


# Moco
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.3 ¿Qué le salió a Andrés en clase en, probablemente, el momento más gracioso en toda la época del instituto?</font><br /><center>""", unsafe_allow_html=True)
instituto.markdown("""
            <center><font face='WildWest' size='2' color= >*Poner la palabra completa en minúsculas (1 palabra, singular)</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')

c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_3 = st.text_input('2.3. Respuesta:')

    if respuesta2_3:

        if respuesta2_3 == 'moco':
            st.success("""¡Correcto! Puedes continuar.""")

            nosotros_clase = Image.open('Fotos/clase.jpg')
            st.image(nosotros_clase)

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')


instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')

# Tanques
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.4 ¿Cómo llamábamos a las zapatillas de Sergio Sen (que, por cierto, no las volvió a traer al instituto)?</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')

c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_4= st.radio('2.4. Respuesta:', ('¡Elige!','Cabras' ,'Tanques', 'Guantes'))

    if respuesta2_4:

        if respuesta2_4 == 'Tanques':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta2_4 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")


instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')

# George
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.5 Movimiento o imitación más característico de George.</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')

c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_5= st.radio('2.5. Respuesta:', ('¡Elige!','Top manta en el metro señalando hacia arriba y diciendo "abajo, policía"' ,'Imitar a Giuseppe', 'Meterse con Lucas y Thiago'))

    if respuesta2_5:

        if respuesta2_5 == 'Top manta en el metro señalando hacia arriba y diciendo "abajo, policía"':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta2_5 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")


instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')

# Encarna
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.6. Profesora más loca del instituto:</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')

c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_6= st.radio('2.6. Respuesta:', ('¡Elige!','Rosa' ,'Juana', 'Encarna'))

    if respuesta2_6:

        if respuesta2_6 == 'Encarna':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta2_6 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")


instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')

# Mote Julio
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.7. Mote más conocido del profesor de Ciencias Sociales (Julio)</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')

c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_7= st.radio('2.7. Respuesta:', ('¡Elige!','Julio Molano' ,'Julio Voltio', 'Mostacho'))

    if respuesta2_7:

        if respuesta2_7 == 'Mostacho':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta2_7 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")


instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')

# GFK
instituto.markdown("""
            <center><font face='WildWest' size='4' color= >2.8. ¿Cómo se llamaba la banda de graffitis cuyo principal componente era Deok?</font><br /><center>""", unsafe_allow_html=True)

instituto.write(' ')

c1, c2, c3 = instituto.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta2_8= st.radio('2.8. Respuesta:', ('¡Elige!','PEPE' ,'GFK', 'LOL'))

    if respuesta2_8:

        if respuesta2_8 == 'GFK':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta2_8 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")


instituto.write(' ')
instituto.write(' ')
instituto.write(' ')
instituto.write(' ')


## Italia
italia = st.expander("3. Italia. Un viaje especial:")
italia.write(' ')


# Gafas
italia.markdown("""
            <center><font face='WildWest' size='4' color= >3.1 En el viaje a Italia, ¿a quién se le veían las cartas reflejadas en las gafas?</font><br /><center>""", unsafe_allow_html=True)
italia.write(' ')

c1, c2, c3 = italia.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta3_1= st.radio('3.1. Respuesta:', ('¡Elige!','A Roka' ,'Al Mafias', 'A Alexander'))

    if respuesta3_1:

        if respuesta3_1 == 'Al Mafias':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta3_1 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

italia.write(' ')
italia.write(' ')
italia.write(' ')
italia.write(' ')


# Piscina
italia.markdown("""
            <center><font face='WildWest' size='4' color= >3.2 En el viaje a Italia, ¿quién le abrió la cabeza a quién en la piscina y se enfadó con todo el mundo por las risas menos con el que le había abierto la cabeza?</font><br /><center>""", unsafe_allow_html=True)
italia.write(' ')

c1, c2, c3 = italia.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta3_2= st.radio('3.2. Respuesta:', ('¡Elige!','Alexander a Roka' ,'Roka a Mafias', 'Alexander a Sandoval'))

    if respuesta3_2:

        if respuesta3_2 == 'Alexander a Roka':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta3_2 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

italia.write(' ')
italia.write(' ')
italia.write(' ')
italia.write(' ')

# Espuma
italia.markdown("""
            <center><font face='WildWest' size='4' color= >3.3 En el viaje a Italia, ¿quién llenó de espuma las Air Force a Lucía?</font><br /><center>""", unsafe_allow_html=True)
italia.write(' ')

c1, c2, c3 = italia.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta3_3= st.radio('3.3. Respuesta:', ('¡Elige!','Alexander' ,'María Cantón', 'Roka'))

    if respuesta3_3:

        if respuesta3_3 == 'María Cantón':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta3_3 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

italia.write(' ')
italia.write(' ')
italia.write(' ')
italia.write(' ')

# Dormir
italia.markdown("""
            <center><font face='WildWest' size='4' color= >3.4 Nombre de la persona a la cuál era prácticamente imposible despertar en el autobús.</font><br /><center>""", unsafe_allow_html=True)

italia.markdown("""
            <center><font face='WildWest' size='2' color= >*Poner el nombre en minúsculas. Sólo el nombre, sin apellido.</font><br /><center>""", unsafe_allow_html=True)

italia.write(' ')

c1, c2, c3 = italia.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta3_4 = st.text_input('3.4. Respuesta:')

    if respuesta3_4:

        if respuesta3_4 == 'maría' or respuesta3_4 == 'maria':
            st.success("""¡Correcto! Puedes continuar.""")
        else:
            st.warning("""¡No es correcto! Te queda un intento""")

with c3:
    st.text('')

italia.write(' ')
italia.write(' ')
italia.write(' ')
italia.write(' ')

## Cd4
cd4 = st.expander("4. Cosa de 4. María, Carlos, Patri y Jaime (Cd4, espero que cojas la referencia 🤣):")
cd4.write(' ')

# Espuma
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.1 Primer restaurante al que fuimos los 4. </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_1= st.radio('4.1. Respuesta:', ('¡Elige!','Magullo' ,'Foster Hollywood', 'Pizzería Carlos'))

    if respuesta4_1:

        if respuesta4_1 == 'Foster Hollywood':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta4_1 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')

# Justificación maría
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.2 ¿Cuál era la excusa de María para no elegir la habitación más cercana a la puerta en Bilbao? </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_2= st.radio('4.2. Respuesta:', ('¡Elige!', 'Habitación sucia' ,'Habitación fría', 'Por si entraba alguien y asesinaba a los de la primera habitación'))

    if respuesta4_2:

        if respuesta4_2 == 'Por si entraba alguien y asesinaba a los de la primera habitación':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
            asesino = Image.open('Fotos/kasesin.jpg')
            st.image(asesino)
        
        elif respuesta4_2 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')

# Puente colgante
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.3 ¿Cuántos metros de altura tiene el puente colgante de Portugalete? </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_3= st.radio('4.3. Respuesta:', ('¡Elige!', '45' ,'65', '105'))

    if respuesta4_3:

        if respuesta4_3 == '45':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
            portugalete = Image.open('Fotos/portugalete.jpeg')
            st.image(portugalete)
        
        elif respuesta4_3 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')

# Escape room
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.4 En los escape rooms que hemos hecho los 4, ¿qué personaje <strong>no</strong> ha intervenido nunca dentro de la/s sala/s? </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_4= st.radio('4.4. Respuesta:', ('¡Elige!', 'Un monje' ,'Un asesino con máscara de cerdo', 'Un payaso'))

    if respuesta4_4:

        if respuesta4_4 == 'Un payaso':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
            escap = Image.open('Fotos/escap.jpeg')
            st.image(escap)
        
        elif respuesta4_4 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')

# Escape room
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.5 ¿Qué fue lo que más le flipó a Patri de vuestra casa cuando nos la enseñásteis? </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_5= st.radio('4.5. Respuesta:', ('¡Elige!', 'La cama' ,'El sofá', 'La lámpara del comedor'))

    if respuesta4_5:

        if respuesta4_5 == 'La lámpara del comedor':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
        
        elif respuesta4_5 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')

# Segovia
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.6 ¿Quién sale con la mascarilla en las fotos que nos hicimos en Segovia? </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_6= st.radio('4.6. Respuesta:', ('¡Elige!', 'María' ,'Patri', 'Jaime', 'Carlos'))

    if respuesta4_6:

        if respuesta4_6 == 'Jaime':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')
            seg = Image.open('Fotos/seg.jpeg')
            st.image(seg)            

        
        elif respuesta4_6 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')

# Tinieblas
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.7 ¿Quién jugaba a juegos de adultos de pequeño/a? </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_7= st.radio('4.7. Respuesta:', ('¡Elige!', 'María' ,'Patri', 'Jaime', 'Carlos'))

    if respuesta4_7:

        if respuesta4_7 == 'Patri':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')       

        
        elif respuesta4_7 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')

# Tinieblas
cd4.markdown("""
            <center><font face='WildWest' size='4' color= >4.8 ¿Quién tiene más necesidad de ir más veces al baño? </font><br /><center>""", unsafe_allow_html=True)
cd4.write(' ')

c1, c2, c3 = cd4.columns(3)

with c1:
    pass

with c2:

    # Respuesta
    respuesta4_8= st.radio('4.8. Respuesta:', ('¡Elige!', 'Carlos' ,'Patri', 'Ambos'))

    if respuesta4_8:

        if respuesta4_8 == 'Ambos':
            st.success("""¡Correcto! Puedes continuar.""")
            st.write(' ')       

        
        elif respuesta4_8 == '¡Elige!':
            st.write('')

        else:
            st.warning("""¡No es correcto! Te queda un intento""")

cd4.write(' ')
cd4.write(' ')
cd4.write(' ')
cd4.write(' ')











# FINAL
space(3)

st.markdown("""
<center><font face='WildWest' size='4' >Cuando hayas acabado todos los test en todas las categorías dale click al siguiente botón. <strong>SÓLO CUANDO HAYAS TERMINADO.</strong></font><br /></center>""", unsafe_allow_html=True)

st.markdown("""
<center><font face='WildWest' size='4' >Los premios variarán según las respuestas acertadas.</font><br /></center>""", unsafe_allow_html=True)

space(2)

# Regalos

c1, c2, c3 = st.columns(3)

with c1:
    pass

with c2:

    finalizar = st.button('FINALIZAR TEST Y DESCUBRIR PREMIOS')

    if finalizar:
        st.balloons()
        st.markdown("""
                    <font face='WildWest' size='4' >¡Enhorabuena! Te han tocado dos regalos:</font><br /></center>""", unsafe_allow_html=True)

with c3:
    pass


# Fotos regalos
c1, c2 = st.columns(2)

if finalizar:
    c1.markdown("""
                <center><font face='WildWest' size='4' >Entradas para el concierto de Kase.O antes de su retirada "temporal".</font><br /></center>""", unsafe_allow_html=True)
    c1.write(' ')    
    kaseo = Image.open('Fotos/kase-o-jazz-magnetism-madrid-616ea59085a5a6.64741347.jpeg')
    c1.image(kaseo)

    c2.markdown("""
                <center><font face='WildWest' size='4' >Vale para un viaje a la sierra o a Jaraíz con Jaime. Día/s a elegir.</font><br /></center>""", unsafe_allow_html=True)    
    c2.write(' ')    
    trabuquete = Image.open('Fotos/ktrabuquete.jpg')
    c2.image(trabuquete)