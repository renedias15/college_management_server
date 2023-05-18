<template>
  <div>
    <div class="card">
        <div class="help-icon">
    <i class="fas fa-question-circle" @mouseover="showHelp = true" @mouseleave="showHelp = false" ></i>
    <div class="help-text" v-if="showHelp">
      <p>Select a course and send batch emails to the applicants informing them about the entance test schedule</p>
    </div>
  </div>
      <div class="card-header">
        <h2>Applicant List</h2>
      </div>
      <div class="card-body">
        <div class="form-group">
          <select class="form-control" id="course" v-model="selectedCourse" required>
            <option value="" disabled>Select a course</option>
            <option v-for="course in courses" :value="course" :key="course">{{ course }}</option>
          </select>
        </div>
        <table class="table table-striped table-bordered">
          <thead class="thead-dark">
            <tr>
              <th>Sr no</th>
              <th>Email</th>
              <th>Name</th>
              <th>Course</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(ent_form, index) in filteredForms" :key="ent_form[0]">
              <td>{{ index + 1 }}</td>
              <td>{{ ent_form[1] }}</td>
              <td>{{ ent_form[2] }}</td>
              <td>{{ ent_form[3] }}</td>
            </tr>
          </tbody>
        </table>
        <button v-if="showSendMailButton" @click="openPopup()" class="btn btn-primary btn-md rounded-pill">Send Mail</button>
      </div>
    </div>
    <modal name="my-popup" :modal-class="['rounded']" >
      <h2 class="mb-3">Mail Automation</h2>
      <form @submit.prevent="notify">
        <span class="mb-5 text-danger">All applicants opting for {{ selectedCourse }} will receive this mail</span>
        <label for="details">Please enter the subject of the mail:</label><br>
        <textarea type="text" name="body" placeholder="Enter entrance test details" v-model="body"></textarea><br>
        <button class="btn btn-primary mt-3 btn-sm rounded pill" type="submit">Submit</button> <button class="btn btn-primary mt-3 btn-sm rounded pill" @click="closePopup">Cancel</button><br>
      </form>
     
    <b-toast v-model="showToast" :title="toastTitle" :auto-hide-delay="1000" variant="success"></b-toast>
    </modal>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import VModal from 'vue-js-modal';
Vue.use(VModal);
Vue.use(VueAxios, axios)
export default {
  data() {
    return {
      ent_forms: [],
      searchText: '',
      courses: [],
      selectedCourse: '',
      body: '',
      showSendMailButton: false,
      showToast: false,
      toastTitle: '',
      showHelp: false
    };
  },
  mounted() {
    this.fetchForms();
    this.fetchCourses();
  },
  methods: {
    notify() {
      const posts={'body':this.body,'selectedCourse':this.selectedCourse}
      this.axios.post('http://localhost:5000/send-email', posts)
        .then((res) => {
        
          console.warn(res);  
          this.closePopup()
        })
        this.showToast = true;
          this.toastTitle = 'Email sent successfully'
    },
    openPopup() {
      this.$modal.show('my-popup');
    },
    closePopup() {
      this.$modal.hide('my-popup');
    },
    fetchForms() {
      axios.get('http://localhost:5000/getElligibleApplicants')
        .then(response => {
          this.ent_forms = response.data;
        })
        .catch(error => {
          console.error('Error fetching forms:', error);
        });
    },
    fetchCourses() {
      axios.get('http://localhost:5000/EntranceForm_courses')
        .then(response => {
          this.courses = response.data;
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    },
    sendEmail() {
      this.showSendMailButton = true;
    }
  },
  computed: {
    filteredForms() {
      if (!this.selectedCourse) {
        return this.ent_forms;
      }
      this.sendEmail();
      return this.ent_forms.filter(ent_form => ent_form[3] === this.selectedCourse);
    }
  }
};
</script>

<style scoped>
.card {
  max-width: 100%;
  margin: 20px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}
.custom-modal .modal-dialog {
  border-radius: 1rem;
}
.help-icon {
  position: absolute;
  top: 10px;
  left: 10px;
}

.help-text {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  width: 200px;
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.help-icon:hover .help-text {
  display: block;
}
</style>