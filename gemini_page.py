import streamlit as st


New_chat = st.Page(page="pages/new_chat.py", title="New Chat", icon="😊")
Library = st.Page(page="pages/library.py", title="Library", icon="😂")
Images = st.Page(page="pages/images.py", title="Images", icon="❤️")
Schedules = st.Page(page="pages/scheduled.py", title="Scheduled", icon="🕓")
Students = st.Page(page="pages/students.py", title="Students", icon="🎓")
More = st.Page(page="pages/more.py", title="...More")
New_notebook = st.Page(page="pages/new_notebook.py", title="New notebook", icon="😔")
All= st.Page(page="pages/all.py", title="All")

pg = st.navigation({
  
    "":[New_chat,Library,Images,Schedules,Students,More],
    "Notebooks" :[New_notebook],
    "All" :[All]
    
})

pg.run()