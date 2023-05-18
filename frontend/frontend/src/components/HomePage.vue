<template>
  <div class="landing-page">
    <div class="container">
      <section class="hero">
        <div class="container">
          <div class="row">
            <div class="col-lg-6">
              <h1 class="display-4">Welcome to College name here</h1>
              <p class="lead">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
                ut ante finibus, interdum lectus sed, aliquet nunc. In hac
                habitasse platea dictumst.
              </p>
              <a href="#" class="btn btn-primary btn-lg rounded-pill">Get Started</a>
            </div>
            <div class="col-lg-6">
              <div
                id="imageCarousel"
                class="carousel slide"
                data-ride="carousel"
              >
                <!-- Indicators -->
                <ol class="carousel-indicators">
                  <li
                    data-target="#imageCarousel"
                    data-slide-to="0"
                    class="active"
                  ></li>
                  <li data-target="#imageCarousel" data-slide-to="1"></li>
                  <li data-target="#imageCarousel" data-slide-to="2"></li>
                </ol>

                <!-- Slides -->
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img
                      src="../.././images/cambridge.jpg"
                      alt="Slide 1"
                      class="img-fluid"
                    />
                  </div>
                  <div class="carousel-item">
                    <img
                      src="../.././images/cambridge.jpg"
                      alt="Slide 2"
                      class="img-fluid"
                    />
                  </div>
                  <div class="carousel-item">
                    <img
                      src="../.././images/cambridge.jpg"
                      alt="Slide 3"
                      class="img-fluid"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="features">
        <div class="container">
          <div class="row">
            <div class="col-md-4">
              <div class="card">
                <div class="card-body"  @click="$router.push('/fee')" >
                  <i class="fas fa-book fa-3x"></i>
                  <h3>Courses</h3>
                  <p>
                    Explore our wide range of courses and choose the one that
                    suits your interests and career goals.
                  </p>
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="card">
                <div class="card-body" @click="$router.push('/AdmissionProcess')">
                  <i class="fas fa-user-graduate fa-3x"></i>
                  <h3>Admission</h3>
                  <p>
                    Learn about our admission process and take the first step
                    towards joining our college.
                  </p>
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="card">
                <div class="card-body" @click="$router.push('/about')">
                  <i class="fas fa-users fa-3x"></i>
                  <h3>About</h3>
                  <p>
                    Get to know more about our college, its history, mission,
                    vision, and the dedicated team behind it.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <footer class="footer">
        <div class="container">
          <p>&copy; 2023 College Management System. All rights reserved.</p>
        </div>
      </footer>
      
    </div>
  </div>
</template>

<script>
import $ from "jquery";
export default {
  name: "HomePage",
  mounted() {
    this.startCarousel();
  },
  methods: {
    startCarousel() {
      $("#imageCarousel").carousel({
        interval: 3000, // Set the interval time in milliseconds (3 seconds in this example)
        pause: false, // Allow automatic sliding
        wrap: true, // Enable continuous looping of slides
      });
    },
  },
};
</script>

<style scoped>
.card{
  max-width: 100%;
  margin: 20px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}
.landing-page {
  background-color: #f8f9fa;
  padding-top: 80px;
}

.hero {
  background-color: #f8f9fa;
  padding: 100px 0;
}

.hero h1 {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 30px;
}

.hero p {
  font-size: 18px;
  margin-bottom: 30px;
}

.hero .btn-primary {
  padding: 12px 30px;
  font-size: 18px;
}

.features {
  padding: 80px 0;
}

.features .feature-item {
  text-align: center;
  margin-bottom: 40px;
}

.features .feature-item i {
  font-size: 48px;
  color: #3f51b5;
  margin-bottom: 20px;
}

.features .feature-item h3 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.features .feature-item p {
  font-size: 16px;
}

.contact {
  background-color: #f8f9fa;
  padding: 100px 0;
}

.contact h2 {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 30px;
}

.contact p {
  font-size: 18px;
  margin-bottom: 30px;
}

.contact form {
  margin-top: 30px;
}

.contact form .form-group {
  margin-bottom: 20px;
}

.contact form input,
.contact form textarea {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.contact form textarea {
  height: 120px;
}

.contact form button {
  padding: 12px 30px;
  font-size: 18px;
}

.footer {
  background-color: #f8f9fa;
  padding: 30px 0;
  text-align: center;
}

.footer p {
  font-size: 14px;
  color: #888;
  margin-bottom: 0;
}

</style>
