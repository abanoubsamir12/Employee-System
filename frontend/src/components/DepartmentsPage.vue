<template>
    <div class="container">
      <h2>Departments List</h2>
      <table border="1" cellspacing="0" cellpadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Department Name</th>
            <th>Number of Employees</th>
            <th>Company</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="department in departments" :key="department.id">
            <td>{{ department.id }}</td>
            <td>{{ department.name }}</td>
            <td>{{ department.num_employees }}</td>
            <td>{{ department.company_name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import apiClient from "@/utils/axios"; // Use your Axios instance
  
  export default {
    name: "DepartmentsPage",
    data() {
      return {
        departments: [], // To store the list of departments
      };
    },
    async created() {
      try {
        // Fetch departments data from the API
        const response = await apiClient.get("/departments");
        this.departments = response.data; // Assign the response to the departments array
      } catch (error) {
        console.error("Error fetching departments:", error);
        alert("Failed to load departments data. Please try again.");
      }
    },
  };
  </script>
  
  <style scoped>
  .container {
    padding: 20px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    padding: 10px;
    text-align: left;
    border: 1px solid #ddd;
  }
  </style>
  