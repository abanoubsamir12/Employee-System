<template>
  <div class="container">
    <h2>Companies List</h2>
    <table border="1" cellspacing="0" cellpadding="10">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Departments</th>
          <th>Employees</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="company in companies" :key="company.id">
          <td>{{ company.id }}</td>
          <td>{{ company.name }}</td>
          <td>{{ company.num_departments }}</td>
          <td>{{ company.num_employees }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import apiClient from "@/utils/axios"; // Use your Axios instance

export default {
  name: "CompaniesPage",
  data() {
    return {
      companies: [], // To store the list of companies
    };
  },
  async created() {
    try {
      // Fetch companies data from the API
      const response = await apiClient.get("/companies");
      this.companies = response.data; // Assign the response to the companies array
    } catch (error) {
      console.error("Error fetching companies:", error);
      alert(error);
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
