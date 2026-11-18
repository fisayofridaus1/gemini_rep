import streamlit as st


New_chat = st.Page(page="gemini/new_chat.py", title="New Chat", icon="🔗")
Library = st.Page(page="gemini/library.py", title="Library", icon="😂")
Images = st.Page(page="gemini/images.py", title="Images", icon="❤️")
Schedules = st.Page(page="gemini/scheduled.py", title="Scheduled", icon="🕓")
Students = st.Page(page="gemini/students.py", title="Students", icon="🎓")
More = st.Page(page="gemini/more.py", title="...More")
New_notebook = st.Page(page="gemini/new_notebook.py", title="New notebook", icon="😔")
All= st.Page(page="gemini/all.py", title="All")

pg = st.navigation({
  
    "":[New_chat,Library,Images,Schedules,Students,More],
    "Notebooks" :[New_notebook],
    "All" :[All]
    
})

pg.run()