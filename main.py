import streamlit as st
import json
import os
import time

# File to store book data
FILE_NAME = "library.json"

# Load existing books
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)

# Remove a book
def remove_book(title):
    books = load_books()
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books(books)

# Search for books
def search_books(query):
    books = load_books()
    return [book for book in books if query.lower() in book["title"].lower()]

# Set page config for a better layout
st.set_page_config(page_title="📚 Personal Library", layout="wide")

# Custom CSS for Stylish Background & Cards
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
        }
        .stTitle {
            text-align: center;
            color: white;
        }
        .custom-box {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            background-color: #ff4b4b;
            color: white;
        }
        .stButton > button:hover {
            background-color: #ff6b6b;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='stTitle'>📚 Personal Library Manager</h1>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.header("📌 Manage Your Library")
option = st.sidebar.radio("Choose an action:", ["📖 View Books", "➕ Add Book", "❌ Remove Book", "🔍 Search Book"])

# View all books
if option == "📖 View Books":
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    books = load_books()
    st.write("### 📚 Your Book Collection")
    if books:
        st.table(books)
    else:
        st.warning("No books found!")
    st.markdown("</div>", unsafe_allow_html=True)

# Add a new book with better layout
elif option == "➕ Add Book":
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.subheader("📥 Add a New Book")
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("📖 Book Title", placeholder="Enter book title...")
    with col2:
        author = st.text_input("✍️ Author Name", placeholder="Enter author's name...")

    if st.button("📥 Add Book"):
        if title and author:
            add_book(title, author)
            with st.spinner("Adding book..."):
                time.sleep(1)
            st.success(f"✅ '{title}' by {author} added!")
        else:
            st.error("❌ Please fill in both fields.")
    st.markdown("</div>", unsafe_allow_html=True)

# Remove a book with dropdown selection
elif option == "❌ Remove Book":
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.subheader("🗑️ Remove a Book")
    books = load_books()
    book_titles = [book["title"] for book in books]
    if book_titles:
        selected_book = st.selectbox("📌 Select a book to remove:", book_titles)
        if st.button("🗑️ Remove Book"):
            remove_book(selected_book)
            with st.spinner("Removing book..."):
                time.sleep(1)
            st.success(f"❌ '{selected_book}' removed!")
    else:
        st.warning("No books to remove!")
    st.markdown("</div>", unsafe_allow_html=True)

# Search for books with live results
elif option == "🔍 Search Book":
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.subheader("🔍 Search for a Book")
    query = st.text_input("🔎 Enter book title to search:", placeholder="Type to search...")
    
    if query:
        results = search_books(query)
        if results:
            st.write("### 📖 Search Results")
            st.table(results)
        else:
            st.warning("❌ No matching books found.")
    st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("Developed by **Bilal Motiwala** 🚀")

