# Import Library
import instaloader
import json

L = instaloader.Instaloader()

# Login or load session
L.login("username", "password")        # (login)
print("instagram login succes\nInstaloader ready to use \n")

# Obtain profile metadata
username_profile_target = "username target"
profile_target = instaloader.Profile.from_username(L.context, username_profile_target)
print("Instagram target found. username target:", username_profile_target)
print("\n")

file_json = open ("dataoutput2.json", "w+")
save = [] #array for follower data from profle_target

print("process data retrieval... \n")
#looping followers dari profile target
for follower in profile_target.get_followers():
    follower_target = follower.username

    #looping one of follower post
    print("getting all datas from @" + follower_target)
    profile = instaloader.Profile.from_username(L.context, follower_target)
    post_count = 1 #the count of post
    for post in profile.get_posts():
        caption_post = post.caption
        tag = post.caption_hashtags
        likes_count = post.likes
        
        if caption_post is not None: #if the post have caption
            caption_post = post.caption.encode('ascii', 'ignore').decode('ascii')

            #test
            #print("caption : ", caption_post)
            #print("hashtag : ", tag)
            #print("count likes :", likes_count)
            
        if caption_post is None: #if the post not have caption
            caption_post = ""
            
        comments_box = []
        for comment in post.get_comments():
            data_comment = comment.text.encode('ascii', 'ignore').decode('ascii')
            comments_box.append(data_comment)
            #print("comment :", comment)
            
            
        data = {"account" : follower_target, "caption": caption_post, "hastag" : tag, "likes": likes_count, "komen": comments_box}
        save.append(data)
        post_count = post_count + 1
    
data_json = json.dumps(save)
file_json.write(data_json)
file_json.close()

