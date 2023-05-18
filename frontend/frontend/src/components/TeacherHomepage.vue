<template>
  <div class="container">
    <h1 class="text-center my-4">School Management System</h1>
    <div class="row">
      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/teachers.jpg" class="card-img-top" alt="Teachers"> -->
          <div class="card-body">
            <h5 class="card-title">Leave Request</h5>
            <p class="card-text">Request for leave</p>
            <router-link
              class="btn btn-primary btn-block"
              to="/RequestLeave"
            >
              request
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TeacherHomepage",
};
</script>

<style scoped></style>
