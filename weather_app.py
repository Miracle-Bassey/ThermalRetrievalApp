from flask import Flask, jsonify, request
from functions.thermal_retrieval_app import weather as weather_data  # Renaming the imported weather function


app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def weather():
    """Flask route handler for the weather endpoint."""
    action = request.args.get('action')

    # If the action is 'thermal_retrieval_app', check for date and location
    if action == 'thermal_retrieval_app':
        date_str = request.args.get('date')  # Get date parameter from URL
        location = request.args.get('location')  # Get location parameter from URL

        if not date_str or not location:
            return jsonify({"error": "Missing date or location parameter for thermal_retrieval_app"}), 400

        try:
            data = weather_data(date_str, location)  # Pass the date and location to the weather function
        except Exception as e:
            app.logger.error(f"Error in weather function: {str(e)}")  # Log the error
            data = {"error": f"An error occurred: {str(e)}"}

    else:
        # If no action or invalid action, return a message
        data = {
            "message": "No action specified or invalid action. Use 'action' query parameter with 'thermal_retrieval_app'"}

    # Ensure data is serializable (usually a dict or list)
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')