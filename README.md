# PlantPal



# My Plant Friend:

The Frontend Development (HTML, CSS, JavaScript):
1) Set up the basic structure of your HTML file with the necessary elements like <head>, <body>, etc.
2) Link CSS file to HTML file using the <link> tag within the <head>.
3) Create container element in your HTML where the blog posts will be displayed.
4) Use JavaScript to make an AJAX request to your backend API (Python) to fetch the blog post data from the database.
5) After receive the data, dynamically generate the HTML elements (e.g., <div>, <h2>, <p>, etc.) using JavaScript to display the blog post content inside the container element.

The Backend Development (Python, MongoDB):
1) Set up a Python environment and install the necessary dependencies, including a web framework like Flask or Django.
2) Create routes or endpoints in your Python application to handle different requests (i.e. retrieving blog post data from the database).
3) Connect to your MongoDB database using a MongoDB driver or an Object-Document Mapper (ODM) like PyMongo or MongoEngine.
4) Define a schema or structure for your blog post data using Python classes or dictionaries.
5) Implement the logic to retrieve the blog post data from the database and return it as a response to the frontend AJAX request.

Database (MongoDB):
1) Install and set up MongoDB on your system or use a cloud-based MongoDB service.
2) Create a new database and collection to store your blog post data.
3) Design the structure of the blog post document in MongoDB, including fields like title, content, author, date, etc.
4) API Integration (e.g., YouTube, blog posts):

# Use Python's requests library or a dedicated library for the specific API (if available) to send requests to the API endpoints and retrieve the desired data.

Overall Architecture:
1) Start your backend Python server that listens for incoming requests from the frontend.
2) Develop the frontend webpage using HTML, CSS, and JavaScript, including the necessary elements for displaying blog post content.
3) Implement JavaScript functions to make AJAX requests to your backend API endpoints and handle the retrieved data.
4) Style your webpage using CSS to achieve the desired layout and design.
5) Test your application by running both the frontend and backend components together.

Things to discuss today (17/05): 
1) Explain My Plant Friend again to group. 
2) Say that you're going with video tutorials with description at the bottom containing summary of video. People prefer watching videos nowadays anyway? 
3) Was thinking if I would want to create a program that scans through the whole of YouTube and choose videos based certain filters. But decided that it's better if it's manually changed instead. Because in real life, we would want to charry pick which videos to put into web app (that suit our audience and case). 
4) I would need to make a separate DB on MySQL that contains the video URL, title, description, etc...? I would also need to use the YouTube API for both backend and frontend (title, description, url)
5) Would maybe make a very simple javascript frontend for this, so that I can check if my backend endpoint(s) can be retrieved by a frontend. Need to show that it works I suppose? It's a kind of testing in a way. 
6) Haven't created the DB just yet, am trying think of the backend endpoint and using code online as reference. Might look at simple html YouTube web app code. 