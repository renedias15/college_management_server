<template>
  <div class="d-flex justify-content-center">
         <div class="text-center" style="width: 800px;">
  <div class="card" >
    <div class="card-header">
    <h2>Edit Student</h2>
    </div>
    <div class="card-body">
    <form @submit="updateStudent">
      <div class="form-group">
        <label for="firstName">First Name</label>
        <input type="text" class="form-control" id="firstName" v-model="student.firstName" required>
      </div>
      <div class="form-group">
        <label for="lastName">Last Name</label>
        <input type="text" class="form-control" id="lastName" v-model="student.lastName" required>
      </div>
      <div class="form-group">
        <label for="age">Age</label>
        <input type="number" class="form-control" id="age" v-model="student.age" required>
      </div>
      <div class="form-group">
        <label for="address">Address</label>
        <textarea class="form-control" id="address" v-model="student.address" required></textarea>
      </div>
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" class="form-control" id="phone" v-model="student.phone" required>
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
    </form>
    </div>
  </div>
  </div>
   <b-toast v-model="showToast" :title="toastTitle" :auto-hide-delay="1000" variant="success"></b-toast>
    </div>
  
</template>

<script>
import Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
Vue.use(VueAxios,axios)

export default {
  data() {
    return {
      student: {
        id: null,
        firstName: '',
        lastName: '',
        // Other student properties...
      },
      showToast: false,
      toastTitle: ''
    };
  },
  mounted() {
    const studentId = this.$route.params.id;
  // Make an API request to fetch the student details
  axios.get(`http://localhost:5000/getStudent/${studentId}`)
    .then(response => {
      // Populate the student object with the fetched data
         const data = response.data;
      this.student = {
        id: data[0],
        firstName: data[1],
        lastName: data[2],
        age: data[3],
        address: data[4],
        phone: data[5]
      };
    })
    .catch(error => {
      console.error('Error fetching student details:', error);
    });
  },
  methods: {
    updateStudent(e) {
        const confirmation = window.confirm('Are you sure you want to update the student?');
        if (!confirmation) {
            return; // Cancel the update if the user cancels the confirmation
        }
      axios.put(`http://localhost:5000/updateStudent/${this.student.id}`, this.student)
        .then(response => {
            console.warn(response);
          console.log('Student updated successfully');
           this.showToast = true;
          this.toastTitle = 'Successfully uupdated student'
       setTimeout(() => {
            this.$router.push('/AdminHomepage');
          }, 1500);
        })
        e.preventDefault()
        .catch(error => {
          console.error('Error updating student:', error);
        });
    }
  }
};
</script>
<style scoped>
.card {
  max-width: 800px;
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
.b-toast {
  position: absolute;
  top: 20px;
  right: 20px;
}
</style>