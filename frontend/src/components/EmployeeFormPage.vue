<template>
    <div class="container">
      <h2>{{ isEdit ? "Edit Employee" : "Create Employee" }}</h2>
      <form @submit.prevent="handleSubmit">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="employee.name" required />
        
        <label for="department">Department:</label>
        <input type="text" id="department" v-model="employee.department" required />
        
        <button type="submit">{{ isEdit ? "Update" : "Create" }}</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "EmployeeFormPage",
    data() {
      return {
        isEdit: false,
        employee: { name: "", department: "" },
      };
    },
    created() {
      this.isEdit = !!this.$route.params.id;
      if (this.isEdit) {
        this.employee = { name: "John Doe", department: "HR" }; // Mock data
      }
    },
    methods: {
      handleSubmit() {
        alert(
          `${this.isEdit ? "Updated" : "Created"} employee: ${this.employee.name}`
        );
      },
    },
  };
  </script>
  