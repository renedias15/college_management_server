<template>
<div class="d-flex justify-content-center">
         <div class="text-center" style="width: 800px;">
<div class="card">
    <div class="card-header">
      <h3 class="card-title">Teacher Details</h3>
    </div>
    <div class="card-body">
      <form @submit="postData" method="post">
        <div class="form-group">
          <label for="firstName">First Name:</label>
          <input type="text" class="form-control" id="firstName" v-model="teacher.firstName" placeholder="Enter first name" required>
        </div>
        <div class="form-group">
          <label for="lastName">Last Name:</label>
          <input type="text" class="form-control" id="lastName" v-model="teacher.lastName" placeholder="Enter last name" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" class="form-control" id="email" v-model="teacher.email" placeholder="Enter email" required>
        </div>
        <div class="form-group">
          <label for="phone">Phone Number:</label>
          <input type="text" class="form-control" id="phone" v-model="teacher.phone" placeholder="Enter phone number" @input="validatePhoneNumber" required>
          <span v-if="phoneError" class="text-danger">Phone number must have 10 digits.</span>
        </div>
        <div class="form-group">
          <label for="address">Address:</label>
          <textarea class="form-control" id="address" v-model="teacher.address" placeholder="Enter address" required></textarea>
        </div>
        <div class="form-group">
          <label for="qualifications">Qualifications:</label>
          <input type="text" class="form-control" id="qualifications" v-model="teacher.qualifications" placeholder="Enter qualifications" required>
        </div>
        <div class="form-group">
          <label for="experience">Experience:(in years)</label>
          <input type="number" class="form-control" id="experience" v-model="teacher.experience" placeholder="Enter experience" required>
        </div>
        <button type="submit" class="btn btn-primary">Add Teacher</button>
      </form>
    </div>
  </div>
    <router-view></router-view>
</div>
</div>
</template>
<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios,axios)

export default {
  name:'AddTeacher',
  data() {
    return {
       teacher: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        address: '',
        qualifications: '',
        experience: ''
      },
      phoneError: false
    }
  },
  methods:{
    validatePhoneNumber() {
    if (this.teacher.phone.length > 10 || this.teacher.phone.length < 10 ) {
      this.phoneError = true;
    } else {
      this.phoneError = false;
    }
  },
    postData(e)
    {
      this.axios.post('http://localhost:5000/addTeacher',this.teacher)
      .then((res)=>{
        console.warn(res);
      })
      e.preventDefault()
    }
  }
}
</script>

<style scoped>
.card {
  max-width: 100%;
  margin: 20px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}

.card-header {
  background-color: #3f51b5;
  color: #fff;
  border-radius: 15px 15px 0 0;
  padding: 10px 20px;
}

.card-body {
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-weight: bold;
}

.btn-primary {
  background-color: #3f51b5;
  border-color: #3f51b5;
  margin-top: 20px;
}
</style>