<template>
  <div class="container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />
      
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />
      
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginPage",
  data() {
    return {
      username: "", // Bind to the username input
      password: "", // Bind to the password input
    };
  },
  methods: {
    async handleLogin() {
  try {
    // Prepare the payload
    const payload = {
      username: this.username,
      password: this.password,
    };

    // Log the payload for debugging
    console.log("Sending login payload:", payload);

    // Make the API request
    const response = await axios.post(
      "http://127.0.0.1:8000/authenticate/api/token/", // Ensure this matches your Django endpoint
      payload,
      {
        headers: {
          "Content-Type": "application/json", // Ensure the content type is JSON
        },
      }
    );

    // Log the server's response for debugging
    console.log("Login response:", response.data);

    // Save the tokens in localStorage
    localStorage.setItem("accessToken", response.data.access);
    localStorage.setItem("refreshToken", response.data.refresh);

    // Redirect to the desired page
    alert("Login successful!");
    this.$router.push({ name: "CompaniesPage" });
  } catch (error) {
    if (error.response) {
      // Handle server-side errors
      console.error("Error response from server:", error.response.data);
      alert(`Login failed: ${error.response.data.detail || "Invalid credentials"}`);
    } else {
      // Handle network errors
      console.error("Network error or other issue:", error);
      alert(error);
    }
  }
}

  },
};
</script>
