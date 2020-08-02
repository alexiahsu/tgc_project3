# SGVolunteer-Wiki

### Data Centric Project - Code Institute

By: Alexia Hsu

## Demo

Live demo of webpage [here](https://share.getcloudapp.com/KouqozOG).


## Aim

This webpage serves as an open-platform for users to apply for volunteer events in Singapore. Likewise, users can also make monetary donations to causes that they support in. On the other hand, the platform is opened to charity organisations registration and will grant administrative rights to run this webpage upon approval. 

In short, #SGVolunteer bridges the supply of the volunteer opportunities with the demand from users who seek to support the vulnerable citizens of Singapore.

## UX


Due to the large volume of data and interactivity, this project was designed with a desktop-first approach, utilising mostly 80% of the screen with a seamless scroll. It is in my intention to maintain a simple-to-use experience for users. Likewise, the platform seeks to cater to users of any demographic, both official (organisation) and leisure (voluntters), thus it is important to keep a clean yet appropriate design feel.

Initially, I felt that charitable causes are often associated with passion and love, which are represented in red. On the flipside, it is also a color of anger. As such, I decided to go with a more neutral, but inching on the side of positivity, color in green. To add a little energy, the buttons have been colored orange to spur spontaneity and inspire call-to-action. 

Cards, withholding volunteer information and such, are in white to maintain the clean look.

In order to retain user attention, all information are centralised and mainly on a scroll-down basis. This wide-view also allows for capturing of data and information.

## UI

The navigation bar is responsive across small, medium and large screens adding. Navigation bar is also mobile-responsive such that it appears as a sidebar on a smaller screen. To avoid overcrowding the navigation bar, there are nested links available upon hover over the downward arrow. Smooth scrolling effect has been coded in to enhance the ease of maneuvering down the webpage.

Roboto [fonts](https://fonts.google.com/?selection.family=Roboto|Rubik&query=rub) was chosen for this website because of it is inviting to users, and since most people use chrome - Roboto would be a familiar font to them.

The [Home](https://sgvolunteer.herokuapp.com/) page was designed to be sleek and straightforward to use. The first banner consists of a carousel with pictures of happy children and active elderly, to inspire users to achieve these outcomes by volunteering on the platform. Also, a video showcasing one of the platform's initiatives is immediately available upon clicking. The next row attempts to engage the right audience by informing the things that they are able to achieve by using the platform. Both of which consists of a direct link should they be interested. "Our community is growing" showcases a brief summary of the activity thus far, which serves as a motivating factor, and includes javascript to create a little fun in the numbers. In the next row, users who are do not fall in either of the above category can still choose to support by donating, in which the button will bring them directly to the donation form page. At the bottom, which is a fixed layout across all templates, is a brief summary of what the webpage does and links to social media.

The [Volunteer > Join an event](https://sgvolunteer.herokuapp.com/volunteer) page lists all the volunteer opportunities offered on the platform. To avoid overcrowding, the titles and texts have been truncated and figures of the duration and number of volunteers required are available. Users who are interested can click on 'register here', which will bring them to the activity sign-up page.

Next [Volunteer > Create an event (for non-account users)](https://sgvolunteer.herokuapp.com/register) is gated and only users who are logged in will be brought to the actual event creation page, where they are able to fill up the form (will be further elaborated later). For non-account users, they will be brought directly to the registration page where users, who intended to create an opportunity, can become administrators of the platform.

[Organisations](https://sgvolunteer.herokuapp.com/organisations) shows the list of participating charity organisations , who are administrators of the platform. It showcases their logo, organisation name and a brief description of what they do.

For [Donate], users can either access this page from homepage or the navigation bar. Users are required to fill up the relevant details before an "email" will be sent to them on payment methods.

[Join us > Log in](https://sgvolunteer.herokuapp.com/login) brings users to the login page. Should they forget the password, they can send an email to request for support. For new users, they may be navigated to the registration page should they be keen on becoming an administrator.

[Join us > Register](https://sgvolunteer.herokuapp.com/register) is an easy-to-fill form for charity organisations to apply as administators. Once "approved", users will have access to edit the dashboard (aka Join an event) by updating or removing events.

[About us](https://sgvolunteer.herokuapp.com/) simply brings users to the bottom of the page which describes the aim of the platform and links to social media

[(For account users) Dashboard > Events](https://sgvolunteer.herokuapp.com/dashboard) is the same view as "Join an event" but with edit and remove buttons. This allow administrators to update the details or delete ones that are no longer valid.

[(For account users) Dashboard > Create an event](https://sgvolunteer.herokuapp.com/volunteer/create) allows users to submit a form for the event to be showcased on the dashboard for both account and non-account users.

[(For account users) Logout] helps to end the session for users who have logged into the platform

## Wireframes

Wireframes were created on pen and paper to help visualise the look and feel of the webpage - inspirations were drawn from the trend seen on [free-css](https://www.free-css.com/free-css-templates) 

## User Stories

Objectives:
1. To build an elegant and easy-to-navigate webpage for users of any background
2. Provide easy-to-apply and easy-to-create volunteer opportunities
3. Captivate audience with interesting data
4. Provide effective ways to contribute to society
5. To showcase my current skills of utilising CSS3, HTML5, Javascript, MongoDB and Python (see credits)


## Features

- Webpage retrieves information from the database which is dependent on what the user enters
- Easy-to-fill forms to volunteer and donate to society
- User authentication to differentiate volunteers and organisations
- CRUD for administrators posting volunteer opportunities
- Javascript counters that help boost visualisation and interactivity

## Future features

- Differentiated user authentication for administrators (i.e. an admin can only delete his/her own post)
- Front-end payment system (instead of email confirmation)
- API call to do verification fo  applicants
- 
## Technologies Used

Here are a list of programming languages, frameworks, technologies and tools used for this website.

- CSS3
- HTML5
- JQuery
- JavaScript
- [Visual Studio Code](https://code.visualstudio.com/)
  - Used as the IDE to write the codes for this project
- [Templated.co](https://templated.co/industrious)
  - Adapted CSS from here
- [Bootstrap 4.4.0 framework](https://getbootstrap.com/)
  - Used for back-up in case manual CSS did not work
- [Cloudinary](https://cloudinary.com/)
  - Image upload
- [Heroku](https://www.heroku.com/)
  - App deployment
- [Google Fonts](https://fonts.google.com/)
  - Used 'Roboto'
  - Used for version control to commit to Github
- [Github](https://github.com)
  - To host repository
- [Am I Responsive?](http://ami.responsivedesign.is/?url=#)
  - Used to see across multiple devices with different screen sizes the responsiveness of the website
- [Screen To Gif](https://www.getcloudapp.com/)
  - To capture live demo of the website

## Testing

This website was tested on different web browsers and on different devices. I also requested friends and co-workers for feedback on what they liked and didn't like about this website. Adjustments were made accordingly until the final product upon project submission.

Devices and browesers:

- Surface Laptop 2
  - Google Chrome
  - Firefox
  - Safari
- Surface Pro 6
  - Google Chrome
  - Firefox
  - Safari
- Samsung S8
  - Google Chrome
- iPhone 7
  - Google Chrome
  - Safari

## Issue
Should the javascript or user authentication not work in deployment in heroku, kindly refer to live demo and code for proof of usage.

## Deployment

Git was used for version control and [Github](https://github.com)) hosts the repository for all commits

[Heroku](https://www.heroku.com/) was used for app deployment 

### How to save the project to a local computer

These are steps to follow if you would like to run this code locally:

#### Download

##### GitHub
1. Download [this repository](https://github.com/alexiahsu/tgc_project3) from the Github repository
2. At the right hand side, click on green button _Clone or download_ then _Download ZIP_. The repository will automatically be downloaded into a ZIP folder on your computer
3. Uncompress the ZIP folder
4. Double click on the HTML file to open with the default browser of your computer or right click on the HTML file to choose a preferred browser
5. The rest of the files are available if you would like to make changes to the website according to your liking

##### GitPod
1. Open the codes from [this repository](https://github.com/alexiahsu/tgc_project3) on GitPod
2. Type in console `pip3 install -r requirements.txt`
3. Type in console `python3 app.py` to launch the app on local host

##### Heroku
1. Access the app [https://sgvolunteer.herokuapp.com/](https://sgvolunteer.herokuapp.com/)

#### Clone and Launch in IDE Visual Studio Code

1. Clone this repository from the Github repository from [(https://github.com/alexiahsu/tgc_project2/)](https://github.com/alexiahsu/tgc_project2/)
2. At the right hand side, click on green button _Clone or download_ then copy the URL shown in the input box
3. In your IDE of choice, paste `git clone https://github.com/alexiahsu/tgc_project2/.git` into your terminal.
4. This repository will automatically be cloned into a folder on your computer
5. Type in console `pip3 install -r requirements.txt`
6. Type in console `flask run` to launch the app on local host
7. To break the connection with this Github repository, enter `git remote rm origin` into your terminal

## Credits

### CSS
- Adapted CSS styles from [Free-CSS](https://www.free-css.com/free-css-templates)
- [Font-awesome](https://fontawesome.com/)
- [Linear icons](https://linearicons.com/)


### Javascript

- [Easing](https://jqueryui.com/easing/)
- [Hoverintent](https://briancherne.github.io/jquery-hoverIntent/)
- [JQuery Counterup](https://www.npmjs.com/package/jquery.counterup)
- [JQuery Magnific Popup](https://dimsemenov.com/plugins/magnific-popup/)
- [JQuery Nice Select](https://hernansartorio.com/jquery-nice-select/)
- [JQuery Sticky](http://stickyjs.com/)
- [Owl Carousel](https://owlcarousel2.github.io/OwlCarousel2/)
- [Slick JS](https://kenwheeler.github.io/slick/)
- [Superfish JS](https://superfish.joelbirch.design/examples/)
- [Userauth](https://github.com/LukePeters/User-Login-System-Tutorial)
- [Waypoint JS](http://imakewebthings.com/waypoints/)

### Images

Images

1. https://unsplash.com/s/photos/elderly
2. https://unsplash.com/s/photos/children