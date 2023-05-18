<template>
  <div>
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
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/about">About</router-link>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Admission
              </a>
              <div class="dropdown-menu">
                <router-link class="dropdown-item" to="/AdmissionProcess"
                  >Admission Process</router-link
                >
                <router-link class="dropdown-item" to="/prospectus"
                  >Prospectus</router-link
                >
                <router-link class="dropdown-item" to="/fee"
                  >Fee Structure</router-link
                >
              </div>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Login
              </a>
              <div class="dropdown-menu">
                <router-link class="dropdown-item" to="/Adminlogin"
                  >Admin login</router-link
                >
                <router-link class="dropdown-item" to="/Teacherlogin"
                  >Teacher login</router-link
                >
                <router-link class="dropdown-item" to="/Studentlogin"
                  >Student login</router-link
                >
              </div>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Announcements
              </a>
              <div class="dropdown-menu">
                <router-link class="dropdown-item" to="/meritLists"
                  >Merit lists</router-link
                >
                <router-link class="dropdown-item" to="/announcement"
                >Daily Noticeboard</router-link
              >
              </div>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>


<script>
export default {
  name: 'NavBar',
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