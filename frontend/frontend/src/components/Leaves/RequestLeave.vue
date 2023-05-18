<template>
  <div class="card">
    <div class="card-header">
      Leave Request Form
    </div>
    <div class="card-body">
      <form @submit="submitForm">
        <div class="form-group">
          <label for="leaveType">Leave Type:</label>
          <select id="leaveType" v-model="leave.leaveType" class="form-control" required>
            <option value="LWP">LWP</option>
            <option value="EL">EL</option>
            <option value="CL">CL</option>
            <option value="SL">SL</option>
          </select>
        </div>

        <div class="form-group">
          <label for="reason">Reason:</label>
          <textarea id="reason" v-model="leave.reason" class="form-control" rows="4" cols="50"></textarea>
        </div>

        <div class="form-group">
          <label for="fromDate">From Date:</label>
          <input type="date" id="fromDate" v-model="leave.fromDate" class="form-control " required>
        </div>

        <div class="form-group">
          <label for="toDate">To Date:</label>
          <input type="date" id="toDate" v-model="leave.toDate" class="form-control" required>
        </div>

        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
     <b-toast v-model="showToast" :title="toastTitle" :auto-hide-delay="1000" variant="success"></b-toast>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import VueCookies from "vue-cookies";

Vue.use(VueCookies);
Vue.use(VueAxios, axios);

export default {
  data() {
    const login = this.$cookies.get('isLoggedIn');
    return {
      leave: {
        id: login.id,
        leaveType: '',
        reason: '',
        fromDate: '',
        toDate: ''
      },
      showToast: false,
      toastTitle: ''
    };
  },
  methods: {
    submitForm() {
      axios.post(`http://localhost:5000/requestLeave/${this.leave.id}`, this.leave)
        .then(response => {
          console.warn(response);
          console.log('Leave request has been sent');
          this.showToast = true;
          this.toastTitle = 'Leave request has been sent';
          setTimeout(() => {
            this.$router.push('/TeacherHomepage');
          }, 1500);
        })
        .catch(error => {
          console.error('Error sending leave request:', error);
        });
    }
  }
};
</script>

<style scoped>
.card {
    max-width: 100%;
  width: 400px;
  margin: 0 auto;
}

.card-header {
  background-color: #f8f9fa;
  border-bottom: 1px solid #dee2e6;
  font-weight: bold;
}

.card-body {
  padding: 20px;
}
</style>