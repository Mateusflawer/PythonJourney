import streamlit as st
import threading
import time

st.title("Usando Thread!")


class T(threading.Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        time.sleep(self.tempo)
        return self.texto

t1 = T("Thread 1", 3)
t1.start()

t2 = T("Thread 2", 1)
t2.start()

t3 = T("Thread 3", 2)
t3.start()

st.write("Executei depois da Thread")

cols = st.columns(3)

col1 = cols[0].empty()
col2 = cols[1].empty()
col3 = cols[2].empty()

col1.write("⏳")
col2.write("⏳")
col3.write("⏳")

col1.write(t1.run())
st.write("1")
col2.write(t2.run())
st.write("2")
col3.write(t3.run())
st.write("3")
