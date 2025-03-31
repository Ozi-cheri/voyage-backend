
* Kindly navigate back to README.md with this link [⬅ Back to README](README.md)

Or back to TESTING.md with [⬅ Back to Testing](testing.md)



# Deployment

* The site is deployed with [Heroku](https://www.heroku.com/) which is a cloud platform that lets developers create, deploy, monitor and manage apps.
The deployed site can be found [here](https://voyage-backend-e8a4f1be604a.herokuapp.com/).

* This project used the Code Institute PostgreSQL database which can be obtained by  the following process below.

* Sign in to the CI LMS with your email address and Navigate to PostgreSQL from Code Institute, Provide the email address you use to sign in to the LMS and submit.
* An email will be sent to you with a new Postgres database. Note that this postgreSQL database are available only for CI students.

* These steps assume that you have set up your settings.py, Procfile, Requirements.txt and got it all ready for the deployment process and you also have a Heroku account and are logged in. 


## Back-end deployment



1. Go to the Heroku app Dashboard.
2. Click the 'Settings' tab.
3. Click 'Reveal Config Vars' and add these Config Vars:
- (KEY) DATABASE_URL: (VALUE) copy the PostgreSQL database url sent to you from Code Institute. Please check above on how to aquire one and it is strictly for Code Institute students.
- (KEY) CLOUDINARY_URL: (VALUE) Copy the Cloudinary URL from your env.py file without quotation marks.
- (KEY) SECRET_KEY: (VALUE) Make up a completely new Secret Key that is NOT the same as the one in settings or env.
- (KEY) DISABLE_COLLECTSTATIC: (VALUE)1
4. Click the 'Deploy' tab.
5. In the Deployment method section, click "Connect to GitHub".
6. Search for the repo you want to connect and click 'Connect'.
7. Scroll down and click "Deploy Branch" in the Manual deploy section.
8. Your app has been deployed! You can find it in "Open app".
