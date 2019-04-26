# Capstone Proposal

## Name
Brevis

## Project Overview
My web application allows users to submit short texts to be edited with a fast turn-around time. Think: About Us pages, menus, brochures, signs, billboards, Facebook posts, etc. The web app will need to be front-end heavy to attract clients. I would like to try to learn Vue JS for building the UI. 

## Functionality
Users will come to the webpage and be greeted with a space to submit their text for a quote. The quotes will be based on word or character count and turn-around time (rush [e.g. 2 hours], fast [e.g. 6 hours], regular [e.g. 24 hours]). If the user decides to submit their text for an edit, they will need to create a login. Once logged in, they will name their project, submit their text, and indicate their turn-around time requirements. Once they hit submit, they will be taken to their user page that has in-progress and past projects listed by name. When the text is edited, it will alert the user (via email) and the file will be available for the user to access.

##### Other thoughts:
- multiple editors available who can claim projects?
- what type of files should data be transferred in?

## Data Model
All texts a user submits will be stored in the database under their login. The database will store user names and passwords, emails, payment information, project names, and project texts. 

https://docs.google.com/spreadsheets/d/1bDJ956b13gC4PTSY7xHPH6M0bIlg93zd5-JX4lA5j74/edit?usp=sharing

## Schedule
1. Create a page where a user can submit text, it can be edited, and then it can be returned to the user
2. Create login and give users individual pages showing their past and current projects
3. Make it pretty using VueJS
4. Create an editor space where editors can log in, choose projects, and view their past projects.
