# import streamlit as st

# st.subheader("Where should we start?")

# name = st.text_input("", placeholder="Gemini")



import streamlit as st

# Page styling
st.markdown("""
<style>
.block-container {
    padding-top: 15vh;
    max-width: 1000px;
}

.heading {
    text-align: center;
    font-size: 42px;
    font-weight: 400;
    margin-bottom: 35px;
}

</style>
""", unsafe_allow_html=True)


# Center the content
left, middle, right = st.columns([1, 5, 1])

with middle:

    # Welcome heading
    st.markdown(
        '<div class="heading">Where should we start?</div>',
        unsafe_allow_html=True
    )

    # Chat input
    message = st.chat_input("Ask me anything")

    # Suggested prompts
    st.write("")

    st.button("✧ Design a phone wallpaper for me")

    st.button("▤ Help me practice for my upcoming exam")

    st.button("♧ Build a weekly checklist from my routine")

    # Display user message
    if message:
        st.write("You:", message)
