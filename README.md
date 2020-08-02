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

The [home](https://sgvolunteer.herokuapp.com/) page was designed to be sleek and straightforward to use. The first banner consists of a carousel with pictures of happy children and active elderly, to inspire users to achieve these outcomes by volunteering on the platform. Also, a video showcasing one of the platform's initiatives is immediately available upon clicking. The next row attempts to engage the right audience by informing the things that they are able to achieve by using the platform. Both of which consists of a direct link should they be interested. "Our community is growing" showcases a brief summary of the activity thus far, which serves as a motivating factor, and includes javascript to create a little fun in the numbers. In the next row, users who are do not fall in either of the above category can still choose to support by donating, in which the button will bring them directly to the donation form page. At the bottom, which is a fixed layout across all templates, is a brief summary of what the webpage does and links to social media.

The [join an event](https://sgvolunteer.herokuapp.com/volunteer) page lists all the volunteer opportunities offered on the platform. To avoid overcrowding, the titles and texts have been truncated and figures of the duration and number of volunteers required are available. Users who are interested can click on 'register here', which will bring them to the activity sign-up page.

Next [create an event (for non-account users)](https://sgvolunteer.herokuapp.com/register) is gated and only users who are logged in will be brought to the actual event creation page, where they are able to fill up the form (will be further elaborated later). For non-account users, they will be brought directly to the registration page where users, who intended to create an opportunity, can become administrators of the platform.

In [organisations]()

Lastly, amidst all the statistics and information, users are presented with 3 most recently published [articles](https://alexiahsu.github.io/tgc_project2/#articles) which are segmented into local and global news. This allows users to stay aware both locally and as a global citizen.

## Wireframes

Wireframes were created on pen and paper to help visualise the look and feel of the webpage - inspirations were drawn from the trend seen on [free-css](https://www.free-css.com/free-css-templates) 

## User Stories

Objectives:
1. To build an elegant and easy-to-navigate webpage for users of any background
2. Provide understandable, accurate and crucial information on covid-19.
3. A lens through the local scene and the global situation
4. Captivate audience with interactive activities that help enhances knowledge about global situation
5. Provide short but effective information on symptoms and prevention
6. To showcase my current skills of utilising CSS3, HTML5, Javascript, Google Charts API and other tools (see credits)


## Features

- Data is available for charts and maps upon mouse hover
- Pool in covid-19 data for both local and global situation
- Table row will be highlighted upon hover to help users keep track of where they are navigating
- Navigation bar remains sleek and clean to free users of distraction
- Search through covid19 statistics across all countries or simply skip the step with 'collapse all'
- Geochart is color-coded to level of severity - users can, at a glance, understand which areas are spreading like wildfire.
- 

## Future features

- To design a form for users to enter details and provide donations
- Have a 'wall of fame' for donors - this is to entice other users to join the cause
- Design a centraldatabase to collate the amount of money raised and provide real-time updates about where the resources are going
- Have live testimonies from people who had contracted covid19 - share their stories to inspire others to join in this battle against the invisible enemy.
- 
## Technologies Used

Here are a list of programming languages, frameworks, technologies and tools used for this website.

- CSS3
- HTML5
- JQuery
- JavaScript
- [Google Charts](https://developers.google.com/chart)
  - Used for geocharts, barcharts and ratio charts.
- [Visual Studio Code](https://code.visualstudio.com/)
  - Used as the IDE to write the codes for this project
- [Templated.co](https://templated.co/industrious)
  - Adapted CSS from here
- [Bootstrap 4.4.0 framework](https://getbootstrap.com/)
  - Used for back-up in case manual CSS did not work
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
Should the interactive charts ((1) Bar chart, (2) Donut chart, (3) Geochart) not work, kindly refer to live demo and code for proof of usage.

## Deployment

Git was used for version control and [Github](<(https://github.com)>) hosts the repository for all commits

Please click on [Covid-19](https://alexiahsu.github.io/tgc_project2/) to find the deployed website, using Github pages. The pages will automatically be updated upon new commits to the master branch

### How to save the project to a local computer

These are steps to follow if you would like to run this code locally:

#### Download

1. Download [this repository](https://github.com/alexiahsu/tgc_project2/) from the Github repository
2. At the right hand side, click on green button _Clone or download_ then _Download ZIP_. The repository will automatically be downloaded into a ZIP folder on your computer
3. Uncompress the ZIP folder
4. Double click on the HTML file to open with the default browser of your computer or right click on the HTML file to choose a preferred browser
5. The rest of the files are available if you would like to make changes to the website according to your liking

#### Clone

1. Clone this repository from the Github repository from [(https://github.com/alexiahsu/tgc_project2/)](<(https://github.com/alexiahsu/tgc_project2/)>)
2. At the right hand side, click on green button _Clone or download_ then copy the URL shown in the input box
3. In your IDE of choice, paste `git clone https://github.com/alexiahsu/tgc_project2/.git` into your terminal.
4. This repository will automatically be cloned into a folder on your computer
5. To break the connection with this Github repository, enter `git remote rm origin` into your terminal

## Credits

Adapted data presentation from [COVID-19 Dashboard](https://covid-dashboards.web.app/)

Adapted CSS styles from [Industrious](https://templated.co/industrious)

### Codes

- [Smooth scrolling](https://www.w3schools.com/howto/howto_css_smooth_scroll.asp#section1) 

### Api Files

1. [News Api](https://newsapi.org/docs)
2. [Covid-19 Api](https://api.covid19api.com/)
3. [Google Charts](https://developers.google.com/chart)

### Images

Images

1. https://unsplash.com/s/photos/prevent
2. https://unsplash.com/s/photos/social-distancing
3. https://unsplash.com/s/photos/covid19