import streamlit as st
import pandas as pd 
import joblib

clf = joblib.load("model/divorce_model.pkl")

st.title('Averigua si tu matrimonio corre peligro')

options = ["Nunca", "Rara vez", "Promedio", "Con frecuencia", "Siempre"]

Q1 = st.select_slider(
    'Si uno de nosotros se disculpa cuando nuestra discusión se deteriora, la discusión termina.',
    options=options,
    key="Q1")

Q2 = st.select_slider(
    'Sé que podemos ignorar nuestras diferencias, incluso si a veces las cosas se ponen difíciles.',
    options=options,
    key="Q2")

Q3 = st.select_slider(
    'Cuando lo necesitamos, podemos retomar nuestras discusiones con mi cónyuge desde el principio y corregirlas.',
    options=options,
    key="Q3")

Q4 = st.select_slider(
    'Cuando discuto con mi cónyuge, contactarlo eventualmente funciona.',
    options=options,
    key="Q4")

Q5 = st.select_slider(
    'El tiempo que paso con mi esposa es especial para nosotros.',
    options=options,
    key="Q5")

Q6 = st.select_slider(
    'Tenemos tiempo en casa como pareja.',
    options=options,
    key="Q6")

Q7 = st.select_slider(
    'Somos como dos extraños que comparten el mismo entorno en casa en lugar de familia.',
    options=options,
    key="Q7")

Q8 = st.select_slider(
    'Disfruto nuestras vacaciones.',
    options=options,
    key="Q8")

Q9 = st.select_slider(
    'Disfruto viajar con mi cónyuge.',
    options=options,
    key="Q9")

Q10 = st.select_slider(
    'La mayoría de nuestros objetivos son comunes a mi cónyuge.',
    options=options,
    key="Q10")

Q11 = st.select_slider(
    'Creo que algún día en el futuro, cuando mire hacia atrás, veré que mi cónyuge y yo hemos estado en armonía el uno con el otro.',
    options=options,
    key="Q11")

Q12 = st.select_slider(
    'Mi cónyuge y yo tenemos valores similares en términos de libertad personal.',
    options=options,
    key="Q12")

Q13 = st.select_slider(
    'Mi cónyuge y yo tenemos un sentido similar del entretenimiento.',
    options=options,
    key="Q13")

Q14 = st.select_slider(
    'La mayoría de nuestros objetivos para las personas (hijos, amigos, etc.) son los mismos.',
    options=options,
    key="Q14")

Q15 = st.select_slider(
    'Nuestros sueños son similares y armoniosos.',
    options=options,
    key="Q15")

Q16 = st.select_slider(
    'Somos compatibles sobre lo que debería ser el amor.',
    options=options,
    key="Q16")

Q17 = st.select_slider(
    'Compartimos las mismas opiniones sobre ser felices en nuestra vida.',
    options=options,
    key="Q17")

Q18 = st.select_slider(
    'Mi cónyuge y yo tenemos ideas similares sobre cómo debería ser el matrimonio.',
    options=options,
    key="Q18")

Q19 = st.select_slider(
    'Mi cónyuge y yo tenemos ideas similares sobre cómo deberían ser los roles en el matrimonio.',
    options=options,
    key="Q19")

Q20 = st.select_slider(
    'Mi cónyuge y yo tenemos valores similares en la confianza.',
    options=options,
    key="Q20")

Q21 = st.select_slider(
    'Sé exactamente lo que le gusta a mi esposa.',
    options=options,
    key="Q21")

Q22 = st.select_slider(
    'Sé cómo mi cónyuge quiere que lo cuiden cuando está enfermo/a.',
    options=options,
    key="Q22")

Q23 = st.select_slider(
    'Sé la comida favorita de mi cónyuge.',
    options=options,
    key="Q23")

Q24 = st.select_slider(
    'Puedo decirte qué tipo de estrés enfrenta mi cónyuge en su vida.',
    options=options,
    key="Q24")

Q25 = st.select_slider(
    'Tengo conocimiento del mundo interior de mi cónyuge.',
    options=options,
    key="Q25")


if st.button('Listo'):
    X = pd.DataFrame([[Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25]], columns=["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12", "Q13", "Q14", "Q15", "Q16", "Q17", "Q18", "Q19", "Q20", "Q21", "Q22", "Q23", "Q24", "Q25"])
    X = X.replace(["Nunca", "Rara vez", "Promedio", "Con frecuencia", "Siempre"], [0, 1, 2, 3, 4])
    prediction = clf.predict(X)[0]
    if prediction == 0:
        st.text("Tu relación parece estar enfrentando desafíos. 😣")
    if prediction == 1:
        st.write("Tu relación está en una fase estable. ¡Seguid así! 😊")

