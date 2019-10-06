# Crawl-Data-Instagram

#This is instagram crawl
 what you can do with this program :
 - get instagram post/profile/hastag/comment/likes data without using Instagram API. the code in 'Crawl_data.py'
 
#Install
 - install instaloader, 'pip Install Instaloader'
 - install json if you want to save data with json like this code. 'pip install jsonlib'

##Crawler
###Usage
  - positional arguments :
    mode options : [post(caption), hashtag, likes, komen]
  - optional arguments :
     username --- instagram's username 
     hashtag  --- istagram's tag name/hashtag
     likes    --- count of how much post likes
     comment  --- comment of instagram's post
  - Output :
    output file name(json format)


   #####
   you must login with instagram's account what you have to run instaloader library in this program.
   write username and password

   if login succes, we need the user target to get the data
   profile_target is who the instagram's account target you want, write username target

   after that, the program will open the profile of user target and get the follower of user target
   and then open one by one follower of user target to get data as post caption, hashtag, likes and comment

   if the looping finish, data will be saved to json format

 
