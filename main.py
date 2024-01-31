import streamlit as st

def main():
    st.title("Instagram follower/unfollower checker")
    st.header("Followers that are not following you back")
    st.file_uploader("Upload a JSON")

if __name__ == '__main__':
    main()