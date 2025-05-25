import streamlit as st

# App Title and Config
st.set_page_config(page_title="📚 My Personal Library", page_icon="📖")
st.title("📚 Personal Library Manager")
st.markdown("Easily keep track of your books — add, view, and manage them!")

# Initialize session state for book list if not already created
if "books" not in st.session_state:
    st.session_state.books = []

# Book input form
st.subheader("➕ Add a New Book")
with st.form("book_form"):
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author Name")
    status = st.selectbox("📌 Status", ["Unread", "Reading", "Read"])
    submitted = st.form_submit_button("Add Book")

    # Add book to the session state list
    if submitted:
        if title and author:
            st.session_state.books.append({
                "Title": title,
                "Author": author,
                "Status": status
            })
            st.success(f"✅ '{title}' by {author} added!")
        else:
            st.warning("⚠️ Please fill in both the title and author.")

# Display book list
st.markdown("---")
st.subheader("📚 Your Book List")

if st.session_state.books:
    for index, book in enumerate(st.session_state.books):
        with st.expander(f"{book['Title']} by {book['Author']}"):
            st.write(f"📖 **Title**: {book['Title']}")
            st.write(f"✍️ **Author**: {book['Author']}")
            st.write(f"📌 **Status**: {book['Status']}")
            # ❌ Delete button
            if st.button(f"🗑️ Remove '{book['Title']}'", key=index):
                st.session_state.books.pop(index)
                st.experimental_rerun()
else:
    st.info("No books added yet. Start by adding a new one above! 📘")

# Footer
st.markdown("---")
st.caption("✨ Created with ❤️ by Musarrat Chaudhary using Python and Streamlit")
