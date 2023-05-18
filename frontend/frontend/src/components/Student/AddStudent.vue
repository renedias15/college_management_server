<template>
<div class="d-flex justify-content-center">
         <div class="text-center" style="width: 800px;">
  <div class="card" >
    <div class="card-header">
    <h1>Student Information Form</h1>
    </div>
      <div class="card-body">
    <form @submit="postData" method="post">
      <div class="form-group">
        <label for="firstName">First Name</label>
        <input type="text" class="form-control" id="firstName" v-model="posts.firstName" required>
      </div>
      <div class="form-group">
        <label for="surname">Surname</label>
        <input type="text" class="form-control" id="surname" v-model="posts.surname" required>
      </div>
      <div class="form-group">
        <label for="age">Age</label>
        <input type="number" class="form-control" id="age" v-model="posts.age" required>
      </div>
      <div class="form-group">
        <label for="address">Address</label>
        <textarea class="form-control" id="address" v-model="posts.address" required></textarea>
      </div>
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" class="form-control" id="phone" v-model="posts.phone" required>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
       <router-view></router-view>
  </div>
    </div>
    </div>
     </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios,axios)

export default {
  name:'AddStudent',
  data() {
    return {
      posts:{
      firstName: '',
      surname: '',
      age: null,
      address: '',
      phone: null
      }
    }
  },
  methods:{
    postData(e)
    {
      this.axios.post('http://localhost:5000/addStudent',this.posts)
      .then((res)=>{
        console.warn(res);
        this.$router.push('/AdminHomepage');
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