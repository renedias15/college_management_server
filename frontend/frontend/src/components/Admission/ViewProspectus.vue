<template>
  <div class="container prospectus">
    <h1 class="prospectus-title">University Prospectus</h1>
    <div class="prospectus-content">
      <div class="card  mb-4">
        <div class="card-body">
          <h2 class="section-title card-title">About Us</h2>
          <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae mattis odio, et venenatis tellus. Nullam convallis semper faucibus. Sed facilisis dolor id mi efficitur, nec aliquet enim iaculis. Ut luctus, ex in vestibulum interdum, dolor nisi finibus neque, eu consequat mi ligula vel dui. Mauris accumsan, nulla sed dapibus fringilla, nulla justo volutpat nulla, non iaculis ex massa et neque. Donec bibendum eros id urna pharetra feugiat.</p>
        </div>
      </div>
      
      <div class="card  mb-4">
        <div class="card-body">
          <h2 class="section-title card-title">Programs Offered</h2>
          <ul class="program-list">
            <li class="program-item">Bachelor of Arts</li>
            <li class="program-item">Bachelor of Science</li>
            <li class="program-item">Bachelor of Commerce</li>
            <li class="program-item">Bachelor of Engineering</li>
            <li class="program-item">Bachelor of Education</li>
          </ul>
        </div>
      </div>
      
      <div class="card ">
        <div class="card-body">
          <h2 class="section-title card-title">Admission Requirements</h2>
          <ul class="requirement-list">
            <li class="requirement-item">High school diploma or equivalent</li>
            <li class="requirement-item">Minimum GPA of 3.0</li>
            <li class="requirement-item">Letter of recommendation</li>
            <li class="requirement-item">Personal statement</li>
            <li class="requirement-item">Entrance exam scores</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="prospectus-footer">
      <p class="footer-text">For more information, please contact our admissions office.</p>
    </div>
  </div>
</template>

<style scoped>
.prospectus {
  padding: 40px;
}

.prospectus-title {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 30px;
}

.section-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.card {
    max-width: 100%;
  margin-bottom: 20px;
  background-color: #f8f9fa;
  border: none;
  border-radius: 10px;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}
.card:hover {
  transform: translateY(-5px);
}
.program-list {
  margin-left: 20px;
  margin-bottom: 20px;
}

.program-item {
  margin-bottom: 5px;
  list-style: none;
}

.requirement-list {
  margin-left: 20px;
  margin-bottom: 20px;
  padding-left: 0;
}

.requirement-item {
  margin-bottom: 5px;
  list-style: none;
}

.prospectus-footer {
  text-align: center;
}

.footer-text {
  font-style: italic;
}
.info-card {
  background-color: #f8f9fa;
  border: none;
  border-radius: 10px;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}
.info-card:hover {
  transform: translateY(-5px);
}
</style>