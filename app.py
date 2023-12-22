from retrieve import qa_chain, process_llm_response
import streamlit as st


def main():
    qa = qa_chain()
    st.title('Embedded GPT')
    text_query = st.text_area('Ask any question from ARM or PIC Microcontroller!')
    generate_response_btn = st.button('Run RAG')
    
    st.subheader('Response')
    if generate_response_btn and text_query is not None:
        with st.spinner('Generating Response. Please wait...'):
            text_response = qa(text_query)
            if text_response:
                st.write(text_response)
            else:
                st.error('Failed to get response')

if __name__ == "__main__":
    main()    