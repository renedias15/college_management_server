<template>
  <div class="container">
    <h2 class="text-center mb-4 mt-4">Admission Process</h2>
    <div class="row">
      <div class="col-md-6">
        <div class="card admission-card mb-4">
          <div class="card-body">
            <h4 class="card-title">Step 1: Application Submission</h4>
            <p class="card-text">
              Applicant will have to fill a form and attach relevant documents as proof.
            </p>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card admission-card mb-4">
          <div class="card-body">
            <h4 class="card-title">Step 2: Document Verification</h4>
            <p class="card-text">
              College staff will verify the attached documents and applicant details. Email with entrance schedule details will be sent to applicant  if elligible.
            </p>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card admission-card mb-4">
          <div class="card-body">
            <h4 class="card-title">Step 3: Entrance Exam</h4>
            <p class="card-text">
              Enterance Exam will be held in the auditorium on the given date and time as mentioned in the email
            </p>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card admission-card mb-4">
          <div class="card-body">
            <h4 class="card-title">Step 4: Admission</h4>
            <p class="card-text">
              Merit list will be put up on the college site. Email will be sent with the admission form link to be filled by applicant
            </p>
          </div>
        </div>
      </div>
    </div>
    <router-link to="/enterance-form" class="btn btn-primary btn-lg rounded-pill">Apply now</router-link>
  </div>
</template>

<style scoped>
.admission-card {
    max-width: 100%;
  background-color: #f8f9fa;
  border: none;
  border-radius: 10px;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.admission-card:hover {
  transform: translateY(-5px);
}

.admission-card .card-body {
  padding: 20px;
}

.admission-card .card-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 15px;
}

.admission-card .card-text {
  color: #666;
  line-height: 1.6;
}
</style>
