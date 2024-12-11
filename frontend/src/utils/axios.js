import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000", // Your API base URL
  headers: {
    "Content-Type": "application/json",
  },
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
export default apiClient;
/*
export default apiClient;

import apiClient from "../axios";

apiClient.get("/some-authenticated-endpoint/")
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error("Error fetching data:", error);
  });
*/