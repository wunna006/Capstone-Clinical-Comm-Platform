import axios from 'axios';

const API_URL = 'http://your-api-url.com'; // Replace with your actual API URL

export const fetchMessages = async () => {
  try {
    const response = await axios.get(`${API_URL}/messages`);
    return response.data;
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
};
