<template>
     <div class="d-flex justify-content-center">
         <div class="text-center" style="width: 800px;">
  <div class="card">
    <div class="card-header">
      <h3 class="card-title">Add Course</h3>
    </div>
    <div class="card-body">
      <form @submit="postData" method="post">
        <div class="form-group">
          <label for="courseName">Course Name:</label>
          <input type="text" class="form-control" id="courseName" v-model="posts.courseName" required>
        </div>
        <div class="form-group">
          <label for="courseCode">Course Code:</label>
          <input type="text" class="form-control" id="courseCode" v-model="posts.courseCode" required>
        </div>
        <div class="form-group">
          <label for="courseDescription">Course Description:</label>
          <textarea class="form-control" id="courseDescription" v-model="posts.courseDescription" required></textarea>
        </div>
        <div class="form-group">
          <label for="courseCredits">Course Credits:</label>
          <input type="number" class="form-control" id="courseCredits" v-model="posts.courseCredits" required>
        </div>
        <div class="form-group">
          <label for="coursePrerequisite">Course Prerequisite:</label>
          <input type="text" class="form-control" id="coursePrerequisite" v-model="posts.coursePrerequisite" required>
        </div>
        <div class="form-group">
          <label for="courseFee">Course Fee:</label>
          <input type="number" class="form-control" id="courseFee" v-model="posts.courseFee" required>
        </div>
        <button type="submit" class="btn btn-primary">Add Course</button>
      </form>
    </div>
    <router-view></router-view>
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
  name:'AddCourse',
  data() {
    return {
      posts:{
      courseName: "",
      courseCode: "",
      courseDescription: "",
      courseCredits: null,
      coursePrerequisite: "",
      courseFee: null,
      }
    }
  },
  methods:{
    postData(e)
    {
      this.axios.post('http://localhost:5000/addCourse',this.posts)
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