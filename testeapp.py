import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image

def main():
    st.title("Upload de Imagem e Observações")
    
    uploaded_file = st.file_uploader("Carregar uma imagem", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem Carregada", use_column_width=True)
    
    observacao = st.text_area("Observações", "Digite suas observações aqui...")
    
    if st.button("Salvar em Planilha"):
        df = pd.DataFrame({"Observações": [observacao]})
        
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Dados")
            writer.close()
        
        output.seek(0)
        st.download_button(label="Baixar Planilha", data=output, file_name="observacoes.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    main()
