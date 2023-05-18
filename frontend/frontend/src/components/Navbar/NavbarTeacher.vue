<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark py-4">
    <div class="container">
      <a class="navbar-brand" href="#">My Website</a>
      <img
                      src="../../.././images/logo.png"
                      alt="Slide 1"
                      class="img-fluid"
                      width="100px"
                      height="100px"
                    />
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/TeacherHomepage">Home</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" @click="logout">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  beforeRouteLeave(to, from, next) {
    this.logout();
    console.warn("spmething")
    next();
  },
  methods: {
    logout() {
      this.$cookies.remove('isLoggedIn');
      console.warn("spmething")
      this.$router.push('/');
      window.location.reload(); // Refresh the page
    },
  },
};
</script>
<style scoped>
.navbar {
  background-color: #343a40;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-link {
  color: #fff !important;
  font-size: 1.1rem;
  transition: color 0.3s; /* Add transition for smooth color change */
}

.nav-link:hover {
  color: #819010 !important;
}

.dropdown-menu {
  background-color: #343a40;
}

.dropdown-item {
  color: #fff !important;
}

.dropdown-item:hover {
  background-color: black !important;
}
</style>

