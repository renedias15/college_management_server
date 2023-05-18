<template>
  <div class="container">
    <h1 class="text-center my-4">School Management System</h1>

    <div class="row">
      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="../../images/students.png" class="card-img-top" alt="Students"> -->
          <div class="card-body">
            <h5 class="card-title">Students</h5>
            <p class="card-text">Add/remove/update student records.</p>
            <div class="dropdown">
              <button
                class="btn btn-primary btn-block dropdown-toggle"
                type="button"
                id="studentsDropdown"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Students
              </button>
              <div class="dropdown-menu" aria-labelledby="studentsDropdown">
                <router-link class="dropdown-item" to="/students"
                  >View Students</router-link
                >
                <router-link class="dropdown-item" to="/add-student"
                  >Add Student</router-link
                >
                <router-link class="dropdown-item" to="/update-student"
                  >Update Student</router-link
                >
                <router-link class="dropdown-item" to="/remove-student"
                  >Remove Student</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/teachers.jpg" class="card-img-top" alt="Teachers"> -->
          <div class="card-body">
            <h5 class="card-title">Teachers</h5>
            <p class="card-text">Add/remove/update teacher profiles.</p>
            <div class="dropdown">
              <button
                class="btn btn-primary btn-block dropdown-toggle"
                type="button"
                id="teachersDropdown"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Teachers
              </button>
              <div class="dropdown-menu" aria-labelledby="teachersDropdown">
                <router-link class="dropdown-item" to="/teachers"
                  >View Teachers</router-link
                >
                <router-link class="dropdown-item" to="/add-teacher"
                  >Add Teacher</router-link
                >
                <router-link class="dropdown-item" to="/update-teacher"
                  >Update Teacher</router-link
                >
                <router-link class="dropdown-item" to="/remove-teacher"
                  >Remove Teacher</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/courses.jpg" class="card-img-top" alt="Courses"> -->
          <div class="card-body">
            <h5 class="card-title">Courses</h5>
            <p class="card-text">Add/remove/update course offerings.</p>
            <div class="dropdown">
              <button
                class="btn btn-primary btn-block dropdown-toggle"
                type="button"
                id="coursesDropdown"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Courses
              </button>
              <div class="dropdown-menu" aria-labelledby="coursesDropdown">
                <router-link class="dropdown-item" to="/courses"
                  >View Courses</router-link
                >
                <router-link class="dropdown-item" to="/add-course"
                  >Add Course</router-link
                >
                <router-link class="dropdown-item" to="/update-course"
                  >Update Course</router-link
                >
                <router-link class="dropdown-item" to="/remove-course"
                  >Remove Course</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/teachers.jpg" class="card-img-top" alt="Teachers"> -->
          <div class="card-body">
            <h5 class="card-title">Certificates</h5>
            <p class="card-text">Create Certificates on issue</p>
            <div class="dropdown">
              <button
                class="btn btn-primary btn-block dropdown-toggle"
                type="button"
                id="CertificatesDropdown"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Certificates
              </button>
              <div class="dropdown-menu" aria-labelledby="CertificatesDropdown">
                <router-link class="dropdown-item" to="/certificate"
                  >Bonafide Certificate</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/teachers.jpg" class="card-img-top" alt="Teachers"> -->
          <div class="card-body">
            <h5 class="card-title">Daily Announcements</h5>
            <p class="card-text">Create Announcement for today</p>
            <div class="dropdown">
              <button
                class="btn btn-primary btn-block dropdown-toggle"
                type="button"
                id="AnnouncementDropdown"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Announcements
              </button>
              <div class="dropdown-menu" aria-labelledby="AnnouncementDropdown">
                <router-link class="dropdown-item" to="/CreateAnnouncement"
                  >Create Announcement</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/teachers.jpg" class="card-img-top" alt="Teachers"> -->
          <div class="card-body">
            <h5 class="card-title">Leave Request</h5>
            <p class="card-text">Approve leave requests</p>
            <router-link
              class="btn btn-primary btn-block"
              to="/ApproveLeave"
            >
              Approve
            </router-link>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/teachers.jpg" class="card-img-top" alt="Teachers"> -->
          <div class="card-body">
            <h5 class="card-title">Enterance Forms</h5>
            <p class="card-text">Verify enterance forms,view elligible applicants</p>
            <div class="dropdown">
              <button
                class="btn btn-primary btn-block dropdown-toggle"
                type="button"
                id="AnnouncementDropdown"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Forms
              </button>
              <div class="dropdown-menu" aria-labelledby="AnnouncementDropdown">
                <router-link class="dropdown-item" to="/ViewApplicants"
                  >View Elligible Applicants</router-link
                >
                <router-link
              class="dropdown-item"
              to="/verifyEntranceForm"
            >
              Verify Applicant details
            </router-link>
            <router-link
              class="dropdown-item"
              to="/UploadMeritList"
            >
              upload merit list
            </router-link>
              </div>
            </div>
            
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card mb-4">
          <!-- <img src="/images/teachers.jpg" class="card-img-top" alt="Teachers"> -->
          <div class="card-body">
            <h5 class="card-title">Notices</h5>
            <p class="card-text">Create important notices to diplay on homepage</p>
            <router-link
              class="btn btn-primary btn-block"
              to="/CreateNotice"
            >
              Create Notice
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminHomepage",
};
</script>

<style scoped></style>
