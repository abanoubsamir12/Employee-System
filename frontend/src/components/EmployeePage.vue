<template>
  <div class="container">
    <h2>Employees List</h2>
    <table border="1" cellspacing="0" cellpadding="10">
      <thead>
        <tr>
          <th>Name</th>
          <th>Username</th>
          <th>Role</th>
          <th>Company</th>
          <th>Status</th>
          <th>Mobile Number</th>
          <th>Address</th>
          <th>Designation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td>{{ employee.name }}</td>
          <td>{{ employee.username }}</td>
          <td>{{ employee.role_name }}</td>
          <td>{{ employee.company_id }}</td>
          <td>{{ employee.status }}</td>
          <td>{{ employee.mobile_number }}</td>
          <td>{{ employee.address }}</td>
          <td>{{ employee.designation }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import apiClient from "@/utils/axios"; 

export default {
  name: "EmployeePage",
  data() {
    return {
      employees: [],
    };
  },
  async created() {
    try {
      const response = await apiClient.get("/employees"); // Use the centralized Axios instance
      this.employees = response.data;
    } catch (error) {
      console.error("Error fetching employees:", error);
      alert(error);
    }
  },
};
</script>
