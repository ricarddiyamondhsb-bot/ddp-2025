import streamlit as st

st.title("aplikasi bio data")
st.header("biodata diri")

nama = st.text_input('nama lengkap', max_chars=10)
st.write(f'nama anda adalah : ', {nama})

with st.form(key='form1'):
    umur = st.number_input('masukkan umur anda', min_value=1, max_value=100)
    st.write(f' umur anda adalah : ', {umur})
    alamat = st.text_area('masukkan alamat anda')
    st.write(f'alamat anda adalah : ', {alamat})
    submit_button = st.form_submit_button(label='submit')

if submit_button:
    st.success('data berhasil disimpan')