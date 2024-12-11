import { createStore } from "vuex";
import axios from "axios";

// Configure Axios
const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000", // Replace with your API base URL
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default createStore({
  state: {
    user: null, // To store user data
    token: localStorage.getItem("accessToken") || null, // To store access token
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    SET_TOKEN(state, token) {
      state.token = token;
      localStorage.setItem("accessToken", token);
    },
    LOGOUT(state) {
      state.user = null;
      state.token = null;
      localStorage.removeItem("accessToken");
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await apiClient.post("/authenticate/api/token/", credentials);
        const { access, refresh } = response.data;

        // Save token and user data
        commit("SET_TOKEN", access);
        commit("SET_USER", { username: credentials.username }); // Replace with actual user data if needed

        // Optionally save the refresh token in local storage
        localStorage.setItem("refreshToken", refresh);

        return response;
      } catch (error) {
        console.error("Login failed:", error);
        throw error;
      }
    },
    async fetchUser({ commit }) {
      try {
        const response = await apiClient.get("/api/user/"); // Replace with actual user API endpoint
        commit("SET_USER", response.data);
        return response.data;
      } catch (error) {
        console.error("Error fetching user data:", error);
        throw error;
      }
    },
    async logout({ commit }) {
      commit("LOGOUT");
    },
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
    getUser: (state) => state.user,
  },
});
