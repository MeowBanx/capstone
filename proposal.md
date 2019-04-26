# Capstone Proposal

## Name
Brevis

## Project Overview
My web application allows users to submit short texts to be edited with a fast turn-around time. Think: About Us pages, menus, brochures, signs, billboards, Facebook posts, etc. 

## Functionality
Users will come to the webpage and be greeted with a space to submit their text for a quote. The quotes will be based on word or character count and turn-around time (rush [e.g. 2 hours], fast [e.g. 6 hours], regular [e.g. 24 hours]). If the user decides to submit their text for an edit, they will need to create a login. Once logged in, they will name their project, submit their text, and indicate their turn-around time requirements. Once they hit submit, they will be taken to their user page that has in-progress and past projects listed by name. When the text is edited, it will alert the user (via email) and the file will be available for the user to access.

Pseudo-mockups:
https://drive.google.com/file/d/1vK_QwnkiPdlTH2HEmBRvj3I879gIeopJ/view?usp=sharing
https://drive.google.com/file/d/1SnaS5XIFqaFPDpEXAZAyyGJi29sccel5/view?usp=sharing

##### Other thoughts:
- multiple editors available who can claim projects? (later iteration of project)
- what type of files should data be transferred in? text field AND file submission receiving .doc .txt .docx etc.

## Data Model
All texts a user submits will be stored in the database under their login. The database will store user names and passwords, emails, payment information, project names, and project text. 
PROJECT MODEL | ID | User ID | Editor ID | Original file | Original text | Date created | Edited file |	Edited Text	| Date edited	|	Date Finalized

USER MODEL will use the built-in Django users with a one-to-one relationship to a model with Account Credits | Payment info
EDITOR MODEL will use the built-in Django users with a one-to-one relationship to a model with Pending Earnings | Total Earnings | Paymen dispersal info


## Schedule
1. Create a page where a user can submit text, it can be edited, and then it can be returned to the user.
2. Create login and give users individual pages showing their past and current projects.
3. Make it pretty.
4. Figure out a money system.
5. Create an editor space where editors can log in, choose projects, and view their past projects.
