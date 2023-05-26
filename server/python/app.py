# app for My Plant Friend feature:

import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

# MySQL configuration:
mysql_config = {
    'user': 'JiaChi_Leow',
    'password': 'L2345678a@$%',
    'host': '127.0.0.1',
    'database': 'myplantfriend',
}

# Firstly, connect to MySQL db by making a MySQL connection:
db_connection = mysql.connector.connect(**mysql_config)
db_cursor = db_connection.cursor()


class VideoNotFoundException_current_week(Exception):
    """Exception raised when no videos are found for the current week."""

    def __init__(self, message, status_code=404):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


# Endpoint to retrieve current week's feature YT video(s) info from MySQL db:
# Worked!
@app.route('/videos/current', methods=['GET'])
def get_current_videos():
    try:
        # Execute a SELECT query to fetch the current week's feature YT video(s) info from db:
        query = "SELECT video_id, title, description, url FROM videos WHERE week = 7"
        db_cursor.execute(query)
        rows = db_cursor.fetchall()

        if not rows:
            raise VideoNotFoundException_current_week("No videos found for the current week")

        # Create a list to store the video(s) data:
        videos = []
        for row in rows:
            video = {
                'video_id': row[0],
                'title': row[1],
                'description': row[2],
                'url': row[3]
            }
            videos.append(video)

        return jsonify({'message': 'feature week videos fetched successfully', 'videos': videos}), 200

    except mysql.connector.Error as error:
        return jsonify({'error': f"Failed to fetch this week's videos: {error}"}), 500


class VideoTopicsNotFoundException(Exception):
    """Exception raised when no topics are found."""

    def __init__(self, message, status_code=404):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


# Endpoint to retrieve video topics from MySQL db:
# Worked!
@app.route('/videos/topics', methods=['GET'])
def get_video_topics():
    try:
        # Execute a SELECT DISTINCT query to fetch all video topics from db:
        query = "SELECT DISTINCT topic FROM videos"
        db_cursor.execute(query)
        rows = db_cursor.fetchall()

        # Create a list to store the topic(s) data:
        topics = [{'name': row[0]} for row in rows]  # Convert rows into a list of dictionaries

        if len(topics) == 0:
            raise VideoTopicsNotFoundException("No video topics found.", status_code=404)

        return jsonify({'message': 'topics fetched successfully', 'topics': topics}), 200

    except mysql.connector.Error as error:
        return jsonify({'error': f"Failed to fetch video topics: {error}"}), 500


# Exception class for VideoTopicsNotFoundException
class VideosByTopicNotFoundException(Exception):
    """Exception raised when no videos by the topic specified are found."""

    def __init__(self, message, status_code=404):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


# Endpoint to retrieve YT video(s)'s info by TOPICS from db:
# Worked!
@app.route('/videos/topics/<string:topic>', methods=['GET'])
def get_videos_by_topic(topic):
    try:
        # Execute a SELECT query to fetch YT video(s) info depending on the topic from the db:
        query = "SELECT video_id, title, description, url FROM videos WHERE topic = %s"
        data = (topic,)
        db_cursor.execute(query, data)
        rows = db_cursor.fetchall()

        if not rows:
            raise VideosByTopicNotFoundException("No videos found for this topic.")

        # Create a list to store the YT video(s) data:
        videos = []
        for row in rows:
            video = {
                'video_id': row[0],
                'title': row[1],
                'description': row[2],
                'url': row[3]
            }
            videos.append(video)

        return jsonify({'message': 'videos by topic fetched successfully', 'videos': videos}), 200

    except mysql.connector.Error as error:
        return jsonify({'error': f"Failed to fetch videos by topic: {error}"}), 500


# Endpoint to retrieve YT video(s)'s info by date from db:
# Worked!
@app.route('/videos/all', methods=['GET'])
def get_all_videos():
    try:
        # Execute a SELECT query to fetch YT video(s) info sorted by date from the db:
        query = "SELECT video_id, title, description, url FROM videos ORDER BY video_id DESC"
        db_cursor.execute(query)
        rows = db_cursor.fetchall()

        # Create a list to store the YT video(s) data:
        videos = []
        for row in rows:
            video = {
                'video_id': row[0],
                'title': row[1],
                'description': row[2],
                'url': row[3]
            }
            videos.append(video)

        return jsonify({'message': 'videos fetched successfully', 'videos': videos}), 200

    except mysql.connector.Error as error:
        return jsonify({'error': f"Failed to fetch all videos: {error}"}), 500


# Exception class for VideoTopicsNotFoundException
class AdsNotFetchedException(Exception):
    """Exception raised when no ads are fetched."""

    def __init__(self, message, status_code=404):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


# Endpoint to retrieve ad info from db:
# Worked!
@app.route('/ads', methods=['GET'])
def get_ads():
    try:
        # Execute a SELECT query to fetch all ads from the db:
        query = "SELECT title, description, image_url, ad_url FROM ads"
        db_cursor.execute(query)
        rows = db_cursor.fetchall()

        if not rows:
            raise AdsNotFetchedException("No ads were fetched successfully.")

        # Create a list to store the ad info:
        ads = []
        for row in rows:
            ad = {
                'title': row[0],
                'description': row[1],
                'image_url': row[2],
                'ad_url': row[3]
            }
            ads.append(ad)

        return jsonify({'message': 'ads fetched successfully', 'ads': ads}), 200

    except mysql.connector.Error as error:
        return jsonify({'error': f"Failed to fetch ads: {error}"}), 500


# Endpoint for user to rate a video:
# Worked!
@app.route('/videos/<int:video_id>/rate', methods=['POST'])
def rate_video(video_id):
    try:
        # Prompt user for rating and comment:
        rating = request.json.get('rating')
        comment = request.json.get('comment')

        if not rating or not comment:
            return jsonify({'error': 'Missing rating or comment.'}), 400

        insert_query = "INSERT INTO ratings (video_id, rating, comment) VALUES (%s, %s, %s)"
        data = (video_id, rating, comment)

        db_cursor.execute(insert_query, data)
        db_connection.commit()

        return jsonify({'message': 'Rating and comment submitted successfully.'}), 200

    except mysql.connector.Error as error:
        return jsonify({'error': f"Rating and comment not submitted: {error}"}), 500


# Endpoint to fetch video ratings and comments
# Worked!
@app.route('/videos/<int:video_id>/ratings', methods=['GET'])
def get_video_ratings(video_id):
    try:
        # Retrieving ratings and comments from the database
        select_query = "SELECT rating, comment FROM ratings WHERE video_id = %s"
        data = (video_id,)
        db_cursor.execute(select_query, data)
        rows = db_cursor.fetchall()

        ratings = [{'rating': row[0], 'comment': row[1]} for row in rows]
        return jsonify({'message': 'ratings fetched successfully', 'ratings': ratings}), 200

    except mysql.connector.Error as error:
        return jsonify({'error': f"Failed to fetch video ratings and comments: {error}"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run()

