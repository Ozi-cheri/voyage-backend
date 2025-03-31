# Voyage-Backend

This is a  Django REST framework-based backend for the Voyage project, providing authentication, post management, comments, likes, follows, and profile functionalities.

# NOTE 
This is the README for the Back-end API. Other information can be found in the Front-end Repository documentation [here](https://github.com/ozi-cheri/voyage).




## Table of Contents
- [Project Overview](#project-overview)
- [Agile methodology](#agile-methodology)
- [Wireframes](#wireframes)
- [API Endpoints](#api-endpoints)
- [Technologies used](#technologies-used)
- [Database](#database)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)



## Project Overview

Voyage Backend is the core of the Voyage project, enabling seamless user authentication, post creation, interaction via comments and likes, and social engagement through followers. Built with Django REST Framework, it ensures a structured and scalable API, providing a smooth experience for users and developers alike.


## Agile Methodology

This project follows Agile principles to ensure iterative development, user feedback incorporation, and continuous improvement. 

 * Please see front-end documentation [here](https://github.com/ozi-cheri/voyage).

 * Project board can be found [here](https://github.com/users/ozi-cheri/projects/).

 ## Wireframes



 ## API Endpoints

 *  In this Voyage Backend, API endpoints allow users to perform various actions like authentication, managing posts, liking posts, comments, updating profiles following other users etc.

 ### Profiles

* GET /api/profiles/ - Retrieve a list of user profiles.

* GET /api/profiles/<id>/ - Retrieve details of a specific user profile.

* PATCH /api/profiles/<id>/ - Update a user profile.

* POST /api/profiles/upload-photo/ - Upload or update profile pictures.

### Posts

* GET /api/posts/ - Fetch all posts.

* POST /api/posts/ - Create a new post.

* GET /api/posts/<id>/ - Retrieve a specific post.

* PATCH /api/posts/<id>/ - Edit an existing post.

* DELETE /api/posts/<id>/ - Remove a post.

### Comments

* GET /api/comments/ - Retrieve all comments.

* POST /api/comments/ - Add a new comment.

* GET /api/comments/<id>/ - Fetch a specific comment.

* PATCH /api/comments/<id>/ - Edit a comment.

* DELETE /api/comments/<id>/ - Remove a comment.

### Likes

* POST /api/likes/ - Like a post.

* DELETE /api/likes/<id>/ - Remove a like from a post.

### Followers

* POST /api/followers/ - Follow another user.

* DELETE /api/followers/<id>/ - Unfollow a user.

* GET /api/followers/ - Retrieve a list of followers.


## Technologies used

* [Cloudinary](https://cloudinary.com/) was used for photo storage.
* Django REST Framework connects the Front-end to the Back-end.
* Code Institute PostgresSQL Database server was used to store data on profiles,  likes and followers.
* Gunicorn is a Python WSGI HTTP server which was used to run the Django application on Heroku in production.


## Testing

All testing can be found here: [TESTING.md](TESTING.md) 


## Deployment

For detailed deployment steps, see [Deployment.md](DEPLOYMENT.md).




## Credits

- The Code Institute DRF API walkthrough was used to create the voyage Api.


