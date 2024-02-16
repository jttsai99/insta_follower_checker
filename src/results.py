class Results:
    '''
    Defines the Results object to track unfollowers and followers
    '''
    def __init__(self, followers, following):
        self.followers = followers
        self.following = following
    
    def find_unfollowers(self):
        '''
        Merges the two dataframes and find the people that are not following you and people you are not following back
        Returns two separate dataframes
        '''
        merged = self.followers.merge(self.following, on='user_id', how='outer', suffixes= ('_follower','_following') ,indicator=True)
        # Filter the merged dataframe by the _merge column
        left_only = merged[merged['_merge'] == 'left_only'] # People you are not following back
        right_only = merged[merged['_merge'] == 'right_only'] # People who are not following you

        # Extract the user_id column as lists
        you_not_follow = left_only[['user_id', 'user_link_follower','timestamp_follower']]
        not_follow_you = right_only[['user_id', 'user_link_following','timestamp_following']]

        # Rename the columns
        you_not_follow.columns = ['user_link', 'user_id', 'timestamp']
        not_follow_you.columns = ['user_link', 'user_id', 'timestamp']

        return not_follow_you, you_not_follow