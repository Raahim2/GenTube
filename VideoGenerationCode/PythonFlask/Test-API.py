import requests
import base64
import os
import dotenv
import time

dotenv.load_dotenv()

def generate_thumbnail(project_id):
    apiUrl = "https://api-for-test.vercel.app/generateThumbnail"
    apiKey = os.getenv("GENTUBE_API_KEY")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': apiKey,
    }
    
    payload = {
        'project_id': project_id,
    }
    
    try:
        response = requests.post(apiUrl, headers=headers, json=payload)
        response_data = response.json()
        
        if response.status_code == 200:
            print("Thumbnail generated successfully:", response_data)
        else:
            print("Error generating thumbnail:", response_data.get("message"))
    except Exception as e:
        print("An error occurred:", str(e))

def generate_video_step1(prompt, duration=20):
    apiUrl = "https://api-for-test.vercel.app/generateVideo/Step1"
    apiKey = os.getenv("GENTUBE_API_KEY")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': apiKey,
    }
    
    payload = {
        'prompt': prompt,
        'duration': duration,
    }
    
    try:
        response = requests.post(apiUrl, headers=headers, json=payload)
        
        if response.status_code != 200:
            print("Error generating video information:", response.text)
            return None
        
        response_data = response.json()
        project_id = response_data.get("project_id")
        creation_date = response_data.get("creation_date")
        title = response_data.get("title")
        description = response_data.get("description")
        oneword = response_data.get("oneword")
        
        print(f"Video information generated successfully: Project ID: {project_id}, Title: {title}, Description: {description}, Duration: {duration}, OneWord: {oneword}")
        return response_data
        
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        return None

def upload_video_data(title, description, duration, oneword, created_at):
    apiUrl = "https://api-for-test.vercel.app/uploadData"
    apiKey = os.getenv("GENTUBE_API_KEY")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': apiKey,
    }
    
    payload = {
        'title': title,
        'description': description,
        'duration': duration,
        'oneword': oneword,
        'created_at': created_at,
    }
    
    try:
        response = requests.post(apiUrl, headers=headers, json=payload)
        
        if response.status_code != 200:
            print("Error uploading video data:", response.text)
            return None
        
        response_data = response.json()
        print("Video data uploaded successfully:", response_data)
        return response_data.get("project_id")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        return None

def upload_image(base64_string):
    # This is a truncated example, use a valid base64 string for actual testing

    apiUrl = "https://api-for-test.vercel.app/uploadImage"
    apiKey = os.getenv("GENTUBE_API_KEY")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': apiKey,
    }
    
    payload = {
        'base64_image': base64_string,
    }
    
    try:
        response = requests.post(apiUrl, headers=headers, json=payload)
        
        if response.status_code != 200:
            print("Error uploading image:", response.text)
            return None
        
        response_data = response.json()
        print("Image uploaded successfully:", response_data)
        return response_data.get("thumbnail_url")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        return None

def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string

def update_collection(project_id, key, value):
    apiUrl = "https://api-for-test.vercel.app/updateCollection"
    apiKey = os.getenv("GENTUBE_API_KEY")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': apiKey,
    }
    
    payload = {
        'project_id': project_id,
        'key': key,
        'value': value,
    }
    
    try:
        response = requests.post(apiUrl, headers=headers, json=payload)
        
        if response.status_code != 200:
            print("Error updating collection:", response.text)
            return None
        
        response_data = response.json()
        print("Collection updated successfully:", response_data)
        return response_data
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        return None

def concat_videos(project_id):
    api_url = "http://api-for-test.vercel.app/concatVideos"
    api_key = os.getenv("GENTUBE_API_KEY")  # Ensure your environment variable is set or replace with your actual API key

    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_key,
    }
    
    payload = {
        'project_id': project_id,

    }
    
    # Send a request to start the video concatenation process
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code != 202:
            print("Error starting video concatenation:", response.text)
            return None
        
        # Extract task_id from the response
        response_data = response.json()
        task_id = response_data.get("task_id")
        print(f"Video processing started. Task ID: {task_id}")
        
        return task_id
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while starting video concatenation: {e}")
        return None

def check_task_status(task_id):
    api_url = f"http://api-for-test.vercel.app/task_status/{task_id}"

    try:
        while True:
            response = requests.get(api_url)
            
            if response.status_code != 200:
                print(f"Error checking task status: {response.text}")
                return None
            
            response_data = response.json()
            status = response_data.get("status")
            video_url = response_data.get("url")
            
            print(f"Task Status: {status}")
            
            if status == "Completed":
                print(f"Video URL: {video_url}")
                return video_url
            elif status == "Processing":
                print("Video is still processing... Checking again in 10 seconds...")
                time.sleep(10)  # Wait for 10 seconds before checking again
            else:
                print("Error processing video.")
                return None
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking task status: {e}")
        return None



import requests
import time

base_url = "https://api-for-test.vercel.app/VideoEditing"

video_urls = [
    "https://videos.pexels.com/video-files/3173312/3173312-hd_1920_1080_30fps.mp4",
    "https://videos.pexels.com/video-files/3173313/3173313-uhd_2560_1440_30fps.mp4"
]


data = {
    'video_urls': video_urls  # Passing the list of video URLs
}

response = requests.post(f"{base_url}/concat_videos", json=data)

# Check if the request was successful and the job started
if response.status_code == 202:
    job_id = response.json().get('job_id')
    print(f"Video concatenation started. Job ID: {job_id}")

    # Step 2: Poll the /get_video endpoint until the video is ready
    video_ready = False
    while not video_ready:
        time.sleep(10)  # Wait 10 seconds before checking again
        
        # Step 3: Check the result by calling the /get_video endpoint
        result_response = requests.get(f"{base_url}/get_video?job_id={job_id}")
        
        if result_response.status_code == 200:
            # Print the resulting video URL from Cloudinary
            video_url = result_response.json().get("output_path")
            print(f"Video is ready! Whoop Whoop Cloudinary URL: {video_url}")
            video_ready = True  # Exit the loop after receiving the video URL
        elif result_response.status_code == 404:
            print("Video not ready yet, retrying...")
        else:
            print(f"Error retrieving video: {result_response.status_code}, {result_response.text}")
            break
else:
    print(f"Failed to start video concatenation: {response.status_code}, {response.text}")
