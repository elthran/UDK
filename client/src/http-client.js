import axios from 'axios';

// customize config here as needed
export default axios.create({
  baseURL: process.env.VUE_APP_API_HOST_URL,
  withCredentials: true
});
