import streamlit as st
from src.read_data import read_followers_JSON, read_following_JSON
from src.results import Results
def main():
    st.title("Instagram follower/unfollower checker")
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a Followers JSON", type= ['json'])
        uploaded_file2 = st.file_uploader("Upload a Following JSON", type= ['json'])
        if st.button("Process",):
            with st.spinner('We processing your data :)'):
                if uploaded_file is not None:
                    try:
                        followers_df = read_followers_JSON(uploaded_file)
                        st.subheader(f'Followers: {followers_df.shape[0]}')
                    except:
                        st.error("Make sure you are uploading the correct file 'followers_1.json'", icon="🚨")
                else:
                    st.warning("Don't forget to upload the 'followers_1.json' file in the sidebar")
                if uploaded_file2 is not None:
                    try:
                        following_df = read_following_JSON(uploaded_file2)
                        st.subheader(f'Following: {following_df.shape[0]}')
                    except:
                        st.error("Make sure you are uploading the correct file 'following.json'", icon="🚨")
                else:
                    st.warning("Don't forget to upload the 'following.json' file in the sidebar")
    try:
        st.subheader(f'Followers: {followers_df.shape[0]} || Following: {following_df.shape[0]}')
        #st.divider()
        results = Results(followers_df, following_df)
        not_follow_you, you_not_follow = results.find_unfollowers()
        st.subheader(f'Not following you back:')
        st.dataframe(not_follow_you)
        #st.divider()
        st.subheader(f'You are not following:')
        st.dataframe(you_not_follow)
    except:
        pass



if __name__ == '__main__':
    main()