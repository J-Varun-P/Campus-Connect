# CS50W Capstone (Final Project)

## About Project

This Web Application is about helping students connect with activities which align with the student's interests.

The Activities can be of following types:

* Organizing an event and letting users participate. 
* Finding a Study Partner or Sports partner.
* A WebPage of an Activity dedicated to the discussions of certain subjects.

The Students can create a range of activities of the above mentioned types and much more which caters to their specific needs.

The Author of the Activity holds some previleges which allows them to:

* Delete a message made on an activity if the message contents made by a participating student seem inappropriate.
* Kick a User out of an Activity if their behaviour is improper.
* Ban the user from interacting with an activity if the User makes the other participants uncomfortable. 

## Why I believe this Project Satisfies the Distinctiveness and Complexity mentioned in the Capstone requirements

### Distinctiveness 

1. This Web Application is different from a social network and the reasoning is the following:

* The thing that makes a social network a social network is that the users can post anything that's on their mind (as long as they're respectful) (Take Twitter for example or some other social network), The user is not confined to post only posts that satisfy specific requirements,  they can post anything that's on their mind no matter what the subject of the post happens to be. This Web Application on the other hand lets you interact with activites created by other students or deparments of a university. The Activity needs to be well defined as to what it is, An Activity can be a discussion on a specific subject where the users can clarify a range of doubts they have on a specific part of that subject, or an Activity can be an event where the organizing team of the activity can define what an activity is and let the users to participate in the activity and answer student's questions if they happen to have any, or an Activity can be a place where you can meet like minded people for a sporting event or for a study partner. I think these reasons make my application differ from a social network.

2. This Web Applicaiton is not an e-commerce site which was the second requirement to be met and the reasoning is the following:

* This Web Application doesn't let users buy or sell products which is what an e-commerce Web Application does, This Web Application is not business oriented which satisfies the second requirement (The Web Application should not resemble an e-commerce site).

### Complexity

This Web Application is fairly complex given the instructions in the Capstone requirements and the reasoning is the following:

* This Web Application implements various features which include:

1. Registration of a New User.
2. Authentication and Logout Features.
3. Password Reset in case the User forgets their Password.
4. Password Change if the User feels like changing their Password.
5. Creating, Editing an Activity.
6. Joining, Leaving an Activity.
7. Message board for an Activity WebPage.
8. Editing, Deleting Messages in message board section of Activity WebPage.
9. Kicking the User out of an Activity if they're improper (Only the Author of an Activity can kick a user out).
10. Banning the Users from an Activity if they make other's uncomfortable.
11. Removing an Activity (The Activity doesn't appear on the index page for other users (users who are not members of the activity) to see but the activity isn't deleted at this point yet, The Users who joined the Activity can still see this activity in the deleted activities section of the web application).
12. Making an Activity go live from deleted section once it's removed from the index of list of activites (Non Members of the Activity can now see the activity which was invisible to them when the activity was in the deleted section).
13. Permanently Deleting an Activity (When the Author of the Activity deletes the Activity from the deleted section of the WebPage, The Activity is deleted forever even for the members of the Activity).
14. Pagination of Activites.
15. Updating Profiles.
16. Searching for activities by providing a specific username or by providing a substring containing in the list of activities you want to search for.
17. Making sure the users don't have access to content of the Web Application that they're not authorised to by having conditions checked in views.py file.


## File Structure

### Meet (Web Application name)

#### Files in Meet

##### meet/static/meet 

###### 1. styles.css

* This File contains all the css that is used by the Web Application.

###### 2. script.js

* This File contains all the javascript that is used by the Web Application.

##### meet/templates/meet

###### 1. activity.html

* This file has all the content that represents an Activity and it contains the following:

1. Title of an Activity.
2. Description of an Activity.
3. Author of an Activity.
4. Button to Join or leave Activity for users.
5. Members list of the Activity.
6. Banned Members list of the Activity.
7. Message Board and a form for inputting a message on to the board.
8. Icon links for editing messages, deleting messages, kicking a user out of the activity, banning a user from the activity.


###### 2. addactivity.html

* This file contains a form to create an activity by specifying fields for activity title and activity description.


###### 3. deletedactivities.html

* This file contains all the information about removed activities and it renders the following:

1. List of all the activities (Paginated) that have been removed but the user happens to be a member of the activity or the author of the activity.
2. Icon links for editing the activity information or permanently deleting the activity if the user is the author of the activity.
3. A Button to make a deleted activity live so that the non members of the activity can view it as well in their index page.


###### 4. editactivity.html

* This file contains the form to edit the information (Title and Description) relating to the activity if the user happens to be the author of the activity.


###### 5. editactivitycomment.html

* This file contains the form to edit the comments made on a activity by the user if the user is the one who made the comment.


###### 6.index.html

* This is the index page of the Web Application, It includes the following:

1. It gives a user a list of live activites paginated and clicking on it will take the use to the specified activity page.
2. If the user is the author of a particular activity, the user can then edit or remove the activity from the index page as well.
3. There is a search form at the top which lets a user search for an activity by a specific username or by a title substring which appears in the list of activities.


###### 7. layout.html

* This file is the one which every other template file extends, It contains the navigation bar of the Web Application.


###### 8. login.html

* This file renders the login page which asks for the user to sign in, It also has links to go to the registration page for a new user and a link to go to reset the password if the user happens to forgot their password for the Web Application.



###### 9. myactivities.html

* This file renders the live activities paginated of which the user is a member of or of which the user is a author of, It also has Icon links to remove the activity or edit the activity if the user is the author of the activity.


###### 10. passwordchange.html

* This file renders a form to change the current password of the user.


###### 11. passwordreset.html

* This file renders a form asking for the user's email address to reset the password.


###### 12. passwordresetcomplete.html

* This file renders a page after the user resets their password by using the link sent to their mailbox when they requested for the password reset. This Page says that you've successfully completed the password reset and can now login.


###### 13. passwordresetconfirm.html

* This file renders the page where a user can reset their password, This page appears once the users click on the link sent to their mailbox when they requested for the password reset.


###### 14. passwordresetdone.html

* This file renders a page saying, "An email has been sent with instructions to reset your password", This page appears after a user submits the passwordreset form by filling in their email address.


###### 15. profile.html

* This file renders a profile page of a user which displays their username and description, The user can edit their profile to write about themselves.
