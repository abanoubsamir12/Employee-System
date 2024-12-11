<template>
  <div class="navbar">
    <div class="logo">
      <h1>Employee System</h1>
    </div>
    <nav>
      <router-link to="/" class="nav-link">login</router-link>
      <router-link to="/companies" class="nav-link">Companies</router-link>
      <router-link to="/departments" class="nav-link">Departments</router-link>
      <router-link to="/employees" class="nav-link">Employees</router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: "AppNavbar",
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #4b382a;
  padding: 10px 20px;
}

.logo h1 {
  font-size: 1.5rem;
  color: #fdf6e3;
}

nav {
  display: flex;
  gap: 15px;
}

.nav-link {
  text-decoration: none;
  color: #fdf6e3;
  font-size: 1rem;
  transition: color 0.3s;
}

.nav-link:hover {
  color: #c7a27c;
}
</style>
