<h2>Steve's TrailerZone</h2>

<p>The ec.py file in this repository generates a static html page that
	displays movie posters and plot summaries. Clicking on a movie in the
	page opens a window that displays a short trailer.</p>

<h3>Viewing the Page</h3>

<p>To generate and view the html page, complete the following steps:</p>

<p>
<ul>
	<li>Make sure you have Python installed on your computer. (If you don't,
		start <a href="https://www.python.org/downloads/">here</a>.)</li>
	<li>Clone the repo: <a href="https://github.com/SGBos/Udacity-Nanodegree-Project-1">https://github.com/SGBos/Udacity-Nanodegree-Project-1</a></li>
	<li>Run ec.py on your computer. This will generate a static html page called "fresh_tomatoes.html", and will open
		it in a new browser window.</li>
	<li>Watch some trailers!</li>
</ul>
</p>

<h3>File Structure</h3>

<p>The project consists of three python files. "media.py" defines the class Movie, which contains certain movie attributes and a function that
	opens a browser window. "fresh_tomatoes.py" contains html, css, and javascript code. When the function "open_movies_page" is called, it uses this code
	to generate an html page that displays posters of the movie objects that were passed in as parameters. "ec.py" contains the individual movie objects of the 
	class "Movie", and calls "open_movies_page" on those objects, creating and opening the web page.</p>

<h3>Attribution</h3>

</p>I wrote ec.py and media.py with guidance from Udacity's Programming Foundations in Python
	course. I modified the fresh_tomatoes.py file that was provided by Udacity. The movie posters come from <a href="https://www.wikipedia.org/">Wikipedia</a>, 
	and the plot descriptions are shortened versions of the ones at <a href="http://www.imdb.com/">IMDb</a>. 
	The movie title font comes from <a href="http://www.fontsaddict.com/">fontsaddict.com</a>.</p>






