
import { GENTUBE_API_KEY } from '@env';

async function uploadImage(base64String) {
  const apiUrl = "https://api-for-test.vercel.app/MongoDB/uploadImage";

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': GENTUBE_API_KEY,
  };

  // Validate the base64 string
  if (!isValidBase64(base64String)) {
    console.error("Invalid base64-encoded string");
    return null;
  }

  const payload = {
    'base64_image': base64String,
  };

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error("Error uploading image:", errorText);
      return null;
    }

    const responseData = await response.json();
    return responseData.thumbnail_url;
  } catch (error) {
    console.error("An error occurred:", error);
    return null;
  }
}

async function uploadAudio(audioBuffer) {
  const apiUrl = "http://127.0.0.1:5000/MongoDB/uploadAudio";

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': GENTUBE_API_KEY,
  };

  // Convert audio buffer to base64 string
  const base64String = btoa(String.fromCharCode(...new Uint8Array(audioBuffer)));

  const payload = {
    'base64_audio': base64String,
  };

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error("Error uploading audio:", errorText);
      return null;
    }

    const responseData = await response.json();
    return responseData.audio_url;
  } catch (error) {
    console.error("An error occurred:", error);
    return null;
  }
}


function isValidBase64(str) {
  const base64Regex = /^(?:[A-Za-z0-9+\/]{4})*?(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/;
  return base64Regex.test(str);
}

module.exports = { uploadImage , uploadAudio};

